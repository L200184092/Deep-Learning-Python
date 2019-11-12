# --------------------------------------
# kanvas
#
# Contoh penggunaan Canvas untuk membuat
#   gambar mobil
# --------------------------------------

import tkinter

jendela = tkinter.Tk()
jendela.title("Contoh Canvas")
jendela.geometry("350x200")

# Buat kanvas
kanvas = tkinter.Canvas(jendela,
                        height = 200, width = 350)
kanvas.pack()

# Buat bodi mobil
kanvas.create_polygon(40, 140, 40, 115, 80, 100, 100, 60,
                      240, 60, 250, 140, 40, 140, fill = "red")

# Buat jendela
kanvas.create_polygon(82, 100, 102, 62, 140, 62, 140,
                      100, 82, 100, fill = "white")
kanvas.create_rectangle(114, 62, 230, 100,
                        fill = "white", width = 0)

# Buat dua roda
kanvas.create_oval(70, 120, 110, 160, fill = "black")
kanvas.create_oval(190, 120, 230, 160, fill = "black")

# Buat lintasan
kanvas.create_line(20, 163, 330, 163, fill = "gray", width = 5)

jendela.mainloop()
