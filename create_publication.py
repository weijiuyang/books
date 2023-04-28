import os 
import time
import shutil

from bookstool import easydivide
from setting import *
from publication_preprocess import preprocess
import re

'''
The purpose of the program is constract information from essay dir to mysql 
'''


mycursor = mydb.cursor()

print('time.time()')
start = time.time()
# def returncontent():
flag = False
# print(os.listdir(path))
# author_id = 5
author_name = "长安忆"
series_home = None
series_name = '长安忆'

sql = "select id,name from author where name = '%s' " % (author_name)
mycursor.execute(sql)
result = mycursor.fetchall()
if not result or result == []:
    sql = "insert into author (name) values ('%s')" % (author_name)
    mycursor.execute(sql)
    mydb.commit()
sql = "select id,name from author where name = '%s' " % (author_name)
mycursor.execute(sql)
result = mycursor.fetchall()
print(result[0][0])
author_id = result[0][0]
 
# exit()
preprocess(series_name)
# exit()

writeiddictionray = {}
series = [_ for _ in os.listdir(publication_path) if _ != ".DS_Store" and _ == series_name ]
for sery in series:
    # print(writer)
    serypath = os.path.join(publication_path, sery)
    sql = "select id,name from series where name = '%s' and author_id = %s" % (sery, author_id)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    if not result or result == []:
        sql = "insert into series (name, address,author_id) values \
            ('%s','%s',%s)"% (sery, sery,author_id)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        sql = "select id,name from series where name = '%s' and author_id = %s" % (sery, author_id)
        mycursor.execute(sql)
        result = mycursor.fetchall()
    series_id = result[0][0]
    series_name = result[0][1]

    print(serypath)
    # exit()
    essays  = os.listdir(serypath)
    print(series)
    # exit()
    resortlist = []
    for essay in essays:
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', essay)]
        resortlist.append((essay,s))
    resortlist.sort(key = lambda x:x[1])
    print(resortlist)
    for index, essay in enumerate(resortlist):
        oldname , _  = essay
        os.rename(os.path.join(serypath, oldname), os.path.join(serypath, sery+"第%s章"%str(index+1)))
    essays  = os.listdir(serypath)
    for oldname in essays:
        os.rename(os.path.join(serypath, oldname), os.path.join(serypath, oldname+'.txt'))    

    for index in range(len(essays)):
        essay = sery+"第%s章.txt"%str(index+1)
        essaypath =  os.path.join(serypath, essay)
                                # continue
        print(essaypath)
        title, _ = easydivide(essaypath)
        # exit()
        sql = "select * from essay where title = '%s' and author_id = %s" % (title, author_id)
        mycursor.execute(sql)
        result = mycursor.fetchall()

        # result = True
        if not result:    
            if index == 0 :
                series_home, series_left = os.path.join(sery,essay), os.path.join(sery,essay)
            else:
                series_left = os.path.join(sery,sery+"第%s章.txt"%str(index))
            if index < len(essays)-1:
                series_right = os.path.join(sery,sery+"第%s章.txt"%str(index+2))
            else:
                series_right = os.path.join(sery,essay)
            # # print(series_front,series_left,series_right)
            sql = "insert into essay (title, address,series_name,series_home,series_left,\
                 series_right,series_id,author_id,author_name) values \
                ('%s','%s','%s','%s','%s','%s',%s,%s,'%s')"% ( title, os.path.join(sery,essay),\
                 sery,series_home, series_left,series_right,series_id,author_id,author_name)
            print(sql)
            mycursor.execute(sql)
            continue
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


