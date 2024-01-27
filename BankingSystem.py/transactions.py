import login
import json
balance=0.0
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
        else:
            print("Have a great day")
def deposit():
    global balance
    try:
        deposit_amt=float(input("How much do you want to deposit? "))
        file=open("transactions_details.json","a")
        balance+=deposit_amt
        user_balance={"username":login.login_username, "balance":balance, "deposit":deposit_amt}
        file=open("transactions_details.json","a")
        json_userbalance=json.dumps(user_balance)
        file.write(json_userbalance+"-")
        file.close()
        print(f"Successfully deposited Rs {deposit_amt} in your account")
        view=input("Do you want to view your current balance? (y/n)")
        if view=="y":
            view_balance()
    except:
        pass

def withdraw():
    global balance
    withdraw_amt=float(input("How much do you want to withdraw ? "))
    file=open("transactions_details.json","a")
    if True:
        if withdraw_amt>balance:
            raise ValueError("Insufficient balance. ")
        balance-=withdraw_amt
        user_balance={"username":login.login_username,"balance":balance}
        json_userbalance=json.dumps(user_balance)
        file.write(json_userbalance+"-")
        file.close()
        print(f"{withdraw_amt} has been withdrawn from your account")
        view=input("Do you want to view your balance?(y/n) ")
        if view=="y":
            view_balance()

def view_balance():
    global balance
    file=open("transactions_details.json","r")
    json_view_balance=file.read()
    file.close()
    list_view_balance=json_view_balance.split("-")
    for data in list_view_balance:
        if data!="":
            dict_data=json.loads(data)
            if login.login_username==dict_data.get("username"):
                print(dict_data)
    