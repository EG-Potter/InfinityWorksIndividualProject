
""" (*) MENUS & TITLES (*) """

# MAIN_MENU; 
MAIN_MENU = """\n1: Enter Product Menu.
2: Enter Order Menu.
0: Exit Application.\n"""

# PRODUCT_MENU;
PRODUCT_MENU = """\n1: Print a list of Products.
2: Create a new Product for storage.
3: Update existing Product in storage.
4: Delete Product from storage.
0: Return to Main Menu.\n"""

# ORDER_MENU;
ORDER_MENU = """\n1: Print a list of Orders.
2: Create a new Order for storage.
3: Update the order status of an Order.
4: Update existing Order in storage.
5: Delete Order from storage.
0: Return to Main Menu.\n"""

# APP_TITLE;
APP_TITLE = "\n(*) Welcome to the Coffee Application (*)\n"

# PRODUCT_TITLE;
PRODUCT_TITLE = "\n(*) Welcome to the Product Menu Section. (*)\n"

# ORDER_TITLE;
ORDER_TITLE = "\n(*) Welcome to the Order Menu Section. (*)\n"

#TODO create a function to handle a uniform title creation?


""" (*) COLLECTIONS/DATA (*) """

# PRODUCT_LIST; 
PRODUCT_LIST = ["Tea", "Green Tea", "Black Tea", "Cappuccino", "Americano", "Black Coffee", "Vanilla Latte", "Latte"]

# ORDER_STATUS_LIST;
ORDER_STATUS_LIST = ["preparing", "out-for-delivery", "delivered"]

# UK_REGISTERED_PLACES_LIST;
UK_REGISTERED_PLACES_LIST = []

# CUSTOMER_ORDER_LIST; 
CUSTOMER_ORDER_LIST = [{
   "customer_name": "John",
   "customer_address": "Unit 1, 11 Main Street, LONDON, WH1 1ER",
   "customer_phone": "0789887331",
   "status": "preparing"
},
{
   "customer_name": "Erica",
   "customer_address": "Unit 2, 12 Main Street, LONDON, WH2 2ER",
   "customer_phone": "0789887332",
   "status": "starting"
},
{
   "customer_name": "Corrin",
   "customer_address": "Unit 3, 13 Main Street, LONDON, WH3 3ER",
   "customer_phone": "0789887333",
   "status": "preparing"
},
{
   "customer_name": "Ahmed",
   "customer_address": "Unit 4, 14 Main Street, LONDON, WH4 4ER",
   "customer_phone": "0789887334",
   "status": "completed"
},
{
   "customer_name": "Eugene",
   "customer_address": "Unit 5, 15 Main Street, LONDON, WH5 5ER",
   "customer_phone": "0789887335",
   "status": "preparing"
}]

""" URL & File Names """

# UK_REGISTERED_PLACES_STORAGE;
UK_REGISTERED_PLACES_STORAGE = 'uk_registered_places.txt'