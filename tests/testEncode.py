import unittest,base64

import b64

class TestEncode(unittest.TestCase):
    def test_string(self):
        string = "Hello World"
        correctEncode = base64.b64encode(string.encode()).decode("utf-8")
        test = b64.encode(string)
        
        self.assertEqual(correctEncode,test)
        
    def test_byte(self):
        testData = bytes.fromhex("db 0b e6 f4 83 4b fd 89 1c 59 eb 36 f4 82 48 c5")
        correctEncode = base64.b64encode(testData).decode("utf-8")
        test = b64.encode(testData)
        
        self.assertEqual(correctEncode,test)
        
if __name__ == '__main__':
    unittest.main()