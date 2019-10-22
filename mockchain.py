# Tested on Raspbian, but should work the same on other Linux distros.
# You'll need python and pip and virtualenv set up first.
# Git clone this repository to your machine then from the terminal...

# cd mockchain-python
# virtualenv -p python3 venv
# source venv/bin/activate
# pip install pycryptodome
# python mockchain.py


import base64
import collections
import datetime
import hashlib
import Crypto
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Node:
    def __init__(self, name):
        self.name = name
        self._wallet = self.Wallet()
        self._blockchain = self.Blockchain()
        self._transaction_pool = self.TransactionPool()

    @property
    def wallet_id(self):
        return self._wallet.identity
    
    @property
    def get_block_count(self):
        return str(self._blockchain.block_count)
        
    @property
    def get_mempool_count(self):
        return str(self._transaction_pool.get_transaction_count)
        
    def sign_transaction(self, transaction):
        self._wallet.sign_transaction(transaction)
        
    def add_transaction_to_mempool(self, transaction):
        self._transaction_pool.append_transaction(transaction)
        
    def generate_block(self, block, difficulty):
        return self.Mining.generate_block(self._transaction_pool, block, difficulty)
        
    def append_block(self, block):
        self._blockchain.append_block(block)
        
    def validate_entire_blockchain(self, validate_signatures = True):
        self._blockchain.validate_entire_blockchain(validate_signatures)
        
    def print_blockchain_data(self, print_transaction_data = True):
        self._blockchain.print_blockchain_data(print_transaction_data)
        
    class Wallet:
        def __init__(self):
            random = Random.new().read
            # Generate a new private and public key pair
            self._private_key = RSA.generate(1024, random)
            self._public_key = self._private_key.publickey()
            # Create a signer object using private key
            self._signer = PKCS1_v1_5.new(self._private_key)
            # Export the public key in a useful format
            exported_public_key = self._public_key.export_key(format='OpenSSH').decode('UTF-8')
            pubkey_b64_encoded_bytes = base64.b64encode(bytes(exported_public_key.encode('UTF-8')))
            self.pub_key_encoded = pubkey_b64_encoded_bytes.decode('UTF-8')

        @property
        def identity(self):
            return self.pub_key_encoded

        def sign_transaction(self, transaction):
            if transaction.sender != self.identity:
                raise Exception('The sender must be the one signing the transaction')
            # Create our text to sign
            message = transaction.unsigned_to_string.encode('utf-8')
            # Create a hash digest of the text to sign
            digest = SHA256.new()
            digest.update(message)
            # Sign the digest
            signature = self._signer.sign(digest)
            # Get signature as b64 encoded string
            signature_b64_encoded = base64.b64encode(signature).decode('UTF-8')
            transaction.signature = signature_b64_encoded
            transaction.pub_key = self.pub_key_encoded


    class Blockchain:
        def __init__(self):
            self._blocks = []
            self._utils = CryptographyUtils()
        
        @property
        def block_count(self):
            return len(self._blocks)
            
        def append_block(self, block):
            self._blocks.append(block)

        def validate_entire_blockchain(self, validate_signatures = True):
            previous_block_hash = ''
            block_hash = ''
            include_sigs = '(Excluding transactions)'
            if validate_signatures:
                include_sigs = '(Including transactions)'
            info = 'VALIDATING BLOCKCHAIN ' + include_sigs
            log('\n' + str('=' * len(info)))
            log(info)
            log('=' * len(info))
                        
            for block in self._blocks:
                log('Verifying block ' + str(block.height))
                # Genesis block check
                if block.height == 1 :
                    previous_block_hash = CryptographyUtils.sha256('Chancellor on brink of second bailout for banks')
                assert(block.previous_block_hash == previous_block_hash)
                previous_block_hash = block.derive_block_hash
                assert CryptographyUtils.verify_pow(block, block.difficulty)
                log('Verified block hash (using nonce ' + str(block.nonce) + ')')
                if validate_signatures:
                    for transaction in block.get_transactions:
                        assert CryptographyUtils.verify_signature(transaction.signature, transaction.pub_key, transaction.unsigned_to_string)
                    log('Verified transactions (' + str(len(block.get_transactions)) + ')')
                    log('')
                    
        def print_blockchain_data (self, print_transaction_data = True):
            info = 'BLOCKCHAIN DATA'
            print('=' * len(info))
            print('' + info)
            print('=' * len(info))
            print('CHAIN LENGTH : ' + str(self.block_count))
            
            for block in self._blocks:
                info = 'BLOCK ' + str(block.height)
                print('\n' + info)
                print('=' * len(info))
                print('Block hash   : ' + str(block.get_block_hash))
                print('Prev block   : ' + str(block.get_previous_block_hash))
                print('Difficulty   : ' + str(block.difficulty))
                print('Nonce        : ' + str(block.nonce))
                print('Transactions : ' + str(len(block.get_transactions)))
                if print_transaction_data:
                    i = 1
                    for transaction in block.get_transactions:
                        tx_info = info + ' - TRANSACTION ' + str(i)
                        print('\n' + tx_info)
                        print('-' * len(tx_info))
                        transaction.print_transaction_data()
                        i += 1


    class Mining:
        @staticmethod
        def generate_block(mempool_transactions, previous_block, difficulty):
            block = Block()
            for transaction in mempool_transactions.get_transactions:
                block.append_transaction(transaction)
            block.previous_block_hash = previous_block.get_block_hash
            Node.Mining.mine(block, difficulty, previous_block.height + 1)
            log('\nFound block ' + str(block.height) + ' using nonce ' + str(block.nonce))
            log('  Block ' + str(block.height) + ' hash: ' + block.id + '\n')
            # Remove mined transactions from the mempool
            if debug_log:
                block.print_transaction_ids()
            for transaction in block.get_transactions:
                mempool_transactions.remove_transaction(transaction)
            return block

        @staticmethod
        def mine(block, difficulty=1, height=0):
            utils = CryptographyUtils()
            nonce = None
            assert difficulty >= 1
            prefix = '0' * difficulty
            i = 0
            # Warning - this will keep trying until it finds a block, so don't
            # set network difficulty too high ;-)
            while not nonce:
                digest = CryptographyUtils.sha256(str(block.get_block_data_as_string) + str(i))
                if digest.startswith(prefix):
                    nonce = str(i)
                    block.nonce = nonce
                    block.id = digest
                    block.difficulty = difficulty
                    block.height = height
                    break
                i += 1


    class TransactionPool:
        def __init__(self):
            self._transactions = []
        
        def append_transaction(self, transaction):
            if CryptographyUtils.verify_signature(transaction.signature, transaction.pub_key, transaction.unsigned_to_string):
                self._transactions.append(transaction)
            else:
                raise Exception('Cannot add transaction to mempool - Invalid signature')
        
        @property
        def get_transactions(self):
            return self._transactions
            
        @property
        def get_transaction_count(self):
            return len(self._transactions)
            
        def remove_transaction(self, transaction):
            return self._transactions.remove(transaction)


