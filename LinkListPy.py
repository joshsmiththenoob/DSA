## LinkedList by Python
class Node:
    def __init__(self, value: int, node: object = None) -> None:
        self.value = value
        self.next = node


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.node = None

    def append(self, node: object):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            


if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)

    linked_list = LinkedList()

    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.append(node3)
    linked_list.append(node4)
    linked_list.append(node5)

    print(linked_list.head.value)
    print(linked_list.head.next.value)
    print(linked_list.head.next.next.value)
    print(linked_list.head.next.next.next.value)
    print(linked_list.head.next.next.next.next.value)
    print(linked_list.head.next.next.next.next.next)

            