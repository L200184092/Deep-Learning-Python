# -------------------------------------------------
# judulikon
#
# Contoh untuk mengubah judul dan ikon pada jendela
# -------------------------------------------------

import tkinter

jendela = tkinter.Tk()
jendela.wm_iconbitmap("favicon.ico")
jendela.title("Aplikasiku")
jendela.geometry("350x250")
jendela.mainloop()
