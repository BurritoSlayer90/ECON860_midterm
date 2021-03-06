import json
import requests
import pandas
import csv
#this file completes 1e,(1f), and 1g

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
#importing the list of top repositories for users
topRepos = list(csv.reader(open("parsedGitFiles/repoList.csv")))

#access point is the base url to access the github api
access_point = "https://api.github.com"

#we run a for loop for every ghid in our nameList to get the data we want for 1e
for rows in range(len(nameList)):
	#the first row has ghid and not a name, so we ignore it...
	if rows > 0:
		#idString saves the current ghid from nameList 
		idString = nameList[rows][0]
		#we add idString to our url to access their information from the github API
		user_url = access_point + "/users/" + idString
		#result has all the information we need. Except number of starred, which takes more work
		result = json.loads(github_session.get(user_url).text)

		#saving the necessary data from result to variables 
		#I printed them all to make sure they work
		gitid = result['id']
		print(gitid)
		avurl = result['avatar_url']
		print(avurl)
		url = result['url']
		print(url)
		followers = result['followers']
		print(followers)
		following = result['following']
		print(following)
		#starred needs work...
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
		bio = result['bio']
		print(bio)
		created = result['created_at']
		print(created)
		update = result['updated_at']
		print(update)

		#bonus
		repo = topRepos[rows][0]
		print(repo)

		#this url allows us to access the user's top repository info with the api
		repo_url = access_point + "/repos/" + idString + "/" + repo
		#we save the data from that webpage to result
		result = json.loads(github_session.get(repo_url).text)

		#we don't want to try to store data for users with no repositories
		if repo == "":
			stars = ""
			repoURL = ""
			language = ""
			wiki = ""
			size = ""
			repoCreated = ""
			repoUpdated = ""
		else:
			#we save the following variables from result to give useful information about the repository
			stars = result['stargazers_count']
			print(stars)
			repoURL = result['url']
			print(url)
			language = result['language']
			print(language)
			wiki = result['has_wiki']
			print(wiki)
			size = result['size']
			print(size)
			repoCreated = result['created_at']
			print(created)
			repoUpdated = result['updated_at']
			print(repoUpdated)

		#this code adds all the data we collected from 'result' into our data frame to satisfy 1e
		df = df.append({
				'GHID': idString,
				'ID': gitid,
				'Avatar URL':avurl,
				'URL': url,
				'Follower Count': followers,
				'Following Count': following,
				#'Stars': starred,
				'Public Repositories': repos,
				'Name': name,
				'Company': company,
				'Blog': blog,
				'Location': location,
				'Email': email,
				'Hireable': hireable,
				'Bio': bio,
				'Created At': created,
				'Last Update': update,
				'Top Repository': repo,
				'Repository Stargazers': stars,
				'Repo URL': repoURL,
				'Repo Language': language,
				'Has Wiki': wiki,
				'Repo Size': size,
				'Repo Created At': repoCreated,
				'Repo Update At': repoUpdated
				}, ignore_index = True
				)
#saving the data to a csv, this satisfies 1g
df.to_csv("parsedGitFiles/gitinfo.csv", index = False)
