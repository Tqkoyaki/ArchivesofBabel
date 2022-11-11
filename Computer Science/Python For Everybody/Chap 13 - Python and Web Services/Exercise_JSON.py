# In this assignment you will write a Python program somewhat similar to
# [http://www.py4e.com/code3/json2.py]. The program will prompt for a URL,
# read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file
import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceURL = 'http://py4e-data.dr-chuck.net/comments_1678827.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(serviceURL, context=ctx).read()
data = json.loads(data)
data = data['comments']

total = 0
for result in data:
    total += int(result['count'])

print(total)
