class Account:
    def __init__(self, initial):
        self.balance = initial

    def get_balance(self):
        return self.balance

    def deposit(self):
        self.balance += int(input("Deposit amount: "))
        return self.balance

    def withdrawal(self):
        withd = int(input("Withdrawl amount: "))
        if withd > self.balance:
            print("Cannot withdrawal more what is in the account.")
        else:
            self.balance -= withd
        return self.balance


"""initial amount"""
balance = 500

account1 = Account(balance)
while True:
    print("1. Balance\n2. Deposit\n3. Withdrawal\n4. Exit")
    user_input = str(input("Hello. What would you like to do? Enter the number: "))

    if user_input == "1":
        print("Current Balance: $" + str('%.2f' % (account1.get_balance())))
    elif user_input == "2":
        print("Current Balance: $" + str('%.2f' % (account1.deposit())))
    elif user_input == "3":
        print("Current Balance: $" + str('%.2f' % (account1.withdrawal())))
    elif user_input == "4":
        break

    print("")

print("Ending Program.")

"""
    while True:
        try:
            user_input = str(input())
        except ValueError:
            print("Invalid input, try again.")

        if 1 <= user_input <= 4:
            continue
        else:
            break
"""
