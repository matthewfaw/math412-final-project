from urlparse import urlparse, parse_qs
from scrape import get_all_grammy_pages, scrape_sections
from csv_helper import serialize, deserialize

def get_grammy_data():
    """Collects grammy data from all years into a single list"""
    grammy_data = []
    for url in get_all_grammy_pages():
        print 'Scraping %s'%url
        print parse_qs(urlparse(url).query)['year'][0]
        grammy_data.extend(scrape_sections(url))
    return grammy_data

# grammies = get_grammy_data()
# serialize(grammies, 'GRAMMIES.csv')
