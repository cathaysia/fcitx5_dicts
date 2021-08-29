#!/usr/bin/python3
from Cedict.Cedict import CeDict
import logging
import os
from os import path
from Utils.Utils import trans2dict, txt2dict

if __name__ == '__main__':
    logging.root = logging.RootLogger(logging.DEBUG)
    logging.debug("ready Cedict")

    cedict = CeDict(path.join(os.getcwd(), "extern"))
    cedict_data = cedict.get_words(lambda str: 0.5)
    # 转换数据
    trans2dict(cedict_data, path.join(os.getcwd(), 'dict/cedict.dict'))
    txt2dict(path.join(os.getcwd(), 'extern/chinese-frequency-word-list'),
             path.join(os.getcwd(), 'dict/chinese-frequency-word-list.dict')
             )
