# /usr/bin/python3
from Cedict.Cedict import CeDict
import logging
import os
from os import path
from Utils.Utils import trans2dict

if __name__ == '__main__':
    print("ready Cedict")
    cedict = CeDict(path.join(os.getcwd(), "data"))
    cedict_data = cedict.get_words(lambda str: 0.5)
    # 转换数据
    trans2dict(cedict_data, path.join(os.getcwd(), 'dict/cedict.dict'))
