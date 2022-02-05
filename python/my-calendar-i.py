class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value[0] < self.value[0]:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif self.value[0] < value[0]:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def find(self, value):
        available_spot = None
        if value[0] < self.value[0] and self.left:
            available_spot = self.left.find(value)
        elif self.value[0] < value[0] and self.right:
            available_spot = self.right.find(value)
        if not available_spot and self.value[0] <= value[0] and value[1] <= self.value[1]:
            available_spot = self
        return available_spot


class MyCalendar:
    def __init__(self):
        self.available = BSTNode((0,1000000000))        

    def book(self, start: int, end: int) -> bool:
        value = (start, end)
        available_spot = self.available.find(value)
        if available_spot:
            available_start, available_end = available_spot.value
            # update and insert new divided spot
            available_spot.value = (available_start, start)
            available_spot.insert((end, available_end))
            return True
        return False
