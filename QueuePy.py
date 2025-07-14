## Queue by Python
# FIFO: First In First Out

class Node():
    def __init__(self, v: int) -> None:
        self.value = v
        self.next = None


"""
    LinkedList to analogize Queue:
        Head:
            pop_first: O(1)
            prepend: O(1) -> the first guy of queue who's ready to dequeue
        Tail:
            pop: O(n)
            append: O(1)  -> the last guy of queue who has enqueued 
"""
class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    

    def enqueue(self, v: int):
        node = Node(v)
        if (self.first is None):
            # if empty
            self.first = node
            self.last = node
        else:
            # if >= 1 element
            self.last.next = node
            self.last = node
        self.length += 1
        
        return True
    
    def dequeue(self):
        # return the dequeue of first guy
        if (self.first is None):
            # if empty
            raise IndexError("No element to dequeue")
        temp_node = self.first
        if (self.length == 1):
            # if 1 element
            self.first = None
            self.last = None
        else:
            # if 2 or more eleemnts 
            self.first = temp_node.next
            temp_node.next = None
        self.length -= 1

        return temp_node


    def print_queue(self):
        temp = self.first
        while (temp is not None):
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    q = Queue()
    q.print_queue()
    q.enqueue(2)
    q.print_queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()