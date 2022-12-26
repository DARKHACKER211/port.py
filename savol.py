import os
from savolcik import igra, menu

if __name__ == "__main__":
    while True:
        os.system('cls')
        tanlov = menu()
        if tanlov == 1:
            print("\u001b[32mOson o'yin")
            igra(daraja=1)
        elif tanlov == 2:
            print("\u001b[36mO'rta o'yin")
            igra(daraja=2)
        elif tanlov == 3:
            print("\u001b[31mJuda qiyin o'yin")
            igra(daraja=3)
        elif tanlov == 4:
            print("Chiqish")
        if input("\u001b[31m   Oyinni davom ettirasizmi? Ha(h) Yo'q (y): ") != 'h':
            break
