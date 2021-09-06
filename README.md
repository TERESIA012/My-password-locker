# My Password Locker
### Author:Teresia King'ori

# Description

## This is an application that allows the user to create a password locker by log  in using username and password.The user can also also store password of an already existing account.The user also has an option of using their own password or allow the application to generate a random password.

# Setup requirements
 - Github
 - Code Editor

# Setup Installation

* Fork from Github
* $git clone 
* $ chmod +x run.py
* $ ./run.py command

# BDD

|Behaviour|Input|Output|
|:--------|:-------|:------|
|Run the application in the terminal of your code editor|$ ./run.py|Hello what is your name?|
|input your name|name|Welcome name to My Password locker what do you want to do? -ca - create a new account , log - login to your account ex-exit
| input ca|input username and password.| username new account created successfully.Proceed to login|
|input log|input created username and password| logged in successfully where would you like to navigate to? sc-store your credentials, cc-create new credentials dip-display your credentials, de-delete existing credentials ,ex-exit|
input sc|input application name,username and password|your application name have been successfully saved|
input cc|input application name and username|Choose the following options:  create my own password by using shortcodecp or let password locker generate a password for me using shortcode rp|
|input dip|Here is a list of all your credentials|
|input ex| ex|bye...|
____




## Bugs
### No known bugs at the moment

# Technologies Used
 * Python 
# Licence
## &copy;2021 Teresia King'ori 
