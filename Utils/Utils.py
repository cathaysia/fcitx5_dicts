from typing import List
from Dictionary.Dictionary import Word
from os import path
import os
import tempfile
import logging


def trans2dict(data: List[Word], dict_path: str) -> int:
    f = tempfile.NamedTemporaryFile()
    for item in data:
        f.write(str(item).encode('utf-8'))
        f.write('\n'.encode('utf-8'))
    if not path.exists(path.split(dict_path)[0]):
        os.mkdir(path.split(dict_path)[0])
    return txt2dict(f.name, dict_path)


def txt2dict(file_path: str, dict_path: str) -> int:
    cmd = "libime_pinyindict {txt_name} {dict_name}".format(
        txt_name=file_path, dict_name=dict_path)
    logging.debug(cmd)
    return os.system(cmd)
