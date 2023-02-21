import requests
import json
import serpapi_keys
from serpapi import GoogleSearch
import csv

params = {
    "q": "fencing contractors",
    "location": "Atlanta,Georgia",
    "tbm": "lcl",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "api_key": "2138236ad96418651468b24b36957924069897ad7a89cc3931421218140d902e",
}

search = GoogleSearch(params)
results = search.get_json()

print(results)
outfile = open("serp_results.json", "w")
json.dump(results, outfile, indent=5)
