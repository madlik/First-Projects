## This repository contains the first small projects I have done in Python:

### **1. Primitive desktop cleaner** 
If you often find your desktop cluttered with files, the Primitive Desktop Cleaner for Windows operating system can help you organize your space efficiently. This script utilizes Python's os and shutil modules to move files from your desktop to designated folders based on file type or all at once, saving you time and keeping your workspace tidy.

#### Features
* Move Files by Type: Automatically organizes Microsoft Office files, PDFs, pictures, Python scripts, and more into folders.
* Custom Folder Creation: Create a new folder directly from the script if one doesn't already exist.
* Multi-Folder Support: Works not just for the desktop but also for other directories like Downloads or Documents.

#### Usage Example
* Input Path: Specify your desktop path when prompted.
* Select File Type: Choose which types of files to move.
* Move Files: Confirm the move, and your files will be organized into their respective folders.

### **2. Password generator** 
Whenever it's time to create a new password I run out of ideas what should be my new password. With password generator I have a helping hand in keeping my accounts safe. This password generator generates a password of any length given by the user of random characters which are stored in a file. Whether the user needs a password of 6 elements or 12 the generator has a password in store. The most challenging part of this project was using the tkinter module as it was the first time I experimented with it in Python to create an interface for the password generator. 

#### Features
* Customizable Length: Users can specify the desired length of the password.
* User-Friendly Interface: A GUI built with tkinter for ease of use, with buttons for generating passwords.

#### Usage Example
* Start the Program: Run the script using "Password generator.py".
* Specify Length: Enter the desired length of the password.
* Generate Password: Click the "Generate" button to create a new password.
  
### **3. Random recipe generator** 
When I thought about issues that take too much time away from my everyday life, then 2 came to find: what to wear next and what on Earth should I be cooking for next week. To solve the latter problem I created a random recipe generator, which helpes me choose a random recipe from the list of my most common recipes.

#### Features
* Recipe Database: A list of pre-entered recipes that the program can randomly select from.
* Recipe Display: Once a recipe is selected, the program displays the ingredients.

#### Usage Example
* Run the Program: Execute python "Random recipe generator.py".
* Generate Recipe: The program randomly selects and displays a recipe.
  
### **4. Food items list modifier** 
When I created the random recipe generator I had an idea to also try to synthesize it with a list of food items I already have at home. For the first step in the project I created the list for food items where I can add and remove items in the list. The next step is to synthesize the list with random recipe generation. For now it's an ongoing process, but soon I'll be able to share some results!

#### Features
* Add Items: Users can manually add items to the list.
* Remove Items: Easily remove items from the list.
* Check Inventory: Quickly check the list to see what ingredients are available.

#### Usage Example
* Launch the Program: Start the script using python "Food items list.py".
* View Inventory: Display the current list of food items.
* Add or Remove Items: Use the appropriate options to update the inventory.
* Check Recipe Compatibility (Future Feature): Use the integration with the recipe generator to suggest meals based on available items.


The projects can be found on this site: https://github.com/madlik/First-Projects

