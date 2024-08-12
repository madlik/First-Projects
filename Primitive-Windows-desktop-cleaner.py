#PRIMITIVE DESKTOP CLEANER

#Import necessary modules

import os
import shutil
import sys

#Determine the Desktop directory

source_directory = input("\033[1mWelcome to Desktop Cleaner! Insert path to Desktop (C:\\Users\\...\\Desktop): \033[0m")
if not os.path.exists(source_directory):
    print("\n\033[91mInvalid path. Exiting.\033[0m\n")
    exit()

os.chdir(source_directory)

#FUNCTIONS

def move_files(files_to_move, destination_directory):
    for file in files_to_move:
        source_file = os.path.join(source_directory, file)
        destination_file = os.path.join(destination_directory, file)
        try:
            shutil.move(source_file, destination_file)
            print("Moved " + file)
        except FileNotFoundError:
            print("File not found: " + file)
        except shutil.Error as e:
            print("Error moving file " + file + ": " + str(e))
        except PermissionError:
            print("Access to " + file + " is not allowed. Please check file/folder permissions or run the script with appropriate privileges.")
            
    
    print("\033[1m\nSuccess! All files have been moved.\033[0m")
    

#Function which moves files based on their extension from Desktop to a designated folder

def clean_files(file_extension, file_description):
    files_to_move = []
    try:
        for file_name in os.listdir(source_directory):
            if file_name.endswith((file_extension)):
                
                # If a matching file is found, perform the move operation
                files_to_move.append(file_name)
    except FileNotFoundError:
        print("Source directory not found: " + source_directory)
        return
    except PermissionError:
        print("Access to " + source_directory + " is not allowed. Please check file/folder permissions or run the script with appropriate privileges.")
        return
            
    if not files_to_move:
        print("\033[1mThere are no more " + file_description + " files on Desktop\033[0m")
        return
        
    how_many_files = len(files_to_move)
    print("\033[1m\nFound " + str(how_many_files) + " " + file_description + " files: \033[0m")
    for file in files_to_move:
        print(file)
        
    while True:    
        user_input = input("\nAre you sure you want to move the files (yes/no)? You can see the files above. ").strip().lower()
        if user_input != "yes" and user_input != "no":
            print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            break
            
    if user_input == "no":
        return
        
    destination_directory = move_file_to_directory()
    move_files(files_to_move, destination_directory)

#Function to clean all Microsoft Office, PDF, picture and Python files

def clean_all_files():
    
    files_to_move = []
    try:
        for file_name in os.listdir(source_directory):
            if file_name.endswith((".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".pdf", ".jpg", ".jpeg", ".png", ".py")):
                
                # If a matching file is found, perform the move operation
                files_to_move.append(file_name)
    except FileNotFoundError:
        print("Source directory not found: " + source_directory)
        return
    except PermissionError:
        print("Access to " + source_directory + " is not allowed. Please check file/folder permissions or run the script with appropriate privileges.")
        return
            
    if not files_to_move:
        print("There are no more cleanable files on Desktop")
        return
    
    how_many_files = len(files_to_move)
    print("\033[1m\nFound " + str(how_many_files) + " files: \033[0m")
    for file in files_to_move:
        print(file)
        
    while True:    
        user_input = input("\nAre you sure you want to move the files (yes/no)? You can see the files above.").strip().lower()
        if user_input != "yes" and user_input != "no":
            print("\n\033[91mInvalid input. Please enter 'yes' or 'no'.\033[0m\n")
        else:
            break
        
    if user_input == "no":
        return

        
    destination_directory = move_file_to_directory()
    move_files(files_to_move, destination_directory)
    
        
#Function which shows all items currently on Desktop
    
def show_all_items_on_desktop():
    try: 
        items = os.listdir(source_directory)
        for item in items:
            print(item)
    except FileNotFoundError:
        print("Desktop directory not found: " + source_directory)
    except PermissionError:
        print("Access to " + source_directory + " is not allowed. Please check file/folder permissions or run the script with appropriate privileges.")
        

#Function which ables to create a new directory where to move the files or move the files to an existing directory

def move_file_to_directory():
    while True:
        user_input = input("\nDo you already have a folder on Desktop where you would like to move the cleaned files (yes/no)? ").lower().strip()    
        if user_input == "yes":
            destination_directory = input("\nPlease insert the path for files (C:\\Users\\...\\Desktop\\...): ")
            if os.path.exists(destination_directory):
                return destination_directory
            else:
                print("\n\033[91mInvalid directory. Please try again.\033[0m\n")
        elif user_input == "no":
            folder_name = input("Enter the name for the new folder: ").strip()
            directory_path = os.path.join(source_directory, folder_name)
            print(directory_path)
            try:
                os.makedirs(directory_path)
                return directory_path
            except FileExistsError:
                print("Directory already exists: " + directory_path)
            except PermissionError:
                print("Cannot create directory: Access denied. Please check file/folder permissions or run the script with appropriate privileges.")
        else:
            print("\n\033[91mInvalid input. Please enter 'yes' or 'no'.\033[0m\n")
                

# Function to display the menu with different user actions

def cleaning_choice():
    while True:
        print("""\n\033[1mClean your desktop! Please choose which files to clean from menu.
    Menu:
    1 - Microsoft Office files (Word, Excel, PowerPoint)
    2 - PDF files
    3 - Picture files
    4 - Python files
    5 - Clean all Microsoft Office, PDF, picture and Python files
    6 - Clean other type of files not specified
    7 - Show items on desktop
    8 - Exit
    \033[0m""")
        choice = input("What do you wish to do? Enter a number: ").strip()
        match choice:
            case "1":
                clean_files((".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"), "Microsoft Office")
            case "2":
                clean_files((".pdf",), "PDF")
            case "3":
                clean_files((".jpg", ".jpeg", ".png"), "picture")
            case "4":
                clean_files((".py",), "Python")
            case "5":
                clean_all_files()
            case "6":
                file_extension = input("Enter the extension of files you wish to clean from desktop (e.g., .mp4, .exe, .zip): ").strip().lower()
                clean_files((file_extension,), file_extension + " files")
            case "7":
                print("\n\033[1mHere are all the items on the Desktop:\033[0m")
                show_all_items_on_desktop()
            case "8":
                print("Thank you for using desktop cleaner! Bye!")
                sys.exit()
            case _:
                print("\n\033[91mInvalid input\033[0m\n")
                
                
def main():
    cleaning_choice()


if __name__ == "__main__":
    main()

