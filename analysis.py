#%matplotlib inline
import matplotlib.pyplot as plt
import feedparser
import urllib

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

def count_words_abstract(url, entry_number=0):
    """counts the number of words in the abstract 
    
       default is that it takes the first hit of the search query 
       otherwise change entry_number, useful in for loop :)
    """
    abstract = extract_abstract(url, entry_number)
    words = abstract.split()
    return len(words)

def init_figure(size_x,size_y):
    plt.figure(figsize=(size_x,size_y))
    
def plot_histogram(data, bins, size_x=3,size_y=3):
    init_figure(size_x, size_y)
    n, bins, patches = plt.hist(data, bins, range=[0,max(data)], normed=False, facecolor='green')
    plt.xlabel("Number of words")
    plt.ylabel("Number of abstracts")
    plt.show()

def words_forall_abstarcts(url):
    n_max   = extract_totalentries(url)
    n_words = []
    for i in range(n_max):
        n_words.append(count_words_abstract(url, i))
    return n_words
