#!/usr/bin/python3.7
#pylint; ignore invalid-name
import logging

"""
   Single Linked List implementation

"""

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
#logger.setLevel(logging.DEBUG)
#ch = logging.StreamHandler()
#ch.setLevel(logging.ERROR)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
#ch.setFormatter(formatter)
#logger.addHandler(ch)

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
        
    def list_add(self, data):
        """
            Add a new element to the list
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
            currenthead = self.head
            currenthead.next = new_node     # Point at the new node
            self.next = currenthead         # Move head to new node
            self.tail = self.next
            self.logger.debug("  added as new Next {}".format(self.next))

        self.count = self.count + 1

        self.logger.debug("  Head {}".format(hex(id(self.head))))
        self.logger.debug("  Tail {}".format(hex(id(self.tail))))

        self.logger.info(">> list_add Exit")
        
    def list_show(self):
        """
            Show contents of the list
        """
        if self.head is None:
            raise ValueError("List is empty!")
            return

        current = self.head
        print("Head ", current)
        print("Count ", self.count)
        
        while current is not None:
            print("data ", current.data)
            current = current.next
            

if __name__ == "__main__":
    list1 = listSingle(10)

    try:
        list1.list_show()
    except ValueError as e:
        logger.error(e)

    list1.list_add(100)
    list1.list_add(101)
    list1.list_add(102)        
    try:
        list1.list_show()
    except ValueError as e:
#        print("- ", e)
        logger.error(e)
    
    
