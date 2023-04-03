import tkinter as tk

root = tk.Tk()
root. geometry ("408x200+500+200")

menubar = tk.Menu(root)
file = tk.Menu(menubar, tearoff-0)

# add_cascade digunakan untuk menampilkan submenu
menubar. add_cascade(label="File", menu=file)

# add_command digunakan untuk menambah menu item
file.add_command(label="new")
file.add_command(label="open")
file.add_command(label="save")
file.add_command(label="Close")

# add_separator untuk menampilkan pemisah
file.add_separator()
file.add_command(label="Exit", command=root.quit)

edit = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

# menampilkan menu
root. config(menu=menubar)
root .mainloop()
