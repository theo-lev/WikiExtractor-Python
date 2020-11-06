def getConvertUrl():
    listConvertUrl = []
    totalUrl = 0
    names = open("./spiders/wikiurl.txt").readlines()
    for namePage in names:
        listConvertUrl.append(('https://en.wikipedia.org/wiki/'+namePage).rstrip("\n"))
        totalUrl += 1
        print(str(totalUrl) + ' lines convert in url.')
    return listConvertUrl
