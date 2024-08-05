class Account:
    def __init__(self):
        self._balance = 1

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
        account = Account()
        print("Current balance:", account.balance)
        account.deposit(1001)
        print("New balance after deposit:", account.balance)
        account.withdraw(501)
        print("New balance after withdrawal:", account.balance)

# Call the main function
main()
