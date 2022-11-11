# In this assignment you will write a Python program similar to
# [http://www.py4e.com/code3/urllink2.py]. The program will use
# urllib to read the HTML from the data files below, and parse
# the data, extracting numbers and compute the sum of the numbers
# in the file.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# For urls with only https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# BeautifulSoup object connected to the url
url = 'http://py4e-data.dr-chuck.net/comments_1678824.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Gets all the numbers from span
tags = soup('span')
total = 0
for tag in tags:
    total += int(tag.contents[0])

# Prints the total
print(total)