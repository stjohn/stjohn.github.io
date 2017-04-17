# decodeMessage.py
#     A program to decode the Python Challenge (2) message.
#     Each character must be mapped to the character 2 places ahead.

def main():
    offset = -2
    print("This program decodes a textual message")
    print("Each character is replaced with the character 2 places ahead in the alphabet.")
    print("The characters \"\'\", \".\", \"(\", \")\", and \" \" are not decoded.\n")  
    
    # Get the message to encode
    message = input("Please enter the message to decode: ")

    print("\nHere is the decoded message:")

    # decode the message 1 character at a time
    decodedMessage = ""
    for ch in message:
        if (ch == '.') or (ch == "'" ) or (ch == '(') or (ch == ')') or (ch == ' '):
            decodedMessage = decodedMessage + ch
        elif ord('a') <= ord(ch) <= ord('z'):
            codeNumber = ord('a') + ((ord(ch) - ord('a') - offset) % 26)
            decodedMessage = decodedMessage + chr(codeNumber)
        elif ord('A') <= ord(ch) <= ord('Z'):
            codeNumber = ord('A') + ((ord(ch) - ord('A') - offset) % 26)
            decodedMessage = decodedMessage + chr(codeNumber)
        elif ord('0') <= ord(ch) <= ord('9'):
            codeNumber = ord('0') + ((ord(ch) - ord('0') - offset) % 10)
            decodedMessage = decodedMessage + chr(codeNumber)     
        else:
            decodedMessage = decodedMessage + ch
        
    print("\nThe decoded message is:", decodedMessage)
    print()

main()
