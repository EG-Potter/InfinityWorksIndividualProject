import unittest

from main_functions import *


class TestMethods(unittest.TestCase):

    #TODO create a unit-test for clear_screen() function?

    # display_list_elements() testing.
    def test_display_list_elements_with_elements_in_list(self):
        test_list = ["First", "Second", "Third"]
        result = display_list_elements(test_list)
        self.assertEqual(result, '\nList of Products in Storage:\n\nFirst\nSecond\nThird\n')

    def test_display_list_elements_with_empty_list(self):
        test_list = []
        result = display_list_elements(test_list)
        self.assertEqual(result, '\nList of Products in Storage:\n\n')
    

    # display_elements_with_index_values() testing.
    def test_display_elements_with_index_values_with_elements_in_list(self):
        test_list = ["First", "Second", "Third"]
        result = display_elements_with_index_values(test_list)
        self.assertEqual(result, '\nList of Products and Indexes:\n\n0: First\n1: Second\n2: Third\n')
    
    def test_display_elements_with_index_values_with_empty_list(self):
        test_list = []
        result = display_elements_with_index_values(test_list)
        self.assertEqual(result, '\nList of Products and Indexes:\n\n')


    # user_index_validation() testing.
    def test_user_index_validation_with_value_within_index_range(self):
        test_list = ["First", "Second", "Third"]
        test_value = 0
        result = user_index_validation(test_value, test_list)
        self.assertEqual(result, True)

    def test_user_index_validation_with_value_outside_index_range(self):
        test_list = ["First", "Second", "Third"]
        test_value = 4
        result = user_index_validation(test_value, test_list)
        self.assertEqual(result, False)


    # user_product_validation() testing.
    def test_user_product_validation_with_element_within_list(self):
        test_list = ["First", "Second", "Third"]
        test_value = "First"
        result = user_product_validation(test_value, test_list)
        self.assertEqual(result, False)

    def test_user_product_validation_with_element_not_in_list(self):
        test_list = ["First", "Second", "Third"]
        test_value = "Forth"
        result = user_product_validation(test_value, test_list)
        self.assertEqual(result, True)


#TODO review this functionality.
if __name__ == "__main__":
    unittest.main()