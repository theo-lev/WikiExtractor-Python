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