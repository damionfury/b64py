import sys, base64

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
        sys.exit("Error: Bad length binary string")

    for i in range(0,len(binaryString),6):
        bin = binaryString[i:i+6]
        dec = int(bin,2)
        outputString += base64Chars[dec]
        
    return outputString + pad

def base64Decode(string):
    output = ""
    binaryString = ""
    
    for char in string:
        if char != "=":
            dec = base64Chars.index(char)
            binaryString += f'{dec:06b}'
        else:
            binaryString = binaryString[0:len(binaryString)-2]
    
    if len(binaryString) % 8 > 0:
        # Length should be evenly divisible by 8
        print("Decoded binary is the wrong length. This should not happen.")
        print("String length: " + str(len(binaryString)))
        sys.exit("Error: Bad length binary string")
        
    for i in range(0,len(binaryString),8):
        bin = binaryString[i:i+8]
        dec = int(bin,2)
        output += chr(dec)
        
    return output

def testEncode(string):
    
    correctEncode = base64.b64encode(string.encode()).decode("utf-8")
    test = base64Encode(string)
    
    if test != correctEncode:
        print("Encode test failed.")
        print("Correct: " + correctEncode)
        print("Test: " + test)
    else:
        print("Encode test passed.")
        
def testDecode(string):
    
    correctDecode = base64.b64decode(string.encode()).decode("utf-8")
    test = base64Decode(string)
    
    if test != correctDecode:
        print("Decode test failed.")
        print("Correct: " + correctDecode)
        print("Test: " + test)
    else:
        print("Decode test passed.")

testText = "Hello World"
testB64 = "SGVsbG8gV29ybGQ="

testDecode(testB64)
