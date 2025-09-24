class Transaction:
    def __init__(self,amount,transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

class Account:
    def __init__(self,account,name,balance=0):
        self.account = account
        self.name = name
        self.balance = balance
        self.Transactions = []
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.Transactions.append(Transaction(amount,"Deposit"))
            print(f"Deposit of {amount} is successful. New Balance {self.balance}")
        else:
            print("Invalid Deposit")
    
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.Transactions.append(Transaction(amount,"Withdrawl"))
            print(f"Withdrawl of {amount} is successfull, New balance {self.balance}")
        else:
            print("Invalid Withdrawl or insufficient funds")

    def display_transactions(self):
        print("\nTransaction History")
        for transaction in self.Transactions:
            print(f"\n {transaction.amount} {transaction.transaction_type}")

    def display_balance(self):
        print(f"Current Balance for Account {self.account}: {self.balance}")

class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = {}

    def create_acc(self,account,name,balance=0):
        if account not in self.accounts:
            new_account = Account(account,name,balance)
            self.accounts[account] = new_account
            print(f"Account successfully created for {name}. Account Number : {account}")
        else:
            print("Account already exists.")
    
    def get_account(self,account):
        return self.accounts.get(account)

def create_account(bank):
    acc_num = int(input("Enter the Account Number : "))
    name = input("Enter account Holder's name : ")
    balance = float(input("Enter Initial Balance : "))
    bank.create_acc(acc_num,name,balance)

def deposit_money(bank):
    acc_no = int(input("Enter Account Number: "))
    account = bank.get_account(acc_no)
    if account:
        amount = float(input("Enter Deposit Amount: "))
        account.deposit(amount)
    else:
        print("Account not found.")

def withdraw_money(bank):
    acc_no = int(input("Enter Account Number: "))
    account = bank.get_account(acc_no)
    if account:
        amount = float(input("Enter Withdrawal Amount: "))
        account.withdraw(amount)
    else:
        print("Account not found.")


def check_balance(bank):
    acc_no = int(input("Enter Account Number: "))
    account = bank.get_account(acc_no)
    if account:
        account.display_balance()
    else:
        print("Account not found.")


def view_transactions(bank):
    acc_no = int(input("Enter Account Number: "))
    account = bank.get_account(acc_no)
    if account:
        account.display_transactions()
    else:
        print("Account not found.")

def main():
    bname = "India Bank"
    bank = Bank(bname)
    while True:
        print(f"\n====== Welcome to {bname} ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            create_account(bank)
        elif choice == "2":
            deposit_money(bank)
        elif choice == "3":
            withdraw_money(bank)
        elif choice == "4":
            check_balance(bank)
        elif choice == "5":
            view_transactions(bank)
        elif choice == "6":
            print(f"👋 Thank you for using {bname}!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()