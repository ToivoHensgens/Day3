import feedparser

def extract_totalentries(url):
	"""This function extracts the number of results in the search query

	"""
	d = feedparser.parse(url)
	return len(d["entries"])


