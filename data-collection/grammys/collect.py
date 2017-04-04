import urllib2, re
from urlparse import urlparse, parse_qs
from browser_manager import open_browser, scroll_to_bottom
from grammy_page_parser import construct_grammy_entries

GRAMMY_DATA_URL = 'https://www.grammy.com/awards'

def get_all_grammy_pages():
    """Return a list of grammy pages to scrape.  Each page represents a different year"""
    res = urllib2.urlopen(GRAMMY_DATA_URL)
    html = res.read()

    lines = [line.strip() for line in html.split("\n") if "More Winners" in line]
    urls = [re.search('\".*\"',line).group(0).replace('"','') for line in lines]
    return urls


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

def get_grammy_data():
    """Collects grammy data from all years into a single list"""
    grammy_data = []
    for url in get_all_grammy_pages():
        print 'Scraping %s'%url
        print parse_qs(urlparse(url).query)['year'][0]
        grammy_data.extend(scrape_sections(url))
    return grammy_data

# all_urls = get_all_grammy_pages()
# grammy_entries = scrape_sections(all_urls[0])
get_grammy_data()
