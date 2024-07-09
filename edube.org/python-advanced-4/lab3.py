# https://edube.org/learn/pcpp1-working-with-restful-apis/new-york-stock-exchange

import xml.etree.ElementTree as ET

COMPANY_COL_WIDTH = 40
LAST_COL_WIDTH = 10
CHANGE_COL_WIDTH = 10
MIN_COL_WIDTH = 10
MAX_COL_WIDTH = 10

if __name__ == '__main__':
    try:
        data = ET.parse('nyse.xml').getroot()

        print('COMPANY'.ljust(COMPANY_COL_WIDTH), end='')
        print('LAST'.ljust(LAST_COL_WIDTH), end='')
        print('CHANGE'.ljust(CHANGE_COL_WIDTH), end='')
        print('MIN'.ljust(MIN_COL_WIDTH), end='')
        print('MAX'.ljust(MAX_COL_WIDTH))

        print('-' * (COMPANY_COL_WIDTH +
                     LAST_COL_WIDTH +
                     CHANGE_COL_WIDTH +
                     MIN_COL_WIDTH +
                     MAX_COL_WIDTH))

        for quote in data.findall('quote'):
            print(quote.text.ljust(COMPANY_COL_WIDTH), end='')
            print(quote.attrib['last'].ljust(LAST_COL_WIDTH), end='')
            print(quote.attrib['change'].ljust(CHANGE_COL_WIDTH), end='')
            print(quote.attrib['min'].ljust(MIN_COL_WIDTH), end='')
            print(quote.attrib['max'].ljust(MAX_COL_WIDTH))
    except FileNotFoundError as e:
        print(e)
    except ET.ParseError as pe:
        print(pe)
