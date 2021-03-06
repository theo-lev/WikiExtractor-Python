import csv
import os
import re
import scrapy
from scrapy import Request, Selector
from Wikipedia.spiders import convertURL
from definitions import ROOT_DIR


class ExtractcsvSpider(scrapy.Spider):
    """
    ExtractcsvSpider : Class
    Contains all methods to parse a wikipedia table
    cmd : scrapy crawl extractcsv
    """
    name = 'extractcsv'
    allowed_domains = ['wikipedia.org']
    name_pages = []
    stats = []
    numberHtmlTables = 0
    parseList = True

    def __init__(self, page=None, *args, **kwargs):
        super(ExtractcsvSpider, self).__init__(*args, **kwargs)
        if page is not None:
            self.parseList = False
            self.start_urls = [page]

    def closed(self, _):
        stats = self.crawler.stats.get_stats()
        stats['numberHtmlTables'] = self.numberHtmlTables
        end_execution(stats)

    def start_requests(self):
        if self.parseList:
            for url in convertURL.getConvertUrl():
                yield Request(url, dont_filter=True)
        else:
            for url in self.start_urls:
                yield Request(url, dont_filter=True)

    def parse(self, response, **kwargs):
        name_page = response.request.url.replace('https://en.wikipedia.org/wiki/', '')

        print("Extracting page : " + name_page)

        list_new_tables = []

        list_tables = response.css('table.wikitable')  # list of tables from start_urls page

        for table in list_tables:
            list_new_tables.append(parse_table(table))
            self.numberHtmlTables += 1

        convertCSV(name_page, list_new_tables)


def parse_table(table):
    """
    Get a table in scrapy format, parse it and return a new table ready to extract in csv
    :param table: Table Wikipedia under scrapy format
    :return: parsed table
    """

    i_rowToSpan = 0  # index of the next row
    new_table = []  # table to return
    cells_span = {}  # list of cells with rowspan > 1 : which takes more than 1 row in the table

    rows = table.xpath('.//tr')  # get list of rows from the table
    maxColumns = getMaxColumns(rows)

    for row in rows:  # iterate on rows
        i_maxColumns = 0
        i_cells = 0
        i_totalColSpan = 0
        new_row = []
        i_rowToSpan += 1
        cells = row.xpath('.//td | .//th')  # get list of every cells in the row, only td and th are consider as cells

        while i_maxColumns < maxColumns or i_cells < len(cells):

            if (i_rowToSpan, i_maxColumns) in cells_span:
                new_cell = parse_extract_cell(cells_span.pop((i_rowToSpan, i_maxColumns)))
                new_row.append(new_cell)
                i_totalColSpan += 1

            elif i_cells < len(cells):
                cell = cells[i_cells]
                rowSpan, colSpan = getRowColSpan(cell)

                for i_colSpan in range(colSpan):

                    for nbRowSpan in range(rowSpan - 1):
                        # add cell to span for next rows
                        cells_span[(i_rowToSpan + nbRowSpan + 1, i_totalColSpan)] = cell

                    new_cell = parse_extract_cell(cell)
                    new_row.append(new_cell)
                    i_totalColSpan += 1

                i_cells += 1

            i_maxColumns += 1

        new_table.append(new_row)  # add row

    return new_table


def parse_extract_cell(cell):
    """
    Extract and parse cell
    :param cell:
    :return:
    """

    cell = cell.extract()
    cell = cell.replace(' <br>', ' ')
    cell = cell.replace('<br>', ' ')

    sel = Selector(text=cell)

    link_images = sel.xpath('.//img/@src').extract()  # extract images link
    new_cell = sel.xpath('string(.)').extract()[0]  # extract string for every child in cell
    new_cell = new_cell.replace(u'\xa0', ' ')
    new_cell = new_cell.rstrip('\n')
    new_cell = new_cell.strip()

    for link in link_images:
        if new_cell != "":
            new_cell = new_cell + " " + link.strip()  # add every link images at the end of the cell
        else:
            new_cell = link.strip()

    return new_cell


def getRowColSpan(cell):
    """
    Get rowspan and colspan values from cell
    :param cell: Cell from HTML table in scrapy format
    :return: the value from attributes rowspan and colspan
    """
    rowSpan, colSpan = 1, 1

    if cell is not None:
        res = cell.xpath('string(@rowspan)').extract()
        if res is not None and res[0] != '':
            rowSpan = res[0]
            rowSpan = int(re.findall(r'(\d+)', rowSpan)[0])
            if rowSpan is None:
                rowSpan = 1
        res = cell.xpath('string(@colspan)').extract()
        if res is not None and res[0]:
            colSpan = res[0]
            colSpan = int(re.findall(r'(\d+)', colSpan)[0])
            if colSpan is None:
                colSpan = 1

    return rowSpan, colSpan


def getMaxColumns(rows):
    """
    Return number max of columns from rows
    :param rows: list of rows <tr>
    :return: int
    """
    maxColumns = 0
    for row in rows:
        count = float(row.xpath('count(*)').extract()[0])
        if count > maxColumns:
            maxColumns = count
    return int(maxColumns)


def convertCSV(name_page, list_tables):
    dirOutput = os.path.join(ROOT_DIR, 'output')

    i = 0
    for table in list_tables:
        a = str(i)
        with open(os.path.join(dirOutput, name_page) + '_' + a + '.csv', 'w', newline='', encoding='utf-8') as csvFile:
            csv_writer = csv.writer(csvFile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            for row in table:
                csv_writer.writerow(row)

        i += 1


def end_execution(stats):
    # You can modify scrapy log display in settings.py
    # LOG_ENABLED = True and adjust with LOG_LEVEL

    print('-- STATS --')
    if 'elapsed_time_seconds' in stats and stats['elapsed_time_seconds'] is not None:
        print('EXECUTION TIME : ' + str(stats['elapsed_time_seconds']) + 'seconds')

    if 'downloader/request_count' in stats and stats['downloader/request_count'] is not None \
            and 'robotstxt/request_count' in stats and stats['robotstxt/request_count'] is not None:
        print('TOTAL URL : ' + str(stats['downloader/request_count'] - stats['robotstxt/request_count']))

    if 'downloader/response_status_count/200' in stats and stats['downloader/response_status_count/200'] is not None \
            and 'robotstxt/request_count' in stats and stats['robotstxt/request_count'] is not None:
        print('NUMBER CORRECT URL : ' +
              str(stats['downloader/response_status_count/200'] - stats['robotstxt/request_count']))

    if 'httperror/response_ignored_count' in stats and stats['httperror/response_ignored_count'] is not None:
        print('NUMBER IGNORED URL : ' + str(stats['httperror/response_ignored_count']))

    if 'numberHtmlTables' in stats and stats['numberHtmlTables'] is not None:
        print('NUMBER OF EXTRACTED HTML TABLES : ' + str(stats['numberHtmlTables']))
