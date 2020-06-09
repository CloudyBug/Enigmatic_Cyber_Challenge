# Overview of Encryption
Takes text character at a time, converts to its ASCII number.
Number is then scrambled by adding numbers from several arrays of random numbers.
Arrays taken from Rotors file. 
Arrays are incremented so number added is unpredictable (first one +1, each increments the next after a full cycle). 
New scrambled numbers saved to file. 

Reverse by taking away the numbers from the Arrrays.

Arrays starting positions determined by user input, without the correct start positions you cannot Decrypt the Message. 


# Decrypter.py
The program that will be given to the user, it will decrypt the message if the correct settings are input.

# DecrypterBrute.py
Example solution, Decrypter.py modified to brute force the correct setting using a crib. 

# Encrpyter.py 
Encrypter program, included if you want to generate more/different messages. 

# RotorGenerator.py
Used to generate "Rotors" files of varying complexity and length to be used by the other programs. Included so you can adjust complexity of cipher if brute force is too fast/slow. 

# Message.txt 
Input taken by the Encrypter.

# Encrypted
The encrypted message (Binary file)

# Rotors
The numbers used to scramble the message. (Binary file)
