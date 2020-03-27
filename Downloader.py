#!/usr/bin/env python

# Author: dspec13
# Date: 27 March 2020 

from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup

# For pages 0 through 1714 of the Manga
for x in range(0, 1715):

        # Page 9 & 21 are non-existent (pages 8 and 20 are horizontal)
        # Page 1000 is special. Go to this link to choose yourself: https://www.dragonball-multiverse.com/en/page-1000.html#h_read
        if x != 9 and x != 21 and x != 1000
                # Save the HTML as a BeautifulSoup Object
                websiteToSearch = "https://www.dragonball-multiverse.com/en/page-%d.html#h_read" % x
                content = urlopen(websiteToSearch)
                read_content = content.read()
                soup = BeautifulSoup(read_content,'html.parser')

                # Save the line of code containing the URL to the image as a str
                lineContainingURL = str(soup.find(id="balloonsimg"))

                # Save the URL in a new string
                startingIndex = lineContainingURL.find("/image")

                # For some weird reason, the first page is formatted differently than the rest.
                # This if statement resolves this issue 
                if x:
                        endingIndex = lineContainingURL.rfind("\" title=")
                else:
                        endingIndex = lineContainingURL.rfind(");width")

                unfilteredURL = lineContainingURL[startingIndex:endingIndex]

                # Remove all occurences of amp; from url
                filteredURL = unfilteredURL.replace("amp;", "")        

                # Finally Store Real Image URL for Download
                imageURL = "https://www.dragonball-multiverse.com" + filteredURL


                newFileName = "Dragon Ball Multiverse/%d.png" % (x)
                urlretrieve(imageURL, filename=newFileName)
