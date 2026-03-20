# Zadanie 1
# Za pomocą funkcji input() wczytaj do programu dowolny tekst od użytkownika.
# Stwórz obiekt typu słownik (obiekt typu dict), którego kluczami będą unikalne
# wyrazy z tekstu, a wartościami przypisanymi do tych kluczy będzie liczba
# wystąpień tego wyrazu we wczytanym tekście. Pozbądź się z tekstu dowolnych
# znaków interpunkcyjnych przed zliczeniem.

import string

tekst = input("Podaj swoj tekst: ")

for znak in string.punctuation:
    tekst = tekst.replace(znak, "")

tekst = tekst.lower()
wyrazy = tekst.split()
slownik = {}

for wyraz in wyrazy:
    if wyraz in slownik:
        slownik[wyraz] += 1
    else:
        slownik[wyraz] = 1

print("\nWyniki:")
for wyraz, liczba in slownik.items():
    print(f" '{wyraz}' : {liczba}")

# Zadanie 2
# Zapisz do pliku tekstowego dane ze słownika z zadania 1 tak,
# aby plik miał postać jak w przykładzie poniżej.
wyrazy_oryginalne = tekst.split()
zapisane = []

with open("wyniki.txt", "w", encoding="utf-8") as plik:
    for wyraz_org in wyrazy_oryginalne:
        wyraz_czysty = wyraz_org
        for znak in string.punctuation:
            wyraz_czysty = wyraz_czysty.replace(znak, "").lower()
        if wyraz_czysty and wyraz_czysty not in zapisane:
            plik.write(f"{wyraz_org.strip(string.punctuation)},{slownik[wyraz_czysty]}\n")
            zapisane.append(wyraz_czysty)       
# Zadanie 3


def wypisz_liczby(n):
    for i in range(1, n + 1):
        spacje = " " * (i-1)
        print(f"{spacje}{i}")


wypisz_liczby(10)