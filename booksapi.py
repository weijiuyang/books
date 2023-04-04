import os
import shutil

from bookstool import *
from setting import *


"""
the program offer some webapi about essay and wait

"""
mycursor = mydb.cursor()


""""  随机挑选一个文章 """
def random_essay(table):
    sql = "select * from %s where is_exist = 1 order by rand() limit 1" % (table)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    # print(result)
    return result

""""  根据文章ID去数据库取相关信息 """
def id_essay(id):
    sql = "select * from essay where id = %s " % id
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result
    
def mainimg(address):
    if os.path.exists(address[:-3]+'png'):
        shutil.copy2(address[:-3]+'png',pythonpath + "./static/images/mainimg.jpg")
    elif os.path.exists(address[:-3]+'jpg'):
        shutil.copy2(address[:-3]+'jpg',pythonpath  + "/static/images/mainimg.jpg")


def delete_essay(essay_id):
    sql = "update essay set is_exist = 0 where essay_id=%s" % essay_id
    mycursor.execute(sql)
    mydb.commit()
    
def delete_wait(id):
    sql = "update wait set is_exist = 0 where id=%s" % id
    mycursor.execute(sql)
    mydb.commit()

def save_wait(id):
    sql = "update wait set is_exist = 2 where id=%s" % id
    mycursor.execute(sql)
    mydb.commit()

def coadvance(essay_id):
    sql = "select id,title from essay where series_id = (select series_id from essay\
                where id = %s)" % essay_id
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result






