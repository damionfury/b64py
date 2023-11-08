import sys, base64

capitalChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseChars = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "+/"

base64Chars = capitalChars + lowercaseChars + digits + symbols

def base64Encode(input):
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
        sys.exit("Error: Bad length binary string")

    for i in range(0,len(binaryString),6):
        bin = binaryString[i:i+6]
        dec = int(bin,2)
        outputString += base64Chars[dec]
        
    return outputString + pad

def base64Decode(string, outputType = "string"):
    output = bytearray()
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
        output += int(bin,2).to_bytes(1, byteorder='big')
        
    if outputType == "string":
        return output.decode()
    else:
        return output
    
# Tests –––––––––––––––––––––––––––––––
def testStringEncode():
    string = "Hello World"
    
    correctEncode = base64.b64encode(string.encode()).decode("utf-8")
    test = base64Encode(string)
    
    if test != correctEncode:
        print("❌ Encode string test")        
        return False
    else:
        print("✅ Encode string test")
        return True

def testStringDecode():
    string = "SGVsbG8gV29ybGQ="
    
    correctDecode = base64.b64decode(string.encode()).decode("utf-8")
    test = base64Decode(string, "string")
    
    if test != correctDecode:
        print("❌ Decode string test")
        return False
    else:
        print("✅ Decode string test")
        return True

def testByteEncode():
    testData = bytes.fromhex("db 0b e6 f4 83 4b fd 89 1c 59 eb 36 f4 82 48 c5")
    
    correctEncode = base64.b64encode(testData).decode("utf-8")
    test = base64Encode(testData)

    if test != correctEncode:
        print("❌ Encode byte test")
        return False
    else:
        print("✅ Encode byte test")
        return True
        
def testByteDecode():
    testData = "2wvm9INL/YkcWes29IJIxQ=="
    
    correctDecode = base64.b64decode(testData.encode())
    test = base64Decode(testData, "bytes")
    
    if test != correctDecode:
        print("❌ Decode bytes test")
        return False
    else:
        print("✅ Decode bytes test")
        return True

# Run test suite
def runTests():
    passCount = 0
    failCount = 0
    
    if testStringEncode():
        passCount += 1
    else:
        failCount += 1
        
    if testStringDecode():
        passCount += 1
    else:
        failCount += 1
        
    if testByteEncode():
        passCount += 1
    else:
        failCount += 1
        
    if testByteDecode():
        passCount += 1
    else:
        failCount += 1
        
    print("––––––––––––––––")
    print("Results:")
    print(f"✅ - {passCount}")
    print(f"❌ - {failCount}")

runTests()
