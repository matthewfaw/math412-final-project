from grammy_entry import Entry

def _get_grammy_field(entry, field):
    """Gets the grammy field from the requested table entry in the web page"""
    t =  entry.find_element_by_xpath(".//td[@class='views-field views-field-"+field+"']").text
    return t

def construct_grammy_entries(entries):
    """
    Given a list of Grammy entries in the HTML table,
    construct the Grammy Entry objects, and return the objects as a list
    """
    grammy_entries = []
    for i in range(0,len(entries)):
        entry = entries[i]
        year = _get_grammy_field(entry, 'year')
        category = _get_grammy_field(entry, 'category-code')
        nominee_work = _get_grammy_field(entry, 'field-nominee-work')
        credits = _get_grammy_field(entry, 'field-nominee-extended')
        print category

        e = Entry(year, category, nominee_work, credits)
        grammy_entries.append(e)

    return grammy_entries
