# -*- coding: utf-8 -*-

import os
import jieba
import jieba.analyse
import pprint
#from text_analysis_tools.api.keywords import STOPWORDS
#from text_analysis_tools.text_analysis_tools.api.keywords import STOPWORDS

#STOPWORDS = ['te']

# class TfidfKeywords:
#     def __init__(self, delete_stopwords=True, topK=20, withWeight=False):
#         #if delete_stopwords:
#             #jieba.analyse.set_stop_words(STOPWORDS)
#         self.topk = topK
#         self.with_wight = withWeight
#
#     def keywords(self, sentence):
#         return jieba.analyse.extract_tags(sentence, topK=self.topk, withWeight=self.with_wight)

class TfidfKeywords:
    def __init__(self, topK = 20, withWeight = True):
        self.topK = topK
        self.withWeight = withWeight

    def keywords(self, sentence):
        return jieba.analyse.extract_tags(sentence, topK=self.topK, withWeight=self.withWeight)



if __name__ == "__main__":
    text = '当某一个模态的标记数据非常少时，可以利用协同训练生成更多的标注训练数据，或者利用模态间的不一致性过滤不可靠标注样本'
    kw_extract = TfidfKeywords()
    print(kw_extract)
    kw = kw_extract.keywords(text)
    print(kw)
    #pprint(kw)