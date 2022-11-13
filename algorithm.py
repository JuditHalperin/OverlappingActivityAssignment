
"""

Overlapping Activity Assignment

Given a set of activities and a natural number N, the algorithm tells whether all the
activities can be performed, when maximum N conflicting activities are allowed at a time.

This algorithm, based on the activity selection algorithm, was developed for rentals app,
to determine whether a product can be rented, considering the already existing rentals and the number of
available items. It is a boolean method that also returns the assignment of available items to the rental list.


Note:
1. Start and end time are integers here.
2. Activity list is not sorted (by end and then by start).
3. Difference of 0 is not considered as an overlap (e.g. 1-2 and 2-3 do not overlap).   TODO: add 'difference' argument to allow various values of differences.

"""


def activity_selection(activities, new_activity, overlaps):
    """
    Algorithm for activity selection with overlaps
    Adds the new activity and checks whether or not all activities can be assigned to items, considering the allowed number of overlaps
    Also, assign the item of each activity, when the items = 0, 1, ..., (overlaps-1)
    """

    all_activities = activities + [new_activity]  # create a temporary list of activities with the new one (keep sorted?)
    all_activities = sorted(all_activities, key=lambda x: (x.end, x.start))  # sort list by end time and then by start time (needed?)

    assert overlaps >= 1
    max_end_time = [0] * overlaps  # list indicating for each item what is the max end time of the activities assigned to it

    for index in range(len(all_activities)):  # index = 0, 1, ..., (length-1)
        activity = all_activities[index]  # current iteration activity

        # check if activity can be assigned to some item:
        if len(activity.invalid_items) == overlaps:  # too much overlaps of this activity
            return False  # all activities cannot be assigned to items, so the new activity cannot be added

        # otherwise, assign item to activity:
        # the optimal assignment minimizes the space between this activity and the last activity in the item
        # in other words, it chooses the item with the largest 'max_end_time'
        best_item = -1
        for item in range(overlaps):  # iterate existing items: 0, 1, ..., (overlaps-1)
            if item not in activity.invalid_items:  # if current item is valid (meaning, overlapping activities are not assigned to it)
                if best_item == -1 or max_end_time[item] > max_end_time[best_item]:  # if it is the first valid item or if its max_end_time is better
                    best_item = item  # update the optimal assignment
        activity.item = best_item  # assign item to activity using the optimal assignment
        max_end_time[activity.item] = activity.end  # update max_end_time of the chosen item (based on the last added activity because of the sort by end time)

        # update invalid items of the rest activities:
        if index + 1 != len(all_activities):  # in case it is not the last in the list
            for next_activity in all_activities[index + 1:]:  # all_activities[index + 1:] includes activities following the current activity (which not included)
                if next_activity.start < activity.end:  # overlapping activities (since: next_activity.end >= activity.end)
                    if activity.item not in next_activity.invalid_items:  # in case the activity has not been found already to overlap with previous activities assigned to this item
                        next_activity.invalid_items += [activity.item]  # add the assigned item to the invalid items list, to make sure overlapping activities will not be assigned to the same item

    return True  # all activities can be assigned to items, so the new activity can be added


def print_assignments(activities):
    """Prints sorted items with activities. Assumes all activities are assigned to items (i.c. not None)"""
    print("\nAssignment:")
    item = 0
    print("Item " + str(item) + ":", end=" ")
    for activity in sorted(activities, key=lambda x: (x.item, x.start)):
        if activity.item != item:
            item += 1
            print("\nItem " + str(item) + ":", end=" ")
        print(activity, end=" ")
    print()


def check_new_rental(rentals, new_rental, num_items):
    """Checks if a new rental can be added to the already existing rentals, considering the number of available items, and prints the results"""

    # input:
    print("Number of items:", num_items)
    print("Existing rentals:", end=" ")
    for rental in sorted(rentals, key=lambda x: (x.start, x.end)):
        print(rental, end=" ")
    print("\n")

    # output:
    if activity_selection(rentals, new_rental, num_items):  # all rentals can be assigned to items
        print("Rental " + str(new_rental) + " can be added :)")
        rentals += [new_rental]  # add the new rental (keep the list sorted?)
        print_assignments(rentals)  # print assignments for debugging (using field Rental.item, assuming 'rentals' and 'new_rental' are sent by reference)
    else:  # not all rentals can be assigned to items
        print("Rental " + str(new_rental) + " can not be added :(")
        # cannot print_assignments() because the assignment has might been stopped before all rentals were assigned
