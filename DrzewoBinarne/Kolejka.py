from typing import Any
from Lista import LinkedList

class Queue:
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
            x += "->" + str(li[i - 1])

        return x

    def __len__(self) -> int:
        x = 0
        gl = self.storage.head
        while gl is not None:
            x += 1
            gl = gl.next
        return x

    def peek(self):
        return self.storage.head

    def enqueue(self, element: Any) -> None:
        self.storage.append(element)

    def dequeue(self) -> Any:
        return self.storage.pop()


# kolejka = Queue()
# assert kolejka.storage.head is None and kolejka.storage.tail is None
# kolejka.enqueue(5)
# kolejka.enqueue(10)
# assert str(kolejka) == "->10->5"
# kolejka.enqueue(15)
# kolejka.enqueue(20)
# kolejka.dequeue()
# assert len(kolejka) == 3
# print(kolejka)
# print(len(kolejka))
