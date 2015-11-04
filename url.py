'''This function is supposed to create a urld that returns search results from arxiv
Input
=====
Can only be a string!
kind can be 'all' for all
            'au' for authors
            'abs' for abstracts

'''


def create(method='search_query', kind='all', query='electron', start='0', number='10'):
   ''' if query.find(' ')==-1:
        break
    else:
        '''
    
    url='http://export.arxiv.org/api/query?'+ method +'='+ kind +':'+ query1 +'&start='+ start +'&max_results='+ number
    return(url)
