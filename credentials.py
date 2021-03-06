class Credentials:
    
    """
    Class that creates new instance for credentials
    """
    credentials_list=[]#an empty credentials list
    
    def __init__(self,account,username,password):
        """
        new application and credentials are being generated
        """
        self.account=account
        self.username=username
        self.password=password
    
    def save_credentials(self):
        """
        save credentials in the credentials list
        """  
        Credentials.credentials_list.append(self) 
        
    def delete_credentials(self):
        """
        deletes a saved credential from the user list
        """ 
        Credentials.credentials_list.remove(self)
        
    @classmethod
    
    def find_by_acc(cls,account):
        """
        A method that takes an account name and returns the users credentials that matches the account name
        """
        for account_credentials in cls.credentials_list:
            if account_credentials.account == account:
                return account_credentials
            return False 
    
    @classmethod
    def  display_credentials(cls):
        """
        displays the list in the credential_list
        """ 
        return cls.credentials_list
    
    # @classmethod
    # def random_password(passwordLength=13):
    #     """
    #     generates random password for a user
    #     """ 
         
        
    #     password = string.ascii_letters + string.digits + '!@#$%^&*()'
    #     random.seed = (os.urandom(1024))

    #     return ''.join(random.choice(password) for i in range(passwordLength))                
    