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
        
    def delete_user(self):
        """
        deletes a saved contact from the user list
        """ 
        User.user_list.remove(self)
        
    @classmethod
    def check_user(cls,username):
        """
        method that runs in a user"s username  and returns a user that matches it
        """  
        for user in cls.user_list:
            if user.username == username:
             return user
         
    @classmethod
    def check_user_exists(cls,username,password): 
        """
        method that runs to check whether the user exists and confirms the password
        """ 
        user = cls.check_user(username)
        if user and user.password == password:
                return True
        return False     