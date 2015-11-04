%matplotlib inline
import matplotlib.pyplot as plt
import feedparser
import process

def count_words_abstract(url, entry_number=0):
    """counts the number of words in the abstract 
    
       default is that it takes the first hit of the search query 
       otherwise change entry_number, useful in for loop :)
    """
    abstract = extract_abstract(url, entry_number):
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
    n_max = extract_totalentries(url)

    for i in range(n_max):
        n_words.append(count_words_abstract(url, i))
    