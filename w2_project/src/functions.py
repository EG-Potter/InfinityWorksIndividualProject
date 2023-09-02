import os

""" (*) TERMINAL/DISPLAY FUNCTIONS (*) """

# clear_screen(); function to clear the terminal.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# display_list(); function to display all elements within a list.
#TODO add in another argument to take in the display.
def display_list(list : list) -> str:
    display = "\nList of Products in Storage:\n\n"
    for element in list:
        display += element + "\n"
    return display


# display_list_with_index_values(); function to print list elements with index values.
#TODO add in another argument to take in the display.
def display_list_with_index_values(list : list) -> str:
    display = "\nList of Products and Indexes:\n\n"
    for idx, element in enumerate(list):
        display += f"{idx}: " + element + "\n"
    return display


# display_list_of_dictionary();
#TODO add in another argument to take in the display.
def display_list_of_dictionary(list_of_dictionary : list) -> str:
    display = "\nList of Orders in Storage:\n\n"
    for dictionary in list_of_dictionary:
        for key, value in dictionary.items():
            key = key.replace("_", " ").title()
            display += f"\n{key}: {value}"
        display += "\n"
    return display


# display_list_of_dictionary_with_index_values();
#TODO add in another argument to take in the display.
def display_list_of_dictionary_with_index_values(list_of_dictionary : list) -> str:
    display = "\nList of Orders and Indexes:\n\n"
    for idx, dictionary in enumerate(list_of_dictionary):
        pass
    pass


""" (*) VALIDATION FUNCTIONS (*) """

# user_index_validation(); function to check if index value is valid.
def user_index_validation(index_value : int, list_of_elements : list) -> bool:
    idx_list = [idx for idx, product in enumerate(list_of_elements)]
    if index_value in idx_list:
        return True
    return False
    
    
# user_product_validation(); function to check if an element is within a list.
def user_product_validation(user_value : str, list_of_elements : list):
    normalized_list = [product.lower().replace(" ", "") for product in list_of_elements]
    #TODO figure out how to deal with entries with no spaces.
    if user_value.lower().replace(" ", "") not in normalized_list:
        return True
    return False
    