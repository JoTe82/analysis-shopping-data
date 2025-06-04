"""
Datenüberprüfung customer_shopping_data.csv

Datenquelle: Der verwendete Datensatz „Customer Shopping Dataset – Retail Sales Data“ 
stammt von der Plattform Kaggle.com und wurde unter der 
Lizenz Creative Commons CC0 1.0 Universal (Public Domain Dedication) veröffentlicht. 
Die Urheber haben auf sämtliche Urheberrechte an diesen Daten verzichtet.

Lizenzdetails: https://creativecommons.org/publicdomain/zero/1.0/deed.de
"""

# pandas importieren
import pandas as pd

# es sollen immer alle Spalten eines DataFrames ausgegeben werden
pd.set_option("display.max_columns", None)

# Daten aus der Datei customer_shopping_data.csv importieren
daten = pd.read_csv("customer_shopping_data.csv")

# die ersten zehn Zeilen ausgeben
print(daten.head(10))
print()

# Information über die DataFrame-Struktur ausgeben
print(daten.info())
print()

# einfache statistische Auswertung
print(daten.describe(include="all"))
print()

# die Spaltentitel in Werte für eine Liste umwandeln
spaltentitel = daten.columns.tolist()
print(spaltentitel)
print()

# eine for-Schleife, um die Werte innerhalb jeder Spalte zu zählen und
# absteigend zu sortieren
# das Ergebnis soll auf falsche Daten geprüft werden
for i in spaltentitel:
    print(daten.value_counts(i, ascending=False))
    print()

# das DataFrame wird auf NaN-Werte geprüft
if daten.isnull().any(axis=None):
    print("Es gibt fehlende Werte:")
    print(daten[daten.isnull().any(axis=1)])
    print()
else:
    print("Das DataFrame enthält keine NaN-Werte.")
    print()

# das DataFrame wird auf doppelte Zeilen geprüft
if daten[daten.duplicated()].any(axis=None):
    print("Es gibt doppelte Zeilen:")
    print(daten[daten.duplicated()])
    print()
else:
    print("Es gibt keine doppelten Zeilen.")
    print()

# Datenüberprüfung abgeschlossen, visuelle Trennung
print(f"{'Datenüberprüfung abgeschlossen':*<60}")

"""
Eine überprüfung des Datensatzes war fehlerfrei. Deshalb ist
eine Datenbereinigung nicht notwendig.
"""
