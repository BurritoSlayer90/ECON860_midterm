import json
import requests
import pandas
import csv
#this file completes 1e, 1f, and 1g

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

github_session = requests.Session()
github_session.auth = (username, token)



#importing our list of names for further manipulation
nameList = list(csv.reader(open("parsedGitFiles/midtermGHIDs.csv")))
#curname = nameList[2][0]
#print(curname)

access_point = "https://api.github.com"

#result = json.loads(github_session.get(user_url).text)
#print(result)
print("test")

#need to figure out how to access with credentials!!
#read the namelist csv
#for rows in range(len(nameList)):
#print("test?")



for rows in range(len(nameList)):
	#the first row has ghid and not a name, so we ignore it...
	if rows > 0:
		idString = nameList[rows][0]
		print(idString)
		user_url = access_point + "/users/" + idString
		result = json.loads(github_session.get(user_url).text)
		print(result)
		#print(result['public_repos'])

		gitid = result['id']
		print(gitid)
		avurl = result['avatar_url']
		print(avurl)
		url = result['url']
		print(url)
		followers = result['followers']
		print(followers)
		#fuck starred omfg
		#starred = github_session.get(user_url + "/starred").text
		#print(starred)
		repos = result['public_repos']
		print(repos)
		name = result['name']
		print(name)
		company = result['company']
		print(company)
		blog = result['blog']
		print(blog)
		location = result['location']
		print(location)
		email = result['email']
		print(email)
		hireable = result['hireable']
		print(hireable)
		created = result['created_at']
		print(created)
		update = result['updated_at']
		print(update)

		#for the bonus, I can sort repositiories by starred and get the user's most popular repository. 
		#a column for "most popular" or sum

		df = df.append({
				'ID': gitid,
				'Avatar URL':avurl,
				'URL': url,
				'Follower Count': followers,
				#'Stars': starred,
				'Reposts': repos,
				'Name': name,
				'Company': company,
				'Blog': blog,
				'Location': location,
				'Email': email,
				'Hired Time': hireable,
				'Created At': created,
				'Last Update': update
				}, ignore_index = True
				)
#saving the data to a csv, this satisfies 1g
df.to_csv("parsedGitFiles/gitinfo.csv", index = False)
