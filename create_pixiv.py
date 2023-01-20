import os 
import time

from tools import *
from setting import *

'''
The purpose of the program is constract information from essay dir to mysql 
'''


mycursor = mydb.cursor()
def create_user():
    mycursor = mydb.cursor()
    for k, v in returnwriters().items():
        print(v)
        sql = "select * from author where user_id = %s and user_name = '%s'" % (k, v)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if not result:
            sql = "insert into author (user_id,user_name) values (%s,'%s')" % (k,v)
            print(sql)
            mycursor.execute(sql)
    #或者写成:
    #sql = "insert into biao1 (id,name,passwd) values (%s,%s,%s)"
    #val = ('1','admin','admin')
    #mycursor.execute(sql,val)
    mydb.commit()

allkeyword = dict()

print('time.time()')
start = time.time()

# def returncontent():
flag = False
# print(os.listdir(path))
writeiddictionray = {}
writers  = os.listdir(allessaypath)
for writer in writers:
    # print(writer)
    writerpath = allessaypath + "/" + writer
    if len(writer.split("｜")) > 1:
        print(writer)
        writeiddictionray[writer.split("｜")[0]] = writer.split("｜")[1]
        author_id = writer.split("｜")[0]
        # exit()
        series  = os.listdir(writerpath)
        # print(series)
        for sery in series:

            serypath =  writerpath + "/" + sery
                                    # continue

            # print(serypath)
            # print(sery)
            if  os.path.isdir(serypath):

                sql = "select * from series where series_name = '%s' and author_id = %s" % (sery, author_id)
                # print(sql)
                # print(serypath)
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
                # print(sery)
                # continue
                essay = sery
                essaypath = serypath
                if essaypath[-3:] == "txt":
                        # print(essaypath)
                    essay_id = essaypath.split("｜")[-1][:-4]
                    title, website, description, keywords, content = divide(essaypath)
                    for one in keywords:
                            if one in allkeyword:
                                allkeyword[one] += 1
                            else :
                                allkeyword[one] = 1
                    # continue
                    # print(essaypath)
                    # with open(essaypath,"r") as f:
                    #     t=f.read()
                    # print(t)
                    sql_title = title
                    sql = "select * from essay where essay_id = %s and title = '%s'" % (essay_id, title)
                    # print(sql)
                    # print(essaypath)
                    # mycursor.execute(sql)
                    r = mycursor.execute("select id from essay where essay_id = %s and title = %s",(str(essay_id), title,))
                    result = mycursor.fetchall()
                    # exit()
                    # result = True
                    if not result:
                        sql = "insert into essay (essay_id, title, address, keywords,description,\
                            key_gils,is_pixiv,author_id) values \
                            (%s,'%s','%s','%s','%s','%s',%s,'%s')"% (essay_id, title, essaypath,\
                            ",".join(keywords),description, "",1,author_id)
                        
                        # print(sql)
                        # continue
                        # mycursor.execute(sql)
                        mycursor.execute("insert into essay (essay_id, title, address, keywords,description,\
                            key_gils,is_pixiv,author_id) values \
                            (%s,%s,%s,%s,%s,%s,%s,%s)", (essay_id, title, essaypath,\
                            ",".join(keywords),description, "",1,author_id))
                        
                        # mydb.commit()
                        # exit()

            # print(essay_id)
            # exit()
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


