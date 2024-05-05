#!/usr/bin/env python

# Author: dspec13
# Reviser: Timboman
# Date: 05 April 2024 

import os
import errno
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

print("                                    _           _ _     __     __ ")
print("  ____                             | |         | | |   |  \\   /  |")
print(" |  _ \ _ __ __ _  __ _  ___  _ __ | |__   __ _| | |   |   \\ /   |")
print(" | | | | '__/ _` |/ _` |/ _ \\| '_ \\| '_ \\ / _` | | |   |  |` `|  |")
print(" | |_| | | | (_| | (_| | (_) | | | | |_) | (_| | | |   |  |   |  |")
print(" |____/|_|  \\__,_|\\__, |\\___/|_| |_|_.__/ \\__,_|_|_|   |__|   |__|")
print("                   __/ |")                            
print("                  |___/")                       
print("     ____                      _                 _")
print("    |  _ \  __ __      _ _ __ | | ___   __ _  __| | ___  _ __ ")
print("    | | | |/ _ \\ \\ /\\ / | '_ \\| |/ _ \\ / _` |/ _` |/ _ \\| '__| ") 
print("    | |_| | (_)|\\ V  V /| | | | | (_) | (_| | (_| |  __/| |   ")
print("    |____/ \\___/ \\_/\\_/ |_| |_|_|\\___/ \\__,_|\\__,_|\\___||_| ")
print("                                                            -by dspec13\n")
print("                                                   -Revised by Timboman")


# Create Directory to be imported into Kindle Comic Converter
try:
        os.mkdir("Dragon Ball Multiverse")
        print("Directory \"Dragon Ball Multiverse\" was created successfully!")
except OSError as e:
        if e.errno == errno.EEXIST:
                print("Directory \"Dragon Ball Multiverse\" already exists.")
        else:
                raise

print("\nBeginning Downloads:")

# For Every Page of the Manga
currentNumberOfPagesPublished = 2334
for x in range(0, currentNumberOfPagesPublished + 1):

        # Page 9 & 21 are non-existent (pages 8 and 20 are horizontal double spreads on one image), later double pages don't use up multiple page numbers
        # Many other pages follow a non-standard sytax for the URL so this filters them to use a slightly different parsing
		# Some pages are hardcoded since they too have a rarer URL format that is not worth creating a new filter for
        if x != 0 and x != 9 and x != 21 and x != 1000 and x != 1190 and x != 1232 and x != 1691 and x != 1736 and x != 1840 and x != 1854 and x != 1864 and x != 1870 and x != 1879 and x != 1896 and x != 1899 and x != 1900 and x != 1904 and x != 1906 and x != 1906 and x != 1907 and x != 1908 and x != 1909 and x != 1910 and x != 1911 and x != 1930 and x != 1938 and x != 1940 and x != 1944 and x != 2000 and x != 2008 and x != 2010 and x != 2012 and x != 2033 and x != 2045 and x != 2053 and x != 2056 and x != 2128 and x != 2167 and x != 2168 and x != 2171 and x != 2172 and x != 2173 and x != 2174 and x != 2175 and x != 2176 and x != 2177 and x != 2178 and x != 2179 and x != 2180 and x != 2181 and x != 2182 and x != 2183 and x != 2184 and x != 2185 and x != 2186 and x != 2187 and x != 2188 and x != 2190 and x != 2238 and x != 2239 and x != 2243 and x != 2245 and x != 2246 and x != 2247 and x != 2248 and x != 2249 and x != 2250 and x != 2252 and x != 2253 and x != 2254 and x != 2255 and x != 2258 and x != 2259 and x != 2260 and x != 2261 and x != 2262 and x != 2264 and x != 2266 and x != 2272 and x != 2284 and x != 2286 and x != 2287 and x != 2289 and x != 2296 and x != 2306 and x != 2307 and x != 2312 and x != 2320 and x != 2326:
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

                # Remove all occurences of amp; and spaces from url
                filteredURLA = unfilteredURL.replace("amp;", "")        
                filteredURL = filteredURLA.replace(" ","")        

                # Finally Store Real Image URL for Download
                imageURL = "https://www.dragonball-multiverse.com" + filteredURL


                newFileName = "Dragon Ball Multiverse/%d.png" % x
                urlretrieve(imageURL, filename=newFileName)
                
                print("Page %d Downloaded" % x)
        elif x == 0:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?idp=1000000&lg=en&ext=jpg&pw=1b25cd99393af52ddfb55f355ced4e58", filename="Dragon Ball Multiverse/0.png")
        elif x == 9 or x == 21:
                print("Dummy Page")
        elif x == 1000:
                urlretrieve("https://www.dragonball-multiverse.com/imgs/pages_1000/AlbertoCubatas.jpg", filename="Dragon Ball Multiverse/1000.png")
        elif x == 1190:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?comic=page&num=1190&lg=ono&ext=jpg&pw=c471809e2879b77e2a41ef3dcff35a7a", filename="Dragon Ball Multiverse/1190.png")
        elif x == 1232:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?comic=page&num=1232&lg=ono&ext=jpg&pw=0611d55d650fdc3fccc397fd24f414db", filename="Dragon Ball Multiverse/1232.png")
        elif x == 1691:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?comic=page&num=1691&lg=ono&ext=png&pw=d99d2823a5e87d6c128abb995758457a", filename="Dragon Ball Multiverse/1691.png")
        elif x == 1736:
                urlretrieve("https://www.dragonball-multiverse.com/image.php?idp=1001736&lg=ono&ext=png&pw=8c9cd19a72243397b0c3f4ae97a71dc7", filename="Dragon Ball Multiverse/1736.png")
        elif x == 2000:
                urlretrieve("https://www.dragonball-multiverse.com/imgs/pages_2000/Asura.jpg", filename="Dragon Ball Multiverse/2000.png")
        elif x == 2312:
                urlretrieve("https://www.dragonball-multiverse.com/imgs/pages_2312/Gogeta%20Jr.jpg", filename="Dragon Ball Multiverse/2312.png")
        elif x == 1840 or x == 1854 or x == 1864 or x == 1870 or x == 1879 or x == 1896 or x == 1899 or x == 1900 or x == 1904 or x == 1906 or x == 1906 or x == 1907 or x == 1908 or x == 1909 or x == 1910 or x == 1911 or x == 1930 or x == 1938 or x == 1940 or x == 1944 or x == 2008 or x == 2010 or x == 2012 or x == 2033 or x == 2045 or x == 2053 or x == 2056 or x == 2128 or x == 2167 or x == 2168 or x == 2171 or x == 2172 or x == 2173 or x == 2174 or x == 2175 or x == 2176 or x == 2177 or x == 2178 or x == 2179 or x == 2180 or x == 2181 or x == 2182 or x == 2183 or x == 2184 or x == 2185 or x == 2186 or x == 2187 or x == 2188 or x == 2190 or x == 2238 or x == 2239 or x == 2243 or x == 2245 or x == 2246 or x == 2247 or x == 2248 or x == 2249 or x == 2250 or x == 2252 or x == 2253 or x == 2254 or x == 2255 or x == 2258 or x == 2259 or x == 2260 or x == 2261 or x == 2262 or x == 2264 or x == 2266 or x == 2272 or x == 2284 or x == 2286 or x == 2287 or x == 2289 or x == 2296 or x == 2306 or x == 2307 or x == 2320 or x == 2326:
                # Save the HTML as a BeautifulSoup Object
                websiteToSearch = "https://www.dragonball-multiverse.com/en/page-%d.html#h_read" % x
                content = urlopen(websiteToSearch)
                read_content = content.read()
                soup = BeautifulSoup(read_content,'html.parser')

                # Save the line of code containing the URL to the image as a str
                lineContainingURL = str(soup.find(id="balloonsimg"))

                # Save the URL in a new string
                startingIndex = lineContainingURL.find("/image")
                endingIndex = lineContainingURL.rfind(");width")

                unfilteredURL = lineContainingURL[startingIndex:endingIndex]

                # Remove all occurences of amp; and spaces from url
                filteredURLA = unfilteredURL.replace("amp;", "")        
                filteredURL = filteredURLA.replace(" ","")        

                # Finally Store Real Image URL for Download
                imageURL = "https://www.dragonball-multiverse.com" + filteredURL


                newFileName = "Dragon Ball Multiverse/%d.png" % x
                urlretrieve(imageURL, filename=newFileName)
                
                print("Page %d Downloaded with Fixed URL" % x)



