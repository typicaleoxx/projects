import login
def main():
    print(f"Hi, {login. login_username.capitalize()} welcome to your account. ")
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
        amount=int(input("How much do you want to deposit? "))
        file=open("transaction_details.json","a")
        
    except:
        pass

def withdraw():
    pass
def view_balance():
    pass