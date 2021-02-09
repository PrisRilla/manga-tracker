# Helper functions
import json
from urllib.parse import urlparse


def url_check(url):
	min_attr = ('scheme', 'netloc', 'path')
	try:
		result = urlparse(url)
		if result.scheme and result.netloc and result.path:
			return True
		else:
            		return False
	except:
		return False


def read_json(data):
	records = data["sites"]["tracked"]
	d = {}
	last_id = 0
	for r in records:
		if r["title"] not in d:
			d[r["title"]] = [r["links"]["root"]]
		if r["entryId"] > last_id:
			last_id = r["entryId"] 
	print("Below are the current tracked manga title(s) and link(s):")
	print(d)
	print(last_id)

	return last_id

def new_record(last_id):
	"""Prompt user to input data to create new record for tracking."""
	entryId = last_id + 1
	root_link = input("Enter main/root site to track: ")
	if root_link[-1] != '/':
		root_link = root_link + '/'
	print(root_link)
	print(url_check(root_link))	
	anchor = input("Which chapter did you read up until? ")

	# To scrape
	# title
	# recent_read_chapter
	# recent_read_release_date
	print(entryId, root_link, anchor)


def delete_record():
	"""Prompt user to select record to not track."""
	pass


def validate_link(link):
	"""Check if link already added and if the link is valid."""
	pass



if __name__=="__main__":
	with open('/Users/priscillacheng/Documents/projects/manga-tracker/src/data.json') as f:
        	data = json.load(f)
	last_id = read_json(data)
	new_record(last_id)
	#primary = request_input()
	#validate_link(primary)
