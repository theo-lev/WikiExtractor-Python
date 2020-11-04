import scrapy
import csv

class ExtractcsvSpider(scrapy.Spider):

    name = 'extractcsv'
    allowed_domains = ['wikipedia.org']
    start_urls = ['']
    '''Urls dynamically appended to a text file from where we add them to start urls'''

    for url in open("./spiders/wikiurl.txt"):
        start_urls.append(url)

    def reformat_url(self, url):
        ''' Manipulate url to structure to proper format or extract some information from it'''
        url = 'https://en.wikipedia.org/wiki/' +  url
        return url

    def start_requests(self):

        for url in self.start_urls:
            ''' call function to manipulate url'''
        new_url = self.reformat_url(url)
        yield self.make_requests_from_url(new_url)

    def parse(self, response, **kwargs):
        list_new_tables = []
        list_tables = response.css('table.wikitable')

        for table in list_tables:
            list_rows = table.css("tr")
            new_table = []

            for row in list_rows:
                new_row = row.css("th::text,th a::text,td::text, td a::text").extract()
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
        with open('./spiders/tmp/france' + a + '.csv', 'w') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            for row in table:
                csv_writer.writerow(row)
            i += 1
