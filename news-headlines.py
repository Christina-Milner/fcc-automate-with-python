from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# I am absolutely, positively, over-my-dead-body not scraping The Sun

website = "https://www.theguardian.com/food"
path = "F:\Downloads\chromedriver-win64"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(website)


# This is deprecated in the video, see:
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L12-L13
# Fix for browser immediately closing: https://www.youtube.com/watch?v=ijT2sLVdnPM

# Oof, unfortunately the node tree for the guardian does not play nice
# li > div > div > div > div > div > div > h3 > div > span, the latter 3 are the interesting parts smh
# buuut since hte last two are rammed inside the h3 for reasons, just grabbing h3 should work?

hthrees = driver.find_elements(by="xpath", value="//h3")
links = driver.find_elements(by="xpath", value="//li/div/div/div/a").get_attribute("href")

# From the video: //div[@class="teaser__copy-container"]/a/h2
# put that in a for loop through the parent elements

for hthree in hthrees:
    info = hthree.find_element(by="xpath", value='./span').text

#  Exporting to CSV
    