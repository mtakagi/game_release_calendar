from . import util
from lxml import html
from lxml.objectify import NoneElement
from abc import *


class Content:
    def __init__(self, data, encoding):
        self.html = html.fromstring(str(data, encoding))

    def xpath(self, query):
        return self.html.xpath(query)


class AbstractParser(metaclass=ABCMeta):
    @abstractmethod
    def parse(self):
        pass


class YearParser(AbstractParser):

    xpath = "/html/body/div[@id='all']/div[@id='contents930']/div[@id='game']/form/div[@id='monthSelectArea']/select[@id='year']/option"

    def __init__(self, content):
        self.content = content

    def parse(self):
        select_content = self.content.xpath(YearParser.xpath)

        return [content.get('value') for content in select_content]


class CalendarParser(AbstractParser):

    xpath = "/html/body/div[@id='all']/div[@id='contents930']/div[@id='game']/div[@id='releaseMain']/table[@id='titleSche']/tbody/tr/td"

    def __init__(self, content):
        self.content = content

    def _htmlparse(self, td_content):
        array = []
        for content in td_content:
            if content.get("class") == 'gameCategory':
                if isinstance(content.find("img"), type(None)):
                    continue
                category = content.find("img").get("alt")
                if category != '\xa0' and len(category) > 0:
                    array.append(category)
            elif content.get("class") == 'gameTitle':
                txt = content.text_content()
                if txt != '\xa0' and len(txt) > 0:
                    array.append(txt)
                if isinstance(content.find("a"), type(None)):
                    continue
                array.append(content.find('a').get("href"))
            elif content.get("class") == 'gamePrice':
                txt = content.text_content()
                if txt == '\xa0':
                    txt = ''
                array.append(txt)
            else:
                txt = content.text_content()
                if txt != '\xa0' and len(txt) > 0:
                    array.append(txt)

        return array

    def _todict(self, array):
        dic = {}
        count = 0
        current_date = None

        while count < len(array):
            element = array[count]
            if util.is_date(element):
                current_date = element
                dic[element] = []
                count += 1
                if array[count] == '':
                    count += 1
            else:
                category = array[count]
                title = array[count + 1]
                url = array[count + 2]
                maker = array[count + 3]
                price = array[count + 4]
                # print({"category": category, "url": url, "title": title, "maker": maker, "price": price})
                dic[current_date].append({
                    "category": category,
                    "url": url,
                    "title": title,
                    "maker": maker,
                    "price": price
                })
                count += 5

        return dic

    def parse(self):
        td_content = self.content.xpath(CalendarParser.xpath)
        array = self._htmlparse(td_content)

        return self._todict(array)
