# Flask Project Description
#### Video Demo:  <https://youtu.be/DZdSoNwlmOs>


## __Definition__
This project is used to run a Python web server using the flask library
I'm reading a Gayson file here to get to the list of authorized users
and writing to a file to create new users


 Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - README.md
 - users.json
 - static
 - index.css
 - templates
 - about.html
 - index.html
 - login.html
 - register.html



## __Libraries__


__Flask__ : Flask: Flask is a Python framework used to build web applications. It is a small, efficient and easy to understand tool designed to solve cases where a small and simple web server is needed. Flask provides tools and frameworks for building web services, and is modular so functionality can be easily added and removed.

__ART__ : ASCII art is also known as "computer text art". It involves the smart placement of typed special characters or letters to make a visual shape that is spread over multiple lines of text.[(Readmore)](https://pypi.org/project/art/)

__waitress__ : waitress : waitress is a library that provides a small and efficient WSGI (Web Server Gateway Interface) server for Python. WSGI is a protocol that defines an interface between a Python application and the web server, so that web applications such as Flask and Django can be run on an HTTP server.


## **Installing Libraries**
there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

```pip install -r requirements.txt```


- **Main Functionality**: The core functionality includes user registration, login, and logout.

- **Data Storage**: User information is stored in a JSON file (`users.json`), allowing for persistent data storage.

- **Pages**:
  - `/`: The main login page, allowing users to enter their credentials.
  - `/about`: A page providing information about the application.
  - `/home`: The home page, accessible after successful login.
  - `/logout`: A route to log out users.
  - `/register`: The registration page, enabling users to create a new account.

## __Usage__

```python project.py```
```

 ____                          _____  _              _     
|  _ \  _   _  _ __           |  ___|| |  __ _  ___ | | __ 
| |_) || | | || '_ \   _____  | |_   | | / _` |/ __|| |/ / 
|  _ < | |_| || | | | |_____| |  _|  | || (_| |\__ \|   <  
|_| \_\ \__,_||_| |_|         |_|    |_| \__,_||___/|_|\_\ 

  ____                                  _
 / ___|   ___  _ __ __   __  ___  _ __ | |
 \___ \  / _ \| '__|\ \ / / / _ \| '__|| |
  ___) ||  __/| |    \ V / |  __/| |   |_|
 |____/  \___||_|     \_/   \___||_|   (_)


If you want to exit press CTRL + C
     Welcome To Server :),        
     Select a script run:
- 1 for Run server
- 2 for View all users
- 3 for Dell all users
- 4 for Exit
 Select:
```
After that, the user can choose action 1, 2, 3, 4

And it has the ability to exit at any time using CTRL + C.
```
If we choose the first option, we will activate the server and be able to access it at the address http://localhost/
There we can login or register to the site
The listing will be saved in a JSON file

```
There are 4 pages on the site, one for registration, one for login, one for the home page that is displayed after the login, and one for about
```
The other options are by clicking on 2 the list of users from the JSON file will be displayed
```
Pressing 3 will delete all users from the JSON file
```
Pressing 4 will take me out of the program
```