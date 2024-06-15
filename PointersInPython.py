# Pointers: Just like variable point to the address of memory which stored different datatype

num1 = 11

num2 = num1 # but It's the references actually! = alias

print("\n------------------------------------------------")
print("Before num2 update its value: ")
print("num1 is: ", num1)
print("num2 is: ", num2)

print("variable num1 is pointing to: ", id(num1))
print("variable num2 is pointing to: ", id(num2))

## Immutable object: int, double... -> const value on the address
# In Python, if one of the variable(pointer) want to chnage the immutable object's value(int) holded by address the pointer pointing to
# the variable (pointer) will pointer anywhere else of address assigned the specified immutable object's value(int) we want
# different in C++, the C++ has the standard pionter!, when we change the value holded by address, any dereference of the pointer will change Synchronously
num1 = 32

print("\nAfter num2 update its value: ")
print("num1 is: ", num1)
print("num2 is: ", num2)

print("variable num1 is pointing to: ", id(num1))
print("variable num2 is pointing to: ", id(num2))

## mutable object: list, tuple, dictionary... -> variable value on the address
# In contrary, mutable object can be changed on the address, so if one of the variable change the mutable object's value hold by address.
# and the changed was allowed, result in two variables still refer to the same address 
# ofc the value of 2 variables refer to change Synchronously

list1 = [1, 2, 3, 4]
list2 = list1
print("\n------------------------------------------------")
print("Before list2 update its element: ")
print("num1 is: ", list1)
print("num2 is: ", list2)

print("variable list1 is pointing to: ", id(list1))
print("variable list2 is pointing to: ", id(list2))


list2[0] = 40

print("\nAfter list2 update its element: ")
print("num1 is: ", list1)
print("num2 is: ", list2)

print("variable list1 is pointing to: ", id(list1))
print("variable list2 is pointing to: ", id(list2))

## But!! if we created the NEW LIST = NEW OBJECT and assign it to one of variables
# -> Python would allocated the new address and assign NEW LIST to it combined by specified variable
# -> just Like what immutable object do in python

list2 = [10, 22, 23, 55]

print("\nAfter list2 change its whole list: ")
print("num1 is: ", list1)
print("num2 is: ", list2)

print("variable list1 is pointing to: ", id(list1))
print("variable list2 is pointing to: ", id(list2))