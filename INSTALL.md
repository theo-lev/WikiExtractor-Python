## Installation with PyCharm 
To execute this project, you will have to use an IDE. This documentation is for PyCharm. The language use is Python and 
you need to install libraries Scrapy, csv and unittest. 

Requirements : 
- [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/)
- [Python](https://www.python.org/)

Before starting, to install Scrapy :

### For Linux
- Open a terminal and copy "sudo apt install python-pip"
- Then copy "pip install Scrapy"

### For Windows
- Install Anaconda or Miniconda to use conda forge. 
- Open a terminal and copy "conda install -c conda-forge scrapy"
- Check to change your interpreter with Settings > Project : WikiMatrixChallenge > Project Interpreter and choose your python version with Anaconda logo

You can see scrapy is add to libraries.

Start by opening PyCharm and close all opened projects. Then get the project with the HTTPS link :
- Click "Get from Version Control"
- In Repository URL, copy the URL of the project and choose the directory to save

The project is ready to be execute. You can also read the part "Extract with function parse" (below).

## Extract with terminal

First of all, I will show you how to extract HTML code from one 
Wikipedia page. First step, open a terminal and type : 

```
scrapy shell "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido"
```

Congratulation, you scrap your first website ! 
Next step is to recover table element. In HTML, the content of a table is with < th >.
So let's say to the terminal we want to recover table elements : 

```
response.xpath("//th").extract()
```

After a quick load, you can see all the HTML code with th.

## Extract with function parse

For this one, you just have to call your method with :

```
scrapy crawl extractcsv
```

in the terminal.

Be careful ! 
If you have an error like "no such file or directory" when you run extractcsv, check the path in function open.
If there is "./spider/..." the point is the root, so, in PyCharm Terminal copy "cd Wikipedia".
