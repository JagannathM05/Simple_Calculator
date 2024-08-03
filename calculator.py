
import tkinter as tk

# Function to handle button clicks for numbers
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

# Function to handle addition operation
def button_add():
    global first_number
    global operation
    operation = "add"
    first_number = float(display.get())
    display.delete(0, tk.END)

# Function to handle subtraction operation
def button_subtract():
    global first_number
    global operation
    operation = "subtract"
    first_number = float(display.get())
    display.delete(0, tk.END)

# Function to handle multiplication operation
def button_multiply():
    global first_number
    global operation
    operation = "multiply"
    first_number = float(display.get())
    display.delete(0, tk.END)

# Function to handle division operation
def button_divide():
    global first_number
    global operation
    operation = "divide"
    first_number = float(display.get())
    display.delete(0, tk.END)

# Function to handle equals button
def button_equal():
    second_number = float(display.get())
    if operation == "add":
        result = first_number + second_number
    elif operation == "subtract":
        result = first_number - second_number
    elif operation == "multiply":
        result = first_number * second_number
    elif operation == "divide":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error"
    display.delete(0, tk.END)
    display.insert(0, result)

# Clear button function
def button_clear():
    display.delete(0, tk.END)

# Main program
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying numbers
display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons for numbers
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Define buttons for operators
button_add = tk.Button(root, text="+", padx=20, pady=20, command=button_add)
button_add.grid(row=1, column=3)

button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=button_subtract)
button_subtract.grid(row=2, column=3)

button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=button_multiply)
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(root, text="/", padx=20, pady=20, command=button_divide)
button_divide.grid(row=4, column=2)

# Define buttons for clear and equals
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)
button_clear.grid(row=4, column=0)

button_equal = tk.Button(root, text="=", padx=20, pady=20, command=button_equal)
button_equal.grid(row=4, column=3)

root.mainloop()
