import pandas as pd

# Scraping tables of Simpsons episodes from wikipedia
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
#print(simpsons[1])

# Use pandas and a for loop to download all CSV links on a page and scrape them

footie = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')


# Rename columns

footie.rename(columns={"FTHG": "home_goals",
                       "FTAG": "away_goals"}, inplace=True)
print(footie)

# Extract tables from PDF to CSV

import camelot

tables = camelot.read_pdf('foo.pdf', pages="1")


tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')