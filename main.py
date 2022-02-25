from sanic import Sanic
from sanic.response import json
from utils import Utils
from user import User
from caching import Cache


app = Sanic("user_authentication")

@app.route('/login', methods=["POST"])
async def create_user(request):
    #Default status code
    status_code = 201
    # Parameters json
    params = request.json
    # Validating if keys are present
    if "email" not in params or "password" not in params:
        return json({'status_msg': 'email or password missing'}, status=400)
    # Retrieve parameters
    email_id = params["email"]
    password = params["password"]
    # Validate email
    valid_email = Utils.validate_email(email_id)
    if not valid_email:
        return json({'status_msg': 'invalid email'}, status=400)
    #create user
    user_creation_response = User(email_id=email_id, password=password).create_user()
    if user_creation_response.get("status_msg") == "existing":
        status_code = 409
    return json(user_creation_response, status=status_code)

@app.route('/get_data', methods=["GET"])
async def get_user_data(request):
    # Default status message
    status_msg = "success"
    status_code = 200
    # Retrieve token from headers
    auth_token = request.headers.get('authorization')
    if auth_token is None:
        return json({"status_msg":"invalid"}, status=401)
    istoken_valid = Utils.is_token_valid(auth_token=auth_token)
    if not istoken_valid:
        status_code = 401
        status_msg = "invalid"
    return json({"status_msg":status_msg}, status=status_code)

@app.route('/post_data', methods=["POST"])
async def post_data(request):
    # Default status message
    status_msg = "success"
    status_code = 201
    # Retrieve token from headers
    auth_token = request.headers.get('authorization')
    if auth_token is None:
        return json({"status_msg":"invalid"}, status=401)
    istoken_valid = Utils.is_token_valid(auth_token=auth_token)
    if not istoken_valid:
        status_code = 401
        status_msg = "invalid"
    return json({"status_msg":status_msg}, status=status_code)

@app.route('/delete_data', methods=["DELETE"])
async def delete_data(request):
    # Default status
    status_code = 200
    # Retrieve token from headers
    auth_token = request.headers.get('authorization')
    if auth_token is None:
        return json({"status_msg":"invalid"}, status=401)
    # Get token without prefix
    token_without_prefix = Utils.token_without_prefix(auth_token=auth_token)
    token = token_without_prefix.get("token")
    #Get email for token
    email = Cache.get_val_in_cache(token)
    Cache.delete_key_in_cache(email)
    Cache.delete_key_in_cache(token)
    response = {
        "status_msg": "success"
    }
    return json(response, status=status_code)

if __name__ == '__main__':
    app.run(debug=True)