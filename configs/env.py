import dotenv
import os

if '.env' in os.listdir():
    dotenv.load_dotenv('.env')
