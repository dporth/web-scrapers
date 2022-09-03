# USCF Web Scraper
## Introduction
This web scaper will retrieve the USCF regular game ratings for USCF numbers. The output will be saved to a csv named "uscf_player_ratings.csv" in the directory that this program is executed from.

## Usage
Install this application's dependencies from within the current directory by using the command:
`pip install -r requirements.txt`

Run the web scraper by replacing the placerholder with at least one USCF number, then execute the command:
`python uscf_scraper.py <uscf number>`

For example...
`python uscf_scraper.py 12743305 13145890 14744935 12641216 13648621 12852765 12847250 12528459 13493815 16113717`
