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

    # Used to verify that the two sets are actually identical.
    cardSetURL = "https://api.scryfall.com/sets/" + user_set

    cardListURL = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ user_set +"&unique=prints"

    setData = requests.get(cardSetURL)
    responseData = requests.get(cardListURL)

    if(verboseSetting): print("Set URL  =   " + str(cardSetURL))
    if(verboseSetting): print("Card URL =   " + str(cardListURL))

    if(verboseSetting): print("Response code: " + str(responseData.status_code) + "\n")

    parsedSetFile = json.loads(jsonParse(setData.json()))
    parsedCardFile = json.loads(jsonParse(responseData.json()))

    print("Card set from the set search ...  ? -> " + parsedSetFile['name'])

    print("Card set from the card ID    ... " + parsedCardFile["data"][0]["collector_number"] + "? -> "+ parsedCardFile['data'][0]['set_name'])

    setNameFromSearch = parsedSetFile['name']
    setNameFromCard = parsedCardFile['data'][0]['set_name']

    if(verboseSetting):
        print("Are strings the same?")
        if(setNameFromCard == setNameFromSearch):
            print("Yes!")
        else:
            print("No!")

    print("\n\n--!-- Does output have \"next page\"?")
    print(parsedCardFile['has_more'])


if __name__ == "__main__":
    main()
