#COSC1519 Introduction to Programming
#Assessment 3 Programming Project
#Student name: Eamon Butler
#Student number: s3923505
#Practical group Teacher: Gayan

#read file
#save to list
def read_file():
    infile = open("A3_s3923505_stock.txt","r")
    print("\t\t Welcome to the backend of 'The Dragon Seal' weapon shop!")
    print("Inventory file loaded:", infile.name)
    first_line = True
    #initialise all column lists as well as the parent dictionary 
    stock = {}
    first_col = []
    second_col = []
    third_col = []
    fourth_col = []
    fifth_col = []
    columns = [first_col, second_col, third_col, fourth_col, fifth_col]
    for line in infile:
        #use this to debug reading each line
        #print("\ncurrent line is:", line, end="")
        
        item_info = line.strip().split(", ")
        if first_line == True: #extract first line to be used as keys in dictionary
            col_titles = item_info
            ##use this to debug and show titles for first line/column titles
            #print(col_titles)
            
            first_line = False #set to false so each line after first gets passed to else statement
        else: 
            columns[0].append(item_info[0]) #Item Name
            columns[1].append(item_info[1]) #Price
            columns[1] = [float(price) for price in columns[1]] #convert prices to floats using list comprehension
            columns[2].append(item_info[2]) #Quantity
            columns[2] = [int(item) for item in columns[2]] #convert quantity to int using list comprehension
            columns[3].append(item_info[3]) #Class
            columns[4].append(item_info[4]) #Core Material
    infile.close() #closing file as soon as possible 
    
    #use this to debug column list formatting
    #print("\nfirst column:", columns[0])
    
    #needed to use a dictionary and this seems the most useful place to use it
    #technically I could have made the program work without a dict but with it, expanding the program to do different tasks is easier
    for key in range(len(col_titles)): #iterate through the number of column titles
        stock[col_titles[key]] = columns[key] #make each column title the key and add the corresponding data column to value
        
    #use this to debug dictionary definition and traversal
    #print(stock)
    #print(stock['Item Name'])
    return stock #return the complete dictionary, cases is kept so written file isn't all lowercase
    
#show user the main menu options
def options_menu(stock_info):
    user_option = 0
    while (user_option := input(f"\n\nWhat would you like to do?\n\t1. Look up single stocked item\n\t2. Look up all stocked items\n\t3. Add/Update item\n\t4. Remove item\n\t5. Calculate total stock value\n\t6. Save and exit\n\t7. Exit without saving\n")) not in ["1", "2", "3", "4", "5", "6", "7"]: 
        print("Error: Accepted responses are '1', '2', '3', '4', '5', '6' or '7'. \n")
    if user_option == "1": #Look up single stocked item
        lookup_stock(stock_info, user_option)
    elif user_option == "2": #Look up all stocked items
        lookup_stock(stock_info, user_option)
    elif user_option == "3": #Add/Update item
        add_update_remove(stock_info, user_option)
        options_menu(stock_info)
    elif user_option == "4": #Remove item
        add_update_remove(stock_info, user_option)
        options_menu(stock_info)
    elif user_option == "5": #Calculate total stock value
        total_value(stock_info)
    elif user_option == "6": #Save and exit
        #confirm user wants to exit before actually exiting in case they selected the wrong option
        while (confirm := input("Are you sure you want to save and exit?\n").lower()) not in ["yes", "no", "y", "n"]: 
            print("Error: Accepted responses are 'yes', 'y', 'no' or 'n'")
        if confirm == "yes" or confirm == "y":
            save_file()
        else:
            options_menu(stock_info)
    elif user_option == "7": #Exit without saving
        #confirm user wants to exit without saving as they might get mixed up with save and exit
        while (confirm := input("Are you sure you want to exit without saving?\n").lower()) not in ["yes", "no", "y", "n"]: 
            print("Error: Accepted responses are 'yes', 'y', 'no' or 'n'")
        if confirm == "yes" or confirm == "y":
            pass
        else:
            options_menu(stock_info)
        
