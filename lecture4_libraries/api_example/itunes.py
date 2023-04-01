import requests as r
import json
import sys

if len(sys.argv) != 2:
    sys.exit()
else:
    response = r.get(
        url='https://itunes.apple.com/search',
        params={'entity': 'song', "limit": 1, "term": sys.argv[1]}
    )

o = response.json()

for r in o["results"]:
    print(r["trackName"])
print(o)
