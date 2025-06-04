"""
Statistische Auswertung quantitativer Werte customer_shopping_data.csv

Datenquelle: Der verwendete Datensatz „Customer Shopping Dataset – Retail Sales Data“ 
stammt von der Plattform Kaggle.com und wurde unter der 
Lizenz Creative Commons CC0 1.0 Universal (Public Domain Dedication) veröffentlicht. 
Die Urheber haben auf sämtliche Urheberrechte an diesen Daten verzichtet.

Lizenzdetails: https://creativecommons.org/publicdomain/zero/1.0/deed.de
"""

# das Modul statistics, numpy, pandas und matplotlib importieren
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# es sollen immer alle Spalten eines DataFrames ausgegeben werden
pd.set_option("display.max_columns", None)

# eine Funktion zur statistischen Auswertung 
# der komplette Datensatz wird ausgewertet sowie jede einzelne Shopping Mall
def stats(datensatz):
    # statistische Auswertung der Spalten mit quantitativen Werten
    stat = pd.DataFrame(datensatz.describe())

    # fehlende statistische Werte berechnen, d.h. Median, Modus u Spannweite
    liste = ["age","quantity","price"]
    liste_median = []
    liste_modus = []
    liste_spannweite = []

    # eine for-Schleife um die gesuchten Werte zu ermitteln
    # diese werden anschließend in einer Liste gespeichert
    for i in liste:
        median = statistics.median(datensatz[i])
        modus = statistics.mode(datensatz[i])
        spannweite = max(datensatz[i]) - min(datensatz[i])
        liste_median.append(median)
        liste_modus.append(modus)
        liste_spannweite.append(spannweite)

    # die Listen werden jeweils in ein Series gewandelt
    # Index für die Series festlegen
    index_columns_series = ["age", "quantity","price"]
    median = pd.Series(liste_median, index=index_columns_series)
    modus = pd.Series(liste_modus, index=index_columns_series)
    spannweite = pd.Series(liste_spannweite, index=index_columns_series)

    # aus den Series ein DataFrame erstellen
    # einen Index für die Zeilen festlegen
    index_rows_df = ["median","mode","span"]
    stat_zwei = pd.DataFrame([median,modus,spannweite], index=index_rows_df)

    # beide DataFrames mit concat verbinden
    stat = pd.concat([stat,stat_zwei])

    return stat

# die Daten in ein DataFrame importieren
daten = pd.read_csv("customer_shopping_data.csv")

# die ersten zehn Zeilen des DataFrame ausgeben
print(daten.head(10))
print()

# Information über die DataFrame-Struktur ausgeben
print(daten.info())
print()

# Daten auf Korrelationen untersuchen
print(daten.corr(numeric_only=True))
print()

# ein DataFrame mit statistischen Auswertungen 
# für den kompletten Datensatz erstellen
daten_komplett = stats(daten)
print("Die statistische Auswertung für den gesamten Datensatz:")
print(daten_komplett)
print()

# statitische Auswertung für jede einzelne Shopping Mall
mall = list(daten["shopping_mall"].unique())

# eine for-Schleife um die Auswertung für jede Shopping Mall durchzuführen
for i in mall:
    mall_df = daten[daten["shopping_mall"] == i]
    mall_df = stats(mall_df)
    print("Die statistische Auswertung für die mall " + str(i) + ":")
    print(mall_df)
    print()
    # mall_df.to_excel(str(i)+"_stats_customer_shopping_data.xlsx")

"""
Es gab nur wenige auffällige Abweichungen zwischen den statistischen Werten
einzelner Shopping Malls gegenüber dem kompletten Datensatz. Diese Abweichungen
sind hauptsächlich bei den Modalwerten aufgetreten. Im folgenden werden diese
durch eine Visualisierung mittels Histogramm nochmal genauer betrachtet.
"""

# der Modus bei age, quantity und price variiert je mall
# deshalb werden die Modalwerte visualisiert um zu prüfen wie stark
# sich diese voneinander unterscheiden
# zunächst werden plots zu den Modalwerten des gesamten Datensatzes erstellt
spalten = ["age", "quantity","price"]
print("Histogramme des gesamten Datensatzes zu den Modalwerten für age, quantity und price.")
print()

# for-Schleife zur Erstellung dreier Histogramme
for i in spalten:
    plt.hist(daten[i])
    plt.title("Mode of column " + str(i))
    if np.issubdtype(daten[i].dtype, np.integer):
        min_val = daten[i].min()
        max_val = daten[i].max()
        plt.xticks(np.arange(min_val, max_val + 1, 1),size=6,rotation=45)
    plt.xlabel(i)
    plt.ylabel("Häufigkeit")
    plt.show()

# plots zu den Modalwerten einzelner Shopping Malls
# zunächst für die Spalte age
for i in mall:
    mall_age = daten[daten["shopping_mall"] == i]
    plt.hist(mall_age["age"])
    plt.title("Mode of column age for mall " + str(i))
    plt.xticks(range(16,72,1),rotation=45, size=4)
    plt.xlabel("age")
    plt.ylabel("Häufigkeit")
    plt.show()

"""
Gesamter Datensatz: 18-22 jährige und 65-69 jährige sind am häufigsten in allen Shopping Malls vertreten
Kaynyon: wie gesamter Datensatz
Forum Istanbull: 65-69 jährige stärker als 18-22 jährige, 2832 jährige auf Platz drei
Metrocity: wie gesamter Datensatz
Metropol AVM: 33-37 jährige auf Platz drei
Istinye Park: wie gesamter Datensatz
Mall of Istanbull: wie gesamter Datensatz
Emaar Square: 29-44 jährige bilden zusätzlich eine starke Gruppe, ebenso die 60-64 jährigen
Cevahir AVM: 18-33 jährige stark vertreten, ebenso 38-42 jährige
Viaport Outlet: 38-42 jährige stark vertreten
Zorlu Center: 34-38 jährige und 44-60 jährige stark vertreten

"""
# plots zu den Modalwerten einzelner Shopping Malls
# für die Spalte quantity
for i in mall:
    mall_quantity = daten[daten["shopping_mall"] == i]
    plt.hist(mall_quantity["quantity"])
    plt.title("Mode of column quantity for mall " + str(i))
    plt.xticks(range(0,6,1),rotation=45, size=8)
    plt.xlabel("quantity")
    plt.ylabel("Häufigkeit")
    plt.show()

"""
Der Modus für die quantity variiert durchaus zwischen einzelnen Shopping Malls. Allerdings
liegen alle untersuchten Werte so dicht zusammen, dass es für keine Shopping Mall eine 
klare Tendenz zu einer bestimmten Menge und gegen eine andere gibt.
"""

# plots zu den Modalwerten einzelner Shopping Malls
# für die Spalte price
for i in mall:
    mall_price = daten[daten["shopping_mall"] == i]
    plt.hist(mall_price["price"])
    plt.title("Mode of column price for mall " + str(i))
    plt.xticks(range(0,6000,250),rotation=45, size=8)
    plt.xlabel("price")
    plt.ylabel("Häufigkeit")
    plt.show()

"""
Die Visualisierung der Modalwerte für die Spalte price je Shopping Mall deckt sich mit der 
Visualisierung für den kompletten Datensatz. Am häufigsten kommen Preise zwischen
0 und 500 türkischen Lira vor. Deutlich weniger wurden Preise zwischen 500 und
1500 türkischen Lira bezahlt. Darüber hinaus wurden gab es kaum Bereitschaft 
höheren Preise zu bezahlen.
"""