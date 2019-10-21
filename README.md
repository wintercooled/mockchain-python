# mockchain-python

A little example of Bitcoin blockchain basics* written in Python.

A work in progress and a starting point for looking into things like digitial signatures, 
hashing, block sequence etc. 

Might be good if you were learning Python as well and wanted to build the example out yourself.


# How to run the example

Tested on Raspbian, but should work the same on other Linux distros.

You'll need python and pip and virtualenv set up first.

Git clone this repository to your machine then from the terminal...

```
# cd mockchain-python
# virtualenv -p python3 venv
# source venv/bin/activate
# pip install pycryptodome
# python mockchain.py
```

# Example output

```

  +-------------------------------------------------------------------+
  |                                                                   |
  |  A little example of Bitcoin blockchain basics written in Python  |
  |  https://github.com/wintercooled/mockchain-python                 |
  |                                                                   |
  +-------------------------------------------------------------------+

Found block 1 using nonce 150
  Block 1 hash: 0087bb3ac8cbbd5ed632180b38c62dedccc158d960f2895aca1d0037462d0913

  Transactions in block 1:
    f97aaf1c811c825156f5703e6b42dbe0dbb349c31cc41851ec5864dd570ea02d

Found block 2 using nonce 2621
  Block 2 hash: 00083af3658d82387023218a6e98f0ac7c61032253d847d6ec6854d570e2b559

  Transactions in block 2:
    e38f1648d07609cf690f7cd246ea8d546f4f9348819eaeb82a08fffb6a2be03d
    f0d6f429d116ae5c2f861083be5e32ea7de52f9e2ca2b2c770d10ece21f213bc
    f5451985907fea425fced624c56b2141195d182f0a360b3b74dda039007ac1d1

================================
NETWORK INFO (at block height 2)
================================
Blockcount    : 2
Mempool depth : 0

==============================================
VALIDATING BLOCKCHAIN (Including transactions)
==============================================
Verifying block 1
Verified block hash (using nonce 150)
Verified transactions (1)

Verifying block 2
Verified block hash (using nonce 2621)
Verified transactions (3)

===============
BLOCKCHAIN DATA
===============
CHAIN LENGTH : 2

BLOCK 1
=======
Block hash   : 0087bb3ac8cbbd5ed632180b38c62dedccc158d960f2895aca1d0037462d0913
Prev block   : 8131e6f4b45754f2c90bd06688ceeabc0c45055460729928b4eecf11026a9e2d
Difficulty   : 2
Nonce        : 150
Transactions : 1

BLOCK 1 - TRANSACTION 1
-----------------------
Sender       : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FEYXA5dkNkTUh6MkwxZ3RvMmYrRjlIbFZ3MjFlcms5Uk9HbFRtek15SThQM0FEaU9EZ1plZ0ZvaUVMMTgwU1hzYzVkdVV6VS9QM0wwSklrMklGeE01SFVYMkt5SmpMemZ1SlVaS0ROZ28ySld1bnZrbjlzOFZOWVdBTzY2MFpaNmZGaE5FbGczVkgwbzBNZXh4b1ZROUNPOUZ1YkcycXlyMkk3dG0zVDhkaUd3PT0=
Recipient    : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FDYlNEMjZCUU10TjRCUmc5ekprc1ltTVpqRWhHMFJhWGJDVm1DblZFcFFwY2pxaC9udllUQ0NuTXdMdVN6WEttbGhtVVNEd05FS2ZmZExNRWVFeFJkNGtyaDhRTFRDZEtwbVYxd3BNdk5IUmk2WU1IZi9uZ0Y3UDZCUmcrNlJXRm53OUdPV1o1MWloN2tMbVErQzhsSHhrVVM3ak80c3ZvNm03djBITWJwWFBRPT0=
Value        : 50.0
Created      : 2019-10-21 20:10:56.785336
Signature    : Boh9FwIiTfhCZ6TOeEzkUWsq+SqwwhKh4VIrh77WCKO2bRcONUQV6GFMxN5Qoch7SY2bPhoQgaGfM6lhAa7OueXGZujkmaKIZw1fVfXDUXBRYvxUIkBfQ93FSUFQ2sRZRptyO/zslnKGV+AryLQLD6RxfeIhWq2ppW/S7CKex3M=
Pub key      : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FEYXA5dkNkTUh6MkwxZ3RvMmYrRjlIbFZ3MjFlcms5Uk9HbFRtek15SThQM0FEaU9EZ1plZ0ZvaUVMMTgwU1hzYzVkdVV6VS9QM0wwSklrMklGeE01SFVYMkt5SmpMemZ1SlVaS0ROZ28ySld1bnZrbjlzOFZOWVdBTzY2MFpaNmZGaE5FbGczVkgwbzBNZXh4b1ZROUNPOUZ1YkcycXlyMkk3dG0zVDhkaUd3PT0=

BLOCK 2
=======
Block hash   : 00083af3658d82387023218a6e98f0ac7c61032253d847d6ec6854d570e2b559
Prev block   : 0087bb3ac8cbbd5ed632180b38c62dedccc158d960f2895aca1d0037462d0913
Difficulty   : 3
Nonce        : 2621
Transactions : 3

BLOCK 2 - TRANSACTION 1
-----------------------
Sender       : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FEYXA5dkNkTUh6MkwxZ3RvMmYrRjlIbFZ3MjFlcms5Uk9HbFRtek15SThQM0FEaU9EZ1plZ0ZvaUVMMTgwU1hzYzVkdVV6VS9QM0wwSklrMklGeE01SFVYMkt5SmpMemZ1SlVaS0ROZ28ySld1bnZrbjlzOFZOWVdBTzY2MFpaNmZGaE5FbGczVkgwbzBNZXh4b1ZROUNPOUZ1YkcycXlyMkk3dG0zVDhkaUd3PT0=
Recipient    : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FDYlNEMjZCUU10TjRCUmc5ekprc1ltTVpqRWhHMFJhWGJDVm1DblZFcFFwY2pxaC9udllUQ0NuTXdMdVN6WEttbGhtVVNEd05FS2ZmZExNRWVFeFJkNGtyaDhRTFRDZEtwbVYxd3BNdk5IUmk2WU1IZi9uZ0Y3UDZCUmcrNlJXRm53OUdPV1o1MWloN2tMbVErQzhsSHhrVVM3ak80c3ZvNm03djBITWJwWFBRPT0=
Value        : 5.0
Created      : 2019-10-21 20:10:56.798307
Signature    : 2LIgnwMcHUd1N+7RgaacT9HheAQZ3N+Zf4HAKJq52o2tsh7myoh8CO3vgNUPzgtKH42vQ4nqqXXOCA9tbx/fAurnJ/Zr8QWwRqOAyk2o7vkG3mCNBXLek82gvja2FlIctchX62G9El/DcSTV72i0Zw1cFIKsbIwYobPhaEQ49TQ=
Pub key      : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FEYXA5dkNkTUh6MkwxZ3RvMmYrRjlIbFZ3MjFlcms5Uk9HbFRtek15SThQM0FEaU9EZ1plZ0ZvaUVMMTgwU1hzYzVkdVV6VS9QM0wwSklrMklGeE01SFVYMkt5SmpMemZ1SlVaS0ROZ28ySld1bnZrbjlzOFZOWVdBTzY2MFpaNmZGaE5FbGczVkgwbzBNZXh4b1ZROUNPOUZ1YkcycXlyMkk3dG0zVDhkaUd3PT0=

BLOCK 2 - TRANSACTION 2
-----------------------
Sender       : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FDYlNEMjZCUU10TjRCUmc5ekprc1ltTVpqRWhHMFJhWGJDVm1DblZFcFFwY2pxaC9udllUQ0NuTXdMdVN6WEttbGhtVVNEd05FS2ZmZExNRWVFeFJkNGtyaDhRTFRDZEtwbVYxd3BNdk5IUmk2WU1IZi9uZ0Y3UDZCUmcrNlJXRm53OUdPV1o1MWloN2tMbVErQzhsSHhrVVM3ak80c3ZvNm03djBITWJwWFBRPT0=
Recipient    : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FEYXA5dkNkTUh6MkwxZ3RvMmYrRjlIbFZ3MjFlcms5Uk9HbFRtek15SThQM0FEaU9EZ1plZ0ZvaUVMMTgwU1hzYzVkdVV6VS9QM0wwSklrMklGeE01SFVYMkt5SmpMemZ1SlVaS0ROZ28ySld1bnZrbjlzOFZOWVdBTzY2MFpaNmZGaE5FbGczVkgwbzBNZXh4b1ZROUNPOUZ1YkcycXlyMkk3dG0zVDhkaUd3PT0=
Value        : 6.0
Created      : 2019-10-21 20:10:56.803186
Signature    : GGxMFEi3zkDttL12l3D/xNYNy2pD4pl9WtEGfu2mhKA/fJ1yGNIjyaWlG5tp/N4DD8tRu0WE5uY6y5zX5EYMenqvsyeXTgxI5vszn9Yu5B9TSimX5l/jb8F6b56/JwIPnw3hX0vh3A/9wK8wsSU05a3HEfvKLsenBR0DIPsRKc4=
Pub key      : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FDYlNEMjZCUU10TjRCUmc5ekprc1ltTVpqRWhHMFJhWGJDVm1DblZFcFFwY2pxaC9udllUQ0NuTXdMdVN6WEttbGhtVVNEd05FS2ZmZExNRWVFeFJkNGtyaDhRTFRDZEtwbVYxd3BNdk5IUmk2WU1IZi9uZ0Y3UDZCUmcrNlJXRm53OUdPV1o1MWloN2tMbVErQzhsSHhrVVM3ak80c3ZvNm03djBITWJwWFBRPT0=

BLOCK 2 - TRANSACTION 3
-----------------------
Sender       : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FDYlNEMjZCUU10TjRCUmc5ekprc1ltTVpqRWhHMFJhWGJDVm1DblZFcFFwY2pxaC9udllUQ0NuTXdMdVN6WEttbGhtVVNEd05FS2ZmZExNRWVFeFJkNGtyaDhRTFRDZEtwbVYxd3BNdk5IUmk2WU1IZi9uZ0Y3UDZCUmcrNlJXRm53OUdPV1o1MWloN2tMbVErQzhsSHhrVVM3ak80c3ZvNm03djBITWJwWFBRPT0=
Recipient    : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FEYXA5dkNkTUh6MkwxZ3RvMmYrRjlIbFZ3MjFlcms5Uk9HbFRtek15SThQM0FEaU9EZ1plZ0ZvaUVMMTgwU1hzYzVkdVV6VS9QM0wwSklrMklGeE01SFVYMkt5SmpMemZ1SlVaS0ROZ28ySld1bnZrbjlzOFZOWVdBTzY2MFpaNmZGaE5FbGczVkgwbzBNZXh4b1ZROUNPOUZ1YkcycXlyMkk3dG0zVDhkaUd3PT0=
Value        : 7.0
Created      : 2019-10-21 20:10:56.809218
Signature    : HvodbeQdhwc/b6mtUBdlIIuRG+4U7VrVZxsc0PidCfuMZiYrZRp2NYORj335Cg0wpzHvAj2bZawmdzGOSB71EMc3fQFDEl6t1oQoAh34JAqLBrkpYQOeTk+4C/SBZUggE2z7GzgAGThdH7PJ9HS18s6yZ9wVIBmDFrnxuwE+J5k=
Pub key      : c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFBZ1FDYlNEMjZCUU10TjRCUmc5ekprc1ltTVpqRWhHMFJhWGJDVm1DblZFcFFwY2pxaC9udllUQ0NuTXdMdVN6WEttbGhtVVNEd05FS2ZmZExNRWVFeFJkNGtyaDhRTFRDZEtwbVYxd3BNdk5IUmk2WU1IZi9uZ0Y3UDZCUmcrNlJXRm53OUdPV1o1MWloN2tMbVErQzhsSHhrVVM3ak80c3ZvNm03djBITWJwWFBRPT0=

Example completed without errors.

```


# Work in progress notes...

[ ] Remove use of hashlib.sha256 and replace with SHA256.new() etc
[ ] Some code should use transaction.signed_to_string not unsigned_to_string(?)
[ ] Introduce the concept of UTXOs, addresses, wallet balances
[ ] Enable the sharing of transactions between nodes
[ ] Enable the competitive mining of blocks between nodes
[ ] Enable the concept of longest, most worked on valid chain
[ ] Introduce mining rewards and halvings
[ ] Introduce dificulty adjustments
[ ] Introduce transaction fees
[ ] Use base56 not base64 encoding for public keys

* well, very, very basic actually!
