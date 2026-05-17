class PasswordManager:
    def __init__(self, password: str):
        """ Initializes the password object. """
        self.__password = password # private attribute
    
    # TODO: Implement the verify_password method
    def verify_password(self, password: str) -> bool:
        return password == self.__password



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
