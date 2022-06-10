# Example connection to an API to grab info
# Author: Gabriella Agathon
# Using the http://fakestoreapi.com/ site + docs

# Import request and json in order to 
# grab information from an API in the form of json
import requests, json

# Return a string object of the json passed in via obj
# !! Unused
def jsonParse(obj):
    text = json.dumps(obj, sort_keys=True, indent = 3)
    return text

# Grab the info from the API via a 'get' request
response_API = requests.get('http://fakestoreapi.com/products')

# Print the response code from the API
# This pulls the response code from the GET request
# '200' -> good response
print("Response code: " + str(response_API.status_code) + "\n")

# !! unused
parsedFile = json.loads(jsonParse(response_API.json()))

# Iterate through the api response, showing id, category
# of item and the 'name' of the itme
"""
The response_API.json() 'object' is a json object that is iterable, 
allowing a for-loop to be iterated across it
"""
for d in response_API.json():
    out = "id: " + str(d["id"]) + " (" + d["category"] + ") " + d["title"]
    print(out)


# Exit the script
exit()
