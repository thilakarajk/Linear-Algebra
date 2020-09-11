class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def multiply(self, scalar):
        new_coordinates = [scalar*x for x in self.coordinates]
        return Vector(new_coordinates)

my_vect = Vector([8.218,-9.341])
my_vect2 = Vector([-1.129, 2.111])
print( my_vect.plus(my_vect2))

my_vect = Vector([7.119,8.215])
my_vect2 = Vector([-8.223,0.878])
print(my_vect.minus(my_vect2))

my_vect = Vector([1.671, -1.012, -0.318])
print(my_vect.multiply(7.41))
