import feedparser

def extract_totalentries(url):
	"""This function extracts the number of results in the search query contained in the url

	"""
	d = feedparser.parse(url)
	return len(d["entries"])


def extract_abstract(url, entry_number):
	"""This function extract the entry_number-th abstract of the search query contained in the url

	""" 
	d = feedparser.parse(url)
	return d["entries"][entry_number]["summary"] 

def extract_title(url, entry_number):
	"This function is cool"

	d = feedparser.parse(url)
	return d["entries"][entry_number]["title"]
