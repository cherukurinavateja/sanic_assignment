from cache_data import cache_data
from create_token import Token

class User:
    # Constructor
    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password

    def create_user(self):
        # Default status message
        status_msg = "newly created"
        # Check if user exists
        if self.email_id in cache_data:
            status_msg = "existing"
            token = cache_data[self.email_id]
        else:
            token = Token(email_id = self.email_id, password = self.password).generate_token()
            cache_data[self.email_id] = token
            cache_data[token] = self.email_id
        # Output json construction
        response = {
            "status_msg": status_msg,
            "token": token
        }
        return response
        
