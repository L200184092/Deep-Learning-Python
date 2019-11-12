# ----------------------------------
# onoff
#
# Contoh untuk membuat tombol on-off
#   untuk mengatur warna jendela
# ----------------------------------

import tkinter

def on_off():
    if tombolOnOff["text"] == "On":
        jendela.configure(background = "white")
        tombolOnOff["text"] = "Off"
    else:
        jendela.configure(background = "black")
        tombolOnOff["text"] = "On"

jendela = tkinter.Tk()
jendela.geometry("250x100")
jendela.title("Tombol On Off")

tombolOnOff = tkinter.Button(jendela, text = "off",
                             width = 10,
                             command = on_off)
tombolOnOff.pack()
jendela.mainloop()
