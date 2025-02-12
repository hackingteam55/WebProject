def functie_input_caractere():
    z = input('Introduceti caracterele: ')
    y = input('Introduceti-va numele: ')
    if z.isdigit():
        print('Caracterele sunt de tip INT')
    elif z.isascii():
        print(f'Caracterele sunt de tip STR')
        print(f'Sirul a fost gasit de {y}')
    else:
        print('Caracterele sunt de tip necunoscut')


functie_input_caractere()


def functie_verificare_numar():
    z = int(input('Introduceti numarul: '))
    if z % 2 == 0:
        print('Numarul este par')
    elif z % 2 != 0:
        print('Numarul este impar')
    else:
        print('Paritate necunoscuta')


functie_verificare_numar()


def verificare_an_bisect():
    z = int(input('Introduceti anul: '))
    if z % 4 == 0:
        print('Anul este bisect')
    elif z % 4 != 0:
        print('Anu nu este bisect')
    else:
        print('An necunoscut')

verificare_an_bisect()


def verificare_numar():
    z = int(input('Introduceti numarul: '))
    if (z > 0) and (z < 10):
        print('Numarul este pozitiv')
        print('Confirmare numar')
    elif z == 0:
        print('Numarul este 0')
    elif z < 0:
        print(f'Numarul {z} este negativ')
        z = abs(z)
        print(f'Numarul transformat este {z}')
    else:
        print('Numar inafara parametriilor')


verificare_numar()


def alegere_optiune():
    print("1 – Afisare lista de cumparaturi\n 2 – Adaugare element \n 3 – Stergere element \n 4 – Sterere lista de "
          "cumparaturi \n 5 - Cautare in lista de cumparaturi ")
    z = int(input('Alegeti optiunea: '))
    if z == 1:
        print('Afisare lista de cumparaturi')
    elif z == 2:
        print('Adaugare element')
    elif z == 3:
        print('Stergere element')
    elif z == 4:
        print('Stergere lista de cumparaturi')
    elif z == 5:
        print('Cautare in lista de cumparaturi')
    else:
        print('Alegerea nu exista. Reincercati')


alegere_optiune()




