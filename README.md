# Supply_chain

--> These are the steps you need to follow for setting your git with this project's repository..

Create a empty folder in environment folder("myenv" in my case) and name it as "InvenTree".

go in that folder by terminal and follow below git commands

$ git init this will create empty repositry in InvenTree folder

$ git remote add origin https://github.com/InvenTree-Management/Supply_chain.git

Sets the new remote
$ git remote -v

Verifies the new remote URL
$ git pull origin master

Then it pulls the all code into the InvenTree folder from GitHub
$ git add .

Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
$ git commit -m "Initial commit"

Message should be in accordance with the changes u've made in your code
Then Commit into it by this above command
$ git push origin master

Then push the all changes into the GitHub by this command
give your username and password to it

then it will push all your changes into GitHub
