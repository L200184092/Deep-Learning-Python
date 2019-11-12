# -----------------------------------
# cekfile
#
# Contoh operasi file untuk memeriksa
#   keberadaan file
# -----------------------------------

def berkas_ada(nama_file):
    ada = True
    try:
        berkas = open(nama_file)
        berkas.close()
    except IOError:
        ada = False
    return ada

print(berkas_ada("pertama.py"))
print(berkas_ada("takada"))

