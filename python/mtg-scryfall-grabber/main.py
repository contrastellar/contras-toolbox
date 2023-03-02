# https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3Aone&unique=prints

import os, requests, json, argparse

# Return a string object of the json passed in via obj
# !! (Likely) Unused
def jsonParse(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text

def main():

    # Current dir the script is running in, can be useful for debugging
    script_dir = os.path.abspath(os.path.dirname( __file__ ))

    description = "Script to pull card info from api.scryfall.com based on specific set"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('set', metavar='set') #set to pull card data from
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')

    # Parse arguments
    args = parser.parse_args()
    verboseSetting = bool(args.verbose)
    user_set = str(args.set)

    if(verboseSetting): print("Outputting verbosely\n"+script_dir)

    response_URL = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ user_set +"&unique=prints"
    responseData = requests.get(response_URL)

    if(verboseSetting): print("URL = " + str(response_URL))

    if(verboseSetting): print("Response code: " + str(responseData.status_code) + "\n")

    parsedFile = json.loads(jsonParse(responseData.json()))
    print(parsedFile['data'][0]['set_name'])

    print("\n\n--!-- Does output have \"next page\"?")
    print(parsedFile['has_more'])


if __name__ == "__main__":
    main()
