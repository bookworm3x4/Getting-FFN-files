# ffn scraper.py
# scrapes html from Fanfiction.net pages to generate text files
# of works


# INITIALIZE

# import packages
from lxml import html
import requests

# initialize program with fic URL and length
ficCode = '10847788' # go to fic and find the 8-digit number in the URL after the s/
ficUrl = 'https://www.fanfiction.net/s/' + ficCode + "/"
chapters = 21


# GET DATA FROM WEBSITE

# create filetree
page = requests.get(ficUrl)
tree = html.fromstring(page.content)

# get metadata
title = tree.xpath('//*[@id="profile_top"]/b/text()')[0]
author = "by " + tree.xpath('//*[@id="profile_top"]/a[1]/text()')[0]
description = tree.xpath('//*[@id="profile_top"]/div/text()')[0]

metadata = []
metadata.append(title)
metadata.append(author)
metadata.append(description)

# pull text chapter-by-chapter
contents = []

for i in range(chapters):
    page = requests.get(ficUrl + str(i+1))
    tree = html.fromstring(page.content)

    chapTitle = tree.xpath('//*[@id="chap_select"]/option[@selected]/text()')
    chapContents = tree.xpath('//*[@id="storytext"]/p/text() | //*[@id="storytext"]/p/*/text()')
    
    chapter = []
    chapter.append(chapTitle[0])
    chapter.append(chapContents)
    
    contents.append(chapter)

# EXPORT DATA TO TEXT FILE

# create text file to hold contents
fileName = ""
title = title.split()
for word in title:
    fileName += word + "_"
fileName = fileName[:-1] + ".txt"
textFile = open(fileName,"w+")

# place metadata at start of file
for item in metadata:
    print(item, file = textFile)
print(file = textFile)

# place contents into file
for chapter in contents:
    print(chapter[0], file = textFile)
    print("", file = textFile)
    for line in chapter[1]:
        print(line, file = textFile)
    print("", file = textFile)

# close the file
textFile.close()

# announce completion
print("Fanfiction.net story has been copied to " + fileName + ".")

