# -------------------------------------------------
# quit2
#
# Contoh pembuatan tombol untuk mengakhiri aplikasi
#   dengan tambahan berupa kotak dialog
#   untuk konfirmasi
# -------------------------------------------------

import tkinter
from tkinter import messagebox

def keluar():
    if tkinter.messagebox.askyesno("Konfirmasi",
                                   "Mau keluar beneran?"):
        jendela.destroy

jendela = tkinter.Tk()
jendela.geometry("250x100")
jendela.title("Slider")

tombolKeluar = tkinter.Button(jendela, text = "Keluar",
                              width = 10,
                              command = keluar)

tombolKeluar.pack()
jendela.mainloop()
