from typing import Any


class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    #
    #  Escribe código aquí.
    #
    def __init__(self, message:str):
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
