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

## Użycie
```python
from Dataset import Dataset

ds = Dataset()
ds.load("student-mat.csv", header=True)
ds.print_labels()
ds.print_data(0, 3)    
train, test, val = ds.split(35, 35, 30)
print(len(train), len(test), len(val))
ds.class_count(-1)
ds.print_class_data("13")
ds.save_do_csv(ds.data, "saved.csv")
