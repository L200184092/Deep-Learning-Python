while True:
    try:
        bil = input("Masukkan bilangan: ")
        bil = int(bil)
        break
    except ValueError:
        print("Anda salah memasukkan bilangan")
    except KeyboardInterrupt:
        print("Maaf jangan menekan tombol Ctrl + C")

print("Anda memasukkan bilangan", bil)
