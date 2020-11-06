import os

listeFichiers = os.listdir('../output')

def IteratorURL(url):
    i = 0
    for file in listeFichiers:
        if file[0:len(file)-6] == url:
            i+=1
        if file[0:len(file)-7] == url:
            i+=1
    return(i)

#IteratorURL('Comparison_of_Asian_national_space_programs')