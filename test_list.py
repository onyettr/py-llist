import unittest
from pylist import listSingle

class TestSingleList(unittest.TestCase):
    """
        unit test harness for the single List
    """

    def test_list_add_one_element(self):
        """
            Test list_add first element
        """
        list = listSingle(10)

        try:
            list.list_add(100)
        except:
            pass

    def test_list_show_no_elements(self):
        """
            Test list_show with no elements
        """
        list = listSingle(10)        
        try:
            list.list_show()
        except ValueError as e:
            print("- ", e)
        else:
            self.fail("test_list_show - didnt see exception error")

    def test_list_show_with_elements(self):
        """
            Test list_show with elements
        """
        list = listSingle(10)
        list.list_add(10)
        list.list_add(11)        

        try:
            list.list_show()
        except ValueError as e:
            print("- ", e)
            
if __name__ == '__main__':
    unittest.main()
        
