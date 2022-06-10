# Basic script to bounce off the akami api, returning a response code
# Author: Gabby Stimac
# ======
# There's a non-zero chance that the akami API will reject any access
# even with a valid key, because this script hasn't been tested 
# from inside the sentry IPv4 block
# ======
# Imports
import requests, json
import argparse

# Declare arguments
parser = argparse.ArgumentParser(description='Basic script to bounce off the akami api, returning a response code')
parser.add_argument('credential_file', metavar='credential_file')
args = parser.parse_args()

# Open the credential file
credFile = open('akami-access.json')
credData = json.load(credFile)
credFile.close()

# Fliter the json information down to usable variables
client_secret = credData['client_secret']
host = credData['host']
access_token = credData['access_token']
client_token = credData['client_token']
