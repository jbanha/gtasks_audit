import dotenv
import os

# Loads data from .env file into os env
if '.env' in os.listdir():
    dotenv.load_dotenv('.env')
