<<<<<<< HEAD
from soda_machine import SodaMachine
=======

>>>>>>> 449ac70045e4b4fa54442ed6eecc46e4b7468f3b

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = False
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
<<<<<<< HEAD
            if user_option == "1":
                soda_machine.begin_transaction(customer)
            elif user_option == "2":
                customer.check_coins_in_wallet()
            elif user_option == "3":
=======
            if user_option = "1":
                soda_machine.begin_transaction(customer)
            elif user_option = "2":
                customer.check_coins_in_wallet()
            elif user_option = "3":
>>>>>>> 449ac70045e4b4fa54442ed6eecc46e4b7468f3b
                customer.check_backpack()
            else:
                will_proceed = False
