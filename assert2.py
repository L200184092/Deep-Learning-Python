# ------------------------
# assert2
# ------------------------
# Contoh penggunaan assert
# ------------------------

def fx(a, b):
    assert b != 0, ("Argumen kedua tak boleh berupa nol")
    return (a, b)

# Program utama
print(fx(1, 2))
print(fx(1, 0))
