# ---------------------------------------
# scrollbar
#
# Contoh penggunaan Scrollbar dan Listbox
# ---------------------------------------

import tkinter

jendela = tkinter.Tk()
jendela.title("Contoh Scrollbar")

# Scrollbar
scrollbar = tkinter.Scrollbar(jendela)
scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)

# Listbox
listbox = tkinter.Listbox(jendela)
listbox.pack(side = tkinter.LEFT, fill = tkinter.Y)

listbox.insert(tkinter.END, "Anggur")
listbox.insert(tkinter.END, "Apel")
listbox.insert(tkinter.END, "Blewah")
listbox.insert(tkinter.END, "Jambu")
listbox.insert(tkinter.END, "Jeruk")
listbox.insert(tkinter.END, "Mangga")
listbox.insert(tkinter.END, "Nanas")
listbox.insert(tkinter.END, "Pepaya")
listbox.insert(tkinter.END, "Pisang")
listbox.insert(tkinter.END, "Salak")
listbox.insert(tkinter.END, "Semangka")
listbox.insert(tkinter.END, "Sirsat")

# Hubungkan scrollbar ke listbox
scrollbar.config(command = listbox.yview)
listbox.config(yscrollcommand = scrollbar.set)

jendela.mainloop()
