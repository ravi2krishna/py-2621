# With Abstraction - End User Sees Only Necessary Details 

from vendors import Dell

dell_laptop = Dell()

dell_laptop.should_have_processor()
dell_laptop.should_have_ram()

# atm_object = ATM()
# atm_object.check_balance()
# atm_object.withdraw()
# atm_object.get_statement()
# atm_object.change_pin()