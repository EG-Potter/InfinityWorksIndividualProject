from ukpostcodeutils import validation

import sys
sys.path.append('../')

from app_data.app_data import *
from src.main_functions import *
from src.main import main_menu_handler


def order_menu_handler():
    while True:
        # Order Title and Menu print.
        print(ORDER_TITLE, ORDER_MENU)

        # Gets a user input in relation to PRODUCT_MENU options.
        order_menu_input = int(input("\nEnter your selection in numeric form: "))
        clear_screen()

        match order_menu_input:
            case 1:
                # Displays elements in CUSTOMER_ORDERS_LIST.
                print(display_list_of_dictionary(CUSTOMER_ORDER_LIST)) 
                input("\nPress any key to continue ... ")
                clear_screen()

            case 2 | 4:

                if order_menu_input == 4:
                    # Prints orders w/ index values, then gets a user input for order index value.
                    while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                        print(display_list_of_dictionary_with_index_values(CUSTOMER_ORDER_LIST))
                        user_order_idx = input("\nEnter numeric index value of order: ")
                        clear_screen()
                        if user_order_idx.isdigit() == False:
                            print(f"\n(!) Invalid Entry: please enter a numeric value. (!)\n")
                            continue
                        else:
                            user_order_idx  = int(user_order_idx)

                        # Checks if inputted user index value exists within CUSTOMER_ORDER_LIST.
                        if user_index_validation(user_order_idx, CUSTOMER_ORDER_LIST):
                            break
                        
                        print(f"\n(!) Invalid Entry: {user_order_idx}. (!)\n")

                name = None; address = None; street = None; city_or_town = None; postcode = None; phone = None
                order_template = [name, address, street, city_or_town, postcode, phone]
                display_template = ["name", "address", "street", "city or town", "postcode", "phone number"]

                for idx, element in enumerate(order_template):
                    if idx in [0,1,2]:
                        while True:
                            element = input(f"\nEnter the {display_template[idx]}: ").title()
                            clear_screen()
                            print(order_menu_input)
                            if len(element.strip()) != 0 or (order_menu_input == 4 and len(element.strip()) == 0):#TODO make into a function?
                                break
                            print(f"\n(!) Invalid Entry: Null Entry. (!)\n")

                    if idx == 3:
                        while True:
                            element = input(f"\nEnter the {display_template[idx]}: ").title()
                            clear_screen()
                            if element.strip() in UK_REGISTERED_PLACES_LIST or (order_menu_input == 4 and len(element.strip()) == 0):
                                break
                            print(f"\n(!) Invalid Entry: Location not Registered. (!)\n")

                    if idx == 4:
                        while True:
                            element = input(f"\nEnter the {display_template[idx]}: ").upper()
                            clear_screen()
                            if validation.is_valid_postcode(element.replace(' ', '')) or (order_menu_input == 4 and len(element.strip()) == 0):
                                break
                            print(f"\n(!) Invalid Entry: Postcode is not valid. (!)\n")

                    if idx == 5:
                        while True: #TODO figure out a better validation for phone numbers.
                            element = input(f"\nEnter the {display_template[idx]}: ")
                            clear_screen()
                            if element.isdigit() == True and len(element.strip()) == 11 or (order_menu_input == 4 and len(element.strip()) == 0):
                                break
                            print(f"\n(!) Invalid Entry: phone numbers need to be 11 numeric characters. (!)\n")

                    order_template[idx] = element

                    if order_menu_input == 4 and len(element.strip()) != 0:
                        if idx == 0:
                            CUSTOMER_ORDER_LIST[user_order_idx]["customer_name"] = element
                            print(CUSTOMER_ORDER_LIST[user_order_idx]["customer_name"])

                        if idx in [1, 2, 3, 4]:
                            element = customer_address_modification(idx, element, CUSTOMER_ORDER_LIST[user_order_idx]["customer_address"])
                            CUSTOMER_ORDER_LIST[user_order_idx]["customer_address"] = element
                            print(CUSTOMER_ORDER_LIST[user_order_idx]["customer_address"])

                        if idx == 5:
                            CUSTOMER_ORDER_LIST[user_order_idx]["customer_phone"] = element
                            print(CUSTOMER_ORDER_LIST[user_order_idx]["customer_phone"])

                if order_menu_input == 2:
                    CUSTOMER_ORDER_LIST.append({"customer_name" : order_template[0], 
                                            "customer_address" : f"{order_template[1]}, {order_template[2]}, {order_template[3]}, {order_template[4]}",
                                            "customer_phone" : order_template[5], 
                                            "status" : "preparing"})
                    
                if order_menu_input == 4:
                    # Prints orders statuses w/ index values, then gets a user input for order statuses index value.
                    while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                        print(display_list_with_index_values(ORDER_STATUS_LIST))
                        user_order_status_idx = input("\nEnter numeric index value of status: ")
                        clear_screen()
                        if len(user_order_status_idx.strip()) == 0:
                            break
                        elif user_order_status_idx.isdigit() == False:
                            print(f"\n(!) Invalid Entry: please enter a numeric value. (!)\n")
                            continue
                        else:
                            user_order_status_idx  = int(user_order_status_idx)

                        # Checks if inputted user index value exists within ORDER_STATUS_LIST.
                        if user_index_validation(user_order_status_idx , ORDER_STATUS_LIST):
                            CUSTOMER_ORDER_LIST[user_order_idx]["status"] = ORDER_STATUS_LIST[user_order_status_idx]
                            break
                        
                        print(f"\n(!) Invalid Entry: {user_order_status_idx}. (!)\n")
                
                print(f"(*) Order Index: {user_order_idx}, has been updated! (*)")

            case 3:
                # Prints orders w/ index values, then gets a user input for order index value.
                while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                    print(display_list_of_dictionary_with_index_values(CUSTOMER_ORDER_LIST))
                    user_order_idx = input("\nEnter numeric index value of order: ")
                    clear_screen()
                    if user_order_idx.isdigit() == False:
                        print(f"\n(!) Invalid Entry: please enter a numeric value. (!)\n")
                        continue
                    else:
                        user_order_idx = int(user_order_idx)

                    # Checks if inputted user index value exists within CUSTOMER_ORDER_LIST.
                    if user_index_validation(user_order_idx, CUSTOMER_ORDER_LIST):
                        break
                    
                    print(f"\n(!) Invalid Entry: {user_order_idx}. (!)\n")
                
                # Prints orders statuses w/ index values, then gets a user input for order statuses index value.
                while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                    print(display_list_with_index_values(ORDER_STATUS_LIST))
                    user_order_status_idx = input("\nEnter numeric index value of status: ")
                    clear_screen()
                    if user_order_status_idx.isdigit() == False:
                        print(f"\n(!) Invalid Entry: please enter a numeric value. (!)\n")
                        continue
                    else:
                        user_order_status_idx = int(user_order_status_idx)

                    # Checks if inputted user index value exists within ORDER_STATUS_LIST.
                    if user_index_validation(user_order_status_idx, ORDER_STATUS_LIST):
                        print(f"\n(!) Order Index: {user_order_idx}, Order Status updated to:  {ORDER_STATUS_LIST[user_order_status_idx]}. (!)\n")
                        CUSTOMER_ORDER_LIST[user_order_idx]["status"] = ORDER_STATUS_LIST[user_order_status_idx]
                        break
                    
                    print(f"\n(!) Invalid Entry: {user_order_status_idx}. (!)\n")

            case 5:
                # Prints orders w/ index values, then gets a user input for order index value.
                while True: #TODO merge while loop into single unit-testable function, unit-test would require Mock.
                    print(display_list_of_dictionary_with_index_values(CUSTOMER_ORDER_LIST))
                    user_order_idx = input("\nEnter numeric index value of order: ")
                    clear_screen()
                    if user_order_idx.isdigit() == False:
                        print(f"\n(!) Invalid Entry: please enter a numeric value. (!)\n")
                        continue
                    else:
                        user_order_idx = int(user_order_idx)

                    # Checks if inputted user index value exists within CUSTOMER_ORDER_LIST.
                    if user_index_validation(user_order_idx, CUSTOMER_ORDER_LIST):
                        # Delete product at index value in CUSTOMER_ORDER_LIST.
                        print(f"\n(!) Order Index: {user_order_idx}, removed from storage. (!)\n")
                        del CUSTOMER_ORDER_LIST[user_order_idx]
                        break

                    print(f"\n(!) Invalid Entry: {user_order_idx} (!)\n")

            case 0:
                # Return to main menu.
                main_menu_handler()

            case unknown_command:
                # Catches unknown user inputs not present in match case.
                print(f"\n(!) Invalid Entry: {unknown_command}. (!)\n")

#TODO review this functionality.
if __name__ == '__main__':
    clear_screen()
    order_menu_handler()