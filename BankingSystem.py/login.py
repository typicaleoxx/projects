import json
import transactions as trans
def login():
    global login_username
    login_username=input("Please enter your username: ").strip().lower()
    login_password=input("Please enter your password: ").strip().lower()
    file=open("user_details.json","r")
    json_userdetails=file.read()
    file.close()
    list_userdetails=json_userdetails.split("-")
    for details in list_userdetails:
        if details!="":
            dict_userdetails=json.loads(details)
            if dict_userdetails.get("username")==login_username:
                if dict_userdetails.get("password")==login_password:
                    print("Login successful.\n")
                    trans.main()
                else:
                    print("Incorrect password. Try again!\n")
        else:
            again=input("Incorrect username. Do you want to try again? (y/n)").strip().lower()
            if again=="y":
                login()
            