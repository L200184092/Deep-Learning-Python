# ----------------------------------------------
# quit
# 
# Contoh untuk membuat tombol pengakhir aplikasi
# ----------------------------------------------

import tkinter

jendela = tkinter.Tk()
jendela.geometry("250x100")
jendela.title("Tombol Quit")

tombolKeluar = tkinter.Button(jendela, text = "Keluar",
	width = 10,
	command = jendela.destroy)
tombolKeluar.pack()
jendela.mainloop()