from tkinter import * 

root = Tk()


def add_item():
    listbox.insert(END, textbox.get("1.0", END).strip())
    textbox.delete("1.0", END)


def del_selected_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])


textbox = Text(root, height=1)
addbutton = Button(root, text="Добавить", command=lambda: add_item())
listbox = Listbox(root, width=30, height=5)
delbutton = Button(root, text="Удалить", command=lambda: del_selected_item())


listbox.insert(END, "Элемент 1")
listbox.insert(END, "Элемент 2")
listbox.insert(END, "Элемент 3")


textbox.pack(pady=10)
addbutton.pack(pady=10)
listbox.pack(pady=10)
delbutton.pack(pady=10)

addbutton = Button(root, text="Добавить")

root.mainloop()