import os
import shutil

from tools import *
from setting import *


"""
the program offer some webapi about essay and wait

"""
mycursor = mydb.cursor()

def random_essay(table):
    sql = "select * from %s where is_exist = 1 order by rand() limit 1" % (table)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    # print(result[0])
    return result
    address = result[0][3]
    return address

def id_essay(essay_id):
    sql = "select * from essay where essay_id = %s " % essay_id
    # print(sql)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result
    is_series = result[0][6]
    if is_series:
        series_front = result[0][7]
        series_left = result[0][8]
        series_right = result[0][9]
        return series_front, series_left, series_right
    
def mainimg(address):
    if os.path.exists(address[:-3]+'png'):
        print("ssss")
        shutil.copy2(address[:-3]+'png',"./static/images/mainimg.jpg")
    elif os.path.exists(address[:-3]+'jpg'):
        print("qqqq")
        shutil.copy2(address[:-3]+'jpg',"./static/images/mainimg.jpg")


def delete_essay(essay_id):
    sql = "update essay set is_exist = 0 where essay_id=%s" % essay_id
    # print(sql)
    
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
