class User:
    """"
    class that generates new instance of user
    """
    
    user_list=[] #an empty user list
    
    def __init__(self,username,password):
    
   
        self.username=username
        self.password=password
    
    def save_user(self):
        """
        saves user in the user list
        """
        User.user_list.append(self)    