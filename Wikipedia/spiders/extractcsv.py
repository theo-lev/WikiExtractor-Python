import scrapy
import csv

class ExtractcsvSpider(scrapy.Spider):
    name = 'extractcsv'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://fr.wikipedia.org/wiki/France']

    def parse(self, response):
        tables = response.css('table.wikitable')
        tableau = {}
        i = 0
        for row in tables:
            tableau[i] = row.css('tr th::text, tr td::text').extract()
            i += 1
            yield tableau
        convertCSV(tableau)


def convertCSV(tableau):
    i = 0
    for row in tableau:
        a = str(i)
        with open('Wikipedia/spiders/tmp/france' + a + '.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([tableau[i]])
            i += 1
