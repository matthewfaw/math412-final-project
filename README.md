# math412-final-project

A music data exploration project using Topological Data Analysis

# Dependencies

- [Spotipy](https://spotipy.readthedocs.io/en/latest/#installation)
  - Simple API for Spotify queries
- [Pickle](https://docs.python.org/3/library/pickle.html)
  - For object serialization/deserialization
- [Selenium](http://selenium-python.readthedocs.io/)
  - For crawling webpages to scrape data
- [urllib2](https://docs.python.org/2/library/urllib2.html)
  - For more simple web requests
- [re](https://docs.python.org/2/library/re.html)
  - For string parsing
- [time](https://docs.python.org/2/library/time.html)
  - To delay code execution over a time interval
- [urlparse](https://docs.python.org/2/library/urlparse.html)
  - To easily access query parameters of a URL

# API

## Grammy API (data_collection/grammys/)

### collect.py

- `get_grammy_data()`
  - Scrapes all years of Grammy award data
  - Output: 
      - list of Entry objects for all awards in all categories for all years

### csv_helper.py

- `serialize(array, filename)`
  - Saves the array to a CSV file
  - Inputs:
    - `array`: List of Entry objects
    - `filename`: name of the CSV file to save
  - Output:
    - DATETIMEfilename.csv in DEFAULT_DIRECTORY contains the contents of array
- `deserialize(filename)`
  - Loads the contents of filename into an array of Entry objects
  - Input:
    - `filename`: a filepath relative to DEFAULT_DIRECTORY
  - Output:
    - list of Entry objects
      
  
### filter.py

- `filter_by_categories(array, categories)`
  - Filter the array by categories
  - Inputs:
    - `array`: list of Entry objects
    - `categories`: list of categories to filter by
  - Output:
    - list of Entries for which the category field of each entry is in categories
- `convert_credits_to_names(array)`
  - Attempt to convert the credit field of each entry into the artist name
  - Inputs:
    - `array`: a list of Entry objects
  - Output:
    - same list of Entries, where the credits field of each entry now corresponds to an Artist name
    
## Spotify API

### queries.py

- `get_spotify_id(song_name, artist_name)`

- `vectorize_song(song_id)`

- `spotify_query(song_name, artist_name)`

### artists.py

- `get_all_track_ids(artist_name)`
  - Get the ids of all songs artist_name has released on Spotify
  - Input:
    - artist_name: Name of the artist, e.g. Arcade Fire
  - Output:
    - A dictionary in format { AlbumName: [song_ids] }

- `convert_map_vals_to_list(map)`
  - Converts the dictionary values into one array.  Useful in converting the song ids of get_all_track_ids into one list
  - Input:
    - a dictionary
  - Output:
    - a list of the values of that dictionary
