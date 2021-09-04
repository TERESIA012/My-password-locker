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
        
    def test_save_credentials(self):
        """
        test whether credentials are saved in the credentials_list
        """ 
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self): 
        """
        clears up after every test is done
        """ 
        Credentials.credentials_list=[]    
