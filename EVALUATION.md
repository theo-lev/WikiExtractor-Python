## Extractors evaluation from Java to Python
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
|Elapsed time (in seconds)|281| 91|
 
## List of problems
|<h3>Problems </h3>| <h3>Java Extractor</h3>       |  <h3>Python Extractor</h3>  |
|:---------------:|:------------:|:------------:| 
|Bad extract of headers of rows| X | ✔ |
|When the value of cells is a link, it extract the content| X | ✔ |
|Merged cells create a new column for each rows| X | ✔ |
|When cells are merged, only one row include the value| X | ✔ |
|When the content of cells is a picture link, the picture don't load | X | X |

### Problems explanation

#### Heads of rows

On the Java extractor, there is a problem for the header extraction of rows.

Below, you can see first the good extraction with Python extractor :

```
Present tense infinitive,-ar (irar)
Past tense infinitive,-ir (irir)
Future tense infinitive,-or (iror)
```

And now, this is the result of the Java (HTML) Extractor : 

```
Infinitive,-ar (irar)
Infinitive,-ir (irir)
Infinitive,-or (iror)
```

With Java, there isn't an entire extraction of headers row.

#### Link cells

Sometimes, contributors of Wikipedia can link a value to an other Wikipedia page.
Like the header line, both extractors do not work properly at this level. 

Python result (right): 

```
IPA phonemes,a,b
```

Java result : 

```
International Phonetic Alphabet International Phonetic Alphabet,Open front unrounded vowel,Voiced bilabial plosive
```

#### HTML attributes

For the extraction with Java code, there is a bug which isn't recurring. 
Extractor extract, sometimes, HTML attributes. Exemple : 

```
irgatempe,|nulatempe,,style="background: #d8ffd8" | omnatempe, sempre
```

#### Merged cells

When the table contains merged cells, for Java extractors, it don't support this. 
For example the Python extractor work, the CSV return :

```
Present tense infinitive,-ar (irar),to be going,to go,-anti (iranti),-i (iri)
Past tense infinitive,-ir (irir),to have gone,to go,-inti (irinti),-i (iri)
Future tense infinitive,-or (iror),to be going to go,to go,-onti (ironti),-i (iri)
```
The cell with the value "to go" being merged on three lines.

But the result for two extractors is :

```
to be going,to go,-anti (iranti),-i (iri)
to have gone,,-inti (irinti)
to be going to go,,-onti (ironti)
```

Indeed, there is the good value for the first row, but the others have a blank. So, when Wikipedia table contains merged cells, a new column (or row) is added.

The problem is, with the good extraction, the table will look like 3 separated cells, but not merged.
