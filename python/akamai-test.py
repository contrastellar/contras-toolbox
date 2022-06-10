# Basic script to bounce off the akamai api, returning a response code
# Author: Gabby Stimac
# ======
# There's a non-zero chance that the akamai API will reject any access
# even with a valid key, because this script hasn't been tested 
# from inside the sentry IPv4 block
# ======
# Imports
import requests, json
from logging import debug
from akamai.edgegrid import EdgeGridAuth
from urllib.parse import urljoin
import argparse

# Declare arguments
parser = argparse.ArgumentParser(description='Basic script to bounce off the akamai api, returning a response code')
parser.add_argument('credential_file', metavar='credential_file', type=str)
parser.add_argument('-v', '--verbose', help="increase output verbosity", action='store_true')
args = parser.parse_args()
verboseSetting = args.verbose

debug('Opening file ' + args.credential_file)
if verboseSetting:
    print('Opening file ' + args.credential_file)

# Open the credential file
credFile = open(args.credential_file)
credData = json.load(credFile)
credFile.close()
if verboseSetting:
    print('File has been closed')

# Fliter the json information down to usable variables
host = credData['host']
file_client_token = credData['client_token']
file_client_secret = credData['client_secret']
file_access_token = credData['access_token']
debug("Connecting to " + host)

# start API request
s = requests.session()
s.auth = EdgeGridAuth(
    client_token = file_client_token,
    client_secret = file_client_secret,
    access_token = file_access_token
)

apiResult = s.get(urljoin(host, '/contract-api/v1/contracts/identifiers'))
print("Status code: " + str(apiResult.status_code))
exit
