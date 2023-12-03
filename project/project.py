from flask import Flask, jsonify, redirect, render_template, request, url_for
from waitress import serve
import json
import art
import sys

app = Flask(__name__)


def main():
    
    print(art.text2art("Run - Flask \n Server!"))
    while True:
        script = getScript()
        if script == 1:
            runServer()
            break
        elif script == 2:
            showUsers()
            break
        elif script == 3:
            delAllUsers()
            break
        elif script == 4:
            exitScript()
            break
        else:
            continue

    
    
def getScript():
    try :        
        print("If you want to exit press CTRL + C")
        n = int(input('     Welcome To Server :),  \n     Select a script run: \n- 1 for Run server \n- 2 for View all users \n- 3 for Dell all users \n- 4 for Exit \n Select: '))
        if n not in [1,2,3,4]:
            raise Exception()
    except (ValueError,Exception):
        print("please Enter a Value 1 2 3 4")
    except KeyboardInterrupt:
        exitScript()
    else:
        return n

def runServer():    
        
    if __name__ == "__main__":
        
        print("server flask run ")
        print("If you want to exit press CTRL + C")
        print("open website http://localhost/")
        serve(app, host='0.0.0.0', port=80)
        
        print("exit flask")
        # app.run(debug=False, host='0.0.0.0', port=80) 
    

def read_users_from_file():
    with open('users.json', 'r') as file:
        data = json.load(file)
        return data['users']
    



def write_user_to_file(username, password):
    users = read_users_from_file()
    new_user = {'username': username, 'password': password}
    users.append(new_user)
    
    with open('users.json', 'w') as file:
        json.dump({'users': users}, file)   


@app.route("/", methods=['GET', 'POST'])
def login():        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = read_users_from_file()
        valid_credentials = any(user['username'] == username and user['password'] == password for user in users)

        if valid_credentials:
            return redirect(url_for('home'))
    
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/logout",methods=['GET'])
def logout():
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = read_users_from_file()
        
        if any(user['username'] == username for user in users):
            return jsonify({'error': 'Username already exists'}), 400

        
        write_user_to_file(username, password)
        
        jsonify({'success': 'Registration successful'}), 200
        return redirect(url_for('home'))
                

    return render_template("register.html")


    

    

def showUsers():
    # קריאת קובץ JSON
    with open('users.json', 'r') as file:
        data = json.load(file)

    # הדפסת רשימת המשתמשים
    i = 1
    for user in data['users']:
        print(f"user {i}: {user['username']}")
        i += 1
    
    
def delAllUsers():
    
    # קריאת קובץ JSON
    with open('users.json', 'r') as file:
        data = json.load(file)

    # מחיקת רשימת היוזרים
    data['users'] = []

    # שמירת השינויים בקובץ
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("All users have been successfully deleted.")
    return "All users have been successfully deleted."
      
    
def exitScript():
    sys.exit("Exit")
    
        

if __name__ == "__main__":
    
    main()