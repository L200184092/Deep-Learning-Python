# ------------------------------
# label
#
# Contoh untuk menyertakan label
# ------------------------------

import tkinter

jendela = tkinter.Tk()
labelA = tkinter.Label(jendela, text = "Selamat belajar GUI")
labelB = tkinter.Label(jendela, text = "Sukses selalu",
                        foreground = "yellow", background = "blue")
labelA.pack()
labelB.pack()
jendela.mainloop()
