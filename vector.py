from math import sqrt


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

    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.multiply(1./magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize zero vector')


my_vect = Vector([-0.221,7.437])
print('{:.3f}'.format(my_vect.magnitude()))
print(my_vect.normalize())
