#encrypter V2.0

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

print("Welcome to Enigmatic Encrypter V2.0!")
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

#reads data from file
Message_File = open("Message.txt", "r")
Message_String = Message_File.read()
Message_File.close()


Message_Bytes = bytearray(b'') 

for Character in Message_String: # encodes character by character
    Num = ord(Character) # converts from ASCII to number

    Positions[0] += 1 # increments first rotor by one
    for i in range(0,len(Rotors)): # for each rotor
        if(Positions[i] >= len(Rotors[i])):# if a rotor reaches the end
            Positions[i] = 0 # reset it
            if(i + 1 < len(Rotors)): 
                Positions[i+1] += 1 # and increment next rotor

    for i in range(0,len(Rotors)): # for each rotor
        Num += Rotors[i][Positions[i]] # adds number on each wheel


    while Num < 0: # loops over until the number fits the number of bytes used
        Num += 255 ** Bytes
    while Num > 255 ** Bytes:
        Num += -255 ** Bytes
        
    Message_Bytes += Num.to_bytes(Bytes, byteorder='big', signed=False) # adds number to bytearray
    
#print(Message_Bytes)
Out = open("Encrypted","wb") # opens output file as binary
Out.write(bytes(Message_Bytes)) # writes bytearray
Out.close()

print("Done!")

