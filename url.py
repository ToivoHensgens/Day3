'''This function is supposed to create a url that returns search results from arxiv
Input
=====
Can only be a string!
kind1/2 can be 'all' for all
                'ti' for title
                'au' for authors
                'abs' for abstracts
start defines what is the index of the first result.
number defines the number of results obtained starting from the start index.
query is the search term and can be multiple words.
'''
import time

def create(method='search_query', kind1='all', kind2='bla', query1='akhmerov sticlet', query2='electron photon',start='0', number='100', beginning='2001-01-01', end=time.strftime('%Y-%m-%d')):    
    if kind2=='bla':
        url='http://export.arxiv.org/api/query?'+ method +'='+ kind1 +':'+ query1.replace(' ','+AND+'+kind1+':') +'+AND+'+'submittedDate:['+ beginning.replace('-','') +'0000+TO+'+ end.replace('-','') +'0000]' +'&start='+ start +'&max_results='+ number
    else:
        url='http://export.arxiv.org/api/query?'+ method +'='+ kind1 +':'+ query1.replace(' ','+AND+'+kind1+':') +'+AND+'+kind2+':'+ query2.replace(' ','+AND+'+kind2+':') +'+AND+'+'submittedDate:['+ beginning.replace('-','') +'0000+TO+'+ end.replace('-','') +'0000]' +'&start='+ start +'&max_results='+ number
    return(url)