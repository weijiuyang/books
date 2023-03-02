import jieba
from setting import publication_origin_path
import os
import jieba.posseg as pseg 
from collections import Counter

path = os.path.join(publication_origin_path , '水镜百花美人图.txt')

with open(path, "r") as f:
    content = f.read()
sentence = "我来自中国人民大学"
# 默认精确模式
words = pseg.cut(content,use_paddle = True)
# print("精确模式:  %s" % " ".join(words))
l = []
nrl = []
for word, flag in words:
    # print('%s %s' % (word, flag))
    l.append((word, flag))
    if flag == "nr":
        nrl.append(word)
c = Counter(l)
print(c.most_common(20))
nrc = Counter(nrl)
print(nrc.most_common(20))





