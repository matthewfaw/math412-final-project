from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time

def open_browser(url):
    """Opens Firefox browser, and loads the requested url"""
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

def scroll_to_bottom(driver, pauseTime):
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

