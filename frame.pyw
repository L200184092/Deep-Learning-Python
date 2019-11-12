# -----------------------
# frame
#
# Contoh penggunaan Frame
# -----------------------

import tkinter

jendela = tkinter.Tk()
jendela.title("Contoh Frame")
jendela.geometry("200x100")

kerangka1 = tkinter.Frame(jendela,
                          height = 50, width = 200)
kerangka1.pack(side = tkinter.TOP)

kerangka2 = tkinter.Frame(jendela,
                          height = 50, width = 200)
kerangka2.pack(side = tkinter.BOTTOM)

# Tambahkan 2 button ke kerangka1
tombolApel = tkinter.Button(kerangka1, text = "Apel",
                            bg = "white", fg = "red")
tombolApel.pack(side = tkinter.LEFT)

tombolMelon = tkinter.Button(kerangka1, text = "Melon",
                             bg = "white", fg = "green")
tombolMelon.pack(side = tkinter.LEFT)

# Tambahkan 1 Button ke kerangka2
tombolKeluar = tkinter.Button(kerangka2, text = "Keluar")
tombolKeluar.pack()

jendela.mainloop()
