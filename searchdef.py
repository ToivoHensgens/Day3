# searchdef: contains the class definition for the search class

class searchclass(object):
    
    def __init__(self,title=[],author=[],abstract=[],date=[]):
        self.title = title
        self.author = author
        self.abstract = abstract
        self.date = date
        
    # All of the set functions!
    def set_title(self,new):
        self.title = new
    def set_author(self,new):
        self.author = new
    def set_abstract(self,new):
        self.abstract = new
    def set_date(self,new):
        self.date = new
        
    # All of the get functions!
    def get_Nres(self):
        return self.Nres
    def get_author(self):
        return self.author
    def get_abstract(self):
        return self.author
    def get_date(self):
        return self.author
    