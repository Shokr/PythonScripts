from Crypto.Cipher import AES
import hashlib
import sys
import binascii


plaintext='hello how are you?'
password='qwerty123'


if (len(sys.argv)>1):
  plaintext=(sys.argv[1])
if (len(sys.argv)>2):
  password=(sys.argv[2])

def encrypt(plaintext,key, mode):
  encobj = AES.new(key, AES.MODE_GCM)
  ciphertext,authTag=encobj.encrypt_and_digest(plaintext)
  return(ciphertext,authTag,encobj.nonce)

def decrypt(ciphertext,key, mode):
  (ciphertext,  authTag, nonce) = ciphertext
  encobj = AES.new(key,  mode, nonce)
  return(encobj.decrypt_and_verify(ciphertext, authTag))

key = hashlib.sha256(password.encode()).digest()

print("GCM Mode: Stream cipher and authenticated")
print("\nMessage:\t",plaintext)
print("Key:\t\t",password)


ciphertext = encrypt(plaintext.encode(),key,AES.MODE_GCM)

print("Cipher:\t\t",binascii.hexlify(ciphertext[0]))
print("Auth Msg:\t",binascii.hexlify(ciphertext[1]))
print("Nonce:\t\t",binascii.hexlify(ciphertext[2]))


res= decrypt(ciphertext,key,AES.MODE_GCM)


print ("\n\nDecrypted:\t",res.decode())
