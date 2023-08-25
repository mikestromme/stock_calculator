import tkinter as tk
from tkinter import messagebox

def calculate_final_value():
    try:
        hourly_wage = float(price_entry.get())
        cost_of_proucet = float(gains_entry.get())
        
        final_value = cost_of_proucet / hourly_wage
        
        messagebox.showinfo("Final Value", f"It would take you this many hours to buy the item: {final_value:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Investment Calculator")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the desired width and height for the GUI
gui_width = 400
gui_height = 300

# Calculate the x and y coordinates for centering the GUI
x_coordinate = (screen_width - gui_width) // 2
y_coordinate = (screen_height - gui_height) // 2

# Set the geometry for the GUI window
root.geometry(f"{gui_width}x{gui_height}+{x_coordinate}+{y_coordinate}")

# Create and place labels and entry widgets
price_label = tk.Label(root, text="Hourly Wage:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()

gains_label = tk.Label(root, text="Cost of Item:")
gains_label.pack()
gains_entry = tk.Entry(root)
gains_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_final_value)
calculate_button.pack()


# Set focus on the price_entry widget
price_entry.focus()

# Bind the Enter key to the calculate_final_value function
gains_entry.bind('<Return>', lambda event: calculate_final_value())

# Start the GUI event loop
root.mainloop()
