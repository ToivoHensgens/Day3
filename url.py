'''This function is supposed to create a url that returns search results from arxiv
Input
=====
Can only be a string!
kind can be 'all' for all
            'au' for authors
            'abs' for abstracts

'''
def create(method='search_query', kind='all', query='electron photon', start='0', number='10'):    
    url='http://export.arxiv.org/api/query?'+ method +'='+ kind +':'+ query.replace(' ','+AND+'+kind+':') +'&start='+ start +'&max_results='+ number
    return(url)
