# Polyglot Wikipedia Matrix Extractor (2020-2021)
This project is held at the University of Rennes 1, ISTIC, in Master 1 MIAGE during the year 2020-2021.

## Project context
This project is inspired by the project "Wikipedia Matrix" started last year by a group of M1 MIAGE (2019-2020). 

### What is the project « Polyglot Wikipedia Matrix Extractor » ?
Like the project "Wikipedia Matrix", the goal is to collect and extract Wikipedia's tables. 
These tables are on several Wikipedia pages retrieved by their url. The content of these tables will be returned 
in files using CSV format. Last year, the extractor have been realized in language Java. 
This year, the goal was to realized an other extractor which works in the same way but the language use is Python. 
Then, we will be able to compare the two extractors.

Wikipedia's pages were write in two language, HTML and Wikitext. Unlike the extractor "Wikipedia Matrix", 
this extractor read and analyze Wikipedia pages only in HTML format.

# Objectives
## Improvement of extractors
Get better extractions (comparisons), more precise tests.

## Tools to evaluate our extractors
Develop new tools which allow us to evaluate the quality and the performance of extractors. 
Develop a tool which allow us to evaluate the best extractor between Java and Python.

## Getting started 
Make the project easy to use by anyone thanks to a complete and functional dataset and a clear documentation to launch it.

## Functionnality of the project
The software takes a file with a list of wikipedia's pages title (taken from the page URL : with "_" in place of " ") 
and process each one to get the HTML URL of the page. After testing the URL, it treats all the HTML code 
of each page and try to extract as much table as it can in CSV.

## Project license
This project is licensed under the MIT License.

## Technologies used
- Git – The distributed version-control system used
- PyCharm IDEA - The IDE mainly used by our crew
- IntelliJ IDEA - The IDE used last year
- Scrapy - Python library to extract HTML 
- csv - Python library to write in CSV
- UniTest - Python library to make uni tests

## Authors
Clément Depond, Adèle Lecler, Théo Lévêque, Sadou Barry, Jean Zamble.