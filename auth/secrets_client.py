import json
import configs.env

with open(os.getenv('client_credentials_path'),'r') as f:
    secrets_dict = json.loads(f.read())

CLIENT_ID = secrets_dict.get('web').get('client_id')
CLIENT_SECRET = secrets_dict.get('web').get('client_secret')
AUTH_URI = secrets_dict.get('web').get('auth_uri')
TOKEN_URI = secrets_dict.get('web').get('token_uri')

# REDIRECT_URI = secrets_dict.get('web').get('redirect_uris')[0]
