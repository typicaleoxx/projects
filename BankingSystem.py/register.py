import login
import json
def register():
    username=input("Create your username: ").strip()
    password=input("Create your password: ").strip()
    user_details={"username":username,"password":password}
    file=open("user_details.json","a")
    try:
        json.dump(user_details,file)
        print("Registration successful. Thank you!")
        file.close()
        login_user=input("Do you want to login? (y/n)").strip().lower()
        if login_user=="y":
            login.login()
        else:
            print("Thank you. Have a great day!")
    except:
            print("Registration error.")
    