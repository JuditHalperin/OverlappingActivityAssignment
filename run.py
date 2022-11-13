
from rental import Rental
from algorithm import check_new_rental


num_items = 2  # number of existing items
rentals = [Rental(1, 2), Rental(1, 3)]  # list of rentals (sorted list?)
new_rental = Rental(5, 10)  # new rental to check

check_new_rental(rentals, new_rental, num_items)
