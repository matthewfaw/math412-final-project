import urllib2, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time

class Entry:
    def __init__(self, year, category, nominee_work, credits):
        self.year = year
        self.category = category
        self.nominee_work = nominee_work
        self.credits = credits

def open_browser(url):
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

def scroll_to_bottom(driver, pauseTime):
    currHeight = driver.execute_script("return document.body.scrollHeight")
     
    while True:
        print currHeight
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(pauseTime)
        nextHeight = driver.execute_script("return document.body.scrollHeight")
        if nextHeight == currHeight:
            break
        currHeight = nextHeight

def get_grammy_field(entry, field):
    return entry.find_element_by_xpath("//td[@class='views-field views-field-"+field+"']").text

def construct_grammy_entries(entries):
    grammy_entries = []
    for entry in entries:
        year = get_grammy_field(entry, 'year')
        category = get_grammy_field(entry, 'category-code')
        nominee_work = get_grammy_field(entry, 'field-nominee-work')
        credits = get_grammy_field(entry, 'field-nominee-extended')

        e = Entry(year, category, nominee_work, credits)
        grammy_entries.append(e)

    return grammy_entries

# https://paulhoganreid.wordpress.com/2015/01/19/using-python-and-selenium-to-scrape-an-infinitely-scrolling-table/
def scrape_sections(url):
    driver = open_browser(url)
    
    scroll_to_bottom(driver, 3)

    entries = driver.find_elements_by_xpath("//table[@class='views-table cols-4']/tbody/tr")
    # entries = table.find_elements_by_tag_name('tr')
    
    grammy_entries = construct_grammy_entries(entries)

    driver.quit()
           
    return grammy_entries

GRAMMY_DATA_URL = 'https://www.grammy.com/awards'

res = urllib2.urlopen(GRAMMY_DATA_URL)
html = res.read()

lines = [line.strip() for line in html.split("\n") if "More Winners" in line]
urls = [re.search('\".*\"',line).group(0).replace('"','') for line in lines]

print urls

scrape_sections('https://www.grammy.com/nominees/search?year=2015')
