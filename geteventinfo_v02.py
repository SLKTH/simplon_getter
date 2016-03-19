## GET EVENT INFO

import urllib
import htmllib
from BeautifulSoup import *
import re


# 'http://simplon.nl/events/benefietavond-hamelhuys'

## Remove tags function

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out

def unescape(s):
    s = s.replace("&lgt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last
    s = s.replace("&amp;", "&")
    return s


#    p = htmllib.HTMLParser(None)
#    p.save_bgn()
#    p.feed(s)
#    return p.save_end()

#def remove_tags(text):
#    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())


# try(url = raw_input('Enter - ')):
url =  'http://simplon.nl/events/def-p-30xpi-tour'
url = 'http://simplon.nl/events/benefietavond-hamelhuys'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
eventlinks = []

# Retrieve all of the anchor tags
# Get all links on the Simplon site

## Find all '<div class="date">'
date = soup('div', {'class':'date'})

event_date = date[0]

# Put all event links into a list
tags = soup('div', {'id':'event'})

## Get the tags
for tag in tags:
    event_title = tag.h1
    event_subtitle = tag.h2
    event_info = tag.td ## <<<< Get the class instead of <p> ???

content = soup('td', {'class':'content'})




# content_info = cont


## PRINT DATE AND EVENT NAME

print "Date:", event_date.getText()
print "Title:", event_title.getText()
print "Subtitle:", event_subtitle.getText()
print "\n"
print "Content:"

## GET EVENT INFO

for alinea in content:
    # print alinea.p.strong
    for alinea.p.strong in alinea:
         content_text = remove_html_markup(unicode(alinea.p.strong))
         print unicode(unescape(content_text).strip())



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
