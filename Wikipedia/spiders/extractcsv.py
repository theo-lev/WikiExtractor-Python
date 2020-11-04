import scrapy
import csv


class ExtractcsvSpider(scrapy.Spider):
    name = 'extractcsv'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://fr.wikipedia.org/wiki/France']

    def parse(self, response, **kwargs):
        list_new_tables = []
        list_tables = response.css('table.wikitable')

        for table in list_tables:
            list_rows = table.xpath('./tbody/tr')
            new_table = []

            for row in list_rows:
                new_row = row.xpath('.//text()[not(ancestor::sup or ancestor::span/@class="flagicon")]').extract()
                new_row = [element.strip('\n') for element in new_row]
                while '\n' in new_row:
                    new_row.remove('\n')
                while '' in new_row:
                    new_row.remove('')
                new_table.append(new_row)

            list_new_tables.append(new_table)

        convertCSV(list_new_tables)


def convertCSV(list_tables):
    i = 0
    for table in list_tables:
        a = str(i)
        with open('./spiders/tmp/france' + a + '.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            for row in table:
                csv_writer.writerow(row)
            i += 1
