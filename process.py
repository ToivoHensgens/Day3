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

def extract_date(url, entry_number, layer=0):
    """This function extract the date that the paper is submitted to Arxiv
    
    Layer specifies the year/month/day ect, default is year
    0: year
    1: month
    2: day
    """
    
    d = feedparser.parse(url)
    return d['entries'][entry_number]['updated_parsed'][0]

