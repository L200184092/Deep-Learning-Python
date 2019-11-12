# --------------------------------------
# Kanvas2
#
# Contoh penggunaan Canvas untuk membuat
#   diagram kue
# --------------------------------------

import tkinter

jendela = tkinter.Tk()
jendela.title("Contoh Canvas")
jendela.geometry("400x250")

# Buat kanvas
kanvas = tkinter.Canvas(jendela,
                        height = 250, width = 400)
kanvas.pack()

# Buat potongan kue besar
kanvas.create_arc(20, 20, 280, 180,
                  start = 90, extent = 270, fill = "blue")

# Buat potongan kue kecil
kanvas.create_arc(24, 16, 284, 176,
                  start = 0, extent = 90, fill = "light blue")

# Buat tulisan
kanvas.create_text(300, 30, text = "Produk A")
kanvas.create_text(140, 230, text = "Produk B")

# Buat garis
kanvas.create_line(140, 150, 140, 220)
kanvas.create_line(220, 80, 280, 40)

jendela.mainloop()
