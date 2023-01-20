from setting import *
import re

def removejap(string):
    for one in jap_set:
        if one in string:
            return False
    return True


def keywordsdrop(string):
    """" 处理不需要关键字 """
    if string in keyworddrop :
        return False, ""
    
    """" 移除日语  """
    if not removejap(string):
        return False, ""
    
    """ 替换"""
    if string in keywordreplace:
        string = keywordreplace[string]


    return True, string

def divide(essaypath):
    with open(essaypath, "r") as f :
        # content=f.read()
        # print(content.rstrip())
        temp = f.readlines()
    index = 0
    while temp[index] == "\n":
        index += 1
    title = temp[index].strip()
    index += 1
    # print("title ", title.strip())
    # print(temp[index]+ str(index))
    while temp[index] == "\n":
        index += 1
        # print(temp[index]+ "Ssss")

    writeragin = temp[index].strip()
    # print("writer", writeragin.strip(),index)
    index += 1

    while temp[index] == "\n":
        index += 1
    website = temp[index].strip()
    # print(website.strip(),index) 
    index += 1


    while temp[index] == "\n":
        index += 1
    description = ""    
    while temp[index][0] != "#":
        description += temp[index]
    # print(description.strip(),index) 
        index += 1
    description = description.strip()
    keywords = set()

    # while temp[index] == "\n":
    #     index += 1
    # print(index)
    while temp[index][0] == "#":

        """
            用下面的方法，太慢了
        """
        # str = temp[index][1:].strip()

        # jap = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\uAC00-\uD7A3]')  # \uAC00-\uD7A3为匹配韩文的，其余为日文
        # if jap.search(str):
        #     print('Yes')
        keyword = temp[index][1:].strip()

        keyword_list = re.split("[/ ,]", keyword)

        # keyword_list = keyword.split("",",s")
        for keyword in keyword_list:
            isdrop, waitkeywords = keywordsdrop(keyword)
        if isdrop :
            keywords.add(waitkeywords)
        index += 1
    # print(keywords)                                                   
    while temp[index] == "\n":
        index += 1
    content = "".join(temp[index:])  
    # print(content)
    return title, website, description, keywords, content 


