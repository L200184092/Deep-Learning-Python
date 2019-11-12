# --------------------------------
# assert
# --------------------------------
# Contoh penggunaan assertionError
# --------------------------------

def fx(a, b):
    if __debug__:
        if b == 0:
            raise AssertionError("Argumen kedua tidak boleh berupa nol")
    return(a, b)

# Program utama
print(fx(1, 2))
print(fx(1, 0))
