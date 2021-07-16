"""
documentaton here
"""
from tkinter import Tk, END, Text, Entry, Listbox, Scrollbar, Button, Label, StringVar
import backend

def view_command():
    data_list.delete(0, END)
    for row in backend.view():
        data_list.insert(END, row)

def search_command():
    data_list.delete(0, END)
    for row in backend.search(title.get(), author.get(), year.get(), isbn.get()):
        data_list.insert(END, row)

def add_command():
    backend.insert(title.get(), author.get(), year.get(), isbn.get())
    data_list.delete(0, END)
    data_list.insert(END, (title.get(), author.get(), year.get(), isbn.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title.get(), author.get(), year.get(), isbn.get())

def get_selected_row(event):
    global selected_tuple
    
    if not len(data_list.curselection()):
        return

    index = data_list.curselection()[0]
    selected_tuple = data_list.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[4])


window = Tk()

window.wm_title("BookStore")

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)
title = StringVar()
title_entry = Entry(window, textvariable=title)
title_entry.grid(row=0, column=1)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)
author = StringVar()
author_entry = Entry(window, textvariable=author)
author_entry.grid(row=0, column=3)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)
year = StringVar()
year_entry = Entry(window, textvariable=year)
year_entry.grid(row=1, column=1)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)
isbn = StringVar()
isbn_entry = Entry(window, textvariable=isbn)
isbn_entry.grid(row=1, column=3)

data_list = Listbox(window, height=6, width=35)
data_list.grid(row=2, column=0, rowspan=6, columnspan=2)
data_scrollbar = Scrollbar(window)
data_scrollbar.grid(row=2, column=2, rowspan=6)
data_list.configure(yscrollcommand=data_scrollbar.set)
data_scrollbar.configure(command=data_list.yview)

data_list.bind('<<ListboxSelect>>', get_selected_row)

view_button = Button(window, text="View all", width=12, command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry", width=12, command=add_command)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()