import sys
sys.path.append('../')

from app_data.app_data import *

from functions.main_functions import *
from src.main import main_menu_handler


def product_menu_handler():
    while True:
        # Product Title and Menu print.
        print(PRODUCT_TITLE, PRODUCT_MENU)

        # Gets a user input in relation to PRODUCT_MENU options.
        product_menu_input = int(input("\nEnter your selection in numeric form: "))
        clear_screen()

        match product_menu_input:
            case 1:
                # Displays elements in PRODUCT_LIST.
                print(display_list(PRODUCT_LIST)) 
                input("\nPress any key to continue ... ")
                clear_screen()

            case 2:
                # Gets user input for a product name, then appends product name to PRODUCT_LIST.
                while True:
                    new_product_entry = input("\nEnter name of new product: ").title()
                    clear_screen()
                    # Check to see if the entered product already exists.
                    if user_product_validation(new_product_entry, PRODUCT_LIST):
                        print(f"(!) {new_product_entry} added into storage. (!)")
                        PRODUCT_LIST.append(new_product_entry)
                        break
            
                    print(f"\n(!) Invalid Entry: {new_product_entry}.\n (!)")

            case 3:
                # Prints product names w/ index values, then gets a user input for product index value.
                while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                    print(display_list_with_index_values(PRODUCT_LIST))
                    user_product_idx = input("\nEnter numeric index value of product: ")
                    clear_screen()
                    if user_product_idx.isdigit() == False:
                        print(f"\n(!) Invalid Entry: please enter a numeric value. (!)\n")
                        continue
                    else:
                        user_product_idx = int(user_product_idx)

                    # Checks if inputted user index value exists within PRODUCT_LIST.
                    if user_index_validation(user_product_idx, PRODUCT_LIST):
                        break
                    
                    print(f"\n(!) Invalid Entry: {user_product_idx}. (!)\n")

                # Gets user input for a new product name, updates the product name at chosen index in PRODUCT_LIST.
                while True:
                    new_product_entry = input("\nEnter name of new product: ").title()
                    clear_screen()
                    # Check to see if the entered product already exists.
                    if user_product_validation(new_product_entry, PRODUCT_LIST):
                        print(f"{PRODUCT_LIST[user_product_idx]} has been replace by {new_product_entry} in storage.")
                        PRODUCT_LIST[user_product_idx] = new_product_entry
                        break
                    
                    print(f"\n(!) Invalid Entry: {new_product_entry}. (!)\n")

            case 4:
                # Prints product names w/ index values, then gets a user input for product index value.
                while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                    print(display_list_with_index_values(PRODUCT_LIST))
                    user_product_idx = input("\nEnter numeric index value of product: ")
                    clear_screen()
                    if user_product_idx.isdigit() == False:
                        print(f"\n(!) Invalid Entry: please enter a numeric value. (!)\n")
                        continue
                    else:
                        user_product_idx = int(user_product_idx)

                    # Checks if inputted user index value exists within PRODUCT_LIST.
                    if user_index_validation(user_product_idx, PRODUCT_LIST):
                        # Delete product at index value in PRODUCT_LIST.
                        print(f"\n(!) {PRODUCT_LIST[user_product_idx]} removed from storage. (!)\n")
                        del PRODUCT_LIST[user_product_idx]
                        break

                    print(f"\n(!) Invalid Entry: {user_product_idx} (!)\n")
                
            case 0:
                # Return to main menu.
                main_menu_handler()

            case unknown_command:
                # Catches unknown user inputs not present in match case.
                print(f"\n(!) Invalid Entry: {unknown_command}. (!)\n")

#TODO review this functionality.
if __name__ == '__main__':
    clear_screen()
    product_menu_handler()