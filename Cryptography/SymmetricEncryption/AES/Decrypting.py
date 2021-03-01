import base64

from Crypto.Cipher import AES

key = "3BvB5mXhqbMXSmuk35TfuF5dciAKm24X"
iv = "ROdfH3KsFNEy0gb9"

encoded_cipher_text = "5PIejP1sxmO1XvxXLJFK4pDEqpVHTInYOEK4kXGx6Uyg"

decryption_suite = AES.new(key, AES.MODE_CFB, iv)
plain_text = decryption_suite.decrypt(base64.b64decode(encoded_cipher_text))

print(plain_text)
