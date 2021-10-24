# ECON860_midterm
This repository includes my code and the data I collected for my ECON 8600 Midterm at Clemson University. It is used to scrape a list of github user ID's from a webpage, and return information from their profile in CSV format.

Contents:

The python file 'listdownloader.py' does a couple things: It creates a folder called midtermHTML, and stores the webpage "http://45.79.253.243/index.html" in that folder in html format as "names.html" This folder and its contents are in the Midterm8600 folder.
The python file 'listmaker.py' is more involved: When ran, it takes names.html, converts the page into a Soup using BeautifulSoup, and makes a list of all the ghid's from the html in csv format. The list is cleaned by removing duplicates before being saved as a csv, and results in a list of 640 ghid's. It creates a folder called parsedGitFiles to store the csv. The csv that will be created is called "midtermGHIDs.csv"
The python file 'gitinfo.py' is the most complex file: When ran, it accesses the github api to save the characteristics of the github users from midtermGHIDs.csv in a new csv. These characteristics include the user's name, follower count, and many other details. The new csv is called "gitinfo.csv," and is saved in the parsedGitFiles folder. It accesses the github api through an authenticated session. To do this, we create a .gitignore file and 2 files that store our username and token. These ^^ files are called ".gitignore," "username," and "token" respectively. We read them into variables in gitinfo.py to keep them hidden on github.
The folder "midtermHTML" contains the "names.html" file mentioned above
The folder "parsedGitFiles contains the "midtermGHIDs.csv" and "gitinfo.csv" files mentioned above.
The .gitignore, token, and username files are described in 3

Instructions for running the program:

Save the program to your computer. I recommend saving to the desktop.
Open your command module on PC or similar for Mac/Linux
Navigate to the proagram folder through the command module. If you saved to desktop(recommended) it should look like this: cd Desktop (Enter) cd ECON860_midterm (Enter) cd Midterm8600
Using the command module, run the first file, listdownloader.py: python listdownloader.py (Enter)
Next, run the second file, listmaker.py: python listmaker.py (Enter)
Finally, run the third file, gitinfo.py: python gitinfo.py (Enter)
Now, if you open the folder "parsedGitFiles," there will be a file called "gitinfo.csv." This is the final output of the code. Enjoy!
