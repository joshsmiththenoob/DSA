## Stack by Python
"""
Stack property:
    Top of Stack : O(1) for pop_first, prepend
    Bottom of Stack : O(n) for pop, append
"""
# Can adjust Single LinkedList to create Stack
class Node():
    # class constructor method
    def __init__(self, v: int) -> None:
        # class attribute
        self.value = v
        self.next = None


class Stack():
    # remove tail of LinkedList that Stack could realize its property
    """
    Stack property:
        Top of Stack : O(1) for pop_first, prepend
        Bottom of Stack : O(n) for pop, append
    """
    def __init__(self):
        self.top = None
        self.height = 0 # like length of linkedlist

    
    def print_stack(self):
        temp = self.top
        while (temp != None):
            print(temp.value)
            temp = temp.next


    def push(self, v: int):
        # push new node onto top of stack
        node = Node(v)

        # boundary condition 1: if empty
        if (self.top == None):
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

        return True
    

    def pop(self):
        # return top node of stack we want to pop
        # boundary condition: if empty
        if (self.top == None):
            raise IndexError("Stack is empty. No element to pop")
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1

        return temp



if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.print_stack()
    stack.push(1)
    stack.print_stack()
    print(stack.pop().next)
    print(stack.pop().next)
    print(stack.pop().value)