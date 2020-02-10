#Wes Petrimoulx
#Hasing with python

import hashlib

print("Please give and input to be hashed:")
strInput = input()

hashOutput = hashlib.sha256(strInput.encode())

print("Here is your input hash in SHA-256:")
print(hashOutput.hexdigest())
