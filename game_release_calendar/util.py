import re

pattern = re.compile("\d{4}年\d{1,2}月\d{1,2}日（.）")


def is_date(self):
    result = pattern.match(self)

    return result != None