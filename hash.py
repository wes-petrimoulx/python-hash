#Wes Petrimoulx
#Hasing with python

import hashlib

salt = "4jyt3jxc4hf49l8liobza6kj9gtwa873"
print("Please give an input to be hashed:")
strInput = input() + salt
hashOutput = hashlib.sha512(strInput.encode())

print("Here is your input hash:")
print(hashOutput.hexdigest())
