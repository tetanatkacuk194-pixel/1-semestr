korystuvachi = {"tanya": ["1234", [10, 11, 8, 12, 9, 4, 7]], 
                "anna": ["qwerty", [9, 10, 6, 12, 3, 5]], 
                "ivan": ["1111", [7, 8, 4, 2, 10, 11]], 
                "maksym": ["2222", [12, 9, 10, 3, 4, 8]]}
login = input("Vvedit login: ")
parol = input("Vvedit parol: ")
if login in korystuvachi and parol == korystuvachi[login][0]:
    ocinky = korystuvachi[login][1]
    print("Vashi ocinky:", ocinky)
    zadovilni = 0
    nezadovilni = 0
    for ocinka in ocinky:
        if ocinka >= 5:
            zadovilni += 1
        else:
            nezadovilni += 1
    print("Ocinok vid 5 do 12:", zadovilni)
    print("Ocinok vid 1 do 4:", nezadovilni)
else:
    print("Nepravylni login abo parol")
