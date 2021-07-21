<<<<<<< HEAD
from coins import Coin
=======

>>>>>>> 449ac70045e4b4fa54442ed6eecc46e4b7468f3b

class Wallet:
    def __init__(self):
        self.money = []
        self.fill_wallet()
<<<<<<< HEAD
        
=======
>>>>>>> 449ac70045e4b4fa54442ed6eecc46e4b7468f3b


def fill_wallet(self):
    """Method will fill wallet's money list with certain amount of each type of coin when called."""
    for index in range(8):
<<<<<<< HEAD
        self.money.append(self.Quarter())
    for index in range(10):
        self.money.append(self.Dime())
    for index in range(20):
        self.money.append(self.Nickel())
    for index in range(50):
        self.money.append(self.Penny())
=======
        self.money.append(coins.Quarter())
    for index in range(10):
        self.money.append(coins.Dime())
    for index in range(20):
        self.money.append(coins.Nickel())
    for index in range(50):
        self.money.append(coins.Penny())
>>>>>>> 449ac70045e4b4fa54442ed6eecc46e4b7468f3b
