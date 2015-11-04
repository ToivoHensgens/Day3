# The main file of our master project of total awesomeness
# that does some ArXiv queries and results plotting or something

# Start by setting the mood
print(" ")
print("Once upon a time")

# Next import all the relevant stuffs
import searchdef
import resultsdef
import url
#import process
import urllib
#import ProcessWebPage
#import ProcessOutputData
print(" ")
print("we imported some things and classes")

# And create the SEARCH and RESULTS objects
SEARCH = searchdef.searchclass()
RESULTS = resultsdef.resultsclass()
print(" ")
print("and made some data objects that store the infos")

# Feed the SEARCH by adding relevant parameters
SEARCH.set_author('Akhmerov')
print(" ")
print("such as the following:")
print("Author: " + SEARCH.get_author())

# Call Lucas's superduper URL create script
searchURL = url.create()#kind='author',query=SEARCH.get_author())
print(" ")
print("creating this superduper URL:")
print(searchURL)

# that allows us to overload the ArXiv server with our queries!
PAGE = urllib.urlopen(searchURL).read()
print(" ")
print("that we look up")
#ProcessWebPage.PROCESSTHETHINGALREADY() #Which puts all the things in the results script
print(" ")
print("and we process the hell out of!")
print(" ")
