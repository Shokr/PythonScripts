#!/usr/bin/env python2.7

# ASymmetric pub/pri

from Crypto.PublicKey import RSA


#################generate keys#########################
new_key = RSA.generate(4096)

private_key = new_key.exportKey("PEM")

public_key = new_key.publickey().exportKey("PEM")

print(private_key)
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print(public_key)
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

##############use generated keys########################
public_key_string = open("public_key.pem","r").read()
public_key = RSA.importKey(public_key_string)

private_key_string = open("private_key.pem","r").read()
private_key = RSA.importKey(private_key_string)



message = "Hello wonvjfs."

encrypted = public_key.encrypt(message, 32)

decrypted = private_key.decrypt(encrypted)


print("---------encrypted data--------------")
print(encrypted)
print("---------decrypted data----------------")
print(decrypted)
