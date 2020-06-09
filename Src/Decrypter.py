#Decrypter V2.0
#
#good luck!

#Extracting Rotor arrays. 
Rotor_Data = open("Rotors", "rb") # open as binary

Rotors = [] # create empty array

Num = ord(Rotor_Data.read(1)) # first byte is number of rotors in file
Length = ord(Rotor_Data.read(1)) # second byte is length of rotors
Bytes = ord(Rotor_Data.read(1)) # read number of bytes used to store numbers

for i in range(0,Num): # for each rotor
    Rotors.append([]) # make an empty rotor
    for a in range(0,Length): # for each value
        #print(Rotor_Data.read(1))
        Rotors[i].append(int.from_bytes(Rotor_Data.read(Bytes), byteorder='big')) # read off <Byte> bytes to extract.

Rotor_Data.close() # close file

print("Welcome to Enigmatic Decrypter V2.0!")
Start = [int(i) for i in input("Start: ")[::-1]] #reads number, each digit is start position 
print("\n") # for readability

#sets all positions to 0 to start
Positions = [0] * len(Rotors)

#sets rotor positions to start positions 
for i in range(0,len(Start)):
    try:
        Positions[i] = Start[i] # sets Rotors to start positions 
    except IndexError:
        break
    

#opens encrypted message as binary
Encrypted = open("Encrypted", "rb")


Message = "" 


while True: # decrypts character at a time
    Num = int.from_bytes(Encrypted.read(Bytes), byteorder='big') # sets num to value of stored number
    
    if Num == 0: # if the file has ended
        break # finish

    Positions[0] += 1 # increments first rotor by one
    for i in range(0,len(Rotors)): # for each rotor
        if(Positions[i] >= len(Rotors[i])):# if a rotor reaches the end
            Positions[i] = 0 # reset it
            if(i + 1 < len(Rotors)): 
                Positions[i+1] += 1 # and increment next rotor

    for i in range(0,len(Rotors)): # for each rotor
        Num -= Rotors[i][Positions[i]] # subtracts number on each wheel

    
    while Num < 0: # loops over until the number fits the number of bytes used
        Num += 255 ** Bytes
    while Num > 255 ** Bytes:
        Num += -255 ** Bytes
        
    Message += chr(Num) # converts number to character and adds to message


    
Encrypted.close() # closes file
print(Message) # outputs message



