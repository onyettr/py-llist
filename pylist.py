#!/usr/bin/python3.7
#pylint; ignore invalid-name
import logging

"""
   Single Linked List implementation

"""

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

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
        self.logger = logging.getLogger('list single')
        self.logger.info("list ctor ")

    def list_empty(self):
        """
            Test if list is empty
        """
        if self.head is None:
            return True

        return False
        
    def list_add_front(self, data):
        """
            Add a new element to the front of the list
        """
        new_node = Node()               # create a new list element
        new_node.data = data            # 
        new_node.next = self.head       # Move the Head to this new element, making it first
        self.head = new_node            

        self.count = self.count + 1        

    def list_add_back(self, data):
        """ 
           Add a new element to the back of the list
        """
        new_node = Node()               # create a new list element
        new_node.data = data            # 
        new_node.next = None       

        if self.tail is None:           # first element
            self.head = new_node
            self.tail = new_node
        else:
            tail = self.tail
            tail.next = new_node
            self.tail = new_node
        self.count = self.count + 1        
        
    def list_add(self, data):
        """
            Add a new element to the list (append)
        """
        self.logger.info(">> list_add Enter {}".format(data))
        
        new_node = Node()
        new_node.data = data
        new_node.next = None
        self.logger.debug("  new node {}".format( hex(id(new_node))))
        
        if self.head is None:
           """
               We are first element 
           """
           self.head = new_node
           self.tail = new_node
           
           self.logger.debug("  added as first ")
        else:
           current_tail = self.tail
           current_tail.next = new_node
           self.tail = current_tail.next
           self.logger.debug("  added as new Next {}".format(self.next))           

        self.count = self.count + 1

        self.logger.debug("  Head {}".format(hex(id(self.head))))
        self.logger.debug("  Tail {}".format(hex(id(self.tail))))

        self.logger.info(">> list_add Exit")

    def list_get_front(self):
        """
            Return elemnt at the front of the list
        """
        if list_empty():
            raise ValueError("List is empty!")
            return
        head = self.head
        value = head.data

        return data
        
    def list_get_back(self):
        """
            Return elemnt at the back of the list
        """
        
    def list_search(self, value):
        """
            Search list for specific item
        """
        position = 0
        
        if self.head is None:
            raise ValueError("List is empty!")
            return -1
        
        current = self.head
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position = position + 1


        return -1

    def list_show(self):
        """
            Show contents of the list
        """
        if self.head is None:
            raise ValueError("List is empty!")
            return

        current = self.head
        self.logger.info("  Head {}".format(hex(id(self.head))))
        self.logger.info("  Tail {}".format(hex(id(self.tail))))
        self.logger.info("  Count {}".format(self.count))

        banner = "      Address   \tValue\t   pNext\t# Nodes [" + str(self.count) + "]";
        print(banner)
        
        while current is not None:
            print("  [" + hex(id(current)) +  "]\t", end='')
            print(current.data, end='')
            print("\t[" + str(hex(id(current.next))), end='')
            print("]", end='')
            if current == self.head:
                print("   <---- HEAD", end='')
            if current == self.tail:
                print("\t   <---- TAIL", end='')                
            print("")
            current = current.next

if __name__ == "__main__":
    list1 = listSingle(10)
    list2 = listSingle(5)
    
    try:
        list1.list_show()
    except ValueError as e:
        logger.error(e)

    list1.list_add(100)
    list1.list_add(101)
    list1.list_add(102)
    list1.list_add(103)
    list1.list_add(104)
    list1.list_add(105)            
    try:
        list1.list_show()
    except ValueError as e:
        logger.error(e)
    
    list2.list_add(20)
    list2.list_add(21)
    list2.list_add(2)    

    print(list2.list_search(20))
    print(list2.list_search(21))    
    print(list2.list_search(22))

    print("add to front")
    list2.list_show()
    list2.list_add_front(1001)
    list2.list_show()

    print("list_get_front = ", list2.list_get_front())

    print("add to back")
    list2.list_add_back(2002)
    list2.list_show()
