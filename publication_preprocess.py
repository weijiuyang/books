from setting import publication_origin_path,publication_path,publication_done_path
import os
import re
import shutil
# with open(advance_origin_path,"r")as f:



def preprocess(series_name=None):
    publications = os.listdir(publication_origin_path)

    for publication in publications:
        originpublicationpath = publication_origin_path + publication
        # print(allpublicationpath)
        if series_name == None or  publication[:-4] == series_name:
            # print("ss")
            indexlist = []
            publicationpath = publication_path + publication[:-4]
            print(publicationpath)
            if not os.path.exists(publicationpath):
                os.mkdir(publicationpath)
            with open(originpublicationpath, "r") as f :
                content = f.readlines()
                count = 0
                
                for index, line in enumerate(content):
                    flag = False
                    line = line.strip(' ')
                    line = line.replace('\t',' ')
                    line = line.replace('‘','“')
                    line = line.replace('’','”')

                    line = line.replace('\'','"')
                    line = line.replace('“','"')
                    line = line.replace('”','"')
                    # print('uuu',line)

                    line = re.sub(r'[\xa0\u3000]+', '\n', line)
                    # line = re.sub(r'豌豆\s\u3000]+', '\n', line)
                    line = re.sub('豌豆 \d{4}年\d{1,2}月\d{1,2}日', '', line)
                    line = re.sub('豌豆 \d{1,2}个月前', '', line)
                    print('aaaaa',line)
                    line = re.sub(r'\s*\n\s*', '\n    ', line)
                    print('bbbb',line)

                    line = line.strip(' ')
                    print('ccc',line)

                    for i in range(len(line)):
                        if line[i] == '"':
                            if not flag:
                                line = line[:i] +  '“' + line[i+1:] 
                                flag = True
                            else :
                                line = line[:i] +  '”' + line[i+1:] 
                                flag = False
                    print(line[0:4] == '    ')
                    # print('tttt',line)
                    print(line)
                    if line and not line == '':
                        content[index] = '    ' + line
                    count += 1
                    # if count == 100 :
                    #     exit()
                    # line = line.strip()
                # print(content)
                reg="第\s*[0-9]+\s*章"
                for index, item in enumerate(content):
                    result = re.search(reg,item)
                    if not result ==  None:
                        print(result.group())
                        indexlist.append(index)
                if indexlist == []:
                    reg="第\s*[一二三四五六七八九十]+\s*章"
                    for index, item in enumerate(content):
                        result = re.search(reg,item)
                        if not result ==  None:
                            print(result.group())
                            indexlist.append(index)     
                print(indexlist)
                # exit()
                print(publicationpath + "/%s第%s章.txt"%(publication[:-4],index))
                for index in range(len(indexlist)-1):
                    with open(publicationpath + "/%s第%s章.txt"%(publication[:-4],index+1), "w") as fw:
                        # chaptercontent = 
                        currentlines = "".join(content[indexlist[index]:indexlist[index+1]])
                        currentlines = currentlines.replace('\n    \n    \n','\n')
                        currentlines = currentlines.replace('\n    \n','\n')

                        fw.write(currentlines)
                        # print("".join(content[indexlist[index]:indexlist[index+1]]))
                        # print("t")

            shutil.move(originpublicationpath, publication_done_path)

            

            



