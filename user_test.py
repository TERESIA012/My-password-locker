import unittest #importing the unnitest
from user import User #importing the user Class from the user module

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        setUp method runs before the tests
        """
        self.new_user=User("Tess012","passWord") #create user object
        
    def test_init(self):
        """
        test_init test case to test the initialization
        """
    
        self.assertEqual(self.new_user.username,"Tess012")
        self.assertEqual(self.new_user.password,"passWord") 
        
    def test_save_user(self) :
        """
        test_save_user to test whether the user is saves in the user list
        """
        self.assertEqual(len(User.user_list),0)  
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)        
        