from typing import Any


class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    #
    #  Escribe código aquí.
    #
    def __init__(self, message: str):
        #
        # Escribe código aquí.
        #
        super().__init__(message)

    def __str__(self):
        # Opcional: personaliza la representación como cadena
        return f"¡Error de Cola!: {self.args[0]}"


class Queue:
    def __init__(self):
        #
        # Escribe código aquí.
        #
        self.__queue: list[Any] = []

    def put(self, elem: Any):
        #
        # Escribe código aquí.
        #
        self.__queue = [elem] + self.__queue

    def get(self):
        #
        # Escribe código aquí.
        #
        if not self.__queue:
            raise QueueError(f"¡Error! Cola vacía")
        return self.__queue.pop()

    def getQueue(self):
        return self.__queue


class SuperQueue(Queue):
    #
    # Escribe código nuevo aquí.
    #
    def __init__(self):
        super().__init__()

    def isempty(self):
        return not super().getQueue()


def main():
    que = SuperQueue()
    que.put(1)
    que.put("perro")
    que.put(False)
    for i in range(4): # type: ignore
        if not que.isempty():
            print(que.get())
        else:
            print("Cola vacía")


if __name__ == '__main__':
    main()
