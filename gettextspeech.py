    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:37:51 2019

@author: jiuyang.wei
"""

from setting import *
import os
import json
from conversation_extraction import  extract_corpus
from retry import retry

import ssl
import requests
import urllib3
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
 
html=r"https://www.text-to-speech.cn"

html_listen = r"https://www.text-to-speech.cn/getSpeek.php"



"""" 鳄鱼头领 """
m1 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-YunzeNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"0",
    "pitch":"-7",
    "rate":"-11",
    "user_id":"de7a64bb5f5611bb",
    "style":"cheerful",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

"""" 小喽啰 """
m2 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-YunjianNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"0",
    "pitch":"-7",
    "rate":"6",
    "user_id":"de7a64bb5f5611bb",
    "style":"angry",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

"""" 小男孩 """
m3 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-YunxiaNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"0",
    "pitch":"-18",
    "rate":"-8",
    "user_id":"de7a64bb5f5611bb",
    "style":"angry",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

"""" 蛇精，年长女性"""
z1 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-XiaomoNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"0",
    "pitch":"9",
    "rate":"-13",
    "user_id":"de7a64bb5f5611bb",
    "style":"disgruntled",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

"""" 葫芦妹 """
f1 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-XiaoyiNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"Girl",
    "pitch":"12",
    "rate":"0",
    "user_id":"de7a64bb5f5611bb",
    "style":"angry",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

"""" 小女孩，七妹 """
f2 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-XiaoshuangNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"Girl",
    "pitch":"12",
    "rate":"0",
    "user_id":"de7a64bb5f5611bb",
    "style":"angry",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

"""" 温柔姐姐，二姐 """
f3 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-XiaomoNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"YoungAdultFemale",
    "pitch":"12",
    "rate":"0",
    "user_id":"de7a64bb5f5611bb",
    "style":"affectionate",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

"""" 温柔妹妹，五妹 """
f4 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-XiaomoNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"gril",
    "pitch":"12",
    "rate":"0",
    "user_id":"de7a64bb5f5611bb",
    "style":"affectionate",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}


"""" 小蝴蝶 """
f5 = {
    "language":"中文（普通话，简体）",
    "voice":"zh-CN-XiaoshuangNeural",
    "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
    "role":"Girl",
    "pitch":"-8",
    "rate":"-12",
    "user_id":"de7a64bb5f5611bb",
    "style":"angry",
    "silence":"200ms",
    "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
}

# @retry()
def makeaudio(kind,series_name,d):
    for one in os.listdir(kind+ "/" + series_name):    
        print(one)
        talks = extract_corpus(os.path.join(kind, series_name, one), d)
        # print(talks)
        # pass
        # exit()
        if not os.path.exists(os.path.join(audio_path, series_name)):
            os.mkdir(os.path.join(audio_path, series_name))
        for talk in talks:
            speaker = talk["speaker"] if not talk["speaker"] == "" else "金刚妹"
            # print(speaker)
            formdata = d[speaker]
            formdata["text"] = talk["talk"]
            # print(formdata)
            essay_audio_path = os.path.join(audio_path, series_name, one[:-4])
            current_audio_path = essay_audio_path + "/%s.mp3"%talk["talk"][:80]
            if not os.path.exists(current_audio_path) and len(talk["talk"]) > 4:
                # print("ss" ,current_audio_path)
                # print(talk)
                # exit()
                response = requests.post(html_listen, data=formdata,headers=headers)
                if not os.path.exists(essay_audio_path):
                    os.mkdir(essay_audio_path)
                # essay_character_audio_path = essay_audio_path + "/" + talk["speaker"]
                # if not os.path.exists(essay_character_audio_path):
                #     os.mkdir(essay_character_audio_path)
                t = json.loads(response.text)
                # print(t)
                downurl = t["download"]
                audio=requests.get(url=downurl,verify = False)
                f = open(essay_audio_path + "/%s.mp3"%talk["talk"][:80], 'wb')    
                f.write(audio.content)
                f.close() 
            # exit()


if __name__ == "__main__":

    d = {"葫芦妹":f1,"金刚妹":f1,"三妹":f1,"鳄鱼头领":m1,"蛇精":z1,"小妖":m2,"众妖":m2,"甲七":m2,"蛤蟆头领":m2,\
         "蝎子大王":m1,"青蛇":z1,"金蛇":z1, "大姐":f3 ,"二姐":f3 ,"四妹":f1, "五妹":f4, "六妹":f1, "七妹":f2,\
         "紫妹" :f2 ,"小蝴蝶":f5,"莲心":f1,\
         "金刚大王":m1,"美女妖":z1,"伸手大王":m1 ,"神秘人":m1,"爷爷":m1,"蝎子精":m1,\
         "小玄":m3, "颜紫绡":f1, "廉锦枫":f2,"卿卿":f1}
    # print(os.listdir(publication_path+"/葫芦道人全集"))
    series_name = '七彩葫芦妹'
    mycursor = mydb.cursor()
    sql = "select * from series "
    mycursor.execute(sql)
    result = mycursor.fetchall()
    # print(result)
    print(result[10])
    curseries = result[10][0]
    sql = "select * from essay where series_id= %s" % curseries
    mycursor.execute(sql)
    result = mycursor.fetchall()
    # print(result)
    print(result)
    exit()
    makeaudio(pixiv_path,series_name, d)




