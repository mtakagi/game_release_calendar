#! /usr/bin/env python3

from .context import game_release_calendar
import unittest


class TestSuite(unittest.TestCase):
    def test_get_year_list(self):
        client = game_release_calendar.Client(
            game_release_calendar.Request("https://kakaku.com/game/release/"))
        data = client.get()
        content = game_release_calendar.Content(data, 'sjis')
        parser = game_release_calendar.YearParser(content)
        dic = parser.parse()
        print(dic)

    def test_get_current_list(self):
        client = game_release_calendar.Client(
            game_release_calendar.Request("https://kakaku.com/game/release/"))
        data = client.get()
        content = game_release_calendar.Content(data, 'sjis')
        parser = game_release_calendar.CalendarParser(content)
        dic = parser.parse()

        print(dic)


if __name__ == '__main__':
    unittest.main()
