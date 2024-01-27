import json
import transactions as trans
def login():
    global login_username
    login_username=input("Please enter your username: ").strip().lower()
    login_password=input("Please enter your password: ").strip().lower()
    file=open("user_details.json","r")
    for details in file:
        userdetails=json.loads(details)
        if userdetails.get("username")==login_username:
            if userdetails.get("password")==login_password:
                print("Login successful.")
                trans.main()
            else:
                print("Incorrect password. Try again!")
                
        else:
            again=input("Incorrect username. Do you want to try again? (y/n)").strip().lower()
            if again=="y":
                login()
            