# /usr/bin/python3
import re
from typing import List, Callable, Generator, Set
from Dictionary.Dictionary import Dictionary, Word
import os
from os import path
import requests


class CeDict(Dictionary):
    def __init__(self, data_path: str):
        Dictionary.__init__(self, data_path)
        # 检查数据
        if not os.path.exists(path.join(self.data_path, "cedict_ts.u8")):
            # 下载文件
            print("file %s not exists, dowloading" % path.join(self.data_path, "cedict_ts.u8"))
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
            }
            r = requests.get("https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip", headers=headers)
            if r.status_code != 200:
                raise Exception("Cedict downlaod fail!")
            zip_path = path.join(self.data_path, "Cedict.zip")
            with open(zip_path, 'wb') as f:
                f.write(r.content)
            print("extract file to %s" % zip_path)
            os.system("zip %s -d %s" % (zip_path, self.data_path))
        # 现在存在 self.data_path/cedict_ts.u8
        self.dict_path = path.join(self.data_path, "cedict_ts.u8")

    def generate_line(self) -> Generator:
        dict_lines = list()
        with open(self.dict_path, 'r') as f:
            dict_lines = f.read().split('\n')
        # 验证数据有效性
        for line in dict_lines:
            if re.search('^#', line) or re.search('[0-9a-zA-Z\W]', line.split(' ')[0]) or len(line.split(' ')[0]) < 2:
                continue
            # 去除生僻字和方言
            if line.__contains__("coll.") or line.__contains__("broad"):
                continue
            # 现在：既不是注释行，又不是词行，又不是含有英文和数字的行
            # Cedict 包含三个部分：
            # 繁体 简体 [拼音] 注释
            simp = line.split(' ')[1]
            pinyin = re.search('\[.*?]', line).group().replace(' ', "'")
            # 删除[]和数字、空格
            flag = re.search(r"[\[\]0-9]", pinyin)
            while flag != None:
                pinyin = pinyin.replace(flag.group(), '')
                flag = re.search(r"[\[\]0-9]", pinyin)
            pinyin = pinyin.replace('u:', 'v')
            # print(line)
            yield (simp, pinyin)
        pass

    def get_words(self, frequency: Callable) -> List[Word]:
        data: Set[Word] = set()
        for word, pinyin in self.generate_line():
            data.add(Word(word, pinyin, frequency(word)))
        return list(data)


if __name__ == '__main__':
    d = CeDict('../')
    d.get_words(lambda str: 0.5)
