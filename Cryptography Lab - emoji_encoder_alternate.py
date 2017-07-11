# -*- coding: utf-8 -*-
import io
#symbols list and letters list are missing --> WILL NOT RUN

def main(m):
    x = input('Some input: ')
    #input is a keyword in Python which prints out the prompt in the brackets
    #and allows the user to give keyboard letter and punctuation input
    #and submits it when the user presses the Enter key
    
    message = m

    if x == 'fin':
           encode(message)
           return
    else:
        message += x
        
    main(message)
    

def encode(word):
    encryptedMessage = ""
    #need a list of all the letters accepted by the encoder
    #need a list of their corresponding symbols]
    #these lists need to be of the same length
    for letter in word:
       encryptedMessage += symbols[letters.index(letter)]
       #to read this, go from the inside out:
       #take the current letter, and find its index in the list of all letters in your alphabet
       #take that index, and find the character at that index in the list of the symbols in your cipher

    toFile(encryptedMessage)
    #we are going to send the coded message to a file
    #this is so that the message and the coded version won't be viewed together, so the secret won't be given away
    #this is only necessary if your cipher creates text


def toFile(text):
    encryptedMessage = text
    #the message is the text that was passed to this function
    filename = 'message.txt'
    #name of the file where the message will be
    encoding = 'utf-8'
    #ensures that the unicode characters will show up properly in the file
    #only necessary if you ar eusing unicode characters

    with io.open(filename, 'w', encoding=encoding) as file:
        file.write(encryptedMessage)
        #write the message in the file


    #if not using Unicode or other special characters, use the following to write to a file:
    #message = open(filename, 'w')
    #print(encryptedMessage, message)
    #message.close()   
        
    

main("")
