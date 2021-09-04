import unittest
from credentials import Credentials #from credentials import class Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        """
        setup method to run each Testcase
        """
        self.new_credentials=Credentials("facebook","terry012","passLock")
        
    def test_init(self): 
        """
        test if object is initialized well
        """ 
        self.assertEqual(self.new_credentials.account,"facebook")
        self.assertEqual(self.new_credentials.username,"terry012") 
        self.assertEqual(self.new_credentials.password,"passLock") 
