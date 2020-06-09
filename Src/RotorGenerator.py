import random

num = int(input("Num of Rotors: "))
length = int(input("Length of Rotors: "))
Bytes = int(input("Complexity of Numbers (bytes): "))


Rotor_Data = open("Rotors", "wb")

Rotor_Bytes = bytearray(b'') # makes bytearray
Rotor_Bytes.append(num) # first byte is number of rotors
Rotor_Bytes.append(length) # second byte is length of rotors
Rotor_Bytes.append(Bytes) # third byte is number of bytes per number

for i in range(0,num): # for each rotor

    for a in range(0,length): # for each number
        #random num of right size added
        Rotor_Bytes += (random.randrange(0,256 ** Bytes)).to_bytes(Bytes, byteorder='big', signed=False)

Rotor_Data.write(bytes(Rotor_Bytes)) # writes to file
Rotor_Data.close()
