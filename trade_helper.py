import os
from dotenv import load_dotenv
import mfa

def initilizeEnvironment():
    #load auth parameters from .env file
    load_dotenv()


initilizeEnvironment()

print('User Name = ', os.getenv('FINVASIA_USER_ID'))

mfa.getTOTP()
