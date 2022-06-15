
def shopping_cart():

    flag = False
    item_list = []

    while not flag:

        decision = input(
            "\nWelcome to your shopping cart! Would you like to add items to cart, \nremove them, review your cart, " 
            "need help, or done? (Add, Remove, Review, Help, or Done): ").lower()
        if decision == "add":
            added_item = input("What is the name of the item you wish to add?: ").lower()
            item_list.append(added_item)

        elif decision == "remove":
            removed_item = input("What is the name of the item you wish to remove?: ").lower()
            if removed_item in item_list:
                item_list.remove(removed_item)
            else:
                print("Item not in shopping cart. Heading back to home... ")

        elif decision == "review":
            print(f"\nHere's your current shopping cart list: {item_list} ")

        elif decision == "help":
            print("This application is a shopping cart. You add whatever you wish into it, take items out, and take a"
                  "look at your current shopping cart list. Thanks for using our software!")
            continue
        elif decision == "done":
            flag = True
        else:
            print("Invalid input, try again.")
            continue


shopping_cart()
