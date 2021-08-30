import requests
import os
from bs4 import BeautifulSoup as soup
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time

executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape():
    browser = Browser('chrome', **executable_path, headless=False)
    
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
         "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

    url = 'https://mars.nasa.gov/news/'
    
    browser.visit(url)
    html = browser.html
    soup = soup(html, 'html.parser')
   