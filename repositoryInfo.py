import urllib.request
import os
import json
import requests
import pandas
import csv
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import glob
import time

#this file saves the name of each user's most starred repository in a csv, if they have one

#the dataframe we will use to create our csv
df = pandas.DataFrame()

#saving my github token to a variable
f = open("token","r")
token = f.read()
f.close()
#saving my github username to a variable
f = open("username","r")
username = f.read()
f.close()

#this creates an authenticated session so we can access github enough times to complete the project
github_session = requests.Session()
github_session.auth = (username, token)

#importing our list of names for further manipulation
nameList = list(csv.reader(open("parsedGitFiles/midtermGHIDs.csv")))

#access point is the base url to access github
access_point = "http://github.com/"

#this for loop adds each user's most popular repository to df
for name in range(len(nameList)):
	#we start at 1 because the first entry just names the column
	if(name > 0):


		#idString saves the current ghid from nameList 
		idString = nameList[name][0]
		#we add idString to our url and sort by popularity to easily get their top repository
		user_url = access_point + idString + "?tab=repositories&q=&type=&language=&sort=stargazers"
		
		#the repository name is stored in an h3 tag, so we use soupstrainer to only get those tags
		only_h3_tags = SoupStrainer("h3")
		#stores the website data in response
		response = urllib.request.urlopen(user_url)

		#we make a soup with response and our strainer 
		soup = BeautifulSoup(response, "html.parser", parse_only=only_h3_tags)

		#since the list of repos is already sorted, we just need the first h3 tag
		tags = soup.find("h3")
		#the repo name is stored in an a tag
		a = tags.find_all("a")

		#if the user doesn't have any repos, a will = 0, so we set up a conditional to test for this
		if len(a) > 0:
			#a few strings are in a, so we split it up to get our repo name
			raw = (a[0]["href"])
			words = (raw.split("/"))
			repo = (words[2])
			#we print the repo name to make sure it works
			print(repo)
			#and add it to our df under the repository column
			df = df.append({'Repository': repo}, ignore_index= True)
		#if the user has no repos, we save a blank cell to df
		else:
			df = df.append({'Repository': ""}, ignore_index= True)

		#we don't want to spam the website too much so we sleep between access attempts
		time.sleep(10)
#overall, the for loop takes nearly 2 hours to run with the list of 640 users
#we save the dataframe to a csv repoList and we are done
df.to_csv("parsedGitFiles/repoList.csv", index = False)









