#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import re

# ツール用に改変
URL_REGEX1 = r"(https)([\-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)(\n)"
URL_REGEX2 = r"(https)([\-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+\n)([\-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)(\n)"
URL_REGEX3 = r"(https)([\-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+\n)([\-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+\n)([\-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)(\n)"

URL_REGEX_list = [URL_REGEX1, URL_REGEX2, URL_REGEX3]


def extract_urls(text):
    """
    ツール用に改変
    """
    url_list = []
    for URL_REGEX in URL_REGEX_list:
        urls = re.findall(URL_REGEX, text)
        url_list += [''.join(url).replace('\n', '') for url in urls]
    return set(url_list)


def extract_arxiv(text):
    """
    ツール用に改変
    """
    url_list = []
    for URL_REGEX in URL_REGEX_list:
        urls = re.findall(URL_REGEX, text)
        url_list += [''.join(url).replace('\n', '') for url in urls]
    return set(url_list)


def extract_doi(text):
    """
    ツール用に改変
    """
    url_list = []
    for URL_REGEX in URL_REGEX_list:
        urls = re.findall(URL_REGEX, text)
        url_list += [''.join(url).replace('\n', '') for url in urls]
    return set(url_list)


if __name__ == "__main__":
    print(extract_arxiv("arxiv:123 . arxiv: 345 455 http://arxiv.org/abs/876"))
