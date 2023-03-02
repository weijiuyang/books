from setting import *
import re
import os 

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

"""" 读取文件，分割成各个部分 """
def divide(essaypath):
    with open(essaypath, "r") as f :
        temp = f.readlines()
    index = 0
    while temp[index] == "\n":
        index += 1
    title = temp[index].strip()
    index += 1
    while temp[index] == "\n":
        index += 1
    writeragin = temp[index].strip()
    index += 1
    while temp[index] == "\n":
        index += 1
    website = temp[index].strip()
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


def easydivide(essaypath):
    with open(essaypath, "r") as f :
        temp = f.readlines()
    index = 0
    if temp[index][0] == "第" or  "(":
        index += 1                                                 
    while temp[index] == "\n":
        index += 1
    title = temp[index].strip()
    index += 1
    content = "".join(temp[index:])  
    return title, content 

def linkaudio(path):
    allpath = os.path.join(publication_path,path) 
    title, content = easydivide(allpath)
    # audio = re.compile(r'“([^”]*)”')  
    audio = re.compile("\\“(?:(?!\\”).)*(\\,|\\~|\\。|\\！|\\？|(\\……))”");
    audiolist = []
    for match in audio.finditer(content): # content为需要查找的内容
        currentaudio = match.group()[1:-1]
        if len(currentaudio) > 4:
            # audiopathabsolute = "/home/vajor/books/static/audio/" + currentaudio + ".mp3"
            audiopath = "../static/audio/" + path[:-4] + '/' + currentaudio[:80] + ".mp3"
            print(audiopath)
            audiolist.append((audiopath, currentaudio))
    content = re.sub(audio, audiore,content)
    return title,content,audiolist

def audiore(match):
    audio = match.group()
    return '<a onclick="playAudio(\'%s\')">'%audio[1:-1] + audio + "</a>"
