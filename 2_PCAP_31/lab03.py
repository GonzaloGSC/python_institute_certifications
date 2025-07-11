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


def main():
    que = Queue()
    que.put(1)
    que.put("perro")
    que.put(False)
    try:
        for i in range(4):  # type: ignore
            print(que.get())
    except:
        print("Error de Cola")


if __name__ == '__main__':
    main()
