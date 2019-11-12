# --------------------------------
# message
#
# Contoh penggunaan widget Message
#   untuk mengatur warna jendela
# --------------------------------

import tkinter

jendela = tkinter.Tk()
jendela.geometry("250x100")
jendela.title("Contoh Message")

pesan = tkinter.Message(jendela,
                        text = "Inilah pesannya. Multibaris bisa",
                        width = 100)
pesan.pack()
jendela.mainloop()
