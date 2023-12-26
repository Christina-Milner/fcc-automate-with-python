from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pandas as pd

# This stuff is to prepare for executable
from datetime import datetime
import os
import sys

# application_path = os.path.dirname(sys.executable)

# Following block is yoinked off here as video instructions (above) no longer work
# https://stackoverflow.com/questions/404744/determining-application-path-in-a-python-exe-generated-by-pyinstaller
# This puts the file in G: rather than the subdirectory I want but ok, problem for another day

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))


# "If we don't put datetime into the file name, we don't know what day it's from"
# Well no we do because it shows you when the file was created, but the bigger problem is overwriting the previous one, no? 

now = datetime.now()
# check format at strftime.org
day_month_year = now.strftime("%d%m%Y")



# I am absolutely, positively, over-my-dead-body not scraping The Sun

# website = "https://www.theguardian.com/food"
website = "https://www.nytimes.com/international/"
path = "F:\Downloads\chromedriver-win64"

#headless mode

options = Options()
options.add_argument("--headless=new")
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(website)


# This is deprecated in the video, see:
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L12-L13
# Fix for browser immediately closing: https://www.youtube.com/watch?v=ijT2sLVdnPM

# Oof, unfortunately the node tree for the guardian does not play nice
# li > div > div > div > div > div > div > h3 > div > span, the latter 3 are the interesting parts smh
# buuut since hte last two are rammed inside the h3 for reasons, just grabbing h3 should work?
'''
hthrees = driver.find_elements(by="xpath", value="//h3")
links = driver.find_elements(by="xpath", value="//li/div/div/div/a").get_attribute("href")

for hthree in hthrees:
    info = hthree.find_element(by="xpath", value='./span').text
'''
    
# From the video: //div[@class="teaser__copy-container"]/a/h2
# put that in a for loop through the parent elements



#  Exporting to CSV
# Going to go find myself a website that more closely matches what he is doing    

titles = []
subtitles = []
links = []

sections = driver.find_elements(by="xpath", value='//section[contains(@class, "story-wrapper")]')



for section in sections:
    try:
        title = section.find_element(by="xpath", value="./a/div/div/p[contains(@class, 'indicate-hover')]").text
        subtitle = section.find_element(by="xpath", value="./a/div/p[contains(@class, 'summary-class')]").text
        link = section.find_element(by="xpath", value="./a").get_attribute("href")
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
        print("Try block actually ran")
    except:
        print("Issue with this section!")
        continue

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}

df_headlines = pd.DataFrame(my_dict)

file_name = f'/headline-{day_month_year}.csv'


final_path = os.path.join(application_path, file_name)
print(file_name, final_path)
# To avoid issues with different OS using different slashes
df_headlines.to_csv(final_path)

driver.quit()

# Ok a lot of those xpaths aren't working, but I'm getting 15 headlines or so in a CSV, good enough for now!
# Huh, for me it's numbered and in separate columns and for him it's not. (Edit: This is because I'm opening it in Excel durrr)

# Headless mode: Syntax provided is deprecated, see https://stackoverflow.com/questions/75401348/selenium-chrome-driver-headless-mode-not-working

# Automate this to run once per day, like when you turn on the PC
# Convert .py file to executable
# Some steps to prepare first (modules and file path changes above)
# Install pyinstaller
# pyinstaller --onefile <file name>
# (Going to put that stuff on gitignore but this generates a build and dist folder)

# Schedule with crontab
# Not a thing on Windows but I'll note it down anyway
# crontab -e
# go to crontab.guru to make expression, be very careful that you don't set stuff up to run once per minute or something
# Type into window, drop in executable to get path
# Press Esc, colon, wq, press enter, give permission
# crontab -l to verify

# Create pivot tables with Python
# -> pivot-table.py

