# Supply_chain

--> These are the steps you need to follow for setting your git with this project's repository..

1) Create a empty folder in environment folder("myenv" in my case) and name it as "InvenTree".

2) go in that folder by terminal and follow below git commands

3) $ git init
   this will create empty repositry in InvenTree folder
   
4) $ git remote add origin https://github.com/InvenTree-Management/Supply_chain.git
   - Sets the new remote
 
   $ git remote -v
   - Verifies the new remote URL
   
5) $ git pull origin master
   - Then it pulls the all code into the InvenTree folder from GitHub

6) $ git add .
   - Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
   
7) $ git commit -m "Initial commit"
   - Message should be in accordance with the changes u've made in your code
   - Then Commit into it by this above command
   
8) $ git push origin master
   - Then push the all changes into the GitHub by this command
   
9) give your username and password to it
   - then it will push all your changes into GitHub
   
