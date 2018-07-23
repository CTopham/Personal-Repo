#Importing dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np

#Executing Chrome Driver for auto navigation to click links
def init_browser():
    executable_path = {'executable_path': r'C:\Users\Craig\Desktop\chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    #Looping through Nasa website and grabbing the latest title and news
    browser = init_browser()
    listings = {}
    #Setting url to website
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(2)
    #grabbing html
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #Grabbing title and paragraph text
    try:
        listings["News Title"] = soup.find(class_="content_title").get_text()
        xpath = '//*[contains(@class, "list_image")]'
        results = browser.find_by_xpath(xpath)
        img = results[0]
        img.click()
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        #opening new window with [paragraph]
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        listings["News p"] = soup.find(class_="wysiwyg_content").get_text()
    except AttributeError:
        print ("Error found")
        return listings