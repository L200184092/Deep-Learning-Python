# -----------------------------------------
# slider
#
# Contoh pembuatan slider menggunakan Scale
# -----------------------------------------

import tkinter

def infoScale(nilai):
    labelInfo.configure(text = "Nilai yang Anda atur: " +
                        nilai)

jendela = tkinter.Tk()
jendela.geometry("250x150")
jendela.title("Slider")

slider = tkinter.Scale(jendela, from_ = 0, to = 100,
                       command = infoScale)
labelInfo = tkinter.Label(jendela, text = "Info")

slider.pack()
labelInfo.pack()

slider.set(50)

jendela.mainloop()
