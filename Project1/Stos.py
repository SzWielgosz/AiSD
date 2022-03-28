from typing import Any
from LinkedList import LinkedList

class Stack:
    storage: LinkedList

    def __init__(self, storage = LinkedList()) -> None:
        self.storage = storage

    def __str__(self) -> str:
        x = ""
        li = []
        gl = self.storage.head
        while gl is not None:
            li.append(gl.value)
            gl = gl.next
        for i in range(len(li), 0, -1):
            x += str(li[i - 1])
            x += "\n"

        return x

    def __len__(self) -> int:
        x = 0
        gl = self.storage.head
        while gl is not None:
            x += 1
            gl = gl.next
        return x

    def push(self, element: Any) -> None:
        self.storage.append(element)

    def pop(self) -> Any:
        self.storage.remove_last()


# stos = Stack()
# assert stos.storage.head is None and stos.storage.tail is None
# stos.push(10)
# stos.push(15)
# assert str(stos) == "15\n10\n"
# stos.push(20)
#
# print(stos)
