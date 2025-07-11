import math
from typing import Any

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x: float, y: float):
        return math.hypot(x - self.__x, y - self.__y)

    def distance_from_point(self, point: Any):
        if not isinstance(point, Point):
            raise ValueError('Parametro "point" debe ser de tipo "Point"')
        point_x = point.getx()
        point_y = point.gety()
        return math.hypot(point_x - self.__x, point_y - self.__y)


def main():
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))


if __name__ == '__main__':
    main()
