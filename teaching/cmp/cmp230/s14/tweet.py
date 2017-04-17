import urllib.request
import json

response = urllib.request.urlopen("http://search.twitter.com/search.json?q=microsoft")
print(json.load(response))
