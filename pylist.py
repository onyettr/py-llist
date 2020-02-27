#!/usr/bin/python3.7
#pylint; ignore invalid-name
"""
   Single Linked List implementation

"""

class Node(object):
    """
       Node item for the linked lists, contains the actual data
    """
    def __init__(self, nodedata = None):
        self.next = None
        self.data = nodedata

    
class listSingle(object):
    """
        simple class type for a single linked list
    """
    def __init__(self, nodedata):
        self.head = None
        self.tail = None
        self.next = None
        self.count = 0
        self.data = nodedata
        print("list ctor ")
        
    def list_add(self, data):
        """
            Add a new element to the list
        """
        new_node = Node()
        new_node.data = data
        new_node.next = None

        if self.head is None:
           """
               We are first element 
           """
           self.head = new_node
           self.tail = new_node

        else:
            self.next = new_node
            self.tail = self.next
        self.count = self.count + 1
        
    def list_show(self):
        """
            Show contents of the list
        """
        if self.head is None:
            raise ValueError("List is empty!")
            return

        current = self.head
        
        while current is not None:
            print("data ", current.data)
            current = current.next
            

if __name__ == "__main__":
    list1 = listSingle(10)

    try:
        list1.list_show()
    except ValueError as e:
        print("- ", e)
        
    
