import json
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup




def scrape_link(links_to_scrape):
	"""Scrape based on root"""
	
	# Mangatx
	test_site = links_to_scrape[0]
	req = Request(test_site, headers={'User-Agent': 'Mozilla/5.0'})
	web_byte = urlopen(req, timeout=10).read()
	webpage = web_byte.decode('utf-8')
	soup = BeautifulSoup(webpage, "html.parser")
	print(soup.prettify())
	
	all_site_links = []
	for link in soup.find_all('a'):
		if test_site in link.get('href') and test_site != link.get('href'):
			if "comment-page" not in link.get('href') and link.get('href') not in all_site_links:
				all_site_links.append(link.get('href'))
	print(all_site_links, len(all_site_links))

if __name__=="__main__":
	with open('/Users/priscillacheng/Documents/projects/manga-tracker/src/data.json') as f:
		data = json.load(f)
	links_to_scrape = []
	for r in data["sites"]["tracked"]:
		links_to_scrape.append(r["links"]["base"])
	scrape_link(links_to_scrape)