print("")
print("             ___     -._")
print("             `-. \"\"\"--._ `-.")
print("                `.      \"-. `.")
print(" _Seal_           `.       `. \\")
print(" `-.   \"\"\"---.._    \\        `.")
print("    `-.         \"-.  \\         `\\")
print("       `.          `-.\\          \\_.-\"\"\"\"\"\"\"\"--._")
print("         `.           `                          \"-.")
print("           `.                                       `.    __....-------...")
print(" --..._      \\                                       `--\"\"\"\"\"\"\"\"\"\"\"---..._")
print(" __...._\"_-.. \\                       _,                             _..-\"\"")
print(" `-.      \"\"\"--`           /       ,-'/|     ,                   _.-\"")
print("    `-.                 , /|     ,'  / |   ,'|    ,|        _..-\"")
print("       `.              /|| |    /   / |  ,'  |  ,' /        ----\"\"\"\"\"\"\"\"\"_`-")
print("         `.            ( \\  \\      |  | /   | ,'  //                 _.-\"")
print("           `.        .'-\\/'""\\ |  '  | /  .-/'\"`\' //            _.-\"")
print("     /'`.____`-.  ,'\"\\  ''''?-.V`.   |/ .'..-P''''  /\"`.     _.-\"")
print("    '(   `.-._\"\"  ||(?|    /'   >.\\  ' /.<   `\\    |P)||_..-\"___.....---")
print("      `.   `. \"-._ \\ ('   |     `8      8'     |   `) /\"\"\"\"\"    _\".\"\"")
print("       `.   `.   `.`.b|   `.__            __.'   |d.'  __...--\"\"")
print("          `.   `.   \".`-  .---      ,-.     ---.  -'.-\"\"")
print("            `.   `.   \"\"|      -._      _.-      |\"\"")
print("              `.  .-\"`.  `.       `\"\"\"\"'       ,'")
print("                `/     `.. \"\"--..__    __..--\"\"")
print("                 `.      /7.--|    \"\"\"\"    |--.__")
print("                   ..--\"| (  /'            `\\  ` \"\"--..")
print("                .-\"      \\\\  |\"\"--.    .--\"\"|          \"-.")
print("               <.         \\\\  `.    -.    ,'       ,'     >")
print("              (P'`.        `%,  `.      ,'        /,' .-\"'?)")
print("              P    `. \\      `%,  `.  ,'         /' .'     ")
print("             | --\"  _\\||       `%,  `'          /.-'   .    )")
print("             |       `-.\"\"--..   `%..--\"\"\"\\\\\"--.'       \"-  |")
print("             \\          `.  .--\"\"\"  \"\\.\\.\\ \\\\.'       )     |")


print("\n\nDownloads Complete! Enjoy Reading!")
