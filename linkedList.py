class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node


class SingleyLinkedList:

    def __init__(self):
        self.head = None

    def add_first(self, new_node):

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_last(self, new_node):

        if self.head == None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next != None:
                temp_node = temp_node.next
                
            temp_node.next = new_node
    
    def remove_first(self):

        if self.head == None:
            print("Linked list is empty")
            return
        else:
            self.head = self.head.next
    
    def remove_last(self):
        
        if self.head == None:
            print("Linked list is empty")
            return
        else:
            temp_node == self.head

            while temp_node.next.next != None:
                temp_node = temp_node.next
            temp_node.next = None
    
    def get_first(self):
        if self.head == None:
            print("Linked list is empty")
            return False
        else:
            return self.head
    
    def get_last(self):
        if self.head == None:
            print("Linked list is empty")
            return False
        else:
            temp_node = self.head

            while temp_node.next != None:
                temp_node = temp_node.next
            return temp_node
        
    def get_node_by_data(self, data):
        if self.head == None:
            print("Linked list is empty")
            return False
        else:
            temp_node = self.head
            while temp_node.data != data:
                temp_node = temp_node.next
                if temp_node.next == None:
                    print("Data is not in list")
                    return False
            return temp_node
            
def main():

    LL = SingleyLinkedList()

    LL.add_last(Node(1))
    LL.add_last(Node(2))
    LL.add_last(Node(3))

    get_head_node = LL.get_first()
    print(get_head_node.data)

    get_middle_node = LL.get_node_by_data(2)
    print(get_middle_node.data)

    get_tail_node = LL.get_last()
    print(get_tail_node.data)

main()
