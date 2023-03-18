import subprocess
import os

#from dotenv import load_dotenv
#load_dotenv()

def getTOTP():
    print('Token  = ', os.getenv('FINVASIA_OTAP_TOKEN'))
    ## call date command ##
    p = subprocess.Popen(f"oathtool --totp -b {os.getenv('FINVASIA_OTAP_TOKEN')}", stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()
    p_status = p.wait()

    output = output.decode()
    output = output.strip()
    #print ("Command output : ", output)
    #print ("Command exit status/return code : ", p_status)
    return output

#print('Token = ', getTOTP())
