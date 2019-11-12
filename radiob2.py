# ---------------------------------------
# radiob2
#
# Contoh penanganan klik pada Radiobutton
# ---------------------------------------

import tkinter
from tkinter import messagebox

def prosesTombolRadio():
    if jender.get() == "P":
        tkinter.messagebox.showinfo("Info", "Anda memilih Pria")
    else:
        tkinter.messagebox.showinfo("Info", "Anda memilih Wanita")

jendela = tkinter.Tk()
jendela.geometry("300x100")
jendela.title("Contoh RadioButton")

labelInfo = tkinter.Label(jendela, text = "Jender:")
labelInfo.pack(anchor = tkinter.W)

jender = tkinter.StringVar()
jender.set("W")
radioPria = tkinter.Radiobutton(jendela, text = "Pria",
                                variable = jender,
                                value = "P",
                                command = prosesTombolRadio)
radioWanita = tkinter.Radiobutton(jendela, text = "Wanita",
                                  variable = jender,
                                  value = "W",
                                  command = prosesTombolRadio)

radioPria.pack(anchor = tkinter.W)
radioWanita.pack(anchor = tkinter.W)
jendela.mainloop()
