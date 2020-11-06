import csv
import os
import re

import scrapy
from scrapy import Request, Selector
from Wikipedia.spiders import convertURL


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

    def closed(self, _):
        stats = self.crawler.stats.get_stats()
        end_execution(stats)

    def start_requests(self):
        for url in convertURL.getConvertUrl():
            yield Request(url, dont_filter=True)

    def parse(self, response, **kwargs):
        name_page = response.request.url.replace('https://en.wikipedia.org/wiki/', '')

        print("Extracting page : " + name_page)

        list_new_tables = []

        list_tables = response.css('table.wikitable')  # list of tables from start_urls page

        for table in list_tables:
            list_new_tables.append(parse_table(table))

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

    :param cell:
    :return:
    """

    cell = cell.extract()
    cell = cell.replace(' <br>', ' ')
    cell = cell.replace('<br>', ' ')

    sel = Selector(text=cell)

    new_cell = sel.xpath('string(.)').extract()[0]  # extract string for every child in cell
    new_cell = new_cell.replace(u'\xa0', ' ')
    new_cell = new_cell.rstrip('\n')

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
    actualDir = os.path.dirname(os.path.realpath('__file__'))
    dirOutput = os.path.abspath(actualDir + '/../output')

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
    print('EXECUTION TIME : ' + str(stats['elapsed_time_seconds']))
    print('TOTAL URL : ' + str(stats['downloader/request_count'] - stats['robotstxt/request_count']))
    print('NUMBER CORRECT URL : ' +
          str(stats['downloader/response_status_count/200'] - stats['robotstxt/request_count']))
    if stats['httperror/response_ignored_count'] is not None:
        print('NUMBER IGNORED URL : ' + str(stats['httperror/response_ignored_count']))
