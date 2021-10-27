# ECON860_midterm
This repository includes my code and the data I collected for my ECON 8600 Midterm at Clemson University. It is used to scrape a list of github user ID's from a webpage, and return information from their profile in CSV format.

Contents:

1.	The python file 'listdownloader.py' does a couple things: 
      It creates a folder called midtermHTML, and stores the webpage "http://45.79.253.243/index.html" in that folder in html format as "names.html" 
      This folder and its contents are in the Midterm8600 folder.
2.	The python file 'listmaker.py' is more involved: 
    	When ran, it takes names.html, converts the page into a Soup using BeautifulSoup, and makes a list of all the ghid's from the html in csv format. 
      The list is cleaned by removing duplicates before being saved as a csv, and results in a list of 640 ghid's. 
      It creates a folder called parsedGitFiles to store the csv. 
      The csv that will be created is called "midtermGHIDs.csv"
3.    The python file repositoryInfo.py takes the names of github users from midtermGHIDs.csv and outputs each user's most starred repository in the file gitinfo.csv. This is used to satisfy the bonus on the midterm.
4.	The python file 'githubinfo.py' is the most complex file: 
    	When ran, it accesses the github api to save the characteristics of the github users from midtermGHIDs.csv in a new csv.
      These characteristics include the user's name, follower count, and many other details. 
      It also includes information about the users' top repositories from repoList.csv
      The new csv is called "gitinfo.csv," and is saved in the parsedGitFiles folder. 
      It accesses the github api through an authenticated session. 
      
      To do this, we create files that store our username and API token. (You will need to make your own files)
      We also have a .gitignore file that tells github to not show those files, as they are sensitive information.
      
      These ^^ files are called ".gitignore," "username," and "token" respectively.
      We read them into variables in githubinfo.py to keep them hidden on github.
5.	The folder "midtermHTML" contains the "names.html" file mentioned above
6.	The folder "parsedGitFiles contains the "midtermGHIDs.csv," "gitinfo.csv," and "repoList.csv" files mentioned above.
7.	The .gitignore, token, and username files are described in 3

Instructions for running the program:

1.	Save the program to your computer. I recommend saving to the desktop.
2.	Open your command module on PC or similar for Mac/Linux
3.	Navigate to the proagram folder through the command module. If you saved to desktop(recommended) it should look like this: cd Desktop (Enter) cd ECON860_midterm (Enter)
4.	You will want to create two files called "username" and "token" that store your github username and API token respectively. 
5.	Using the command module, run the first file, listdownloader.py: python listdownloader.py (Enter)
      This will create the names.html file
6.	Next, run the second file, listmaker.py: python listmaker.py (Enter)
      This will create the midtermGHIDs.csv file
7.	Then run the third file, repositoryInfo.py: python repositoryInfo.py (Enter)
      -Note: this step takes nearly 2 hours to access the site without the website blocking you. Plan to let your computer run uninterrupted, on a solid internet connection for that time.
      This will create the repoList.csv file
8.	Finally, run the fourth file, gitinfo.py: python githubinfo.py (Enter)
      This will create the gitinfo.csv file
9.	Now, if you open the folder "parsedGitFiles," there will be a file called "gitinfo.csv." This is the final output of the code. Enjoy!

Limitations:
1.    I was not able to extract the 'number of starred' data for probllem 1e, so that is not included.
2.    A small number of cells show "1.0" instead of "True." These include the first value in the "hireable" column and the first two in "Has Wiki."
      I do not understrand why this is. I believe it to be a glitch. 
