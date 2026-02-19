def add_expense(expense_list):

    while True:
        #Display available categories to the user
        print("food, housing, clothing, transportation, entertainment, saving")
        category = input("Which expense category: ").lower()

        #check if the category is inside dictionary 
        if category not in expense_list:
            print("enter a category")
            continue
        items = input("What is your item: ")
      
       # check if price is a number 
        try:
            price = float(input("How much does it cost: "))
        except ValueError:
            print("Invalid price.")
            return

# save new expense inside the category's list
        expense_list[category].append({
            "item": items,
            "price": price
        })

 # choose add or return to the main menu
        add = input("Add another category? (yes/no): ").lower()
        if add in ("n", "no"):
            break

        elif add in ("y", "yes"):
            continue

        else:
            print("enter y or n")

        


def total_expenses(expense_list):
    # sum price value found in each category
    total = sum(
        item["price"]
        for category in expense_list.values()
        for item in category
    )
    print(f"Total expense: ${total}")


def remove_expense(expense_list):
   # deletes items from category
    print("\n Remove Expense ")
    category = input("give category to delete!:").lower()
    
    if category in expense_list:
        item_name = input("give item to delete!:")
        found = False
        
        # Look through list to delete items
        for i in range(len(expense_list[category]) - 1, -1, -1):
            if expense_list[category][i]["item"] == item_name:
                expense_list[category].pop(i)
                print(f"Deleted {item_name}.")
                found = True
                break # Exit the loop
        
        if not found:
            print("Item not found.")
    else:
        print("Category does not exist.")

def filter_expenses(expense_list):
    # Shows items and prices in select category
    print("\n Filter by Category")
    category = input("give category to view!:").lower()
    
    if category in expense_list:
        items = expense_list[category]
        if len(items) > 0:
            print(f"\nExpenses for {category}:")
            for x in items:
                print(f"- {x['item']}: ${x['price']}")
        else:
            print("No expenses in this category!")
    else:
        print("Not even a Category!")

# holds a list of expenses
expense_list = {
    "food": [],
    "housing": [],
    "clothing": [],
    "transportation": [],
    "entertainment": [],
    "saving": [],
}

def menu():
# Navigation options
    print("\n Main Menu ")
    print ("1. Add Expense")
    print ("2. Remove Expense")
    print ("3. View Expense")
    print ("4. Total Expense")
    print ("5. Exit Program")

# Program Loop
while True:
    menu()
    choice = input("Select an option (1-5)")

    if choice == "1":
        add_expense(expense_list)

    elif choice == "2":
        remove_expense(expense_list)
        
    elif choice == "3":
        filter_expenses(expense_list)

    elif choice == "4":
         total_expenses(expense_list)

    elif choice == "5":
        print("Thank you for using our Expense Tracker9000 today!")
        break

    else:
        print("Error! Please try again")
