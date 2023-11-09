import unittest,base64

import b64

class TestDecode(unittest.TestCase):
    def test_string(self):
        string = "SGVsbG8gV29ybGQ="
        correctDecode = base64.b64decode(string.encode()).decode("utf-8")
        test = b64.decode(string, "string")
        
        self.assertEqual(correctDecode,test)
        
    def test_byte(self):
        testData = "2wvm9INL/YkcWes29IJIxQ=="
        correctDecode = base64.b64decode(testData.encode())
        test = b64.decode(testData, "bytearray")
        
        self.assertEqual(correctDecode,test)
    
    def test_bad_output_type(self):
        string = "SGVsbG8gV29ybGQ="
        
        self.assertRaises(ValueError,b64.decode, string, "dict")
        
        
if __name__ == '__main__':
    unittest.main()