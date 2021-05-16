from typing import List
from Dictionary.Dictionary import Word
import uuid
from os import path
import os
from tempfile import NamedTemporaryFile


def trans2dict(data: List[Word], dict_path: str) -> int:
    f = NamedTemporaryFile('w')
    for item in data:
        f.write(str(item))
        f.write('\n')
    # file_path = path.join(str(uuid.uuid4()) + '.txt')
    # with open(file_path, 'w') as f:
    #     for item in data:
    #         f.write(str(item))
    #
    if not path.exists(dict_path):
        os.mkdir(path.split(dict_path)[0])
    return os.system("libime_pinyindict {txt_name} {dict_name}".format(txt_name=f.name, dict_name=dict_path))
