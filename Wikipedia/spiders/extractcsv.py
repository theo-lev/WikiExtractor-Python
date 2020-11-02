import scrapy


class ExtractcsvSpider(scrapy.Spider):
    name = 'extractcsv'
    allowed_domains = ['wikipedia.org']
    start_urls = [
        'https://fr.wikipedia.org/wiki/France#:~:text=Au%201er%20janvier%202018,mer%20et%20en%20Nouvelle%2DCal%C3%A9donie.',
        'https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido'
    ]
    # custom_settings = {
    #     'FEED_URI': 'tmp/extractcsv.csv'
    # }

    def parse(self, response):
        tables = response.css('table.wikitable')
        tableau = {}
        i = 0
        for row in tables:
            tableau[i] = row.css('tr th::text, tr td::text').extract()
            i+=1
            yield tableau
        convertCSV(tableau)
        #table = response.css['table.wikitable']
        #print(table.extract())
        # title = response.css('//th').extract()
        #
        # for item in zip(title):
        #     scraped_info = {
        #         'title' : item[0],
        #     }
        #
        # yield scraped_info
def convertCSV(tableau):
    print(tableau)