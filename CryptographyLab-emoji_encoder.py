import io

def main(m):
    x = input('Your message: ')
    #input is a keyword in Python which prints out the prompt in the brackets
    #and allows the user to give keyboard letter and punctuation input
    #and submits it when the user presses the Enter key
    
    message = m

    if x == 'fin':
    #there needs to be a way to indicate that you are done entering your message
    #if you type fin as your input, the program will start encoding your message
           encode(message)
           #calls the function that encodes the message
           return
    else:
    #adds the new letter/word to your message
    # += means take what you already have, and make it equal to itself plus the new thing
    #for example, a = 4, a += 3 would make a == 7
        message += x
        
    main(message)
    #calls the function recursively so you can keep adding things to your message
    

def encode(word):
#this function is where the message is actually encoded
#your cipher goes here
    
    encryptedMessage = ""
    
    for letter in word:
        #checks each letter in the word that you want to encode
        if letter == 'a':
            encryptedMessage += '!2'
        #the encoded message will represent a's as this alarm clock symbol
        elif letter == 'b':
            encryptedMessage += '%3'
        elif letter == 'c':
            encryptedMessage += '#3'
        elif letter == 'd':
            encryptedMessage += '#2'
        elif letter == 'e':
            encryptedMessage += '#1'
        elif letter == 'f':
            encryptedMessage += '$2'
        elif letter == 'g':
            encryptedMessage += '%2'
        elif letter == 'h':
            encryptedMessage += '^2'
        elif letter == 'i':
            encryptedMessage += '*1'
        elif letter == 'j':
            encryptedMessage += '&2'
        elif letter == 'k':
            encryptedMessage += '*2'
        elif letter == 'l':
            encryptedMessage += '(2'
        elif letter == 'm':
            encryptedMessage += '&3'
        elif letter == 'n':
            encryptedMessage += '^3'
        elif letter == 'o':
            encryptedMessage += '(1'
        elif letter == 'p':
            encryptedMessage += ')1'
        elif letter == 'q':
            encryptedMessage += '!1'
        elif letter == 'r':
            encryptedMessage += '$1'
        elif letter == 's':
            encryptedMessage += '@2'
        elif letter == 't':
            encryptedMessage += '%1'
        elif letter == 'u':
            encryptedMessage += '&1'
        elif letter == 'v':
            encryptedMessage += '$3'
        elif letter == 'w':
            encryptedMessage += '@1'
        elif letter == 'x':
            encryptedMessage += '@3'
        elif letter == 'y':
            encryptedMessage += '^1'
        elif letter == 'z':
            encryptedMessage += '!3'

        elif letter == ' ':
            encryptedMessage += letter
        else:
            encryptedMessage += 'fine'
            
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
