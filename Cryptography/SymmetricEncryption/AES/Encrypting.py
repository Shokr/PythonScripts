# Advanced Encryption Standard (AES) Symmetric Block Cipher.
"""
Our AES Key needs to be either 16, 24 or 32 bytes long and our Initialization Vector needs to be 16 Bytes long.
 That will be generated using the random and string modules.
"""

import base64
import random
import string

from Crypto.Cipher import AES

key = "".join(
    random.choice(string.ascii_uppercase +
                  string.ascii_lowercase + string.digits)
    for x in range(32)
)
iv = "".join(
    random.choice(string.ascii_uppercase +
                  string.ascii_lowercase + string.digits)
    for x in range(16)
)

print(key, len(key))
print(iv, len(iv))

enc_s = AES.new(key, AES.MODE_CFB, iv)
cipher_text = enc_s.encrypt("this is a super important message")
encoded_cipher_text = base64.b64encode(cipher_text)
print(encoded_cipher_text)
