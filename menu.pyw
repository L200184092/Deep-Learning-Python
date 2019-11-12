# -----------------------------
# menu
#
# Contoh pembuatan menu pilihan
# -----------------------------

import tkinter
from tkinter import messagebox, filedialog

def prosesPilihanNew():
    tkinter.messagebox.showinfo("Informasi", "Anda memilih New")
def prosesPilihanOpen():
    nama = tkinter.filedialog.askopenfilename()
    if nama:
        tkinter.messagebox.showinfo("Informasi", "Anda memilih file " + nama)
def prosesPilihanAbout():
    tkinter.messagebox.showinfo("Informasi", "Anda memilih About")

jendela = tkinter.Tk()
menuUtama = tkinter.Menu(jendela)
jendela.config(menu = menuUtama)
menuFile = tkinter.Menu(menuUtama, tearoff = 0)
menuUtama.add_cascade(label = "File", menu = menuFile)
menuFile.add_command(label = "New", command = prosesPilihanNew)
menuFile.add_command(label = "Open...", command = prosesPilihanOpen)
menuFile.add_separator()
menuFile.add_command(label = "Exit", command = jendela.destroy)

menuBantuan = tkinter.Menu(menuUtama, tearoff = 0)
menuUtama.add_cascade(label = "Bantuan", menu = menuBantuan)
menuBantuan.add_command(label = "About...",
                        command = prosesPilihanAbout)

jendela.mainloop()
