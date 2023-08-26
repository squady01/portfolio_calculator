import csv
import requests
import pandas as pd
import time
from datetime import datetime
import os


# initialiser une liste pour stocker les résultats
results = []
portfolio_value = 0

# ouvrir le fichier CSV contenant les informations du portefeuille
with open('portfolio.csv') as portfolio_file:
    portfolio_reader = csv.reader(portfolio_file)
    next(portfolio_reader)  # sauter la ligne d'entête
    # pour chaque ligne du fichier CSV (chaque cryptomonnaie dans le portefeuille)
    for row in portfolio_reader:
        ticker, amount = row
        # utiliser l'API de CoinGecko pour récupérer le prix de la cryptomonnaie
        url = f'https://api.coingecko.com/api/v3/coins/{ticker}'
        response = requests.get(url)
        data = response.json()
        if "name" in data and "market_data" in data:
            name = data['name']
            price = data['market_data']['current_price']['eur']
            # calculer la valeur de la cryptomonnaie dans le portefeuille
            holding_value = float(amount) * float(price)
            portfolio_value += holding_value
    
            print(f'{ticker}: {amount} @ {price}€ = {holding_value}€')
            # ajouter les résultats à la liste            
            results.append([name, ticker, price, amount, holding_value])
        else:
            print("{}: {}".format(ticker, data))

        time.sleep(15)


# convertir la liste en dataframe pandas
df = pd.DataFrame(results, columns=['Name', 'Ticker', 'Price', 'Amount', 'Holding Value'])
df = df.sort_values(by='Holding Value', ascending=False)
# ajouter la ligne de total
df.loc['Total', 'Holding Value'] = df['Holding Value'].sum()

now = datetime.now()

# Ajouter la date et l'heure de création du fichier dans un nouvelle colonne "Created"
df['Created'] = now.strftime("%Y-%m-%d %H:%M:%S")


# Obtenir la date et l'heure actuelles pour nommer le fichier Excel
filename = "{}.xlsx".format(now.strftime("%Y-%m-%d %H_%M_%S"))

if not os.path.exists("output"):
    os.mkdir("output")


#exporter le dataframe dans un fichier Excel
df.to_excel("output/" + filename, index=False)

