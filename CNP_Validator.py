import datetime

_JUDETE = {
    '01': 'Alba',
    '02': 'Arad',
    '03': 'Arges',
    '04': 'Bacau',
    '05': 'Bihor',
    '06': 'Bistrita-Nasaud',
    '07': 'Botosani',
    '08': 'Brasov',
    '09': 'Braila',
    '10': 'Buzau',
    '11': 'Caras-Severin',
    '12': 'Cluj',
    '13': 'Constanta',
    '14': 'Covasna',
    '15': 'Dambovita',
    '16': 'Dolj',
    '17': 'Galati',
    '18': 'Gorj',
    '19': 'Harghita',
    '20': 'Hunedoara',
    '21': 'Ialomita',
    '22': 'Iasi',
    '23': 'Ilfov',
    '24': 'Maramures',
    '25': 'Mehedinti',
    '26': 'Mures',
    '27': 'Neamt',
    '28': 'Olt',
    '29': 'Prahova',
    '30': 'Satu Mare',
    '31': 'Salaj',
    '32': 'Sibiu',
    '33': 'Suceava',
    '34': 'Teleorman',
    '35': 'Timis',
    '36': 'Tulcea',
    '37': 'Vaslui',
    '38': 'Valcea',
    '39': 'Vrancea',
    '40': 'Bucuresti',
    '41': 'Bucuresti - Sector 1',
    '42': 'Bucuresti - Sector 2',
    '43': 'Bucuresti - Sector 3',
    '44': 'Bucuresti - Sector 4',
    '45': 'Bucuresti - Sector 5',
    '46': 'Bucuresti - Sector 6',
    '47': 'Bucuresti - Sector 7 (desfiintat)',
    '48': 'Bucuresti - Sector 8 (desfiintat)',
    '51': 'Calarasi',
    '52': 'Giurgiu',
}


def validator_cnp():
    cnp = input('Introduceti cnp: ')
    # print(f'Sex: {cnp[0]}')
    # print(f'Anul_Nasterii: {cnp[1:3]}')
    # print(f'Luna_Nasterii: {cnp[3:5]}')
    # print(f'Ziua_Nasterii: {cnp[5:7]}')
    # print(f'Judet: {cnp[7:9]}')
    # print(f'Numar_Unic_Nastere: {cnp[9:12]}')
    # print(f'Cifra_De_Control: {cnp[-1]}')
    # print(f'CNP: {cnp}')

    s = cnp[0]
    a = cnp[1:3]
    l = cnp[3:5]
    z = cnp[5:7]
    j = cnp[7:9]
    n = cnp[9:12]
    c = cnp[-1]

    if s not in '123456789':
        raise Exception('Invalid Sex digit, Invalid CNP')

    if len(cnp) != 13:
        raise Exception("Invalid CNP")

    def date_nastere(cnp):
        conditii = {'1': 1900,
                    '2': 1900,
                    '3': 1800,
                    '4': 1800,
                    '5': 2000,
                    '6': 2000
                    }
        an = int(a) + conditii.get(s, 1900)
        luna = int(l)
        zi = int(z)
        zi_nastere = datetime.date(an, luna, zi)
        today = datetime.date
        print(today)
        try:
            return zi_nastere
        except ValueError:
            raise Exception('Date nastere invalide, CNP Invalid')

    verificare_judet = j
    if verificare_judet not in _JUDETE.keys():
        raise Exception('Judet din CNP invalid, CNP-ul este invalid')

    def calculare_cifra_control(number):
        control = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
        verificare = sum(w * int(n) for w, n in zip(control, number)) % 11
        return '1' if verificare == 10 else str(verificare)

    if calculare_cifra_control(cnp[:-1]) != c:
        raise Exception("Cifra de control invalida, CNP Invalid")

    print('CNP-ul este valid')


validator_cnp()
