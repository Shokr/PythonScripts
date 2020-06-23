#!/usr/bin/env python2.7

#Symmetric DES

import pyDes

data = "hello world hi"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)

print ("Encrypted: %r" % d)
print ("Decrypted: %r" % k.decrypt(d))

## DES3

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

key = DES3.adjust_key_parity(get_random_bytes(24))

cipher = DES3.new(key, DES3.MODE_CFB)

msg = cipher.nonce + cipher.encrypt(data)

# plaintext = b'We are no longer the knights who say ni!'

print ("DES3 Encrypted: %r" % msg)
print ("DES3 Decrypted: %r" % k.decrypt(msg))
