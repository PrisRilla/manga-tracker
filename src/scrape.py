import json
from bs4 import BeautifulSoup




def scrape_link():
	pass

if __name__=="__main__":
	with open('/Users/priscillacheng/Documents/projects/manga-tracker/src/data.json') as f:
		data = json.load(f)
	links_to_scrape = []
	for r in data["sites"]["tracked"]:
		links_to_scrape.append(r["links"]["root"])
	print(links_to_scrape)
