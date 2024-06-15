# Every data structure is derived from class! like string, list, tuple, np.array, etc...
# These data type mention above are got their attributes and methods -> that's dervied from class 

class Cookie:
    def __init__(self, color: str) -> None:
        self.color = color  # Set Color of Cookie object itself

    def get_color(self):
        # if there's no argument, just Cookie itself, it can describe all attributes & methods from itself
        return self.color 
    
    def set_color(self, color: str): # further more, the object created by blueprint class Cookie, could get another methods to set its color again by send another argument from outside local function.
        self.color = color


# We can create our data structure by class: like Linked List -> just like the list datatype method
# class LinkedList:
    # def __init__(self, value):
    # def append(self, value):
    # def pop(self, value):
    # def prepend(self, value):
    # def insert(self, value):  



if __name__ == "__main__":
    Cookie_one = Cookie("Green")
    Cookie_two = Cookie("Blue")


    print("Cookie one is: ", Cookie_one.get_color())
    print("Cookie two is: ", Cookie_two.get_color())

    Cookie_one.set_color("Yellow")

    print("\nCookie one is: ", Cookie_one.get_color())
    print("Cookie two is: ", Cookie_two.get_color())