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
            if line.__contains__("没谁了") or line.__contains__('ㄅㄧㄤˋ') or line.__contains__("𰻝𰻝面"):
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
