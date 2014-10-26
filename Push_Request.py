import requests
import pprint
import json

url = 'https://go.urbanairship.com/api/push/'
payload = {'notification' : {'alert' : 'Hello!'}, 'device_types' : ['ios']}}
headers = {'<application key>:<master secret>', 'Accept' : 'application/vnd.urbanairship+json; version=3;', 'Content-Type' : 'application/json'}
r = requests.post

print r