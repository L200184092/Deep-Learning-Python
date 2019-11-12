# ------------------------
# spinbox
#
# Contoh pembuatan spinbox
# ------------------------

import tkinter

jendela = tkinter.Tk()
jendela.title("Contoh Spinbox")
jendela.geometry("250x100")

spinbox = tkinter.Spinbox(jendela, from_ = 0, to = 100,
                          increment = 5)
spinbox.pack()

jendela.mainloop()