class Block:
    def __init__(self):
        self._transactions = []
        self.previous_block_hash = None
        self.nonce = None
        self.height = 0
        self.difficulty = 0
        self._block_hash = None

    @property
    def get_transactions(self):
        return self._transactions

    @property
    def get_previous_block_hash(self):
        return self.previous_block_hash
    
    @property
    def get_block_hash(self):
        if not self._block_hash:
            self.derive_block_hash
        return self._block_hash

    # Used to force recalculation of the block hash using block_data and nonce
    @property
    def derive_block_hash(self):
        if not self.nonce:
            raise Exception('You must set a valid nonce before trying to derive the block_hash')
        self._block_hash = CryptographyUtils.sha256(self.get_block_data_as_string + str(self.nonce))
        return self._block_hash

    def append_transaction(self, transaction):
        if CryptographyUtils.verify_signature(transaction.signature, transaction.pub_key, transaction.unsigned_to_string):
            self._transactions.append(transaction)
        else:
            raise Exception('Cannot add transaction, invalid signature')

    @property
    def get_txs_string(self):
        txs_string = ''
        for transaction in self._transactions:
            txs_string += transaction.unsigned_to_string
        return txs_string
            
    @property
    def tx_count(self):
        return len(self._transactions)
    
    @property
    def get_block_data_as_string(self):
        block_string = self.get_previous_block_hash + self.get_txs_string
        return block_string

    def print_transaction_ids(self):
        print('  Transactions in block ' + str(self.height) + ':')
        for transaction in self._transactions:
            print('    ' + transaction.tx_id)


class Transaction:
    def __init__(self, sender, recipient, value):
        self._value = value
        self._time = datetime.datetime.now()
        self.sender = sender
        self.recipient = recipient
        self.signature = ''
        self.pub_key = ''

    @property
    def tx_id(self):
        return CryptographyUtils.sha256(self.unsigned_to_string)

    @property
    def unsigned_to_string(self):
        tx_dict = self.to_dict()
        tx_string = tx_dict['sender'] + tx_dict['recipient'] + str(tx_dict['value']) + str(tx_dict['time'])
        return tx_string
        
    @property
    def signed_to_string(self):
        tx_dict = self.to_dict()
        tx_string = tx_dict['sender'] + tx_dict['recipient'] + str(tx_dict['value']) + str(tx_dict['time']) + tx_dict['signature'] + tx_dict['pub_key']
        return tx_string

    def to_dict(self):
        return collections.OrderedDict({
          'sender': self.sender,
          'recipient': self.recipient,
          'value': self._value,
          'time' : self._time,
          'signature': self.signature,
          'pub_key': self.pub_key})
          
    def print_transaction_data(self):
        tx_dict = self.to_dict()
        print('Sender       : ' + tx_dict['sender'])
        print('Recipient    : ' + tx_dict['recipient'])
        print('Value        : ' + str(tx_dict['value']))
        print('Created      : ' + str(tx_dict['time']))
        print('Signature    : ' + tx_dict['signature'])
        print('Pub key      : ' + tx_dict['pub_key'])


