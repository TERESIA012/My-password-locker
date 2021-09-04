import unittest
from credentials import Credentials #from credentials import class Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        """
        setup method to run each Testcase
        """
        self.new_credentials=Credentials("facebook","terry012","passLock")
