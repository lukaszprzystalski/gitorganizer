@echo off


"C:\**python path**\python.exe" "C:\**create.py project directory**\create.py" %1
echo %*
start "" "C:\default projects directory\%1"
cd "C:\default projects directory the same as above\%1"

type nul > README.txt
git init
git remote add origin https://github.com/yourUsername/%1.git
git add .
git commit -m "Initial commit"
git push -u origin master
code .
