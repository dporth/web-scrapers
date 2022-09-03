import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

def fetch_ratings(id):
	print(f"Fetching rating for USCF number {id} at http://www.uschess.org/msa/MbrDtlRtgSupp.php?{id}")
	return requests.get(f"http://www.uschess.org/msa/MbrDtlRtgSupp.php?{id}")
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("ERROR: Please replace <uscf number> with one or more valid USCF numbers.")
	else:
		name = []
		date = []
		regular_rating = []
		for each in sys.argv[1:]:
			page = fetch_ratings(each)
			soup = BeautifulSoup(page.content, 'html.parser')
			table_container = soup.find(class_='topbar-middle')
			tables_outer = table_container.find_all('table')
			player_info = tables_outer[1]
			player_name = player_info.find_all('tr')[0].find('b')
			ratings_table = player_info.find_all('tr')[1].find_all('table')[2]
			rating_elements = ratings_table.find_all('tr')[1:]
			for element in rating_elements:
				rating_values = element.find_all('td')
				date.append(rating_values[1].text.strip())
				regular_rating.append(rating_values[2].text.strip())
				name.append(player_name.text.strip())
		d = {'name': name, 'date': date, 'regular_rating': regular_rating}

		df = pd.DataFrame(data = d)
		df = df.pivot(index='name', columns='date', values='regular_rating')
		df.to_csv("./uscf_player_ratings.csv")

