# -----------------------------------------
# slider2
#
# Contoh pembuatan slider menggunakan Scale
#   dengan berbagai opsi
# -----------------------------------------

import tkinter

jendela = tkinter.Tk()
jendela.geometry("500x150")
jendela.title("Slider")

slider = tkinter.Scale(jendela, from_ = 0, to = 5,
                       orient = tkinter.HORIZONTAL,
                       resolution = 0.5, length = 300,
                       tickinterval = 0.5, showvalue = 0)

slider.set(2.5) # Atur nilai awal

slider.pack()

jendela.mainloop()
