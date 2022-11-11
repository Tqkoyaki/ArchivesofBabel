# In this assignment you will write a Python program that expands on
# [http://www.py4e.com/code3/urllink2.py]. The program will use urllib to read the HTML
# from the data files below, extract the href= vaues from the anchor tags, scan for a tag
# that is in a particular position relative to the first name in the list, follow that
# link and repeat the process a number of times and report the last name you find.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Gets the url and the number of times to repeat
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos - 1].get('href', None)

print(re.findall('known_by_(.+).html', url)[0])


