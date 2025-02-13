# adunare
def adunare(x, y):
    return x + y


# scadere
def scadere(x, y):
    return x - y


# inmultire
def inmultire(x, y):
    return x * y


# impartire
def impartire(x, y):
    return x / y


print("Selectati o operatie.")
print("1.Adunare")
print("2.Scadere")
print("3.Inmultire")
print("4.Impartire")

while True:
    var = input("Alegeti o optiune(1/2/3/4): ")

    if var in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Primul numar: "))
            num2 = float(input("Al doilea numar: "))
        except ValueError:
            print("Numar invalid")
            continue
        if var == '1':
            print(num1, "+", num2, "=", adunare(num1, num2))
        elif var == '2':
            print(num1, "-", num2, "=", scadere(num1, num2))
        elif var == '3':
            print(num1, "*", num2, "=", inmultire(num1, num2))
        elif var == '4':
            print(num1, "/", num2, "=", impartire(num1, num2))

        next_calculation = input("Executa un calcul nou (da/nu): ")
        if next_calculation == "no":
            break
    else:
        print("Input invalid")
