class account:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"| Current Balance: ${self.balance:.02f}")

    def withdraw(self):
        while True:
            try:
                amount = float(input("| Enter Amount to Withdraw: $"))
                if amount <= self.balance:
                    break
                else:
                    print(f"| Insufficient funds! Current Balance: ${self.balance:.02f}")
            except ValueError as e:
                print(f"| Invalid input: {e}")
        
        self.balance -= amount
        print(f"| ${amount:.02f} has been withdrawed in your account!" +
              f"\n| Current Balance: ${self.balance:.02f}")

    def deposit(self):
        while True:
            try:
                amount = float(input("| Enter Amount to Deposit: $"))
                break
            except ValueError as e:
                print(f"| Invalid input: {e}")

        self.balance += amount
        print(f"| ${amount:.02f} has been deposited in your account!" +
              f"\n| Current Balance: ${self.balance:.02f}")

account1 = account("Neil Sierra", "0211", 45000)
account2 = account("Lei Bulugagao", "0307", 50000)
account3 = account("Joanna Jonson", "0619", 40000)
account4 = account("Philip Bulaso", "0822", 40000)

accounts = [account1, account2, account3, account4]