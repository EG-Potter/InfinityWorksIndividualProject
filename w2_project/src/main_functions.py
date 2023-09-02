import os

# clear_screen(); function to clear the terminal.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# display_list_elements(); function to display all elements within a list.
def display_list_elements(list_of_elements : list):
    display = "\nList of Products in Storage:\n\n"
    for element in list_of_elements:
        display += element + "\n"
    return display


# display_elements_with_index_values(); function to print list elements with index values.
def display_elements_with_index_values(list_of_elements : list):
    display = "\nList of Products and Indexes:\n\n"
    for idx, product in enumerate(list_of_elements):
        display += f"{idx}: " + product + "\n"
    return display


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
    