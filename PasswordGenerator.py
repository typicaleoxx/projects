#generates more characters than asked
import random
import string

def main():
    user_length= int(input("How many characters would you like your generated password to have?"))
    user_upper=input("Include uppercase letters?(y/n) : ").strip().lower()
    user_lower=input("Include lowercase letters?(y/n) : ").strip().lower()
    user_numbers=input("Include symbols numbers?(y/n) : ").strip().lower()
    user_symbols=input("Include symbols letters?(y/n) : ").strip().lower()
    print(f"Your generated password is: {generate_password(user_length,user_upper,user_lower,user_numbers,user_symbols)}")

def generate_password(length, upper, lower, numbers, symbols):
    if upper=="y":
        upper_chars=string.ascii_uppercase
    else:
        upper_chars=""
    if lower=="y":
        lower_chars=string.ascii_lowercase
    else:
        lower_chars=""
    if numbers=="y":
        numbers_chars=string.digits
    else:
        numbers_chars=""
    if symbols=="y":
        symbols_chars="!@#$%^&*_"
        
    all_chars= upper_chars + lower_chars +numbers_chars + symbols_chars
    
    length=max(length,len(all_chars))
    password=random.choices(all_chars,k=length)
    password="".join(password)
    
    return(password)
main()