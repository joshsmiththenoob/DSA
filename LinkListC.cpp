#include <iostream>

class LinkedList{
private:
    int value {};
    int *ptr {nullptr};

public:
    void point_node (int *target_ptr){
        ptr = target_ptr;
    }
    
    void set_value (int int_arg){
        value = int_arg;
    }

    int* get_address_of_value(){
        return &value;
    }

    int* get_pointer_value(){
        return ptr;
    }

    int** get_address_of_pointer(){
        return &ptr;
    }
};


int main(){
    LinkedList node1;
    LinkedList node2;

    node1.set_value(2);
    node2.set_value(3);

    node1.point_node (node2.get_address_of_value());
    
    std::cout << node1.get_pointer_value() << std::endl;
    std::cout << node1.get_address_of_pointer() << std::endl;
    std::cout << "------------ Works! ---------------" << std::endl;
    return 0;
}