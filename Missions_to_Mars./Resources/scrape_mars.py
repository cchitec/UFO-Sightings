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


def mars_news(browser):

   
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    
    articles = soup.find("div", class_='list_text')
    # title
    news_title = articles.find(class_='content_title').get_text()
    # Find paragraph text
    news_para = articles.find(class_='article_teaser_body').get_text()

    return news_title, news_para

def featured_image(browser):
  
    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(jpl_url)

    results = browser.find_by_text(' FULL IMAGE')
    results.click()

    jpl_html= browser.html
    jpl_soup = soup(jpl_html, 'html.parser')
    # Find the featured image
    try:
        featured_image = soup.find_all('img')[1]['src']

    except AttributeError:
        return None

    featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{featured_image}'
    # Link to featured image
    return featured_image_url

def mars_facts():
    try:
        mars_df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    # assign columns and set index of dataframe
    mars_df.columns = ['Description', 'Mars']
    mars_df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")
