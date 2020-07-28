from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        obj = deepcopy(self)
        obj.move(move_x, move_y)

        return obj


#########
# Usage #
#########

P0 = Point(0, 0)
print(P0.__str__())

P1 = P0.clone(1, 1)
print(P1.__str__())
