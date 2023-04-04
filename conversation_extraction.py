import os
import re
from setting import *

def get_conversations(sentence, d):
    '''get the start and end position of the conversation in the
    input sentence
    Returns:
      start_index: int, the starting index in the sentence
      end_index: int, the ending index in the sentence
      conversation: str, the conversation'''
    end_symbols = ['"', '“', '”']
    istart, iend = -1, -1
    talks = []
    # flag = False
    # print(sentence)
    ### get the start and end position for conversation
    for i in range(1, len(sentence)): 

        if (not istart == -1) and sentence[i] in end_symbols:
            iend = i
            conversation = {'istart':istart, 'iend':iend, 'talk':sentence[istart+1:iend],'module': 0}
            for onom in d["onom"]:
                if onom in conversation["talk"]:
                    break
            else:
                flag = False
                for _ in "！，……。？~～":
                    if sentence[i-1] == _ :
                        flag = True
                if flag:
                    talks.append(conversation)
            istart = -1
        # if sentence[i-1] in [':', '：'] and sentence[i] in end_symbols:
        if sentence[i-1] == "\"" or sentence[i-1] == "“":
            # print(sentence[i])
            istart = i-1
    # print(istart,iend, len(sentence))
    ### get the context from where one can extract speaker
    contexts = []
    # print("uuuuu ",talks)
    marks = []
    if len(talks):
        for i in range(len(talks)):
            if i == 0 : 
                # print("ssss", talks[i]['istart'], sentence[:talks[i]['istart']])
                contexts.append(sentence[:talks[i]['istart']])
                # print(contexts)
            else:
                contexts.append(sentence[talks[i-1]['iend']+1:talks[i]['istart']])
                # print(contexts)
            if contexts[-1] == "":
                marks.append(i)

        # append the paragraph after the conversation if iend != len(sentence)
        if talks[-1]['iend'] != len(sentence)-1:
            contexts.append(sentence[talks[-1]['iend']+1:])
        else:
            contexts.append('')
            marks.append(len(sentence)-1)

        ### the situation is not considered if the speaker comes after the talk


        contextsubtalks = min(len(contexts) - len(talks),len(marks))

        relcontextlen = len([ _ for _ in contexts if _!= ""])
        # print(contexts)
        # print(relcontextlen)
        talkssubcontexts = len(talks)  - relcontextlen
        # print("dddddd", contextsubtalks,len(marks),contexts,talks)
        # print(talkssubcontexts)
        exp = 0 
        for i in range(len(talks)):
            if contextsubtalks > 0 and marks[exp] == i:
                 #+ 'XXXXX' + contexts[i+1]
                exp += 1
                contextsubtalks -= 1
            if talkssubcontexts > 0 and contexts[i + exp] == "":
                talks[i]['context'] = contexts[i + exp -1]
                talkssubcontexts -= 1
            else:
                talks[i]['context'] = contexts[i + exp]
                talks[i]['module'] = 1
        for i in range(len(talks)):
            if talks[i]['module'] == 1:
                new = re.split('[。？……！]', talks[i]['context'])
                new = new[::-1]
                findstring = "".join(new)
            else:
                findstring = talks[i]['context']
            mini = 1000 
            miniman = ""
            # if talks[i]['context'] == '说着，甲七缓缓抬高了板子，对着金刚妹高高撅起的光屁股打了下去。':
            #     print(findstring)
            for pattern in d['character']:
                t = re.search(pattern, findstring)
                if  t !=  None:
                    if t.span()[0] < mini:
                        mini = t.span()[0]
                        miniman = pattern
            talks[i]["speaker"] = miniman
            # if talks[i]['context'] == '说着，甲七缓缓抬高了板子，对着金刚妹高高撅起的光屁股打了下去。':
            #     print(miniman,mini)
    return talks, contexts            




def extract_corpus(essaypath,ori_d, save_as="save.py"):

    d = {}
    d["onom"] = "咔嚓噗嗤啪咚"
    d["character"] = list(ori_d.keys())
    # print(d["character"])
    # exit()
    # address = os.join(publication_path, essaypath)
    # print(essaypath)
    fout = open(save_as, "w")
    f2 = open("sss.txt","w")
    alltalks = []
    with open(essaypath, "r") as fin:
        fout.write('#!/usr/bin/env python\n')
        fout.write('talks = [')
        for line in fin.readlines():
            talks, contexts = get_conversations(line.strip(), d)
            alltalks.extend(talks)
            if len(talks) > 0:
                for talk in talks: #print(talk, '|||\n')
                    fout.write(talk.__repr__())
                    f2.write(talk["context"])
                    f2.write('\n')
                    f2.write(talk["talk"])
                    f2.write('   ,  talker is   ')

                    f2.write(talk["speaker"])
                    f2.write('\n')
                    fout.write(',\n')
        fout.write(']')
    fout.close()
    return alltalks


if __name__ == "__main__":
    import time

    start = time.time()
    a = extract_corpus("/home/vajor/essays/publication//葫芦道人全集/葫芦道人全集第15章.txt")
    # print(a)
    end = time.time()

    print(end-start)
