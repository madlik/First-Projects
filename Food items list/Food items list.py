#Food items list (creating and modifying)

###################################################################################################

#Functions

#Menu
def menu():
    while True:
        print("""\nWelcome! Now you can create a list of food items you have!
    Menu:
    1 - Display list
    2 - Add item
    3 - Delete item
    4 - Delete whole list
    5 - Exit
    """)
        choice = input("What do you wish to do? Enter a number: ").strip()
        match choice:
            case "1":
                show()
            case "2":
                add()
            case "3":
                delete()
            case "4":
                deleteall()
            case "5":
                print("List has been created! Bye!")
                break
            case _:
                print("\n\033[91mInvalid input\033[0m\n")
                

#add an item to the list(but also check if it's already on the list)
def add():
    try:
        f = open("toidunimekiri.txt", encoding="utf-8")
        content = f.read()
        f.close()
    except FileNotFoundError:
        print("File not found.")
        return
    show()
    
    while True:
        item = input("Add an item to the list or press 'ENTER' to exit the list: ").lower().strip()
        if item == "":
            return
        
        if item not in content:
            f = open("toidunimekiri.txt", "a", encoding="utf-8")
            f.write("\n" + item)
            print("Item added to the list.")
            f.close()
        else:
            print((item + " already on the list.").capitalize())
            
#show the list    
def show():
    try:
        f = open("toidunimekiri.txt", encoding="utf-8")
        list_of_items = f.read()
        if list_of_items.strip() != "":
            print("\nNimekirjas on:\n" + list_of_items)
        else:
            print("\nThe list is currently empty.")
        f.close()
    except FileNotFoundError:
        print("File not found.")
        return

#delete item from list
def delete():
    try:
        f = open("toidunimekiri.txt", encoding="utf-8")
        list_of_strings = f.read().splitlines()
        f.close()
    except FileNotFoundError:
        print("File not found.")
        return
    
    show()  #show current list before changing
        
    while True:    
        item_to_delete = input("Enter the name of an item to delete or press 'ENTER' to exit the list: ").lower().strip()
        if item_to_delete == "":
            return
        
        if item_to_delete in list_of_strings:
            list_of_strings.remove(item_to_delete)
            print(item_to_delete.capitalize() + " has been deleted from the list.")
            f = open("toidunimekiri.txt", "w", encoding="utf-8")
            f.write("\n".join(list_of_strings))
            f.close()
            return
        else:
            print("\n" + item_to_delete.capitalize() + " is not on the list.")
            
#delete the whole list
def deleteall():
    try:
        question = input("Are you sure you want to delete the whole list? (yes/no) ").lower().strip()
        if question == "yes":
            f = open("toidunimekiri.txt", "w", encoding="utf-8")
            f.write("")
            f.close()
            print("List deleted.")
        else:
            print("Deleting of the list cancelled.")
    except FileNotFoundError:
        print("File not found.")
        return

def main():
    menu()


if __name__ == "__main__":
    main()

