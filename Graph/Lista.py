from typing import Any


class Node:
    def __init__(self, value: Any, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        if self.head is None:
            return 0

        x = 0
        gl = self.head
        while gl is not None:
            x += 1
            gl = gl.next
        return x

    def __str__(self) -> str:
        x = ""
        gl = self.head
        if gl is not None:
            x += str(gl.value)
            gl = gl.next
            while gl is not None:
                x += "->" + str(gl.value)
                gl = gl.next
        return x

    def push(self, value: Any) -> None:
        gl = Node(value, None)
        gl.next = self.head
        self.head = gl
        if self.tail is None:
            self.tail = self.head

    def append(self, value: Any) -> None:
        gl = Node(value, None)
        if self.tail is None:
            self.tail = gl
        else:
            self.tail.next = gl
            self.tail = gl
        if self.head is None:
            self.head = self.tail

    def node(self, position) -> Node:
        gl = self.head
        for i in range(position - 1):
            gl = gl.next
        return gl

    def insert(self, value: Any, after: Node) -> None:
        gl = self.head
        if after == self.head:
            node = Node(value, gl.next)
            self.head.next = node
            return
        if after == self.tail:
            node = Node(value, gl.next)
            self.append(node.value)
            return
        while gl is not None:
            gl = gl.next
            if gl == after:
                node = Node(value, gl.next)
                gl.next = node
                break

    def pop(self) -> Any:
        gl = self.head
        self.head = self.head.next
        return gl

    def remove_last(self) -> Any:
        x = self.tail
        gl = self.head
        while gl.next.next is not None:
            gl = gl.next
        gl.next = None
        self.tail = gl
        return x


    def remove(self, after: Node) -> Any:
        gl = self.head
        if after == self.head:
            node = self.head.next.next
            self.head.next = node
            return
        while gl is not None:
            if gl == after:
                gl.next = gl.next.next
                break
            gl = gl.next


#li = LinkedList()
#li.push(15)
# assert li.head == li.tail
# x = li.node(0)
# li.push(14)
#li.append(16)
# li.append(17)
# assert str(li) == "14->15->16->17"
#li.insert(5, li.head.next)
# li.append(20)
# assert len(li) == 6
# li.remove(li.head)
# assert li.head is not None
#print(li)