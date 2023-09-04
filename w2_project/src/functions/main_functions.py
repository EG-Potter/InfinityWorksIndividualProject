import os

""" (*) IMPORT FUNCTIONS (*) """

# import_txt_as_list(2);
def import_txt_as_list(file_name : str, collection : list) -> list:
    try:
        file = open('.../app_data/import_data/' + file_name, 'r')
        for line in file.readlines():
            collection.append(line.strip())
        file.close()
    except FileNotFoundError as error:
        print("(!) ERROR: Unable to open file. (!)" + '\n' + str(error))


""" (*) TERMINAL/DISPLAY FUNCTIONS (*) """

# clear_screen(-); function to clear the terminal.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# display_list(1); function to display all elements within a list.
#TODO add in another argument to take in the display.
def display_list(list : list) -> str:
    display = "\nList of Products in Storage:\n\n"
    for element in list:
        display += element + "\n"
    return display


# display_list_with_index_values(1); function to print list elements with index values.
#TODO add in another argument to take in the display.
def display_list_with_index_values(list : list) -> str:
    display = "\nList of Products and Indexes:\n\n"
    for idx, element in enumerate(list):
        display += f"{idx}: " + element + "\n"
    return display


# display_list_of_dictionary(1);
#TODO add in another argument to take in the display.
def display_list_of_dictionary(list_of_dictionary : list) -> str:
    display = "\nList of Orders in Storage:\n\n"
    for dictionary in list_of_dictionary:
        for key, value in dictionary.items():
            key = key.replace("_", " ").title()
            display += f"\n{key}: {value}"
        display += "\n"
    return display


# display_list_of_dictionary_with_index_values(1);
#TODO add in another argument to take in the display.
def display_list_of_dictionary_with_index_values(list_of_dictionary : list) -> str:
    display = "\nList of Orders and Indexes:\n\n"
    for idx, dictionary in enumerate(list_of_dictionary):
        display += f"\nOrder Index: {idx}"
        for key, value in dictionary.items():
            key = key.replace("_", " ").title()
            display += f"\n{key}: {value}"
        display += "\n"
    return display


""" (*) VALIDATION FUNCTIONS (*) """

# user_index_validation(2); function to check if index value is valid.
def user_index_validation(index_value : int, list_of_elements : list) -> bool:
    idx_list = [idx for idx, element in enumerate(list_of_elements)]
    if index_value in idx_list:
        return True
    return False
    
    
# user_product_validation(2); function to check if an element is within a list.
def user_product_validation(user_value : str, list_of_elements : list) -> bool:
    normalized_list = [product.lower().replace(" ", "") for product in list_of_elements]
    #TODO figure out how to deal with entries with no spaces.
    if user_value.lower().replace(" ", "") not in normalized_list:
        return True
    return False

""" MODIFICATION FUNCTIONS """

# customer_address_modification(3);
def customer_address_modification(idx : int, address_segment : str, full_address : str) -> str:
    full_address_list = full_address.split(",")
    full_address_list[idx - 1] = address_segment

    new_address = ""
    for element in full_address_list:
        new_address += element.strip() + ", "
    return new_address[:-2]


    