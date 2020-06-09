wyemine@ewales.me.uk

# Enigmatic
A cryptography/coding challenge designed to teach automated codebreaking and the use of cribs.

## Flag
Flag: L2Ioh1aG86T30iS

## Briefing
We have seized a USB drive containing a suspicious encrypted message. The decrypter has been included with the message, however, it needs the correct settings before it will work and there are just too many possibilites! We know the Message starts with "Weather" but we really need the rest! Can you decrypt the message?

By [username].

## Infrastructure
This challenge is all run client side once the files are downloaded.
It uses python 3.8.3 with no imported libraries and two binary files, and therefore should be runnable on any modern machine or VM.

## Risks
As all code is downloaded and then run client side and the only thing that the user needs to submit is the flag, I cannot see any security risk posed by this challenge. 

## Walkthrough
The user should take the python decrypter and modify it to brute force through settings, using the crib provided to find the correct setting.

See DecrypterBrute.py for a demonstration of how this could be done. 
