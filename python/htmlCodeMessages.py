# Script to fetch an html code and then return the associated message
# author: Gabriella Agathon (contrastellar), 2022
# based upon RFC 7231 (fetched 06/10/2022) https://datatracker.ietf.org/doc/html/rfc7231#section-6
# =====
# imports
import json, argparse, os

codeFileName = '/html-codes.json'

def returnCodeMsg(code):
    code = str(code)
    cwd = os.path.abspath(os.path.dirname(__file__))
    codeFile = open(cwd + codeFileName)  # Open html-codes.json
    codeData = json.load(codeFile)      # At this point, the data is loaded in memory 
    codeFile.close()                    # and we can close read access on this file
    return(str(codeData[code]['message']))

def main():
    # Declare arguments
    parser = argparse.ArgumentParser(description='Script to return the message of an HTML response code.')
    parser.add_argument('html_code', metavar='code')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    
    args = parser.parse_args()
    verboseSetting = bool(args.verbose)
    htmlCode = str(args.code)

    codeFile = open('html-codes.json')  # Open html-codes.json
    codeData = json.load(codeFile)      # At this point, the data is loaded in memory 
    codeFile.close()                    # and we can close read access on this file

    # The core of this script is this line here, I think
    print(codeData[htmlCode]['message'])


if __name__ == "__main__":
    main()
