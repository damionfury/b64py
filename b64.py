import sys

inputString = "Hello World"

capitalChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseChars = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "+/"

base64Chars = capitalChars + lowercaseChars + digits + symbols

def base64Encode(string):
    outputString = ""
    binaryString = ""
    pad = ""

    # Convert to a long string of binary
    for char in string:
        binaryString += f'{ord(char):08b}'
        
    # Now determine if padding is needed
    remainder = len(binaryString) % 6

    # Wish python3.9 had switch case but maybe I'll move to 3.10 at some point

    if remainder == 4:
        # Need two more zeroes
        binaryString += "00"
        pad = "="
    elif remainder == 2:
        # Need four more zeroes
        binaryString += "0000"
        pad = "=="
    elif remainder % 2 == 1 :
        # Something went really wrong and we should stop
        print("Binary string is the wrong length. This should not happen.")
        print("String length: " + str(len(binaryString)))
        print(binaryString)
        sys.exit("Error: Bad length binary string")

    for i in range(0,len(binaryString),6):
        bin = binaryString[i:i+6]
        dec = int(bin,2)
        outputString += base64Chars[dec]
        
    return outputString + pad

print(base64Encode(inputString))