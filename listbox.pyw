# ------------------------
# listbox
#
# Contoh pembuatan listbox
# ------------------------

import tkinter
from tkinter import messagebox


def infoBuah(event):
    elemen = event.widget
    pilihan = elemen.get(tkinter.ACTIVE)
    tkinter.messagebox.showinfo("Informasi", pilihan)

jendela = tkinter.Tk()
jendela.title("Contoh Listbox")
jendela.geometry("250x250")

listbox = tkinter.Listbox(jendela)
listbox.pack()

# Memasukkan daftar pilihan
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

listbox.selection_set(first = 0)
listbox.bind("<Double-Button-1>", infoBuah)

jendela.mainloop()
