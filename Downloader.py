#!/usr/bin/env python

# Author: dspec13
# Date: 27 March 2020 

import os
import errno
from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup

# Create Directory to be imported into Kindle Comic Converter
try:
        os.mkdir("Dragon Ball Multiverse")
        print "Directory \"Dragon Ball Multiverse\" was created successfully!"
except OSError as e:
        if e.errno == errno.EEXIST:
                print "Directory \"Dragon Ball Multiverse\" already exists."
        else:
                raise

print "\nDownloading has commenced:"

# For pages 0 through 1714 of the Manga
for x in range(0, 1715):

        # Page 9 & 21 are non-existent (pages 8 and 20 are horizontal)
        # Pages 1000, 1190, 1232, & 1691 do not follow the same pattern & are hardcoded to download.
        if x != 9 and x != 21 and x != 1000 and x != 1190 and x != 1232 and x != 1691:
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


                newFileName = "Dragon Ball Multiverse/%d.png" % x
                urlretrieve(imageURL, filename=newFileName)
                
                print "Page %d Downloaded" % x
        elif x == 1000:
                urlretrieve("https://www.dragonball-multiverse.com/imgs/pages_1000/AlbertoCubatas.jpg", filename="Dragon Ball Multiverse/1000.png")
        elif x == 1190:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?comic=page&num=1190&lg=ono&ext=jpg&pw=c471809e2879b77e2a41ef3dcff35a7a", filename="Dragon Ball Multiverse/1190.png")
        elif x == 1232:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?comic=page&num=1232&lg=ono&ext=jpg&pw=0611d55d650fdc3fccc397fd24f414db", filename="Dragon Ball Multiverse/1232.png")
        elif x == 1691:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?comic=page&num=1691&lg=ono&ext=png&pw=d99d2823a5e87d6c128abb995758457a", filename="Dragon Ball Multiverse/1691.png")