import scrapy


class ExtractcsvSpider(scrapy.Spider):
    name = 'extractcsv'
    allowed_domains = ['https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido']
    start_urls = ['http://https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido/']
    custom_settings = {
        'FEED_URI': 'tmp/extractcsv.csv'
    }

    def parse(self, response):
        title = response.css('//th').extract()

        for item in zip(title):
            scraped_info = {
                'title' : item[0],
            }

        yield scraped_info
