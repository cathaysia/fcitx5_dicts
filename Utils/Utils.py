from typing import List
from Dictionary.Dictionary import Word
import uuid
from os import path
import os
from tempfile import NamedTemporaryFile


def trans2dict(data: List[Word], dict_path: str) -> int:
    # f = NamedTemporaryFile('w')
    f = open('1.txt', 'w')
    list_str:List[str] = list()
    for item in data:
        f.write(str(item))
        f.write('\n')
    if not path.exists(path.split(dict_path)[0]):
        os.mkdir(path.split(dict_path)[0])
    return os.system("libime_pinyindict {txt_name} {dict_name}".format(txt_name=f.name, dict_name=dict_path))
