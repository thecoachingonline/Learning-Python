#!/usr/bin/env python3

import json
obj = json.loads('{"gold": 1271,"silver": 1284,"platinum": 1270}')
print(obj['gold'])

import json
import urllib.request

# download raw json object
url = "https://api.gdax.com/products/BTC-EUR/ticker"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)

# output some object attributes
print('$ ' + obj['price'])
print('$ ' + obj['volume'])