def lookup_stock(stock_info, user_option):
    lower_search = [x.lower() for x in stock_info["Item Name"]] #temp variable for case insensitive searching
    #create list of keys for easier access to the column titles. Iterates through the keys in dict and appends the list
    col_titles = []
    for key in stock_info.keys(): 
        col_titles.append(key) 
    
    #pass user input for single item lookup
    if user_option == "1":
        search_done =  False
        while search_done == False: #loops until user is done searching items
            item_search = input("Which item would you like to see stock data of?\n(Type 'done' to return to main menu)\n")
            if item_search == "done":
                search_done = True
            elif item_search.lower() in lower_search: #search lowercase names with lowercase user input
                search_index = lower_search.index(item_search.lower()) #find index for the item name to be used to locate corresponding data of that item
                print("\n" + col_titles[0] + ":\t" + stock_info["Item Name"][search_index])
                print(col_titles[1] + ":\t\t" + str(stock_info["Price"][search_index]))
                print(col_titles[2] + ":\t" + str(stock_info["Quantity"][search_index]))
                print(col_titles[3] + ":\t\t" + stock_info["Class"][search_index])
                print(col_titles[4] + ":\t" + stock_info["Core Material"][search_index] + "\n")
            else:
                print(item_search,"cannot be found.")
    #if user input not 1 then they are looking for all stock
    else: 
        #create temp lists for displaying values in alphabetical order
        item_name = stock_info["Item Name"]
        price = stock_info["Price"]
        quantity = stock_info["Quantity"]
        weapon_class = stock_info["Class"]
        core_weapon = stock_info["Core Material"]
        #sort all lists according to item_name 'sorted' function (which is alphabetically since it contains str values)
        item_name, price, quantity, weapon_class, core_weapon = zip(*sorted(zip(item_name, price, quantity, weapon_class, core_weapon)))
        #use formatting for nicer looking and easier to followe data print
        print("{:<20s}{:>6s}{:>10s}{:>10s}{:>15s}".format(col_titles[0], col_titles[1], col_titles[2], col_titles[3], col_titles[4]))
        print("-------------------------------------------------------------")
        for index_pos in range(len(item_name)): #iterate through 'item name' till end since all lists are the same length
            print("{:<20s}{:>6.1f}{:>10d}{:>10s}{:>15s}".format(item_name[index_pos], price[index_pos], quantity[index_pos], weapon_class[index_pos], core_weapon[index_pos]))
    options_menu(stock_info) #return to main menu

def add_update_remove(stock_info, user_option):
    lower_search = [x.lower() for x in stock_info["Item Name"]] #temp variable for case insensitive searching
    if user_option == "3": #if passed to function from selecting add/update
        add_item = input("Which item would you like to add/update?")
        if add_item.lower() in lower_search: #search lowercase names with lowercase user input
            remove_stock(stock_info, add_item) #pass to remove function to remove item before updating
        else:
            pass
        #ask user for new item details
        while True:
            try:
                add_price = float(input("\nWhat is the price for " + add_item + "?"))
                break
            except:
                print("Error: please use numbers only for price")
        while True:
            try:        
                add_quant = int(input("\nWhat is the quantity of " + add_item + "?"))
                break
            except:
                print("Error: please use whole numbers only for quantity")
        add_class = input("\nWhat weapon class is " + add_item + "?")
        add_material = input("\nWhat is the core material of " + add_item + "?")
        #add new item data to stock
        stock_info["Item Name"].append(add_item)
        stock_info["Price"].append(add_price)
        stock_info["Quantity"].append(add_quant)
        stock_info["Class"].append(add_class)
        stock_info["Core Material"].append(add_material)
    else: #if passed to function from selecting remove
        search_done = False #initialise search state
        while search_done == False: #loops until user is done removing items
            remove_item = input("\nWhich item would you like to remove from stock?]\n(type 'done' when finished removing items)\n")
            if remove_item == "done":
                search_done = True
            elif remove_item.lower() in lower_search: #search lowercase names with lowercase user input
                remove_stock(stock_info, remove_item) #pass to remove function
            else:
                print(remove_item,"cannot be found.")
    return stock_info #use return so that new data is updated

def remove_stock(stock_info, remove_item):
    lower_search = [x.lower() for x in stock_info["Item Name"]] #temp variable for case insensitive searching
    remove_index = lower_search.index(remove_item.lower()) #find index for the item name to be used to locate corresponding data of that item
    del stock_info["Item Name"][remove_index]
    del stock_info["Price"][remove_index]
    del stock_info["Quantity"][remove_index]
    del stock_info["Class"][remove_index]
    del stock_info["Core Material"][remove_index]
    
    #use this to debug dictionary removed items correctly
    #print(stock_info)

def total_value(stock_info):
    stock_value = 0
    for item in range(len(stock_info["Item Name"])):
        stock_value += stock_info["Price"][item] * stock_info["Quantity"][item]
    print("\nThe total value of all items stocked is: $" + str(stock_value))
    options_menu(stock_info)

def save_file():
    col_titles = []
    #get column titles in list
    for key in stock_info.keys(): 
        col_titles.append(key)
    #initialise with local variable for easier access
    item_name = stock_info["Item Name"]
    price = stock_info["Price"]
    quantity = stock_info["Quantity"]
    weapon_class = stock_info["Class"]
    core_weapon = stock_info["Core Material"]
    first_line = ", ".join(col_titles) #convert title list into string
    #join each items data into one string within a list
    list_data_lines = [str(data_line) for data_line in zip(item_name, price, quantity, weapon_class, core_weapon,)]
    #loop to remove unwanted characters from list
    for item in range(len(list_data_lines)):
        list_data_lines[item] = list_data_lines[item].replace("(","")
        list_data_lines[item] = list_data_lines[item].replace(")","")
        list_data_lines[item] = list_data_lines[item].replace("'","")
    #add the titles to front of list
    list_data_lines.insert(0, first_line)
    
    #use this to debug the list and strings are written properly
    #print(list_data_lines)
    
    outfile = open("updated_A3_s3923505_stock.txt","w")
    outfile.write('\n'.join(list_data_lines))
    outfile.close()

#start in read file then pass the result into options menu
stock_info = read_file()
options_menu(stock_info)