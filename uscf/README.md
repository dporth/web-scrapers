# USCF
The scrapers in this directory are used to scrape data from United State Chess Federation related webpages.

# Getting Started
## Testing
To test the provided scrapers run the following command in this directory:

`python -m pytest`

## Usage
Before you can use any of these scrapers you must install their dependencies. To do so run the following command:
`pip install -r requirements.txt`

## Player History Scraper
This web scaper will retrieve the USCF regular game ratings for USCF numbers. The output
will be saved to a csv named "uscf_player_ratings.csv" in the directory that this program is executed from.

This web scraper is located in the `./player_rating_history` directory.

Run the web scraper by replacing the placerholder with at least one USCF number, then execute the command:
`python ./player_rating_history/uscf_scraper.py <uscf number>`

For example...
`python ./player_rating_history/uscf_scraper.py 12743305 13145890 14744935 12641216 13648621 12852765 12847250 12528459 13493815 16113717`


## Player Existence Scraper
These web scapers will indicate if the provided player ID is a valid USCF numbers. If it is indicated that the
player ID is valid then the player "exists".

These web scrapers are located in the `./player_existence` directory.

### UscfPlayerIdValidatorQueryString
This validator is a specific type of player existence scraper. It uses an HTTP/HTTPS URL with a query string to request
the HTML page to scrape.

To use this scraper import it:
```
from player_existence.UscfValidators import UscfPlayerIdValidatorQueryString

query_string_lookup_base_url='https://www.uschess.org/datapage/player-search.php'
query_string_failed_validation_regex = 'Players found: 0'

validator = UscfPlayerIdValidatorQueryString(
    failed_validation_regex=query_string_failed_validation_regex,
    lookup_base_url='query_string_lookup_base_url'
)
validator.validId(player_id='12345')
```

### UscfPlayerIdValidatorFormData
This validator is a specific type of player existence scraper. It uses an HTTP/HTTPS URL with form data to request
the HTML page to scrape.

To use this scraper import it:
```
from player_existence.UscfValidators import UscfPlayerIdValidatorFormData

form_data_lookup_base_url='https://www.uschess.org/assets/msa_joomla/MbrLst.php'
form_data_failed_validation_regex = 'Sorry - No matches were found for'

validator = UscfPlayerIdValidatorFormData(
    failed_validation_regex=form_data_failed_validation_regex,
    lookup_base_url='form_data_lookup_base_url'
)
validator.validId(player_id='12345')
```