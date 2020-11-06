# # Extractors evaluation from Java to Python
In this project, it is about extracting tables from HTML code. To do this, two types of extractors have been made, one in Java and the other in Python. We have to compare the performances of the two extractors. 
The first comparison will focus on the number of URLs processed. 
The other comparison will be about the quality of the extraction.

## Number of extraction

Like we said before, we have to compare the number of good extraction.

|Extraction|Java|Python|
|:----------:|:---------:|:---------:|
|Url processed|303|305|
|Total Url|336| 336|

### Comparison

| |Java|Python|
|:----------:|:----------:|:---------:|
|Files processed|1657|1645|
|elapsed time seconds|165,7252|87.819747|
 
## List of problems
|<h3>Problems </h3>| <h3>Java Extractor</h3>       |  <h3>Python Extractor</h3>  |
|:---------------:|:------------:|:------------:| 
|Bad extract of headers of rows| X ||
|When the value of cells is a link, it extract the content| X |X|
|Merged cells create a new column for each rows| X | X |
|When cells are merged, only one row include the value| X | X |
|Some cells in colors extract the color attribute|| X |
|When the value of cells is "?", it extract "dunno"|X |  |

### Problems explanation

#### 
