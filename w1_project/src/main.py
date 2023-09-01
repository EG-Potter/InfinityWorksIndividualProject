# Imported external functions.
from main_functions import *

# Created list of products.
PRODUCT_LIST = ["Tea", "Green Tea", "Black Tea", "Cappuccino", "Americano", "Black Coffee", "Vanilla Latte", "Latte"]

# Created main menu, used through print.
MENU = """\n1: Print a list of products.
2: Create a new product for storage.
3: Update existing product in storage.
4: Delete product from storage.
0: Return to Main Menu.\n"""

def main_menu():

    while True:
        print(MENU)

        # Gets a user input ine relation to MENU options.
        menu_input = int(input("\nEnter your selection in numeric form: "))
        clear_screen()

        match menu_input:

            case 1:
                # Prints elements in PRODUCT_LIST.
                clear_screen()
                while True:
                    print(display_list_elements(PRODUCT_LIST)) 
                    input("\nPress any key to continue ... ")
                    clear_screen()
                    break

            case 2:
                while True:
                    # Gets user input for a product name, then appends product name to PRODUCT_LIST.
                    new_product_entry = input("\nEnter name of new product: ").title()
                    clear_screen()
                    # Check to see if the entered product already exists.
                    if user_product_validation(new_product_entry, PRODUCT_LIST) == True:
                        print(f"(!) {new_product_entry} added into storage. (!)")
                        PRODUCT_LIST.append(new_product_entry)
                        break
                    else:
                        print(f"\n(!) Invalid Entry: {new_product_entry}.\n (!)")
                        continue

            case 3:
                # Prints product names w/ index values, then gets a user input for product index value.
                while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                    print(display_elements_with_index_values(PRODUCT_LIST))
                    try:
                        user_idx_value = int(input("\nEnter numeric index value of product: "))
                        clear_screen()
                    except Exception as error:
                        clear_screen()
                        print(f"\n(!) Invalid Entry: {error}. (!)\n")
                        continue

                    # Checks if inputted user index value exists within PRODUCT_LIST.
                    if user_index_validation(user_idx_value, PRODUCT_LIST) == True:
                        break
                    else:
                        print(f"\n(!) Invalid Entry: {user_idx_value}. (!)\n")
                        continue

                # Gets user input for a new product name, updates the product name at chosen index in PRODUCT_LIST.
                while True:
                    new_product_entry = input("\nEnter name of new product: ").title()
                    clear_screen()
                    # Check to see if the entered product already exists.
                    if user_product_validation(new_product_entry, PRODUCT_LIST) == True:
                        print(f"{PRODUCT_LIST[user_idx_value]} has been replace by {new_product_entry} in storage.")
                        PRODUCT_LIST[user_idx_value] = new_product_entry
                        break
                    else:
                        print(f"\n(!) Invalid Entry: {new_product_entry}. (!)\n")
                        continue

            case 4:
                # Prints product names w/ index values, then gets a user input for product index value.
                while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                    print(display_elements_with_index_values(PRODUCT_LIST))
                    try:
                        user_idx_value = int(input("\nEnter numeric index value of product: "))
                        clear_screen()
                    except Exception as error:
                        clear_screen()
                        print(f"\n(!) Invalid Entry: {error}. (!)\n")
                        continue

                    # Checks if inputted user index value exists within PRODUCT_LIST.
                    if user_index_validation(user_idx_value, PRODUCT_LIST) == True:
                        # Delete product at index value in PRODUCT_LIST.
                        print(f"\n(!) {PRODUCT_LIST[user_idx_value]} removed from storage. (!)\n")
                        del PRODUCT_LIST[user_idx_value]
                        break
                    else:
                        print(f"\n(!) Invalid Entry: {user_idx_value} (!)\n")
                        continue
                
            case 0:
                # Return to main menu.
                clear_screen()
                main_menu()

            case unknown_command:
                # Catches unknown user inputs not present in match case.
                clear_screen()
                print(f"\n(!) Invalid Entry: {unknown_command}. (!)\n")


#TODO review this functionality.
if __name__ == '__main__':
    main_menu()