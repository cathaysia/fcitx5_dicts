from abc import ABCMeta, abstractmethod
from typing import List, Callable
import os


class Word:
    def __init__(self, word: str = '', pinyin: str = '', freq: float = 0):
        self.word = word
        self.pinyin = pinyin
        self.freq = freq

    def __str__(self):
        return "%s %s %s"%(self.word, self.pinyin, self.freq)


class Dictionary:
    '''
        @:param data_path 数据的存储路径，所有辞典会将数据存放在此处
    '''

    def __init__(self, data_path: str):
        self.data_path = data_path
        if not os.path.exists(data_path):
            os.mkdir(data_path)

    '''
        @:param frequency 是一个可调用函数，其签名为 def frequency(word:str)->float
    '''

    @abstractmethod
    def get_words(self, frequency: Callable) -> List[Word]:
        pass
