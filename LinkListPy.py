## LinkedList by Python
class Node:
    def __init__(self, value: int, node: object = None) -> None:
        self.value = value
        self.next = node


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value: float):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def pop(self):
        # Method 1: Early Return Pattern : more readable
        # pop node of last element O(n)
        # variable in different scope are independent
        # if that scope couldn't find specific variable, it could find it outside the scope
        
        # we can use early return pattern
        if not self.head:
            raise IndexError("List is empty, no element to pop")
        
        temp_node = self.head
        pop_node = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return pop_node

        while (temp_node.next != self.tail):
            temp_node = temp_node.next

        temp_node.next = None
        self.tail = temp_node
        self.length -= 1

        return pop_node

    # def pop(self):
    #     # Method 2: only 1 return to clarify return statement
    #     # pop node of last element O(n)
    #     # variable in different scope are independent
    #     # if that scope couldn't find specific variable, it could find it outside the scope
        
    #     # we can use early return pattern
    #     # 
    #     if not self.head:
    #         raise IndexError("List is empty, no element to pop")
        
    #     temp_node = self.head
    #     pop_node = self.head

    #     while (pop_node.next != None):
    #         temp_node = pop_node
    #         pop_node = pop_node.next

    #     temp_node.next = None
    #     self.tail = temp_node

    #     if pop_node == temp_node:
    #         # No chnage after while loop -> only 1 element in list 
    #         self.head = None
    #         self.tail = None

    #     return pop_node

    def prepend(self, value):
        # append the element to the head of linked list: O(1)
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
        print("------------------ prepend executed --------------")
            

    def pop_first(self):
        # pop first element of list: O(1)
        if not self.head:
            # nothing in list
            raise IndexError("List is empty, no element to pop")
        
        pop_node = self.head
        self.head = self.head.next
        pop_node.next = None

        if pop_node == self.tail:
            # pop_node == self.head == self.tail
            self.tail = None # tail should binding to None
        self.length -= 1
        print("------------------ pop_first executed --------------")

        return pop_node
    

    def get(self, index: int):
        # READ: get node at specific index: O(n)
        # get length of list

        if (index < 0):
            raise IndexError("Out of index")
        temp_node = self.head
        current_index = 0
        while (temp_node): # if there's node
            if current_index == index:
                return temp_node
            temp_node = temp_node.next
            current_index += 1
        
        # index > count_index 
        raise IndexError("Out of index")
        
            

    def set_value(self, index: int, value: int):
        # UPDATE: set value of node at specific index: O(n)
        temp_node = self.get(index)

        # set value of specific node
        temp_node.value = value
        print("------------------ set_value executed --------------")
        print("Now the value of node is: ", temp_node.value)

    
    def insert(self, index: int, value: int):
        # insert new node at specific index: O(n)  
        if (index < 0) or (index > self.length):
            raise IndexError("Out of Index")
        elif (index == 0):
            self.prepend(value)
        elif (index == self.length):
            self.append(value)
        else:
            node = Node(value)
            pre_node = self.get(index - 1)
            node.next = pre_node.next
            pre_node.next = node    
            self.length += 1     
        print("\n--------------- insert executed ---------------")


    def remove(self, index: int):
        print("\n--------------- remove executed ---------------")
        if (index < 0) or (index >= self.length):
            raise IndexError("Out of Index")
        if (index == 0):
            return self.pop_first()
        if (index == (self.length - 1)):
            return self.pop()

        pre_node = self.get(index - 1)
        temp_node = pre_node.next
        pre_node.next = temp_node.next
        temp_node.next = None
        self.length -= 1
        return temp_node
        

    def reverse(self):
        # switch head, tail first
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node

        # need 3 variable to keep linked connect
        pre_node = None
        next_node = temp_node.next

        while (next_node != None):
            temp_node.next = pre_node
            pre_node = temp_node
            temp_node = next_node
            next_node = next_node.next
        
        self.head.next = pre_node
        print("\n--------------- reverse executed ---------------")

            


    def print_list(self):
        temp_node = self.head
        while (temp_node != None):
            print(temp_node.value)
            temp_node = temp_node.next

if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)

    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)

    print(linked_list.head.value)
    print(linked_list.head.next.value)
    print(linked_list.head.next.next.value)
    print(linked_list.head.next.next.next.value)
    print(linked_list.head.next.next.next.next.value)
    print(linked_list.head.next.next.next.next.next)
    linked_list.print_list()


    for _ in range(5):

        print("\n -------------- pop executed ------------------")
        print("pop value: ", linked_list.pop().value)
        linked_list.print_list()


    linked_list.prepend(4)
    linked_list.prepend(3)
    linked_list.print_list()

    linked_list.pop_first()
 
    linked_list.print_list()

    print(linked_list.get(0).value)

    linked_list.set_value(0, 20)
    linked_list.print_list()

    linked_list.insert(0, 77)
    linked_list.print_list()
    linked_list.insert(0, 80)
    linked_list.print_list()
    linked_list.insert(3, 80)
    linked_list.print_list()
    linked_list.insert(3, 90)
    linked_list.print_list()


    print("value of removed node: ", linked_list.remove(0).value)
    linked_list.print_list()
    print("value of removed node: ", linked_list.remove(3).value)
    linked_list.print_list()
    print("value of removed node: ", linked_list.remove(1).value)
    linked_list.print_list()
    # for _ in range(5):
    #     print("\n --------------------------------")
    #     linked_list.pop(0)
    linked_list.prepend(4)
    linked_list.prepend(3)
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()
    linked_list.append(4)
    linked_list.append(88)
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()

    #     linked_list.print_list()