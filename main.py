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

# Save to file
array_of_items = []

with open("todos", "r") as fl:
    lines = fl.readlines()

for line in lines:
    items_list.insert(END, line.strip())
    array_of_items.append(line.strip())


def on_entry_click(event):
    if entry_box.get() == "Enter your text here":
        entry_box.delete(0, END)
        entry_box.config(fg="black")


def on_focus_out(event):
    if not entry_box.get():
        entry_box.config(fg="gray")
        entry_box.insert(0, 'Enter your text here')


def done_item():
    selected_index = items_list.curselection()
    if selected_index:
        items_list.itemconfig(selected_index, bg="green", fg="white")


def to_do():
    selected_index = items_list.curselection()
    if selected_index:
        items_list.itemconfig(selected_index, bg="white", fg="black")


def delete_item():
    selected_item = items_list.get(ANCHOR)
    if selected_item not in array_of_items:
        print("lol")
    else:
        array_of_items.remove(selected_item)
        items_list.delete(ANCHOR)
    with open("todos", "w") as file:
        for item in array_of_items:
            file.write(item + "\n")


def add_item():
    if not entry_box.get().strip() or entry_box.get() == "Enter your text here":
        entry_box.delete(0, END)
    else:
        items_list.insert(END, entry_box.get())
        array_of_items.append(entry_box.get())
        entry_box.delete(0, END)
        with open("todos", "w") as file:
            for item in array_of_items:
                file.write(item + "\n")


# Create entry box
entry_box = Entry(root,  font=("Helvetica", 12))
entry_box.insert(0, 'Enter your text here')
entry_box.config(fg="gray")
entry_box.bind('<FocusIn>', on_entry_click)
entry_box.bind('<FocusOut>', on_focus_out)
entry_box.pack(pady=20)

# Create buttonFrame
button_frame = Frame(root)
button_frame.pack(pady=20)


# Add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item, width=10, bg="light gray")
add_button = Button(button_frame, text="Add Item", command=add_item, width=10, bg="light gray")
done_button = Button(button_frame, text="Done", command=done_item, bg="light green", fg="black", width=10)
to_do_button = Button(button_frame, text="To Do", command=to_do, width=10, bg="light gray")

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
done_button.grid(row=0, column=2)
to_do_button.grid(row=0, column=3, padx=20)

root.mainloop()
