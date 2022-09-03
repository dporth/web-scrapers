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

Run the web scraper by replacing the placerholder with at least one USCF number, then execute the command:
`python ./player_rating_history/uscf_scraper.py <uscf number>`

For example...
`python ./player_rating_history/uscf_scraper.py 12743305 13145890 14744935 12641216 13648621 12852765 12847250 12528459 13493815 16113717`


## Player Existence Scraper
In this directory you can import the validator with `from player_existence.ValidateUscfNumber import UscfPlayerIdValidatorQueryString` or `from player_existence.ValidateUscfNumber import UscfPlayerIdValidatorFormData`