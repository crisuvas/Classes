class Triangle(object):
    number_of_side = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if(self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        super().__init__()

    def check_angles(self):
        return True


my_triangle = Triangle(90, 30, 60)
my_equilateral = Equilateral
print(my_triangle.number_of_side)
print(my_triangle.check_angles())
