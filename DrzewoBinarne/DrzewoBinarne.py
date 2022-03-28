from typing import Any, Callable, List
from Kolejka import Queue
from binarytree import tree, build2


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[['BinaryNode'], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)

        visit(self.value)

        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[['BinaryNode'], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self.value)

    def traverse_pre_order(self, visit: Callable[['BinaryNode'], None]):
        visit(self.value)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        kolejka: Queue = Queue()
        kolejka.enqueue(tree.root)
        dlugosc: int = len(kolejka)

        wartosci = []
        while True:
            while dlugosc > 0:
                tmp = kolejka.dequeue()
                if tmp.value is None:
                    wartosci.append(None)
                else:
                    wartosci.append(tmp.value.value)
                dlugosc -= 1

                if tmp.value is not None:
                    if tmp.value.left_child is not None:
                        kolejka.enqueue(tmp.value.left_child)
                    else:
                        kolejka.enqueue(None)

                    if tmp.value.right_child is not None:
                        kolejka.enqueue(tmp.value.right_child)
                    else:
                        kolejka.enqueue(None)

            dlugosc = len(kolejka)

            if dlugosc == 0:
                break

        root = build2(wartosci)
        print(root)

def visit(x):
    print(x)

def horizontal_sum(tree: BinaryTree) -> List[int]:
    kolejka: Queue = Queue()
    kolejka.enqueue(tree.root)
    dlugosc: int = len(kolejka)

    wartosci: List[List[int]] = []
    while True:
        li: List[int] = []

        while dlugosc > 0:
            tmp = kolejka.dequeue()
            li.append(tmp.value.value)
            dlugosc -= 1
            if tmp.value.left_child is not None:
                kolejka.enqueue(tmp.value.left_child)
            if tmp.value.right_child is not None:
                kolejka.enqueue(tmp.value.right_child)

        wartosci.append(li)
        dlugosc = len(kolejka)

        if dlugosc == 0:
            break

    wynik:List[int] = []

    for liczby in wartosci:
        x = 0
        for i in liczby:
            x += i
        wynik.append(x)

    return wynik

root = BinaryNode(1)
root.add_left_child(2)
root.left_child.add_left_child(4)
root.left_child.left_child.add_left_child(8)
root.left_child.left_child.add_right_child(9)
root.left_child.add_right_child(5)
root.add_right_child(3)
root.right_child.add_right_child(7)



tree = BinaryTree(root)
tree.show()
print(horizontal_sum(tree))




