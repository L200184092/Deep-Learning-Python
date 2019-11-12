# -----------------------------
# radiob
#
# Contoh penggunaan Radiobutton
# -----------------------------

import tkinter

jendela = tkinter.Tk()
jendela.geometry("300x100")
jendela.title("Contoh RadioButton")

labelInfo = tkinter.Label(jendela, text = "Jender:")
labelInfo.pack(anchor = tkinter.W)

jender = tkinter.StringVar()
jender.set("W")
radioPria = tkinter.Radiobutton(jendela, text = "Pria",
                                variable = jender,
                                value = "P")

radioWanita = tkinter.Radiobutton(jendela, text = "Wanita",
                                  variable = jender,
                                  value = "W")
radioPria.pack(anchor = tkinter.W)
radioWanita.pack(anchor = tkinter.W)

jendela.mainloop()
