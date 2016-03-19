## GET EVENT INFO


import urllib
from BeautifulSoup import *
import re

url = raw_input('Enter - ') # 'http://simplon.nl/events/benefietavond-hamelhuys'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
eventlinks = []

# Retrieve all of the anchor tags
# Get all links on the Simplon site


# Put all event links into a list
tags = soup('div', {'id':'event'})

## Find all '<div class="date">'
date = soup('div', {'class':'date'})
event_date = date[0]

## Get the tags

for tag in tags:
    event_title = tag.h1
    event_info = tag.p ## <<<< Get the class instead of <p> ???

    print event_info


## PRINT DATE AND EVENT NAME

print "Date:", event_date.getText()
print "Title:", event_title.getText()
print "\n"
print "Title:"

## GET EVENT INFO

print event_info

## DIR FUNC    print dir(tag.div['id'])
#    print tag.div['id'].startswith('event-title')



# for ids in tag['id']:


## GET ARTIST
# print tag.h1

# GET EVENT INFORMATION
# print tag.p




#    if "events" in str(tag):
#         eventlinks.append(tag.get('href'))
# set_eventlinks = set(eventlinks)
## Get all events out of event link list

for eventlink in eventlinks:
    print eventlink




# for link in links:
    # print link[0]
