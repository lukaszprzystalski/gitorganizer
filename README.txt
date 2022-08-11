Script is being run by "create folderName" directly from CMD.
File C:\**\create.cmd is responsible for running python script (after path has been added to env variables).
Python scrip opens browser and logs on to github, then it creates new repo with name specified as 'create' argument (ie. create test -> repo name will be test), then it closes the browser.
CMD file creates folder with create argument, then opens it. After that it creates blank Readme.txt file, initializes GIT, remotes to GIT, adds created README file and does Initial Commit.
In last step CMD file opens VSCode.