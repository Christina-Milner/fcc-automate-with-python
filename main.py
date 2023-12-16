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


# Scraping
# HTML Tags & Elements
# XPath (compare this to BeautifulSoup later?)
# This appears to be multiple videos stapled together into one and I am not sure they were meant to go together in this order
# // div/text() gets the text from a div ok
# //p[1] <- gets first p element, note 1-indexing
# //div[@class="full-script"]
# //p[(@class="plot") or (@class="plot2")]
# //p[contains(@class, "plot")]

# Special characters
# / Selects children from node set on left side
# // Matching node set is at any level in the document

# .. parent node
# * wildcard as usual
# ./* all children nodes of the current context
# @ select an attribute
# () Grouping an expression
# [n] Indicates that node of index n should be selected

# Selenium

# chromedriver.chromium.org, download ChromeDriver
# pip install selenium
# continues in news-headlines.py

