import login
import json
balance=0
def main():
    print(f"Hi, {login.login_username.capitalize()} welcome to your account. ")
    print(f"What operation do you want to perform ? \n 1. Deposit money \n 2. Withdraw money \n 3. Check balance ")
    operation=input("Choose operation number: ").strip()
    try:
        if operation=="1":
            deposit()
        elif operation=="2":
            withdraw()
        elif operation=="3":
            view_balance()
    except:
        print("Oops operation error. Do you want to try again? (y/n)")
        try_again=input()
        if try_again=="y":
            main()
def deposit():
    try:
        deposit=float(input("How much do you want to deposit? "))
        file=open("transaction_details.json","a")
        balance=balance+deposit
        user_balance={"username":login.login_username, "balance":balance, "deposit":deposit}
        file=open("transactions.json","a")
        json_userbalance=json.dumps(user_balance)
        file.write(json_userbalance+"-")
        file.close()
        view=input("Do you want to view your current balance? (y/n)")
        if view=="y":
            view_balance(login.login_username)
    except:
        pass

def withdraw():
    withdraw_amt=float(input("How much do you want to withdraw ? "))
    file=open("transactions.json","a")
    try:
        balance=balance-withdraw_amt
        user_balance={"username":login.login_username,"balance":balance}
        json_userbalance=json.dumps(user_balance)
        file.write(json_userbalance+"-")
        file.close()
        print(f"{withdraw_amt} has been withdrawn from your account")
        view=input("Do you want to view your balance?(y/n) ")
        if view=="y":
            view_balance()
    except:
        print("Error occured.Amt cannot be withdrawn")
def view_balance():
    file=open("transactions.json","r")
    json_view_balance=file.read()
    file.close()
    list_view_balance=json_view_balance.split("-")
    for data in list_view_balance:
        if data!="":
            dict_data=json.loads(data)
            if login.login_username==dict_data.get("username"):
                print(dict_data)
    