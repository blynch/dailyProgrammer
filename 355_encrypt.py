#!/usr/bin/python

import sys

if len(sys.argv) < 3:
   print "Requires 2 arguments:  Key StringToEncrypt"
   sys.exit(-1)

#print "Successfully received parameters"

#secret = "snitch"
#message = "thepackagehasbeendelivered"

secret = sys.argv[1]
message = sys.argv[2]

decrypt=False
if(len(sys.argv) > 3):
   decrypt=True

secret_extended = secret 


translation_key = "abcdefghijklmnopqrstuvwxyz";


# Build the snitch string string 
while (len(secret_extended) < len(message)):
   secret_extended = ''.join([secret_extended, secret]);

secret_compare = secret_extended[:len(message)] 

encrypted_letters = [] 

for i in range(0, len(message)):
   x_letter = message[i]
   y_letter = secret_compare[i]

   x_index = translation_key.find(x_letter)
   y_index = translation_key.find(y_letter)
   if decrypt:
      index = (x_index - y_index) % 26
   else:
      index = (x_index + y_index) % 26

   encrypted_letters.append(translation_key[index])

encrypted_string = ''.join(encrypted_letters)

print encrypted_string
   








