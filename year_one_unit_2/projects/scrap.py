import requests
import json
url = "https://api.nasa.gov/DONKI/FLR?startDate=2002-03-19&endDate=2003-03-19&api_key=UomAnqCtf0OUMEnTMdbgOLc8cMWSynVjk9A5kQ0p"
info = requests.get(url).json()

body = info["data"]["children"][0]
print(body["data"]["body"][0])
