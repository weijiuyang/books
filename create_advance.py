import os 
import time

from tools import *
from setting import *

'''
The purpose of the program is constract information from essay dir to mysql 
'''


mycursor = mydb.cursor()

print('time.time()')
start = time.time()
# def returncontent():
flag = False
# print(os.listdir(path))
writeiddictionray = {}
writers = [_ for _ in os.listdir(alladvancepath) if _ != ".DS_Store" and _ == "葫芦道人全集" ]
for writer in writers:
    # print(writer)
    writerpath = alladvancepath + "/" + writer
    print(writer)
    # exit()
    series  = os.listdir(writerpath)
    # print(series)
    for sery in series:
        print(sery)
        serypath =  writerpath + "/" + sery
                                # continue
        # print(serypath)
        # print(sery)
        if  os.path.isdir(serypath):
            exit()
            sql = "select * from series where series_name = '%s' and author_id = %s" % (sery, author_id)
            mycursor.execute(sql)
            result = mycursor.fetchall()
            # result = True
            if not result:
                sql = "insert into series (series_name, series_address,author_id) values \
                    ('%s','%s',%s)"% (sery, serypath,author_id)
                # print(sql)
                # continue
                mycursor.execute(sql)
                
                # exit()

            # continue
            essays  = os.listdir(serypath)
            # print(sery + "   series")
            # print(essays)
            if ".DS_Store" in essays:
                essays.remove(".DS_Store")
            for essay in essays: 
                if essay[-3:] != "txt":
                    essays.remove(essay)
            essays.sort(key=lambda x:int(x.split("｜")[0][1:]))
            # print(essays)
            # exit()
            series_front = 0
            for index, essay in enumerate(essays):
                essaypath = serypath + "/" + essay
                if essaypath[-3:] == "txt":
                    essay_id = essaypath.split("｜")[-1][:-4]
                    # print(essay_id)
                    title, website, description, keywords, content = divide(essaypath)
                    for one in keywords:
                        if one in allkeyword:
                            allkeyword[one] += 1
                        else :
                            allkeyword[one] = 1
                    # continue
                    # if essay_id == "17871937":
                    #     print(title, website, description, keywords)
                    #     exit()
                    # return content
                    # print(essaypath)
                    # print(essay_id)
                    # with open(essaypath,"r") as f:
                    #     t=f.read()
                    # print(t)
                    # continue
                    sql = "select * from essay where essay_id = %s and title = '%s'" % (essay_id, title)
                    # print(sql)
                    mycursor.execute(sql)
                    result = mycursor.fetchall()
                    # print(index )
                    if not result:
                        if index == 0 :
                            series_front, series_left = essay_id, essay_id
                        else:
                            series_left = essays[index-1].split("｜")[-1][:-4]
                        if index < len(essays)-1:
                            series_right = essays[index+1].split("｜")[-1][:-4]
                        else:
                            eries_right = essay_id
                        # print(series_front,series_left,series_right)
                        sql = "insert into essay (essay_id, title, address, keywords,description,is_series,\
                            series_name,series_front,series_left,series_right,key_gils,is_pixiv,author_id) values \
                            (%s,'%s','%s','%s','%s',%s,'%s',%s,%s,%s,'%s',%s,'%s')"% (essay_id, title, essaypath,\
                            ",".join(keywords),description, 1, sery,series_front, series_left,series_right,"",1,author_id)
                        
                        # print(sql)
                        # print(essay_id,essaypath,sery,series_front, series_left,series_right,)
                        # continue
                        mycursor.execute(sql)
                        # mydb.commit()
                        # exit()
                        continue
                        series_left = essay_id
            # exit()
        else:
            essay = sery
            essaypath = serypath
            print(essaypath)
            # exit()
            if essaypath[-3:] == "txt":
                    # print(essaypath)
                title, content = easydivide(essaypath)
                mycursor.execute("insert into essay ( title, address,is_pixiv,advanced) \
                                 values (%s,%s,%s,%s)", ( title, essaypath,0,1))
    mydb.commit()
    # exit()
# print(writeiddictionray)
flag = True
# c = Counter(allkeyword)
# print(c)
end = time.time()
print(end - start, 's')
def returnwriters():
    return writeiddictionray


