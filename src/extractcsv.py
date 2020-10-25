import scrapy

class ExtractCSV(scrapy.Spider):
    name = 'extractcsv'
    start_urls = 'https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido'


    def parse(self, response):
