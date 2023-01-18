import os
import json
import dotenv

import requests

from oauthlib.oauth2 import MobileApplicationClient
from requests_oauthlib import OAuth2Session

from auth.secrets_client import AUTH_URI, TOKEN_URI, CLIENT_SECRET, CLIENT_ID


TASKS_URL = 'https://www.googleapis.com/tasks/v1/users/@me/'

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']

if __name__ == '__main__':
    
    oauth = OAuth2Session(
        client = MobileApplicationClient(
            client_id = CLIENT_ID
        ),
        scope = SCOPES[0],
        redirect_uri = 'https://localhost'
    )
    
    with open('auth/token.json', 'r') as f:
        stored_token = json.loads(f.read())
        
    refreshed_token = oauth.refresh_token(
        TOKEN_URI,
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        refresh_token=stored_token.get('refresh_token')
    )
    
    with open('auth/token.json', 'w') as f:
        f.write(json.dumps(refreshed_token))
        
    task_list_response = oauth.get(TASKS_URL + 'lists')
    
    print(json.loads(task_list_response.content))
        