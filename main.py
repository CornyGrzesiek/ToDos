from tkinter import *

root = Tk()
root.title("MyToDos")
root.geometry("500x500")
root.resizable(False, False)

# Create frame
frame = Frame(root)
frame.pack(pady=15)

# Create listbox
items_list = Listbox(frame, width=40, height=10, bd=0, fg="black", highlightthickness=0, selectbackground="light gray",
                     selectforeground="black",
                     font=("Helvetica", 12), )
items_list.pack(side=LEFT)

# Create ScrollBar
items_scroll = Scrollbar(frame)
items_scroll.pack(side=RIGHT, fill=BOTH)

# Add Scrollbar
items_list.config(yscrollcommand=items_scroll.set)
items_scroll.config(command=items_list.yview)

# Create entryBox
entry_box = Entry(root, font=("Helvetica", 12))
entry_box.pack(pady=20)

# Create buttonFrame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Save to file
array_of_items = []

with open("todos", "r") as fl:
    lines = fl.readlines()

for line in lines:
    items_list.insert(END, line.strip())
    array_of_items.append(line.strip())


# Functions
def delete_item():
    selected_item = items_list.get(ANCHOR)
    array_of_items.remove(selected_item)
    items_list.delete(ANCHOR)
    with open("todos", "w") as file:
        for item in array_of_items:
            file.write(item + "\n")


def add_item():
    items_list.insert(END, entry_box.get())
    array_of_items.append(entry_box.get())
    entry_box.delete(0, END)
    with open("todos", "w") as file:
        for item in array_of_items:
            file.write(item + "\n")


# Add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)

root.mainloop()
