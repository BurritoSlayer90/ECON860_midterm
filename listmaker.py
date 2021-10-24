from bs4 import BeautifulSoup
import pandas
import os
import glob
import time
#this file completes 1a-1d...
#df is the dataframe we will store our list of names in
df = pandas.DataFrame()

#the folder for our list of names
if not os.path.exists("parsedGitFiles"):
	os.mkdir("parsedGitFiles")

#creating a soup from the html...
f = open("midtermHTML/names.html", "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

#div is a list of all div rows in the soup
div = soup.find_all("div")

#run a for loop for all the rows in div to store the ghid's 
for divs in range(len(div)):
	#we only want the tags with ghid's, so that excldes the first 3 lines
	if divs > 3:
		#gitname stores the ghid from the current row in div
		gitname = div[divs]["ghid"]
		#we add gitname to our dataframe
		df = df.append({'ghid': gitname}, ignore_index = True)
		#I used the print line to make sure the names line up with the data
		print(df.loc[divs-4])
#I print the length of the list to compare after we remove duplicates
print(len(df))		
#this line drops duplicates and satisfies 1d
df.drop_duplicates(subset ="ghid", keep = 'first', inplace = True)

print(len(df))
#this shows that we dropped 90 duplicates.

#I save the dataframe to a csv
df.to_csv("parsedGitFiles/midtermGHIDs.csv", index= False)
print("done")
