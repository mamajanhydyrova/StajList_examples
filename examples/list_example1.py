def en_sık_tekrar_sayi(liste):
    liste2 = {}
    for i in liste:
        if i in liste2:
            liste2[i] += 1
        else:
            liste2[i] = 1
    max_sayi = 0
    number = None
    for i, sayi in liste2.items():
        if sayi > max_sayi:
            number = i
            max_sayi = sayi
    return number, max_sayi


liste = [1, 2, 3, 2, 2, 4, 5, 4, 4]
number, max_sayi = en_sık_tekrar_sayi(liste)
print("En sık tekrar eden sayi:", number)
print("Tekrar sayısı:", max_sayi)
