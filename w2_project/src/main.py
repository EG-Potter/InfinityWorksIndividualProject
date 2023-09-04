import sys
sys.path.append('../')
# Imported external sub menus. 
from sub_menus.product_menu import *
from sub_menus.order_menu import *
# Imported external functions and data. 
from app_data.app_data import *
from functions.main_functions import *


import_txt_as_list(UK_REGISTERED_PLACES_STORAGE, UK_REGISTERED_PLACES_LIST)

def main_menu_handler():
    while True:
        # title and menu print for main menu.
        print(APP_TITLE, MAIN_MENU)

        # Gets a user input in relation to MAIN_MENU options.
        menu_input = int(input("\nEnter your selection in numeric form: "))
        clear_screen()

        match menu_input:
            case 1:
                product_menu_handler() # Enters into Product Menu Functionality.

            case 2:
                order_menu_handler() # Enters into Order Menu Functionality.

            case 0:
                sys.exit("\n(*) Exited Application. (*)\n") # Exits Application.

            case unknown_command:
                # Catches unknown user inputs not present in match case.
                print(f"\n(!) Invalid Entry: {unknown_command}. (!)\n")
      

#TODO review this functionality.
if __name__ == '__main__':
    clear_screen()
    main_menu_handler()