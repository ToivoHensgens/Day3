# Resultsdef: contains the class definition for the results class

class resultsclass(object):
    
    def __init__(self,Nres=0,titlelist=[],authorlist=[],abstractlist=[],datelist=[]):
        self.Nres = Nres
        self.titleslist = titlelist
        self.authorlist = authorlist
        self.abstractlist = abstractlist
        self.datelist = datelist
        
    # All of the set functions!
    def set_Nres(self,new):
        self.Nres = new
    def set_titlelist(self,new):
        self.titlelist = new
    def set_authorlist(self,new):
        self.authorlist = new
    def set_abstractlist(self,new):
        self.abstractlist = new
    def set_datelist(self,new):
        self.datelist = new
        
    # All of the get functions!
    def get_Nres(self):
        return self.Nres
    def get_titlelist(self):
        return self.titlelist
    def get_authorlist(self):
        return self.authorlist
    def get_abstractlist(self):
        return self.authorlist
    def get_datelist(self):
        return self.authorlist