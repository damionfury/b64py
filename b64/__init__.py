import sys, base64

capitalChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseChars = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "+/"

base64Chars = capitalChars + lowercaseChars + digits + symbols

__all__ = ['encode','decode']

def encode(input):
    outputString = ""
    binaryString = ""
    pad = ""
    bytesIn = ""
    
    if type(input) == str:
        bytesIn = bytes(input, 'utf-8')
    else:
        bytesIn = bytes(input)

    # Convert to a long string of binary
    for byte in bytesIn:
        binaryString += f'{byte:08b}'
        
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
        raise ArithmeticError('Bad binary string length: Length is odd but must be even.') 

    for i in range(0,len(binaryString),6):
        bin = binaryString[i:i+6]
        dec = int(bin,2)
        outputString += base64Chars[dec]
        
    return outputString + pad

def decode(string, outputType = "string"):
    output = bytearray()
    binaryString = ""
    
    if outputType != "string" and outputType != "bytearray":
        raise ValueError('Bad output type: Must be "string" or "bytearray"')
    
    for char in string:
        if char != "=":
            try:
                dec = base64Chars.index(char)
            except:
                raise ValueError('Bad input string: Contains invalid characters')
            
            binaryString += f'{dec:06b}'
        else:
            binaryString = binaryString[0:len(binaryString)-2]
    
    if len(binaryString) % 8 > 0:
        # Length should be evenly divisible by 8
        print("Decoded binary is the wrong length. This should not happen.")
        print("String length: " + str(len(binaryString)))
        raise ArithmeticError('Bad binary string length: Must be evenly divisible by 8.')
        
    for i in range(0,len(binaryString),8):
        bin = binaryString[i:i+8]
        output += int(bin,2).to_bytes(1, byteorder='big')
        
    if outputType == "string":
        return output.decode()
    else:
        return output
