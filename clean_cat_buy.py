# -*- coding: utf-8 -*-

__author__ = 'huyichao'


import urllib
import sys
import MySQLdb
import time

def extract_from_db():
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test1',port=3306, charset='utf8')
    cur=conn.cursor()
    t1 = time.clock()
    cur.execute("""SET NAMES utf8""")
    data = cur.execute("""select buyofferId, product, amount,category from buy_offer where memberid = 'czlixingg';""")
    t2 = time.clock()
    print u'成功提取信息'
    print 'Time used=%fs'%(t2-t1)
    print 'the set has %d items' % data
    for i in range(data):
        yield cur.fetchone()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    for ele in extract_from_db():
        print urllib.quote(ele[1].encode('gbk'))

