
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re

url = 'http://www.simplon.nl' # raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
eventlinks = []

# Retrieve all of the anchor tags
# Get all links on the Simplon site


# Put all event links into a list

tags = soup('a')
for tag in tags:
    if "events" in str(tag):
         eventlinks.append(tag.get('href'))

## Get all events out of event link list

for eventlink in eventlinks:
    print eventlink




# for link in links:
    # print link[0]
