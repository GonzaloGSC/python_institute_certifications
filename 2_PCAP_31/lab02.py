from typing import Any


class Stack:
    def __init__(self):
        self.__stk: list[Any] = []

    def push(self, val: Any):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        #
        # Llena el constructor con acciones apropiadas.
        #
        Stack.__init__(self)
        self.__count: int = 0

    def get_counter(self):
        #
        # Presenta el valor actual del contador al mundo.
        #
        return self.__count

    def pop(self):
        #
        # Haz un pop y actualiza el contador.
        #
        Stack.pop(self)
        self.__count += 1


def main():
    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()
    print(stk.get_counter())


if __name__ == '__main__':
    main()
