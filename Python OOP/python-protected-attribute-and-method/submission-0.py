class Account:
    def __init__(self, title: str, balance: int):
        """ initialize an account object. """
        self.title = title # a public attribute
        self._balance = balance # protected attribute
    
    def display_balance(self) -> None:
        """ a public getter method to access/display the protected attribute _balance. """
        print(f"Balance: ${self._balance}")

# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
