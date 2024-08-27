from main import return_backwards_string, get_mode
import unittest
import os

class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        self.assertEqual(return_backwards_string('hello'), 'olleh')
        self.assertEqual(return_backwards_string('hello world'), 'dlrow olleh')
        self.assertEqual(return_backwards_string('1234567890'), '0987654321')
    
    def test_get_env(self):
        self.assertEqual(os.getenv('MODE'), get_mode())

if __name__ == '__main__':
    unittest.main()