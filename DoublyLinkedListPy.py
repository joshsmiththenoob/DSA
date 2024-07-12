## DoublyLinkedList(DLL) by Python
class Node():
    # class constructor method
    def __init__(self, v: int) -> None:
        # class attribute
        self.value = v
        self.next = None
        self.pre = None

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, v: int):
        node = Node(v)
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
        self.length += 1

        return True 


    def pop(self):
        # return the popped element 
        if (self.head == None):
            raise IndexError("No element to pop")
        
        temp = self.tail

        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.tail = temp.pre
            temp.pre = None
            self.tail.next = None   
        self.length -= 1

        return temp
    
    
    def prepend(self, v: int):
        # append element to head of DLL
        node = Node(v)
        if (self.head == None):
            # if no element
            self.head = node
            self.tail = node
        else:
            # if >= 1 element
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.length += 1

        return True
    
    
    def pop_first(self):
        # return the popped first element
        if (self.head == None):
            # if empty
            raise IndexError("No element to pop")
        
        temp = self.head
        if (self.length == 1):
            # if 1 element
            self.head = None
            self.tail = None
        else:
            # if >= 1 element
            self.head = temp.next
            temp.next = None
            self.head.pre = None
        self.length -= 1

        return temp

    
    def get(self, index: int):
        # get element of index
        # Note: DLL got more efficiency for get method
        # But Time Complexity still is : O(n/2) -> O(n) if n >> 0, ignore constant 
        if (self.head == None):
            # if empty
            raise IndexError("No element to pop")
        
        if (index < (self.length) / 2):
            # if index < half of length: start with head
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            # if index > half of length: start with tail
            temp = self.tail
            for _ in range(self.length - 1, index, -1): # decrease gradully by 1
                temp = temp.pre

        return temp


    def set_value(self, index: int, v: int):
        temp = self.get(index)
        temp.value = v

        return True
            
        
    def insert(self, index: int, v: int):
        # insert new node of value to specific index
        if (index < 0 or index > self.length):
            raise IndexError("out of index")
        if (index == 0):
            return self.prepend(v)
        if (index == self.length):
            return self.append(v)

        node = Node(v)
        temp = self.get(index)
        prev = temp.pre
        node.next = temp
        node.pre = prev
        prev.next = node
        temp.pre = node
        self.length += 1

        return True
    
    
    def remove(self, index: int):
        # return removed node on specifix index
        if (index < 0 or index >= self.length):
            raise IndexError("out of index")
        if (index == 0):
            return self.pop_first()
        if (index == (self.length - 1)):
            return self.pop()
        
        temp_node = self.get(index)

        # we don't have to declare more variable (reference) to get previous, next node of temp node        
        temp_node.pre.next = temp_node.next # pre_node = temp_node.pre
        temp_node.next.pre = temp_node.pre # next_node = temp_node.next
        temp_node.next = None
        temp_node.pre = None
        self.length -= 1

        return temp_node



            
        
        
    def print_list(self):
        print("------------ Elements of List ------------")
        temp = self.head
        while (temp != None):
            print(temp.value)
            temp = temp.next
    
    
if __name__ == "__main__":
    d_linked_list = DoublyLinkedList()
    d_linked_list.print_list()
    d_linked_list.append(0)
    d_linked_list.append(1)
    d_linked_list.append(2)
    d_linked_list.print_list()
    print(d_linked_list.length)
    d_linked_list.remove(1)
    d_linked_list.print_list()
    print(d_linked_list.length)


    
    print("-------------------------- Works! -------------------------")
    