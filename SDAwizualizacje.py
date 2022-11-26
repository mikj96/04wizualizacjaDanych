"""
WIZUALIZACJE DANYCH - ZADANIA SDA

Zadanie 1
Wczytaj ze zbioru danych ML-datasets https://github.com/matzim95/ML-datasets zeszyt ves-usd.csv i pokaż zależność
boliwara od dolara amerykańskiego.

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data = pd.read_csv('https://raw.githubusercontent.com/matzim95/ML-datasets/master/ves-usd.csv', index_col = 'Date', parse_dates=True)

fig, ax = plt.subplots()
ax.plot(data['Rate'])
plt.show()


Zadanie 2
Skorzystaj z parametrów poznanych na slajdzie 14 i 15 i opisz wykres z poprzedniego zadania.
- tytuł wykresu i osi
- obrót napisów i osi


import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data = pd.read_csv('https://raw.githubusercontent.com/matzim95/ML-datasets/master/ves-usd.csv', index_col = 'Date', parse_dates=True)

fig, ax = plt.subplots()
ax.plot(data['Rate'])
ax.set_title('USD/VED 2019')
ax.set_xlabel('Date')
ax.set_ylabel('Conversion rate')
ax.grid()
ax.xaxis.set_tick_params(rotation=90)
ax.yaxis.set_tick_params(rotation=0)
plt.show()


Zadanie 3
Dokonaj analizy danych zbioru medali (olympic.csv https://github.com/matzim95/ML-datasets) i wykonaj wykres słupkowy
pokazujący ile medali zdobył dany kraj. Za pomocą kolorów oznacz czy medal był złoty, srebrny czy brązowy.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data = pd.read_csv('https://raw.githubusercontent.com/matzim95/ML-datasets/master/olympic.csv')
fig, ax = plt.subplots()
data = data.dropna()
data = data[['Medal','NOC']]


bronze = []
silver = []
gold = []
for medal in data['Medal']:
    for country in data['NOC']:
        if medal == 'Bronze':
            bronze.append(country)
        elif medal == 'Silver':
            silver.append(country)
        elif medal == 'Gold':
            gold.append(country)



Zadanie 4
Korzystając ze zbioru medali, stwórz wykres punktowy pokazujący zależność wzrostu, wagi i liczby zdobytych przez
zawodników medali na igrzyskach.


Zadanie 5
Wczytaj zbiór co2 i wyświetl wykres punktowy wartości co2.

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data = pd.read_csv('https://raw.githubusercontent.com/matzim95/ML-datasets/master/co2.csv',  parse_dates= True)
print(data)
fig, ax = plt.subplots()
ax.scatter(x = data['Decimal Date'], y = data['Interpolated'], marker = '.', color = 'r')
ax.xaxis.set_tick_params(rotation=90)
ax.set_title('Zmiana CO2 w czasie')
ax.set_xlabel('Date')
ax.set_ylabel('CO2')
plt.show()


Zadanie 6
Wykonaj wykresy boxplot, violinplot oraz swarmplot dla zbioru danych olimpijczyków za pomocą biblioteki seaborn.
"""

