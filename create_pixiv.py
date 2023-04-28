import os 
import time

from setting import *
from bookstool import divide


'''
The purpose of the program is constract information from essay dir to mysql 
'''


mycursor = mydb.cursor()
def create_user():
    mycursor = mydb.cursor()
    for k, v in returnwriters().items():
        print(v)
        sql = "select * from author where pixiv_id = %s " % k
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if not result:
            sql = "insert into author (pixiv_id,name) values (%s,'%s')" % (k,v)
            print(sql)
            mycursor.execute(sql)
        else:
            sql = "update author set name = '%s'" %v
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
writers  = os.listdir(pixiv_path)
for writer in writers:
    # print(writer)
    writerpath = os.path.join(pixiv_path, writer)
    if len(writer.split("｜")) > 1:
        print(writer)
        writeiddictionray[writer.split("｜")[0]] = writer.split("｜")[1]
        author_name = writer.split("｜")[1]
        author_pixiv_id = writer.split("｜")[0]
        # continue


        sql = "select * from author where pixiv_id = %s" %  author_pixiv_id
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if not result:
            sql = "insert into author (name, pixiv_id) values ('%s','%s')"% (author_name,author_pixiv_id)
            mycursor.execute(sql)
            mydb.commit()
            # exit()
        else:
            sql = "update author set name = '%s'" %author_name
            mycursor.execute(sql)
            mydb.commit()

        sql = "select id from author where name = '%s' and pixiv_id = %s" % (author_name, author_pixiv_id)
        mycursor.execute(sql)
        author_id = mycursor.fetchall()[0][0]

        print(author_id)
        # exit()
        series  = os.listdir(writerpath)
        # print(series)
        for sery in series:
            serypath =  os.path.join(writerpath,sery)
            if  os.path.isdir(serypath):
                sql = "select * from series where name = '%s' and author_id = %s" % (sery, author_id)
                print(sql)
                mycursor.execute(sql)
                result = mycursor.fetchall()
                if not result:
                    sql = "insert into series (name, address,author_id) values ('%s','%s',%s)"% (sery, os.path.join(writer,sery),author_id)
                    mycursor.execute(sql)
                    # exit()
                    mydb.commit()
                sql = "select * from series where name = '%s' and author_id = %s" % (sery, author_id)
                print(sql)
                mycursor.execute(sql)
                series_id = mycursor.fetchall()[0][0]

                essays  = os.listdir(serypath)
                # print(sery + "   series")
                # print(essays)
                if ".DS_Store" in essays:
                    essays.remove(".DS_Store")
                for essay in essays: 
                    if essay[-3:] != "txt":
                        essays.remove(essay)
                essays.sort(key=lambda x:int(x.split("｜")[0][1:]))
                series_home = 0
                for index, essay in enumerate(essays):
                    
                    essaypath = os.path.join(serypath , essay)

                    # print(os.path.join(writer,sery,essay))
                    # exit()
                    if essaypath[-3:] == "txt":
                        pixiv_id = essaypath.split("｜")[-1][:-4]
                        # print(pixiv_id)
                        title, website, description, keywords, content = divide(essaypath)
                        for one in keywords:
                            if one in allkeyword:
                                allkeyword[one] += 1
                            else :
                                allkeyword[one] = 1
                        # continue
                        # if pixiv_id == "17871937":
                        #     print(title, website, description, keywords)
                        #     exit()
                        # return content
                        # print(essaypath)
                        # print(pixiv_id)
                        # with open(essaypath,"r") as f:
                        #     t=f.read()
                        # print(t)
                        # continue
                        sql = "select * from essay where pixiv_id = %s and title = '%s'" % (pixiv_id, title)
                        # print(sql)
                        mycursor.execute(sql)
                        result = mycursor.fetchall()
                        # print(index )
                        if not result:
                            if index == 0 :
                                series_home, series_left = pixiv_id, pixiv_id
                            else:
                                series_left = essays[index-1].split("｜")[-1][:-4]
                            if index < len(essays)-1:
                                series_right = essays[index+1].split("｜")[-1][:-4]
                            else:
                                series_right = pixiv_id
                            # print(series_home,series_left,series_right)
                            sql = "insert into essay (pixiv_id, title, address, keywords,description,series_id,\
                                series_name,series_home,series_left,series_right,key_girls,author_id,author_name) values \
                                (%s,'%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s','%s','%s')"% (pixiv_id, title, os.path.join(writer,sery,essay),\
                                ",".join(keywords),description[:500], series_id, sery,series_home, series_left,series_right,"",author_id,author_name)
                            
                            print(sql)
                            # print(pixiv_id,essaypath,sery,series_home, series_left,series_right,)
                            # continue
                            mycursor.execute(sql)
                            # mydb.commit()
                            # exit()
                            continue
            else:
                essay = sery
                essaypath = serypath
                sql = "select * from series where name = '单篇合集' and author_id = %s" %  author_id
                mycursor.execute(sql)
                result = mycursor.fetchall()
                if not result:
                    sql = "insert into series (name, address,author_id) values ('单篇合集','%s',%s)"% (os.path.join(writer,sery),author_id)
                    mycursor.execute(sql)
                    mydb.commit()
                sql = "select * from series where name = '单篇合集' and author_id = %s" %  author_id
                print(sql)
                mycursor.execute(sql)
                series_id = mycursor.fetchall()[0][0]
                if essaypath[-3:] == "txt":
                        # print(essaypath)
                    pixiv_id = essaypath.split("｜")[-1][:-4]
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
                    sql_title = title.replace("'","''")
                    sql = "select * from essay where pixiv_id = '%s' and title = '%s'" % (str(pixiv_id), sql_title)
                    print(sql)
                    # print(essaypath)
                    mycursor.execute(sql)
                    # r = mycursor.execute("select id from essay where pixiv_id = %s and title = %s",(str(pixiv_id), title,))
                    result = mycursor.fetchall()
                    # exit()
                    # result = True
                    if not result:
                        sql = "insert into essay (pixiv_id, title, address, keywords,description,series_id,\
                            series_name,key_girls,author_id,author_name) values \
                            (%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"% (pixiv_id, sql_title, os.path.join(writer,sery),\
                            ",".join(keywords),description[:500], series_id, sery,"",author_id,author_name)
                        print(sql)
                        mycursor.execute(sql)
                        
                        # mydb.commit()
                        # exit()

            # print(pixiv_id)
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
# create_user()     



# if __name__ == "__main__":
#     create_user()
