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
        
    def test_multiple_credentials(self):
        """
        tests whether we can save multiple credentials in the credentials list
        """
        self.new_credentials.save_credentials()
        test_credentials=Credentials("facebook","tess012","passWORD")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def  test_delete_credentials(self):
        """
        tests whether credentials can be removed from the credentials_list
        """ 
        self.assertEqual(len(Credentials.credentials_list),0)  
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        self.new_credentials.delete_credentials() 
        
    def  test_find_by_account(self): 
        """
        tests whether a user can find account using account name
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook","tess012","passWORD") # new credentials 
        test_credentials.save_credentials() 
        
        found_credentials=Credentials.find_by_acc("account")
        # self.assertEqual(found_credentials.account,test_credentials.account)              
