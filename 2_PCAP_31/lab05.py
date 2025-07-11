from datetime import datetime, time as datetime_time, timedelta


class Timer:
    def __init__(self, hh: int = 0, mm: int = 0, ss: int = 0):
        self.__otime: datetime_time = datetime_time(hh, mm, ss)

    def __str__(self):
        return str(self.__otime.strftime('%H:%M:%S'))

    def next_second(self):
        dt = datetime.combine(
            datetime.min.replace(year=1900).date(),
            self.__otime
        ) + timedelta(seconds=1)
        self.__otime = dt.time()

    def prev_second(self):
        dt = datetime.combine(
            datetime.min.replace(year=1900).date(),
            self.__otime
        ) - timedelta(seconds=1)
        self.__otime = dt.time()


def main():
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)


if __name__ == '__main__':
    main()
