import random
import os
import tkinter as tk
from tkinter import messagebox

def no_di():
    try:
        val = int(entry.get())
        if val not in [1, 2]:
            raise ValueError('Please enter 1 or 2 only')
        return val
    except ValueError as error:
        messagebox.showerror("Error", error)

def roll_di():
    mini_value = 1
    maxi_value = 6
    total_num = no_di()
    result = ""
    if total_num == 2:
        dc_1 = random.randint(mini_value, maxi_value)
        dc_2 = random.randint(mini_value, maxi_value)
        result += f'DICE_NO_1: {dc_1}\nDICE_NO_2: {dc_2}\nTOTAL DICE: {dc_1 + dc_2}\n'
    else:
        dc_1 = random.randint(mini_value, maxi_value)
        result += f'The value of dice is: {dc_1}\n'
    messagebox.showinfo("Dice Roll Result", result)

# GUI setup
root = tk.Tk()
root.title("Dice Roll Generator")
root.configure(bg="lightpink")

label = tk.Label(root, text="Enter the number of dice (1 or 2):", bg="lightpink", fg="black")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Roll Dice", command=roll_di, bg="grey", fg="lightblue")
button.pack()

root.mainloop()
