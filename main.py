class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        
    def total_balance(self):
        print(f"Your total balance is: ${self.balance}")
       
    def deposit(self, deposit_money):
        self.balance += deposit_money
        self.transactions.append(f"Deposit: +{deposit_money}")
                
    def withdraw(self, withdraw_money):
        if withdraw_money > self.balance:
            print(f"It exceeds your current total balance. ${self.balance}")
        else:
            self.balance -= withdraw_money
            self.transactions.append(f"Withdraw -{withdraw_money}")
            
    def show_transaction(self):
        for transaction in self.transactions:
            print(transaction)
            
bank_owner = BankAccount("Damen", 3200)

print(f"Welcome dear, {bank_owner.owner}")
print()

while True:
    
    print("Choose one of the options:")
    print("1.Check balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Transaction history")
    print("5.Exit")

    selection = int(input("Enter: "))

    if selection == 1: 
        bank_owner.total_balance()
    elif selection == 2:
        print("How much you would like to deposit?")
        amount = int(input("Deposit: "))
        bank_owner.deposit(amount)
        
    elif selection == 3:
        print("How much you would like to withdraw?")
        withdraw = int(input("Withdraw: "))
        bank_owner.withdraw(withdraw)
        
    elif selection == 4:
        print("Transaction history:")
        bank_owner.show_transaction()
        
    elif selection == 5:
        print("Goodbye!")
        break
    else:
        print("Please choose the right number.")
        
    print()