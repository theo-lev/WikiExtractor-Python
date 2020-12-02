import os
from definitions import ROOT_DIR


def getConvertUrl():
    fileName = os.path.join(ROOT_DIR, 'Wikipedia/spiders/wikiurl.txt')  # The name of the file
    listConvertUrl = []  # Creation of a list with all the URLs
    totalUrl = 0

    file = open(fileName, 'r', encoding='utf-8')
    names = file.readlines()

    for namePage in names:
        listConvertUrl.append(('https://en.wikipedia.org/wiki/' + namePage).rstrip("\n"))  # We delete all the "\n"
        totalUrl += 1
        print(str(totalUrl) + ' lines convert in url.')
    return listConvertUrl
