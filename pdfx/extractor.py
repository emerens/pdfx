#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Regexes for reference matching

Web url matching:
* http://daringfireball.net/2010/07/improved_regex_for_matching_urls
* https://gist.github.com/gruber/8891611
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import re

# ツール用に改変
URL_REGEX = r"(https)([-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+\n)([-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+\n)*"


def extract_urls(text):
    """
    ツール用に改変
    """
    url_list = re.findall(URL_REGEX, text)
    url_list = [''.join(url).replace('\n', '') for url in url_list]
    return set(url_list)


def extract_arxiv(text):
    """
    ツール用に改変
    """
    url_list = re.findall(URL_REGEX, text)
    url_list = [''.join(url).replace('\n', '') for url in url_list]
    return set(url_list)


def extract_doi(text):
    """
    ツール用に改変
    """
    url_list = re.findall(URL_REGEX, text)
    url_list = [''.join(url).replace('\n', '') for url in url_list]
    return set(url_list)


if __name__ == "__main__":
    print(extract_arxiv("arxiv:123 . arxiv: 345 455 http://arxiv.org/abs/876"))
