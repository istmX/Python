# Encapsulation
# Encapsulation means bundling data and the methods that work on it,
# and protecting the data from accidental changes from outside.

# Python uses naming conventions to signal how attributes should be used:
#   name        -> public: anyone can access
#   _name       -> protected: internal use, but still accessible
#   __name      -> private: name is mangled to discourage outside access

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._bank = "ISTMX Bank"   # protected (by convention)
        self.__balance = balance    # private (name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        # A controlled way to read the private balance
        return self.__balance


account = BankAccount("Aryan", 1000)

# Public attribute: accessible directly
print("Owner:", account.owner)          # Aryan

# Protected attribute: accessible, but you should not touch it
print("Bank:", account._bank)           # ISTMX Bank

# Private attribute: direct access is blocked by name mangling
# print(account.__balance)              # AttributeError!
print("Balance via method:", account.get_balance())   # 1000

# All changes go through controlled methods
account.deposit(500)        # Deposited 500. New balance: 1500
account.withdraw(2000)      # Invalid withdrawal amount.
account.withdraw(300)       # Withdrew 300. New balance: 1200

# Note: Python's privacy is by convention, not strict enforcement.
# account._BankAccount__balance would still work — but never do that.
# Respect the underscore: it is a promise about how the class should be used.
