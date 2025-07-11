from typing import Any
# from datetime import datetime, time as datetime_time, timedelta


class WeekDayError(Exception):
    def __init__(self, message: str):
        print(message)


class Weeker:
    __values = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day: Any):
        if not isinstance(day, str):
            raise WeekDayError('La variable "day" debe ser tipo "str".')
        if not day in self.__values:
            raise WeekDayError(
                f'La variable "day" debe estar dentro de estos valores: {self.__values}.')
        self.__day: str = day

    def __str__(self):
        return self.__day

    def add_days(self, n: int):
        if n < 0:
            raise WeekDayError(
                'El numero de días ingresado no es valido (negativo).'
            )
        actual_index = self.__values.index(self.__day)
        remainder = (actual_index + n) % 7
        self.__day = self.__values[remainder]

    def subtract_days(self, n: int):
        if n < 0:
            raise WeekDayError(
                'El numero de días ingresado no es valido (negativo).'
            )
        actual_index = self.__values.index(self.__day)
        remainder = (actual_index - n) % 7
        self.__day = self.__values[remainder]


def main():
    try:
        weekday = Weeker('Lun')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Lu')
    except WeekDayError:
        print("Lo siento, no puedo atender tu solicitud.")


if __name__ == '__main__':
    main()
