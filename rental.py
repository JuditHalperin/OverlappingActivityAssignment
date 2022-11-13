
class Rental:

    def __init__(self, start, end):
        """constructor"""
        assert 0 < start < end
        self.start = start  # start time
        self.end = end  # end time
        self.invalid_items = []  # list of items assigned to overlapping rentals - this rental cannot be assigned to them
        self.item = None  # the item this rental is assigned to

    def __str__(self):
        """class-to-string (for nice debugging prints)"""
        return str(self.start) + "-" + str(self.end)
