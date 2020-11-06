import os


def getConvertUrl():
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileName = os.path.abspath(fileDir + '/spiders/wikiurl.txt')
    listConvertUrl = []
    totalUrl = 0
    names = open(fileName).readlines()
    for namePage in names:

        namePage.replace("&", "%26")
        namePage.replace("Home_Owners'_and_Civic_Associations", "homeowner_associations_and_civic_associations")

        listConvertUrl.append(('https://en.wikipedia.org/wiki/' + namePage).rstrip("\n"))
        totalUrl += 1
        print(str(totalUrl) + ' lines convert in url.')
    return listConvertUrl
