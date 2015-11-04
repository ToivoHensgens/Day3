import url

def test_create():
    assert url.create(method='search_query', kind='all', query1='electron', start='0', number='10')=='http://export.arxiv.org/api/query?search_query=all:electron&start=10&max_results=10'
