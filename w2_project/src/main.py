# Imported external functions. 
import sys
sys.path.append('../')
from data.application_data import *
from main_functions import *


def main_menu():

    while True:
        # title and menu print for main menu.
        print(APP_TITLE, MAIN_MENU)

        # Gets a user input in relation to MAIN_MENU options.
        menu_input = int(input("\nEnter your selection in numeric form: "))
        clear_screen()

        match menu_input:

            case 1:
                # Exits into Product Menu Functionality.
                while True:
                     # Title and Menu print for product menu.
                    print(PRODUCT_TITLE, PRODUCT_MENU)

                    # Gets a user input in relation to PRODUCT_MENU options.
                    product_menu_input = int(input("\nEnter your selection in numeric form: "))
                    clear_screen()

                    match product_menu_input:

                        case 1:
                            # Prints elements in PRODUCT_LIST.
                            clear_screen()
                            print(display_list_elements(PRODUCT_LIST)) 
                            input("\nPress any key to continue ... ")
                            clear_screen()

                        case 2:
                            # Gets user input for a product name, then appends product name to PRODUCT_LIST.
                            while True:
                                new_product_entry = input("\nEnter name of new product: ").title()
                                clear_screen()
                                # Check to see if the entered product already exists.
                                if user_product_validation(new_product_entry, PRODUCT_LIST) == True:
                                    print(f"(!) {new_product_entry} added into storage. (!)")
                                    PRODUCT_LIST.append(new_product_entry)
                                    break
                        
                                print(f"\n(!) Invalid Entry: {new_product_entry}.\n (!)")

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
                                
                                print(f"\n(!) Invalid Entry: {user_idx_value}. (!)\n")

                            # Gets user input for a new product name, updates the product name at chosen index in PRODUCT_LIST.
                            while True:
                                new_product_entry = input("\nEnter name of new product: ").title()
                                clear_screen()
                                # Check to see if the entered product already exists.
                                if user_product_validation(new_product_entry, PRODUCT_LIST) == True:
                                    print(f"{PRODUCT_LIST[user_idx_value]} has been replace by {new_product_entry} in storage.")
                                    PRODUCT_LIST[user_idx_value] = new_product_entry
                                    break
                                
                                print(f"\n(!) Invalid Entry: {new_product_entry}. (!)\n")

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

                                print(f"\n(!) Invalid Entry: {user_idx_value} (!)\n")
                            
                        case 0:
                            # Return to main menu.
                            main_menu()

                        case unknown_command:
                            # Catches unknown user inputs not present in match case.
                            print(f"\n(!) Invalid Entry: {unknown_command}. (!)\n")

            case 0:
                # Exits Application.
                sys.exit("\n(*) Exited Application. (*)\n")

            case unknown_command:
                # Catches unknown user inputs not present in match case.
                print(f"\n(!) Invalid Entry: {unknown_command}. (!)\n")
      

#TODO review this functionality.
if __name__ == '__main__':
    clear_screen()
    main_menu()