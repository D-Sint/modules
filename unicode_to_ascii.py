# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:48:03 2018
From: https://www.datacamp.com/community/tutorials/unicode-to-ascii-python
@Author: Dim S
"""

def unicodetoascii(str):

    finalString = (str.
    replace('\xe2\x80\x99', "'").
    replace('\xc3\xa9', 'e').
    replace('\xe2\x80\x90', '-').
    replace('\xe2\x80\x91', '-').
    replace('\xe2\x80\x92', '-').
    replace('\xe2\x80\x93', '-').
    replace('\xe2\x80\x94', '-').
    replace('\xe2\x80\x94', '-').
    replace('\xe2\x80\x98', "'").
    replace('\xe2\x80\x9b', "'").
    replace('\xe2\x80\x9c', '"').
    replace('\xe2\x80\x9c', '"').
    replace('\xe2\x80\x9d', '"').
    replace('\xe2\x80\x9e', '"').
    replace('\xe2\x80\x9f', '"').
    replace('\xe2\x80\xa6', '...').
    replace('\xe2\x80\xb2', "'").
    replace('\xe2\x80\xb3', "'").
    replace('\xe2\x80\xb4', "'").
    replace('\xe2\x80\xb5', "'").
    replace('\xe2\x80\xb6', "'").
    replace('\xe2\x80\xb7', "'").
    replace('\xe2\x81\xba', "+").
    replace('\xe2\x81\xbb', "-").
    replace('\xe2\x81\xbc', "=").
    replace('\xe2\x81\xbd', "(").
    replace('\xe2\x81\xbe', ")"))

    return finalString

def unicodetoascii_double_backslasch(str):

    finalString = (str.
    replace('\\xe2\\x80\\x99', "'").
    replace('\\xc3\\xa9', 'e').
    replace('\\xe2\\x80\\x90', '-').
    replace('\\xe2\\x80\\x91', '-').
    replace('\\xe2\\x80\\x92', '-').
    replace('\\xe2\\x80\\x93', '-').
    replace('\\xe2\\x80\\x94', '-').
    replace('\\xe2\\x80\\x94', '-').
    replace('\\xe2\\x80\\x98', "'").
    replace('\\xe2\\x80\\x9b', "'").
    replace('\\xe2\\x80\\x9c', '"').
    replace('\\xe2\\x80\\x9c', '"').
    replace('\\xe2\\x80\\x9d', '"').
    replace('\\xe2\\x80\\x9e', '"').
    replace('\\xe2\\x80\\x9f', '"').
    replace('\\xe2\\x80\\xa6', '...').
    replace('\\xe2\\x80\\xb2', "'").
    replace('\\xe2\\x80\\xb3', "'").
    replace('\\xe2\\x80\\xb4', "'").
    replace('\\xe2\\x80\\xb5', "'").
    replace('\\xe2\\x80\\xb6', "'").
    replace('\\xe2\\x80\\xb7', "'").
    replace('\\xe2\\x81\\xba', "+").
    replace('\\xe2\\x81\\xbb', "-").
    replace('\\xe2\\x81\\xbc', "=").
    replace('\\xe2\\x81\\xbd', "(").
    replace('\\xe2\\x81\\xbe', ")"))

    return finalString

