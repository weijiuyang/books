    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:37:51 2019

@author: jiuyang.wei
"""

from setting import *
import os
from tools  import *
import json


import ssl
import requests
import urllib3
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
 
html=r"https://www.text-to-speech.cn"

html_listen = r"https://www.text-to-speech.cn/getSpeek.php"



"""" 鳄鱼头领 """
# formdata = {
#     "language":"中文（普通话，简体）",
#     "voice":"zh-CN-YunzeNeural",
#     "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
#     "role":"0",
#     "pitch":"-7",
#     "rate":"6",
#     "user_id":"de7a64bb5f5611bb",
#     "style":"angry",
#     "silence":"200ms",
#     "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
# }

"""" 蛇精，年长女性"""
formdata = {
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
# formdata = {
#     "language":"中文（普通话，简体）",
#     "voice":"zh-CN-XiaoyiNeural",
#     "kbitrate":"audio-16khz-32kbitrate-mono-mp3",
#     "role":"Girl",
#     "pitch":"12",
#     "rate":"0",
#     "user_id":"de7a64bb5f5611bb",
#     "style":"angry",
#     "silence":"200ms",
#     "text":"来呀，别的地方你们射不疼我，就射这里吧！！这可是我身上最软的地方了，你们再射不疼我，就别说我没给你们机会了！"
# }

# print(os.listdir(alladvancepath+"/葫芦道人全集"))
for one in os.listdir(alladvancepath+"/葫芦道人全集"):  
    a,b,c = manageadvance(alladvancepath + "/葫芦道人全集/" +one, True)
    for _, d in c :
        print(d)
        savepath = "./common_hulumei/"
        files = os.listdir(savepath)
        if d+".mp3" in files or len(d) > 80 or "铁妹子" in d or "葫芦妹" in d or "啪" in d or "金刚妹":
            print("pass")
            continue
        formdata["text"] = d
        # print(formdata)
        response = requests.post(html_listen, data= formdata)

        if not os.path.exists(savepath):
            os.mkdir(savepath)
        t = json.loads(response.text)

        downurl = t["download"]

        audio=requests.get(url=downurl,verify = False)

        f = open(savepath + "%s.mp3"%d, 'wb')    
        f.write(audio.content)
        f.close() 
