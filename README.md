# Overlapping Activity Assignment

The activity selection algorithm is an optimal greedy algorithm: given a set of activities, each marked by a start time and end time, it selects the maximum number of non-conflicting activities that can be performed.

The overlapping activity assignment algorithm, based on the above algorithm, solves a more complex problem. Given a set of activities and a natural number N, it tells whether all the activities can be performed, when maximum N conflicting activities are allowed at a time.

This was developed for rentals app, to determine whether a product can be rented, considering the already existing rentals and the number of available items.


### Scripts

`algorithm.py` includes the optimal overlapping activity assignment algorithm. The script documentation explains each step of the algorithm. `rental.py` contains the Rental class, and `run.py` can be used to test the algorithm with various parameters.
