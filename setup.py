#! /usr/bin/python3

from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='game_release_calendar',
    version='1.0',
    description='とあるサイトからゲームの発売日を取得してパースする(自分用)',
    author='mtakagi',
    author_email='mtakagi127@live.jp',
    install_requires=['lxml'],
    url='https://github.com/mtakagi/game_release_calendar',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
)
