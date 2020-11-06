import os

listeFichiers = os.listdir('../output') #Create a list with all results

def IteratorURL(url):
    i = 0
    for file in listeFichiers:
        if file[0:len(file)-6] == url:      #Here, we delete the "_0.csv" of each files and compare with url
            i+=1                            #If the result is equal to the file, we increment i
        if file[0:len(file)-7] == url:      #The function search every file in list, it can be otpimized
            i+=1
    return(i)
