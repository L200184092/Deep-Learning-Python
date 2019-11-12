# ------------------------------------
# checkb
#
# Contoh penanganan klik pada Checkbox
# ------------------------------------

import tkinter
from tkinter import messagebox

def prosesKotakCek():
    pilihan = "Pilihan Anda:\n"
    if varMembaca.get() == "1":
        pilihan = pilihan + "Membaca\n"

    if varTraveling.get() == "1":
        pilihan = pilihan + "Traveling"

    tkinter.messagebox.showinfo("Info", pilihan)

jendela = tkinter.Tk()
jendela.geometry("300x100")
jendela.title("Contoh CheckBox")

labelInfo = tkinter.Label(jendela, text = "Kesukaan Anda:")
labelInfo.pack(anchor = tkinter.W)

varMembaca = tkinter.StringVar()
varTraveling = tkinter.StringVar()

checkMembaca = tkinter.Checkbutton(jendela, text = "Membaca",
                                   variable = varMembaca,
                                   command = prosesKotakCek)

checkTraveling = tkinter.Checkbutton(jendela, text = "Traveling",
                                     variable = varTraveling,
                                     command = prosesKotakCek)

# Membuat kotak cek dalam keadaan tidak terpilih
checkMembaca.deselect()
checkTraveling.deselect()

# Mengatur penampilan kotak cek di jendela
checkMembaca.pack(anchor = tkinter.W)
checkTraveling.pack(anchor = tkinter.W)

jendela.mainloop()
