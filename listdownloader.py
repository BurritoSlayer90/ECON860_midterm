import urllib.request
import os

#making a folder for the webpage html
if not os.path.exists("midtermHTML"):
	os.mkdir("midtermHTML")
#reading the webpage's html into a folder
f = open("midtermHTML/names"+".html", "wb")
response = urllib.request.urlopen("http://45.79.253.243/index.html")
html = response.read()
f.write(html)
f.close()
