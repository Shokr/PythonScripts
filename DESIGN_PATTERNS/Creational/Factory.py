class ShapeInterface:
    def draw(self):
        pass


class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        elif type == 'square':
            return Square()
        else:
            assert 0, 'Could not find shape.' + type


#########
# Usage #
#########

f = ShapeFactory()

s = f.getShape('square')

print(s)
s.draw()


# x = f.getShape('cude')
# print(x)
# x.draw()
