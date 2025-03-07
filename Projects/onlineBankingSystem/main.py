from database import *

def find_account():
    while True:
        user_input = input("\nEnter Account Name: ").title()

        for account in accounts:
            if account.name == user_input:
                print("| Acoount found!")
                return account
        else:
            print("| Account name is not in the database!")

def attempt_login(account):
    attempts = 3
    while True:
        if attempts == 0:
            print("| Account log in failed, closing the system!")
            return False
        
        user_input = input("\nEnter Account PIN: ")
        
        if account.pin == user_input:
            print("| Account logged in successfully!")
            return True
        else:
            attempts -= 1
            print(f"| Incorrect password! {attempts} attempts left!")

def get_action(account):
    while True:
        print("\nChoose an action to proceed:" +
              "\n| 1. Balance Inquiry" +
              "\n| 2. Withdraw Amount" +
              "\n| 3. Deposit" +
              "\n| 4. Exit System")
        
        user_input = input("\nEnter Action: ").strip()

        if user_input == "1":
            account.check_balance()
        elif user_input == "2":
            account.withdraw()
        elif user_input == "3":
            account.deposit()
        elif user_input == "4":
            print("| Thank you for using Python Online Bank! Closing system...")
            return False
        else:
            print("| Invalid input, please try again!")
        
        while True:
            print("\nWan't to start another transaction?")
            user_input = input("| Input choice (Yes/No): ")

            if user_input.lower() in ["yes", "y"]:
                break
            elif user_input.lower() in ["no", "n"]:
                print("| Thank you for using Python Online Bank! Closing system...")
                return False

def main_loop():
    while True:
        print("\nHello and Welcome to Python Online Bank!" +
            "\nTo proceed please log in your online bank account.")
        
        user_account = find_account()
        if not attempt_login(user_account): break
        if not get_action(user_account): break

main_loop()