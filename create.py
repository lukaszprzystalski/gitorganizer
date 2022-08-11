import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, datetime
from gitOrganizer import username, pwd, path, driverPath

'''
Script is being run by "create folderName" directly from CMD.
File C:\**\create.cmd is responsible for running python script (after path has been added to env variables).
Python scrip opens browser and logs on to github, then it creates new repo with name specified as 'create' argument (ie. create test -> repo name will be test), 
then it closes the browser.
CMD file creates folder with create argument, then opens it. After that it creates blank Readme.txt file, initializes GIT, remotes to GIT, adds created 
README file and does Initial Commit.
In last step CMD file opens VSCode.
'''



URL = 'http://github.com/login'
driver = webdriver.Chrome(driverPath)

FOLDERNAME = sys.argv[1]
WORKINGPATH = os.path.join(path, FOLDERNAME)

def create():
    os.makedirs(os.path.join(path, FOLDERNAME))
    print(str(sys.argv[1]))

def login():
    #login
    driver.get(URL)
    time.sleep(2)
    user = driver.find_element_by_id('login_field')
    user.click()
    user.clear()
    user.send_keys(username)
    pword = driver.find_element_by_id('password')
    pword.click()
    pword.clear()
    pword.send_keys(pwd)

    btn = driver.find_element_by_name('commit')
    btn.click() 

def addRepository(folder):
    driver.get('https://github.com/new')
    repName = driver.find_element_by_id('repository_name')
    repName.click()
    repName.clear()
    repName.send_keys(folder)
    submit = driver.find_elements_by_tag_name('button')
    for index, item in enumerate(submit):
        # print(index, item.text, item.get_attribute('class'))
        if item.get_attribute('class') == 'btn-primary btn':
            item.submit()
            break
    time.sleep(1)

def main():
    create()
    login()

    addRepository(FOLDERNAME)

    #cleanup
    driver.quit()


if __name__ == '__main__':
    main()