class CryptographyUtils:
    @staticmethod    
    def sha256(message):
        return hashlib.sha256(message.encode('ascii')).hexdigest()
    
    @staticmethod
    def verify_signature(signature, pub_key, message):
        # Get signature in a format we can use to verify
        signature_b64_decoded_bytes = base64.b64decode(bytes(signature.encode('UTF-8')))
        # Get pubkey in a format we can use to verify
        pubkey_b64_decoded = base64.b64decode(bytes(pub_key.encode('UTF-8')))
        if '' == signature or '' == pub_key:
            raise Exception('No signature, public key combination provided')
        # Import the public key
        imported_public_key = Crypto.PublicKey.RSA.import_key(pubkey_b64_decoded)
        verifier = Crypto.Signature.pkcs1_15.new(imported_public_key)
        message = message.encode('utf-8')
        digest = SHA256.new()
        digest.update(message)
        try:
            verifier.verify(digest, signature_b64_decoded_bytes)
            return True
        except:
            return False

    @staticmethod
    def verify_pow(block, difficulty=1):
        prefix = '0' * difficulty
        digest = CryptographyUtils.sha256(str(block.get_block_data_as_string) + str(block.nonce))
        if digest.startswith(prefix):
            return True
        else:
            return False


class Network:
    def __init__(self, difficulty = 1):
        self.difficulty = difficulty
        
    def print_network_data(self, node):
        info = 'NETWORK INFO (at block height ' + str(node.get_block_count) + ')'
        print('\n' + str('=' * len(info)))
        print('' + info)
        print('=' * len(info))
        print('Blockcount    : ' + str(node.get_block_count))
        print('Mempool depth : ' + str(node.get_mempool_count))


def log(message):
    if debug_log:
        print(message)


# Run example
# -----------
print('\n  +-------------------------------------------------------------------+')
print(  '  |                                                                   |')
print(  '  |  A little example of Bitcoin blockchain basics written in Python  |')
print(  '  |  https://github.com/wintercooled/mockchain-python                 |')
print(  '  |                                                                   |')
print(  '  +-------------------------------------------------------------------+')

# Set to false to see less verbose logging:
debug_log = True

utils = CryptographyUtils()

# Creat two node instances that we will use to send and receive our imagined
# blockchain coins
node_1 = Node('Alice Node')
node_2 = Node('Bob Node')

# The network difficuly defines how many leading zeros must prefix a block hash
# for it to be considered valid
network = Network(difficulty = 2)

# Create genesis block with one transaction that pays mining reward to Bob
# We don't have the concept of a utxo set in this example code yet so we allow
# spends from any wallet, even if it doesn't hold any coins

t = Transaction (
    sender = node_1.wallet_id,
    recipient = node_2.wallet_id,
    value = 50.0
)

# The sender needs to sign the transaction using their private key
node_1.sign_transaction(t)

# The signed transaction is added to the mempool - a collection of transactions
# waiting to be added to a block
node_1.add_transaction_to_mempool(t)

# To view a transaction's data:
#t.print_transaction_data()

# We need a dummy block that we can use to provided the 'previous block hash'
# value for our genesis block
block = Block()
block._block_hash = CryptographyUtils.sha256('Chancellor on brink of second bailout for banks')

# Create the genesis block by mining at the current network difficulty
# Adding transactions to a block will remove them from the mempool
block = node_1.generate_block(block, network.difficulty)

# Apeend the valid block to the node's copy of the blockchain
node_1.append_block(block)

# Create some more transactions ready to be added to a new block. Each 
# transaction needs to be signed by the sender's wallet using the id, 
# which is a base64 encoded public key
t = Transaction(
    node_1.wallet_id,
    node_2.wallet_id,
    5.0
)
node_1.sign_transaction(t)
node_1.add_transaction_to_mempool(t)

t = Transaction(
    node_2.wallet_id,
    node_1.wallet_id,
    6.0
)
node_2.sign_transaction(t)
node_1.add_transaction_to_mempool(t)

t = Transaction(
    node_2.wallet_id,
    node_1.wallet_id,
    7.0
)
node_2.sign_transaction(t)
node_1.add_transaction_to_mempool(t)

# Increase the network difficulty to show how it affects block mining and
# the resulting block hash that is found
network.difficulty += 1

block = node_1.generate_block(block, network.difficulty)
node_1.append_block(block)

# To view the transactions in a block:
#block.print_transaction_ids()

# View the 'network' data for a given node's view
network.print_network_data(node_1)

# Validate the blockchain - including transaction signatures
node_1.validate_entire_blockchain(validate_signatures = True)

# Validate the blockchain - excluding transaction signatures
#node_1.validate_entire_blockchain(validate_signatures = False)

# To view a node's blockchain data (including tx data):
node_1.print_blockchain_data(True)

# To view a node's blockchain data (excluding tx data):
#node_1.print_blockchain_data(False)

print('\nExample completed without errors.\n')
