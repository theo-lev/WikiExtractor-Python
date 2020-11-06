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

#### Heads of rows

On the Java extractor, there is a problem for the header extraction of rows.

Below, you can see first the good extraction with WikiText extractor :

```
Present tense infinitive,-ar (irar)
Past tense infinitive,-ir (irir)
Future tense infinitive,-or (iror)
```

And now, this is the result of the HTML Extractor : 

```
Infinitive,-ar (irar)
Infinitive,-ir (irir)
Infinitive,-or (iror)
```

With HTML, there isn't an entire extraction of headers row.

#### Link cells

Sometimes, contributors of Wikipedia can link a value to an other Wikipedia page.
Like the header line, both extractors do not work properly at this level. 

WikiText result (right): 

```
IPA phonemes,a,b
```

HTML result : 

```
International Phonetic Alphabet International Phonetic Alphabet,Open front unrounded vowel,Voiced bilabial plosive
```

#### HTML attributes

For the extraction with Java code, there is a bug which isn't recurring. 
Extractor extract, sometimes, HTML attributes. Exemple : 

```
irgatempe,|nulatempe,,style="background: #d8ffd8" | omnatempe, sempre
```

For extraction with Python code, there is another bug. 
The extractor does not convert special characters. Exemple :
```
Letter Å in names are not translated in the link #6
Letter é in names are not translated in the link #11

```
