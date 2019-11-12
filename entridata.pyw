# -------------------------------------------
# entridata
#
# Contoh pembuatan Entry untuk pemasukan data
# -------------------------------------------

import tkinter
import time

def ubahJudul():
    jendela.title(entryJudul.get())

jendela = tkinter.Tk()
jendela.geometry("500x100")
jendela.title("Contoh Entry")
labelInfo = tkinter.Label(jendela,
                          text = "Judul Jendela:")
labelInfo.pack()

entryJudul = tkinter.Entry(jendela, width = 70)
entryJudul.pack()

tombolUpdate = tkinter.Button(jendela, text = "Perbaharui Judul",
                              command = ubahJudul)
tombolUpdate.pack()
jendela.mainloop()
