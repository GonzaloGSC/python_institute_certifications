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
            raise ValueError(
                f'Parametro "point" debe ser de tipo "Point", no {type(point)}')
        point_x = point.getx()
        point_y = point.gety()
        return math.hypot(point_x - self.__x, point_y - self.__y)


class Triangle:
    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.__v_list: list[Point] = [v1, v2, v3]

    def perimeter(self):
        sum = 0.0
        for i in range(len(self.__v_list)):
            if i == 0:
                continue
            if i < len(self.__v_list) - 1:
                sum += self.__v_list[i].distance_from_point(
                    self.__v_list[i - 1]
                )
            if i == len(self.__v_list) - 1:
                sum += self.__v_list[i].distance_from_point(
                    self.__v_list[i - 1]
                )
                sum += self.__v_list[i].distance_from_point(
                    self.__v_list[0]
                )
        return sum


def main():
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())


if __name__ == '__main__':
    main()
