import urllib2, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time

GRAMMY_DATA_URL = 'https://www.grammy.com/awards'

class Entry:
    def __init__(self, year, category, nominee_work, credits):
        self.year = year
        self.category = category
        self.nominee_work = nominee_work
        self.credits = credits
    def __str__(self):
        return "Year: %s\nCategory: %s\nNominee Work: %s\nCredits: %s" % (self.year,self.category,self.nominee_work,self.credits)
    def __repr__(self):
        return str(self)

def get_all_grammy_pages():
    """Return a list of grammy pages to scrape.  Each page represents a different year"""
    res = urllib2.urlopen(GRAMMY_DATA_URL)
    html = res.read()

    lines = [line.strip() for line in html.split("\n") if "More Winners" in line]
    urls = [re.search('\".*\"',line).group(0).replace('"','') for line in lines]
    return urls

def _open_browser(url):
    """Opens Firefox browser, and loads the requested url"""
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

def _scroll_to_bottom(driver, pauseTime):
    """
    Given the driver controlling the currently opened web page,
    scrolls to the bottom of the page

    pauseTime is the amount of time the driver will wait between successive scroll events
    """
    currHeight = driver.execute_script("return document.body.scrollHeight")
     
    while True:
        print currHeight
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(pauseTime)
        nextHeight = driver.execute_script("return document.body.scrollHeight")
        if nextHeight == currHeight:
            break
        currHeight = nextHeight

def _get_grammy_field(entry, field):
    """Gets the grammy field from the requested table entry in the web page"""
    t =  entry.find_element_by_xpath(".//td[@class='views-field views-field-"+field+"']").text
    return t

def _construct_grammy_entries(entries):
    """
    Given a list of Grammy entries in the HTML table,
    construct the Grammy Entry objects, and return the objects as a list
    """
    grammy_entries = []
    for i in range(0,len(entries)):
        entry = entries[i]
        year = get_grammy_field(entry, 'year')
        category = get_grammy_field(entry, 'category-code')
        nominee_work = get_grammy_field(entry, 'field-nominee-work')
        credits = get_grammy_field(entry, 'field-nominee-extended')
        print category

        e = Entry(year, category, nominee_work, credits)
        grammy_entries.append(e)

    return grammy_entries

# https://paulhoganreid.wordpress.com/2015/01/19/using-python-and-selenium-to-scrape-an-infinitely-scrolling-table/
def scrape_sections(url):
    """Scrapes the requested url for grammy data. Returns a list of all grammy entries on the page"""
    driver = open_browser(url)
    scroll_to_bottom(driver, 3)
    table = driver.find_element_by_xpath("//table[@class='views-table cols-4']/tbody")
    entries = table.find_elements_by_tag_name('tr')

    grammy_entries = construct_grammy_entries(entries)
    driver.quit()
           
    return grammy_entries

all_urls = get_all_grammy_pages()

grammy_entries = scrape_sections(all_urls[0])
