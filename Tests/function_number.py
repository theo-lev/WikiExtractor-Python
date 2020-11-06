import os

listeFichiers = os.listdir('../output')

def IteratorURL(url):
    i = 0
    for file in listeFichiers:
        if file[0:len(file)-6] == url:
            i+=1
    return(i)

IteratorURL('Comparison_between_Esperanto_and_Ido')