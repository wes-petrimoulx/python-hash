#Wes Petrimoulx
#Hasing with python

import hashlib

salt = "4jyt3jxc4hf49l8liobza6kj9gtwa873"
print("Please give an input to be hashed:")
strInput = input()
hashInput = strInput + salt
hashInput2 = salt + strInput
hashInput3 = strInput + salt[::-1]
hashInput4 = salt + strInput[::-1]
hashInput5 = strInput[::-1] + salt
hashInput6 = salt[::-1] + strInput
hashInput7 = strInput[::-1] + salt[::-1]
hashInput8 = salt[::-1] + strInput[::-1]

for x in range (0, 10):
    hashOutput = hashlib.sha512(hashInput.encode())
    hashInput = hashOutput.hexdigest()

for x in range (0, 10):
    hashOutput2 = hashlib.sha512(hashInput2.encode())
    hashInput2 = hashOutput2.hexdigest()

for x in range (0, 10):
    hashOutput3 = hashlib.sha512(hashInput3.encode())
    hashInput3 = hashOutput3.hexdigest()

for x in range (0, 10):
    hashOutput4 = hashlib.sha512(hashInput4.encode())
    hashInput4 = hashOutput4.hexdigest()

for x in range (0, 10):
    hashOutput5 = hashlib.sha512(hashInput5.encode())
    hashInput5 = hashOutput5.hexdigest()

for x in range (0, 10):
    hashOutput6 = hashlib.sha512(hashInput6.encode())
    hashInput6 = hashOutput6.hexdigest()

for x in range (0, 10):
    hashOutput7 = hashlib.sha512(hashInput7.encode())
    hashInput7 = hashOutput7.hexdigest()

for x in range (0, 10):
    hashOutput8 = hashlib.sha512(hashInput8.encode())
    hashInput8 = hashOutput8.hexdigest()

print("Here is your input hash:")
for x in range(0,1000):
    print(hashOutput.hexdigest() + hashOutput2.hexdigest() + hashOutput3.hexdigest() + hashOutput4.hexdigest() + hashOutput5.hexdigest() + hashOutput6.hexdigest() + hashOutput7.hexdigest() + hashOutput8.hexdigest(), end = '')
print("\n" + str(len(hashOutput.hexdigest() + hashOutput2.hexdigest() + hashOutput3.hexdigest() + hashOutput4.hexdigest() + hashOutput5.hexdigest() + hashOutput6.hexdigest() + hashOutput7.hexdigest() + hashOutput8.hexdigest()) * 1000))

