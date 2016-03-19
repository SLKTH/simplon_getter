
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re

url = 'http://www.simplon.nl' # raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


# Retrieve all of the anchor tags
# tags = soup('a')
tags = soup.find_all('a', href=re.compile('events'))

for tag in tags:
    x = tag.get('href', None)
    b = tag.get('title')
    print b, '-----', x



# for link in links:
    # print link[0]
