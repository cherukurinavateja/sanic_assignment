from caching import Cache
import re

class Utils:
    # Email id validation
    def validate_email(email_id):
        # Regular expression for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email_id)):
            return True
        else:
            return False   
    # Retrieve token from without prefix
    def token_without_prefix(auth_token):
        auth_token = auth_token.split(" ")
        token = None
        if len(auth_token) == 2:
            token = auth_token[1]
            status = True
        else:
            status = False
        response = {
            "token": token,
            "is_present": status
        }
        return response
    # Check if valid token or not
    def is_token_valid(auth_token):
        #Default value
        is_valid = False
        # Get token without prefix
        token_without_prefix = Utils.token_without_prefix(auth_token=auth_token)
        # Check if token is not empty
        if token_without_prefix.get("is_present"):
            token = token_without_prefix.get("token")
            # Check if token in cache
            is_valid = Cache.is_key_in_cache(token)
        return is_valid


