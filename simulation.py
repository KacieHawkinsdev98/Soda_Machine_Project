<<<<<<< HEAD
from soda_machine import SodaMachine
from customer import Customer
import user_interface
=======
from customer import Customer
from soda_machine import SodaMachine
import user_interface 


>>>>>>> da546b0bb481d340effcc55fe0180bedb179096f

class Simulation:
    def __init__(self):
       pass 

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = True
        while will_proceed == True:
            user_option = user_interface.simulation_main_menu()
<<<<<<< HEAD
            if user_option == "1":
                soda_machine.begin_transaction(customer)
            elif user_option == "2":
                customer.check_coins_in_wallet()
            elif user_option == "3":
=======
            if user_option == 1:
                soda_machine.begin_transaction(customer)
            elif user_option == 2:
                customer.check_coins_in_wallet()
            elif user_option == 3:
>>>>>>> da546b0bb481d340effcc55fe0180bedb179096f
                customer.check_backpack()
            else:
                will_proceed = False
