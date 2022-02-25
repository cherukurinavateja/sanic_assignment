import hashlib

class Token:
    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password
    def generate_token(self):
        # Combine email and password as hash data
        data = self.email_id + self.password
        hash_data = data.encode('utf-8')
        # hash key generation
        token = hashlib.sha3_512(hash_data)
        return token.hexdigest() 