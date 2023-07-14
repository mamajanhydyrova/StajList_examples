#liste=[1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 2, 2]
def ardışık_tekrar_gruplayan(liste):
    gruplar = []
    tekrarlar = []
    for i in range(len(liste) - 1):
        if liste[i] == liste[i + 1]:
            tekrarlar.append(liste[i])
        else:
            if tekrarlar:
                tekrarlar.append(liste[i])
                gruplar.append(tekrarlar)
                tekrarlar = []
    if tekrarlar:
        tekrarlar.append(liste[-1])
        gruplar.append(tekrarlar)
    return gruplar

liste = [1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 2, 2]
gruplar = ardışık_tekrar_gruplayan(liste)
print(gruplar)

