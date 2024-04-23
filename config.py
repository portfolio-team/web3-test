from dotenv import load_dotenv
load_dotenv()

import os

INFURA_URL = os.getenv('INFURA_URL')
MY_ACCOUNT = os.getenv('MY_ACCOUNT')
GANACHE_URL = os.getenv('GANACHE_URL')
ACCOUNT_0 = os.getenv('ACCOUNT_0')
ACCOUNT_1 = os.getenv('ACCOUNT_1')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')