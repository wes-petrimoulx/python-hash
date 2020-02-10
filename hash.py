#Wes Petrimoulx
#Hasing with python

import hashlib

salt = "4jyt3jxc4hf49l8liobza6kj9gtwa873"

print("Please give and input to be hashed:")
strInput = input() + salt

hashOutput = hashlib.sha256(strInput.encode())

print("Here is your input hash in SHA-256:")
print(hashOutput.hexdigest())
