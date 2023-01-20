import os

from setting import *
from tools import *

'''
The purpose of the program is constract information from wait dir to mysql 
'''

mycursor = mydb.cursor()
first = [ _ for _ in os.listdir(allwaitpath) if _ != ".DS_Store"]
# print(first)
for firstfile in first:
    firstpath = allwaitpath +r'/' + firstfile
    second = [ _ for _ in os.listdir(firstpath) if _ != ".DS_Store"]
    # print(second)
    for secondfile in second:
        secondpath = firstpath + r'/' + secondfile
        third = [ _ for _ in os.listdir(secondpath) if _ != ".DS_Store"]
        print(third)
        for thirdfile in third:
            thirdpath = secondpath + r'/' + thirdfile
            if os.path.isdir(thirdpath):
                fourth = [ _ for _ in os.listdir(thirdpath) if _ != ".DS_Store"]
                # print(fourth)
                for fourthfile in fourth:
                    fourthpath = thirdpath + r'/' + fourthfile
                    # print(fourthpath)
                    sql = "select * from wait where address = '%s'" % (fourthpath)
                    mycursor.execute(sql)
                    result = mycursor.fetchall()
                    if not result:
                        sql = "insert into wait (title, address) values \
                            ('%s','%s')"% (fourthfile,fourthpath)
                        print(sql)
                        mycursor.execute(sql)
                    # if os.path.isdir(fourthpath):
                    #     print(fourthpath)

            else:
                sql = "select * from wait where address = '%s'" % (thirdpath)
                # print(sql)
                mycursor.execute(sql)
                result = mycursor.fetchall()
                if not result:
                    sql = "insert into wait (title, address) values \
                        ('%s','%s')"% (thirdfile,thirdpath)
                    print(sql)
                    mycursor.execute(sql)
                # if os.path.isdir(thirdpath):
                #     print(thirdpath)
                    # print(fourthpath)
                # print(thirdpath)
mydb.commit()







