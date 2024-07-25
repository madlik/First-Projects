#Password generator

####################################################################################################

#Impordi necessary modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

#Function to generate a password based on user input length
def password_generator():
    try:
        f = open("märgid.txt", encoding="utf-8")
        lines = f.read().split()
        if not lines:
            raise ValueError("File is empty.")
        f.close()
        
        # Get the desired password length
        length = int(password_length.get())
        if length <= 0:
            raise ValueError("Enter a positive number")
        
        # Generate the password
        password = ""
        for character in range(length):
            character = lines[randint(0, len(lines)-1)]
            password = character + password
        return password
    except FileNotFoundError:
        messagebox.showinfo(message="Error, file not found.")
        return None
    except ValueError:
        messagebox.showinfo(message="Enter a positive number")
        return None
        
# Function to display the generated password
def show_password():
    password = password_generator()
    if password:
        messagebox.showinfo(message="Your new password is\n\n" + password)

# Create the main window


window = Tk()
window.title("Password generator")
window.geometry("300x120")

# Add a label to the main window
label = ttk.Label(window, text="How many characters in password?")
label.place(x=60, y=10)

# Add an entry widget to the main window
password_length = ttk.Entry(window)
password_length.place(x=70, y=35, width=150)

# Add a button to generate the password
button = ttk.Button(window, text="Create new password!", command=show_password)
button.place(x=70, y=70, width=150)

# Run the main event loop
window.mainloop()
        