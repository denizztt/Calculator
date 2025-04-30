import tkinter as tk
from tkinter import messagebox
import math



#Create Main Window
#Defines the basic window of the calculator.

window = tk.Tk()                #Main window object
window.title("GUI Calculator")  #Title
window.geometry("450x600")      #Window size (width x height)
window.configure(bg="#f0f0f0")  #Background color (light gray)



#Entry Area (Entry Widget)
#The box where the user enters operations and sees the results.

entry = tk.Entry(

    window,
    width=20,
    font=("Arial", 24),  # Font type and size
    borderwidth=5,  # Edge thickness
    justify="right"  # Right aligned

)

entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)  # Positioning



#Define Buttons
#Clickable buttons for numbers, operators, and special functions.

#First Step : Basic Buttons (Numbers and Operators)

buttons = [

    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)

]

for (text, row, col) in buttons:

    btn = tk.Button(

        window,
        text=text,
        font=("Arial", 18),
        bg="#ff9500" if text in "+-*/=" else "#e0e0e0",  # Operators are orange, others are grey
        command=lambda t=text: on_button_click(t)  # Click function

    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")    # Place on grid


#Second Step : Special Function Buttons (Square Root, Exponent, Clear)

special_buttons = [

    ("√", 5, 0), ("^", 5, 1), ("C", 5, 2), ("←", 5, 3)

]

for (text, row, col) in special_buttons:
    btn = tk.Button(
        window,
        text=text,
        font=("Arial", 18),
        bg="#a6a6a6",  # Gray color
        command=lambda t=text: on_special_click(t)  # Special click function
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


#Click Functions
#Determines what happens when buttons are clicked

#First Step : For Normal Buttons

def on_button_click(char):
    current = entry.get()                         # Get the current text in the input field
    entry.delete(0, tk.END)                  # Clear input field
    entry.insert(0, current + str(char))    # Add new character


#Second Step : For Custom Buttons

def on_special_click(char):
    if char == "C":
        entry.delete(0, tk.END) # Delete entire entry
    elif char == "←":
        entry.delete(len(entry.get())-1)    # Delete last character
    elif char == "√":
        try:
            num =float(entry.get())
            result =math.sqrt(num)
            entry.delete(0, tk.END)
            entry.insert(0, result)     # Calculate the square root

        except:
            messagebox.showerror("Hata!!","Geçersiz sayı !")    # Show error message
    elif char == "^":
        entry.insert(tk.END, "**")  # Add exponentiation operator



# Calculation Function
# Calculates the result when the "=" button is pressed.

def calculate():
    try:
        expression  = entry.get()    # Get the expression in the input field
        # Security check: Only allowed characters
        allowed_chars = set("0123456789+-*/.() ")

        if not set(expression).issubset(allowed_chars):
            raise ValueError("İzin Verilmeyen Karakter !")
        result = eval(expression)   # Calculate the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))    # Show result

    except Exception as e :
        messagebox.showerror("Hata", f"Hata: {e}")  # Error message

window.bind("<Return>", lambda event: calculate())  # Calculate with Enter key



# Start Window
# Runs the GUI and waits for user interaction.

# Adjust grid dimensions (to make buttons flexible)

for i in range(6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i % 4, weight=1)


window.mainloop()   # Keep the window open