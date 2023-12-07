import tkinter as tk
from tkinter import ttk

def on_combobox_selected(event):
    selected_item = combo.get()
    print(f"Selected item: {selected_item}")

root = tk.Tk()

options = ["Option 1", "Option 2", "Option 3"]

# Set the initial value for the ComboBox
initial_value = options[0]

combo = ttk.Combobox(root, values=options, state='readonly')
combo.set(initial_value)  # Set the initial value
combo.pack(pady=10)

# Bind the <<ComboboxSelected>> event
combo.bind("<<ComboboxSelected>>", on_combobox_selected)

root.mainloop()
