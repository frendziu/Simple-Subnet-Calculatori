import sys
import socket
import ipaddress
import json

print ("Kalkulator podsieci")

def getIP ():
    print("IP "+socket.gethostbyname(socket.gethostname()))
    IP = socket.gethostbyname(socket.gethostname())
    return IP

def getMask (IP):
    maska = ipaddress.IPv4Network(IP)
    print(maska)
    return maska

def checkMask(maska):
    a = str(maska).split("/")
    a1 = int(a[1])
    if a1>= 0 or a1 <= 32:
        print("Maska wynosi  "+a[1])
    else:
        print("Maska spoza przedzialu 0-32")
    return maska

def checkKropka (IP):
    y = "."
    for i in range(0, len(IP)):
        if IP[i] != y:
            x = int(IP[i])
        if IP[i] == y:
            print("Adres poprawny")
            continue
        elif x>=0 or x<=9:
            print("Adres poprawny")
            continue
        else:
            print("Adres IP jest nieprawidlowy")
            break

def checkPrzedzial (IP):
    tablica = IP.split(".")
    print(tablica)
    for i in range(0, len(tablica)):
        tablica_int = int(tablica[i])
        if tablica_int >= 0 or tablica_int <=255:
            print("Czlon jest w przedziale 0-255")
            continue
        else:
            print("Czlony nie sa w przedziale 0-255")
            break
    return tablica

def checkDlugosc (tablica):
    ilosc = len(tablica)
    if ilosc == 4:
        print("Sa 4 czlony")
    else:
        print("Ilosc czlonow jest rozna od 4")

def przelicznik_binarne (liczba):
    przeliczenie = []
    for i in range(0, len(liczba)):
        ipsplitedbin = format(int(liczba[i]), '#010b')
    przeliczenie.append(ipsplitedbin)
    przeliczone = ".".join(przeliczenie)
    print(przeliczone)
    return przeliczone

def adres_sieci ():
    mask = ipaddress.IPv4Interface(IP)
    print("Adres sieci: {0}".format(mask.network))
    return mask.network

def klasa_sieci(klasa):
    wynik = ""
    klasa = klasa.split(".")
    klasa = int(klasa[0])
    if klasa<128:
        wynik = "A"
        print("A")
    elif klasa<192:
        wynik = "B"
        print("B")
    elif klasa<224:
        wynik = "C"
        print("C")
    elif klasa<240:
        wynik = "D"
        print("D")
    elif 240<=klasa<256:
        wynik = "E"
        print("E")
    return wynik

def adres_rozgloszeniowy(fr, tab):
    e = []
    wynik = []
    for i in range(0, len(fr)):
        v = int(fr[i])
        e.append(v^0xff)

    for i in range(0, len(fr)):
        p = int(tab[i])+e[i]
        if p>255:
            p = 255
        wynik.append(p)

    print(wynik)
    return wynik

def pierwszy_adres_hosta(first):
    wyn = []
    for i in range(0, 4):
        if i == 3:
            wyn.append(int(first[3])+1)
            continue
        wyn.append(int(first[i]))
    print(wyn)
    return wyn

def ostatni_adres_hosta(last):
    wyn = []
    for i in range(0, 4):
        if i == 3:
            wyn.append(int(last[3]) - 1)
            continue
        wyn.append(int(last[i]))
    print(wyn)
    return wyn

def liczba_hostow(ilosc):
    wyn = []
    ilosc = int(ilosc)
    wynik = (2**(32-ilosc) - 2)
    if wynik<0:
        return str(0)
    else:
        wyn.append(wynik)
        wynik = str(wynik)
        print("Max liczba hostow: "+wynik)
        print("Max liczba hostow binarnie")
        return wyn

