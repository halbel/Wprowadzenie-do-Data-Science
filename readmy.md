# Dataset loader

 Projekt zaliczeniowy z przedmiotu **[Wprowadzenie do Data Science]**.

---

## Opis 

Projekt zawiere klase 'Dataset', która umożliwia:
- wczytywanie danych z pliku CSV,
- wypisanie etykiet,
- wypisanie danych datasetu,
- podział datasetu na zbiór treningowy, testowy, walidacyjny,
- wypisanie klas decyzyjnych,
- wypisanie danych dla podanej wartosci klasy decyzyjnej,
- zapisanie danych do pliku csv.

Dane są wczytywane z plików CSV z separatorem ';'.

## Wymagania
- Python 3.8+
- Biblioteka standardowa ('scv')

? ## Struktura danych
- `labels` – lista nazw kolumn (pierwszy wiersz pliku)
- `data` – lista wierszy danych



## Użycie
```python
from dataset import Dataset

ds = Dataset()
ds.load("student-mat.csv", header=True)

print(ds.labels)
print(len(ds.data))
