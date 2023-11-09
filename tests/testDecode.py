import unittest,base64

import b64

class TestDecode(unittest.TestCase):
    def test_string(self):
        string = "SGVsbG8gV29ybGQ="
        correctDecode = base64.b64decode(string.encode()).decode("utf-8")
        test = b64.decode(string, "string")
        
        print('Test: Decode valid string as string')
        self.assertEqual(correctDecode,test)
        
    def test_byte(self):
        testData = "2wvm9INL/YkcWes29IJIxQ=="
        correctDecode = base64.b64decode(testData.encode())
        test = b64.decode(testData, "bytearray")
        
        print('Test: Decode valid string as bytearray')
        self.assertEqual(correctDecode,test)
    
    def test_bad_output_type(self):
        string = "SGVsbG8gV29ybGQ="
        
        print('Test: Decode valid string with invalid output type')
        self.assertRaises(ValueError,b64.decode, string, "dict")
        
    def test_bad_input_string(self):
        string = "$bad$"
        
        print('Test: Decode invalid string')
        self.assertRaises(ValueError,b64.decode, string)
        
if __name__ == '__main__':
    unittest.main()