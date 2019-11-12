while True:
    try:
        bil = input("Masukkan bilangan: ")
        bil = int(bil)
        break
    except ValueError:
        print("Anda salah memasukkan bilangan")

print("Anda memasukkan bilangan", bil)
