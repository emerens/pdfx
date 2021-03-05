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

# arXiv.org
ARXIV_REGEX = r"""arxiv:\s?([^\s,]+)"""
ARXIV_REGEX2 = r"""arxiv.org/abs/([^\s,]+)"""

# DOI
DOI_REGEX = r"""DOI:\s?([^\s,]+)"""

# URL
URL_REGEX = r"(https)([-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)(\n)([-:_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+\n)*"

ARXIV_REGEX = URL_REGEX
ARXIV_REGEX2 = URL_REGEX
DOI_REGEX = URL_REGEX


def extract_urls(text):
    """
    LiA用に改変
    """
    url_list = re.findall(URL_REGEX, text)
    url_list = [''.join(url).replace('\n', '') for url in url_list]
    return set(url_list)


def extract_arxiv(text):
    res = re.findall(ARXIV_REGEX, text, re.IGNORECASE) + \
          re.findall(ARXIV_REGEX2, text, re.IGNORECASE)
    return set([r.strip(".") for r in res])


def extract_doi(text):
    res = set(re.findall(DOI_REGEX, text, re.IGNORECASE))
    return set([r.strip(".") for r in res])


if __name__ == "__main__":
    print(extract_arxiv("arxiv:123 . arxiv: 345 455 http://arxiv.org/abs/876"))
