# https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3Aone&unique=prints

import os, requests, json

# Return a string object of the json passed in via obj
# !! (Likely) Unused
def jsonParse(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text


script_dir = os.path.abspath( os.path.dirname( __file__ ) )


