class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self, filename = 'account.txt'):
        self.filename = filename
        self.accounts = dict({})
        self.load_from_file()

    def gen_acc_num(self):
        return str(1000 + len(self.accounts) + 1)
    
    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit can not be negative!")
            return
        acc_no = self.gen_acc_num()
        self.accounts[acc_no] = Account(acc_no, name, initial_deposit)
        self.save_to_file()
        print(f'Account created! Account number: {acc_no}')

    def view_account(self, account_number):
        acc = self.accounts.get(account_number)
        if acc:
            print(f'Account number: {acc.account_number}')
            print(f'Name: {acc.name}')
            print(f'Balance: ${acc.balance:.2f}')
        else:
            print("Account Not Found!")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        acc = self.accounts.get(account_number)
        if acc:
            acc.balance += amount
            self.save_to_file()
            print("Deposit successful!")
        else:
            print('Account Not Found!')

    def withdraw(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            if 0 < amount <= acc.balance:
                acc.balance -= amount
                self.save_to_file()
                print("Withdrawal successful!")
            else:
                print("Invalid amount!")
        else:
            print("Account Not Found!")

    def save_to_file(self):
        with open(self.filename, mode='w') as file:
            for acc in self.accounts.values():
                file.write(f'{acc.account_number}, {acc.name}, {acc.balance}\n')

    def load_from_file(self):
        try:
            with open(self.filename, mode='r') as file:
                for line in file:
                    acc = line.strip().split(', ')
                    if len(acc) == 3:
                        acc_num, name, balace = acc
                        self.accounts[acc_num] = Account(acc_num, name, float(balace))
        except FileNotFoundError:
            pass
    
    def main(self):

        while True:
            print("\n--- Simple Bank Menu ---")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                name = input("Enter name: ")
                try:
                    deposit = float(input("Initial deposit: "))
                    bank.create_account(name, deposit)
                except ValueError:
                    print("Invalid deposit amount.")
            elif choice == '2':
                acc_num = input("Enter account number: ")
                bank.view_account(acc_num)
            elif choice == '3':
                acc_num = input("Enter account number: ")
                try:
                    amount = float(input("Deposit amount: "))
                    bank.deposit(acc_num, amount)
                except ValueError:
                    print("Invalid amount.")
            elif choice == '4':
                acc_num = input("Enter account number: ")
                try:
                    amount = float(input("Withdrawal amount: "))
                    bank.withdraw(acc_num, amount)
                except ValueError:
                    print("Invalid amount.")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

bank = Bank()
bank.main()