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
    