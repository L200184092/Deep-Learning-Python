# ---------------------------------------------
# listbox2
#
# Contoh untuk menangani pemilihan pada Listbox
#   baik menggunakan klik, panah atas maupun
#   panah bawah
# ---------------------------------------------

import tkinter

def infoBuah(event):
    elemen = event.widget
    indeks = elemen.curselection()[0]
    pilihan = elemen.get(indeks)
    labelInfo.config(text = "Pilihan Anda: " + pilihan)

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

# Menentukan perubahan pilihan
listbox.bind("<<ListboxSelect>>", infoBuah)

# Label
labelInfo = tkinter.Label(jendela, text = "")
labelInfo.pack()

jendela.mainloop()
