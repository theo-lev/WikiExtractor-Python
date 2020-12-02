import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# process = CrawlerProcess(get_project_settings()) # inside project
process = CrawlerProcess({
    'BOT_NAME': 'Wikipedia',
    'SPIDER_MODULES': 'Wikipedia.spiders',
    'NEWSPIDER_MODULE': 'Wikipedia.spiders',
    'LOG_ENABLED': False,
    'ROBOTSTXT_OBEY': True
})  # outside project

if len(sys.argv) == 2 and sys.argv[1] is not None:
    process.crawl('extractcsv', page=sys.argv[1])
    process.start()
elif len(sys.argv) > 2:
    print('Too many args')
else:
    process.crawl('extractcsv', page=None)
    process.start()
