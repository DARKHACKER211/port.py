import random


def menu():
    birinchimi = True
    while True:
        if birinchimi:
            print("""\u001b[32m                      _
        *                           _____      *     |\       /
\    /  |   | /  =======  |====|   |     |     |     | \     /    /\ 
 \  /   |   |/      |     |    |   |_____|     |     |  \   /    /__\ 
  \/    |   |\      |     |____|   | \         |     |   \_/    /    \ 
                                   |  \     
""")
            tanlov = input("""\u001b[34mQaysi birini tanlaysiz ?\u001b[34m
				\u001b[32m1. Oson\u001b[32m
				\u001b[36m2. qiynalasan baribir\u001b[36m
				\u001b[31m3. qiyin\u001b[31m
				\u001b[37m4. O'yindan chiqish \u001b[37m
(1-4) oraliqda son kiriting: """)
            birinchimi = False
        else:
            tanlov = input("Xato. (1-4) oraliqda son kiriting:")
        if tanlov.isdigit() and int(tanlov) in range(1, 5):
            return int(tanlov)


def igra(daraja):
    takrorlash = 10
    bal = 0
    for j in range(takrorlash):
        amal = random.choice(["+", "-", "*", ":"])
        masala = None
        javob = None
        for i in range(daraja + 1):
            a = random.randint(1, 10)
            if i == 0:
                masala = str(a)
                javob = a
            else:
                masala += f" {amal} {a}"
                if amal == "+":
                    javob += a
                elif amal == "-":
                    javob -= a
                elif amal == "*":
                    javob *= a
                elif amal == "/":
                    javob = round(javob / a, 2)
        natija = input(f" javobini yozing: {masala} = ")
        print()
        if float(natija) == javob:
            print("To'g'ri")
            bal += 1
        else:
            print()
            print(f"Xato toptingiz . To'g'ri javob : {javob}", )
            print()
        print(f"Siz {takrorlash} savoldan {bal} ta to'g'ri javob topdingiz !")
        print()