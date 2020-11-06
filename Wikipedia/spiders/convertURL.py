import os

def getConvertUrl():
    fileDir = os.path.dirname(os.path.realpath('__file__'))         #The path of the file
    fileName = os.path.abspath(fileDir + '/spiders/wikiurl.txt')    #The name of the file
    listConvertUrl = []                                             #Creation of a list with all the URLs
    totalUrl = 0
    names = open(fileName).readlines()                              #We read all the lines in wikiurl
    for namePage in names:

        namePage.replace("&", "%26")                                #A '&' in the URL provock an error
        namePage.replace("Home_Owners'_and_Civic_Associations", "homeowner_associations_and_civic_associations")

        listConvertUrl.append(('https://en.wikipedia.org/wiki/' + namePage).rstrip("\n")) #We delete all the "\n"
        totalUrl += 1
        print(str(totalUrl) + ' lines convert in url.')
    return listConvertUrl