if(len(sys.argv)>1):
    zmienna = sys.argv[1]
    IP_z_maska = zmienna
    zmienna = str(zmienna).split("/")
    IP = sys.argv[1]
    zmienna1 = zmienna[0]
    maska = zmienna[1]
    # main
    checkMask(IP_z_maska)
    checkKropka(zmienna1)
    tablica = checkPrzedzial(zmienna1)
    checkDlugosc(tablica)
    przelicznik_binarne(tablica)
    print("Klasa sieci ")
    klasa_sieci(zmienna1)

    interface = ipaddress.IPv4Interface(IP_z_maska)
    adres = interface.with_netmask
    maska1 = str(adres).split("/")
    print("Maska sieci dziesietnie")
    print(maska1[1])
    maska_sieci = str(maska1[1]).split(".")

    print("Maska sieci binarnie")
    przelicznik_binarne(maska_sieci)

    adres_sieci()

    print("Broadcast dziesietnie")
    broadcast = adres_rozgloszeniowy(maska_sieci, tablica)
    print("Broadcast binarnie")
    przelicznik_binarne(broadcast)

    print("Adres pierwszego hosta dziesietnie")
    first = pierwszy_adres_hosta(tablica)
    print("Adres pierwszego hosta binarnie")
    przelicznik_binarne(first)

    print("Adres ostatniego hosta dziesietnie")
    last = ostatni_adres_hosta(broadcast)
    print("Adres ostatniego hosta binarnie")
    przelicznik_binarne(last)

    a = int(maska)
    max_liczba = liczba_hostow(a)
    przelicznik_binarne(max_liczba)

    print('Dane z JSONa')
    data = {}
    data['Dane o sieci'] = []

    data['Dane o sieci'].append({'Adres sieci': str(adres_sieci())})

    data['Dane o sieci'].append({'Klasa sieci': str(klasa_sieci(IP))})

    data['Dane o sieci'].append({'Maska sieci dziesietnie': str(maska_sieci),
                                 'Maska sieci binarnie': str(przelicznik_binarne(maska_sieci))})

    data['Dane o sieci'].append({'Adres brodcast dzisietnie': str(broadcast),
                                 'Adres brodcast binarnie': str(przelicznik_binarne(broadcast))})

    data['Dane o sieci'].append({'Pierwszy adres hosta dzisietnie': str(first),
                                 'Pierwszy adres hosta binarnie': str(przelicznik_binarne(first))})

    data['Dane o sieci'].append({'Ostatni adres hosta dziesietnie': str(last),
                                 'Ostatni adres hosta binarnie': str(przelicznik_binarne(last))})

    data['Dane o sieci'].append({'Maksymalna ilosc hostow dziesietnie': str(max_liczba),
                                 'Maksymalna ilosc hostow binanie': przelicznik_binarne(max_liczba)})

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

else:
    IP = getIP()
    maska = getMask(IP)
    maska = checkMask(maska)
    # main
    checkKropka(IP)
    tablica = checkPrzedzial(IP)
    checkDlugosc(tablica)
    przelicznik_binarne(tablica)
    print("Klasa sieci ")
    klasa_sieci(IP)

    interface = ipaddress.IPv4Interface(maska)
    adres = interface.with_netmask
    maska1 = str(adres).split("/")
    print("Maska sieci dziesietnie")
    print(maska1[1])
    maska_sieci = str(maska1[1]).split(".")

    print("Maska sieci binarnie")
    przelicznik_binarne(maska_sieci)

    adres_sieci()

    print("Broadcast dziesietnie")
    broadcast = adres_rozgloszeniowy(maska_sieci, tablica)
    print("Broadcast binarnie")
    przelicznik_binarne(broadcast)

    print("Adres pierwszego hosta dziesietnie")
    first = pierwszy_adres_hosta(tablica)
    print("Adres pierwszego hosta binarnie")
    przelicznik_binarne(first)

    print("Adres ostatniego hosta dziesietnie")
    last = ostatni_adres_hosta(broadcast)
    print("Adres ostatniego hosta binarnie")
    przelicznik_binarne(last)

    a = str(maska).split("/")
    max_liczba = liczba_hostow(a[1])

    print('Dane z JSONa')
    data = {}
    data['Dane o sieci'] = []

    data['Dane o sieci'].append({'Adres sieci': str(adres_sieci())})

    data['Dane o sieci'].append({'Klasa sieci': str(klasa_sieci(IP))})

    data['Dane o sieci'].append({'Maska sieci dziesietnie': str(maska_sieci),
                                 'Maska sieci binarnie': str(przelicznik_binarne(maska_sieci))})

    data['Dane o sieci'].append({'Adres brodcast dzisietnie': str(broadcast),
                                 'Adres brodcast binarnie': str(przelicznik_binarne(broadcast))})

    data['Dane o sieci'].append({'Pierwszy adres hosta dzisietnie': str(first),
                                 'Pierwszy adres hosta binarnie': str(przelicznik_binarne(first))})

    data['Dane o sieci'].append({'Ostatni adres hosta dziesietnie': str(last),
                                 'Ostatni adres hosta binarnie': str(przelicznik_binarne(last))})

    data['Dane o sieci'].append({'Maksymalna ilosc hostow dziesietnie': str(max_liczba),
                                 'Maksymalna ilosc hostow binanie': przelicznik_binarne(max_liczba)})

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
