# In this assignment you will write a Python program somewhat similar to
# [http://www.py4e.com/code3/geoxml.py]. The program will prompt for a URL,
# read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceURL = 'http://py4e-data.dr-chuck.net/comments_1678826.xml'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xml = urllib.request.urlopen(serviceURL, context=ctx).read()
tree = ET.fromstring(xml)
results = tree.findall('comments/comment')

total = 0
for result in results:
    total += int(result.find('count').text)

print(total)
