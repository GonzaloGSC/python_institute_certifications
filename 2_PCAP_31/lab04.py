from typing import Any


class QueueError(IndexError):
    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self):
        return f"¡Error de Cola!: {self.args[0]}"


class Queue:
    def __init__(self):
        self.__queue: list[Any] = []

    def put(self, elem: Any):
        self.__queue = [elem] + self.__queue

    def get(self):
        if not self.__queue:
            raise QueueError(f"¡Error! Cola vacía")
        return self.__queue.pop()

    def getQueue(self):
        return self.__queue


class SuperQueue(Queue):
    def __init__(self):
        super().__init__()

    def isempty(self):
        return not super().getQueue()


def main():
    que = SuperQueue()
    que.put(1)
    que.put("perro")
    que.put(False)
    for i in range(4):  # type: ignore
        if not que.isempty():
            print(que.get())
        else:
            print("Cola vacía")


if __name__ == '__main__':
    main()
