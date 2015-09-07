# -*- coding: utf-8 -*-

__author__ = 'huyichao'


import urllib
import sys
import MySQLdb
import time
import redis


def extract_from_db():
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test1',port=3306, charset='utf8')
    cur=conn.cursor()
    t1 = time.clock()
    cur.execute("""SET NAMES utf8""")
    data = cur.execute("""select DISTINCT product from buy_offer where memberid = 'czlixingg';""")
    t2 = time.clock()
    print u'成功提取信息'
    print 'Time used=%fs'%(t2-t1)
    print 'the set has %d items' % data
    for i in range(data):
        yield cur.fetchone()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    r = redis.Redis()
    for ele in extract_from_db():
        quote_string = urllib.quote(ele[0].encode('gbk'))
        print quote_string
        print urllib.unquote(quote_string).decode('gbk')
        print 'http://s.1688.com/selloffer/offer_search.htm?keywords=' + quote_string
        r.lpush('cat_query:start_urls', 'http://s.1688.com/selloffer/offer_search.htm?keywords=' + quote_string)
        print '+1'

