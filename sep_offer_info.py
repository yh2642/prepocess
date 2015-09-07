# -*- coding: utf-8 -*-

import MySQLdb
import threading
import time


class dister(threading.Thread): #The timer class is derived from the class threading.Thread
	def __init__(self, key, zones):
		threading.Thread.__init__(self)
		self.zones = zones
		self.key = key

	def run(self):
		print u"开始进行线程:%s" % self.key
		for ele in self.zones:
			self.create_sub_tables(self.key)
			self.dist_table(self.key, ele)
			#self.out_table(ele)
		print u"线程%s 结束！！！" % self.key

	def out_table(self, zone):
		t1 = time.clock()
		print u'开始导出%s, %s' % (zone[0], zone[1])
		conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test1',port=3306, charset='utf8')
		cur=conn.cursor()
		path_name = '/Users/apple/Desktop/data' + zone[0]+ zone[1]+'.txt'
		cur.execute("""SET NAMES utf8""")
		cur.execute("""select memberid, category, sale,qualitylevel from offer_info where memberid >= %s and memberid < %s
		  				into outfile %s fields terminated by ',' lines terminated by '\r\n';""", (zone[0], zone[1], path_name))
		t2 = time.clock()
		print u'成功导入信息%s' % path_name
		print 'Time used=%fs'%(t2-t1)
		conn.commit()
		conn.close()

	def dist_table(self, key, zone):
		print u'开始导出%s, %s' % (zone[0], zone[1])
		t1 = time.clock()
		conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test2',port=3306, charset='utf8')
		cur=conn.cursor()
		cur.execute("""SET NAMES utf8""")
		cur.execute("""Insert into %s select * from test1.offer_info where memberid >= '%s' and memberid < '%s';""" % ('offer_info' + key, zone[0], zone[1]))
		t2 = time.clock()
		print u'成功导入数据库offer_info%s' % key
		print 'Time used=%fs'%(t2-t1)
		conn.commit()
		conn.close()


	def create_sub_tables(self, key):
		table_name = 'offer_info' + key
		#sql = '''DROP TABLE %s;''' % ele
		sql = '''CREATE TABLE %s(offerId CHAR(12) NOT NULL PRIMARY KEY,type CHAR(4) NOT NULL,memberid VARCHAR(22) NOT NULL,subject VARCHAR(100),category CHAR(9) NOT NULL,company VARCHAR(50) NOT NULL,sale mediumint,status VARCHAR(20), qualitylevel TINYINT)ENGINE=InnoDB DEFAULT CHARSET=utf8;''' % table_name
		conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test2',port=3306, charset='utf8')
		cur=conn.cursor()
		cur.execute(sql)
		conn.commit()
		print u'成功创建数据表: %s' % table_name
		conn.close()




def test(dict, num_of_threads = 8):
	threading_pool = []
	for key in dict:
		threading_pool.append(dister(key,dict[key]))

	while len(threading_pool):
		if len(threading_pool) >= num_of_threads:
			for indx in range(num_of_threads):
				thread = threading_pool.pop()
				thread.setDaemon(True)
				thread.start()
			thread.join()
			print u"%d个线程结束，继续！！！" % num_of_threads
		else:
			length = len(threading_pool)
			for ele in range(length):
				thread = threading_pool.pop()
				thread.setDaemon(True)
				thread.start()
			thread.join()
			print u'最后%d个线程' % length



def create_sub_tables(dict):
	name_ls = ['offer_info' + key for key in dict]
	for ele in name_ls:
		#sql = '''DROP TABLE %s;''' % ele
		sql = '''CREATE TABLE %s(offerId CHAR(12) NOT NULL PRIMARY KEY,type CHAR(4) NOT NULL,memberid VARCHAR(22) NOT NULL,subject VARCHAR(100),category CHAR(9) NOT NULL,company VARCHAR(50) NOT NULL,sale mediumint,status VARCHAR(20), qualitylevel TINYINT)ENGINE=InnoDB DEFAULT CHARSET=utf8;''' % ele
		conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test2',port=3306, charset='utf8')
		cur=conn.cursor()
		cur.execute(sql)
		conn.commit()
		print u'成功创建数据表: %s' %ele
		conn.close()


def det_table(memberid):
	if memberid[0] != 'b':
		return 'offer_info' + memberid[0]
	else:
		if memberid[:5] == 'b2b-1' or memberid[:5] =='b2b-2':
			return 'offer_info' + 'b2b' + str(int(memberid[4:7]) / 2)
		else:
			return 'offer_info' + 'b2b' + 'other'


'''
def out_part_table(dict):
	for key in dict:
		for zone in dict[key]:
			t1 = time.clock()
			conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test2',port=3306, charset='utf8')
			cur=conn.cursor()
			cur.execute("""SET NAMES utf8""")
			cur.execute("""select memberid, category, sale,qualitylevel from temp_info2 where memberid >= %s and memberid < %s
							into outfile %s fields terminated by ',' lines terminated by '\r\n';""", (zone[0], zone[1], 'c:/data_set/' + zone[0]+ zone[1]+'.txt'))
			t2 = time.clock()
			print u'成功导入信息%s' % key
			print 'Time used=%fs'%(t2-t1)
			conn.commit()
			conn.close()
'''







def gen_table_dict():
	'''
	:return: 对memberid进行分块处理，返回table_dict中，key为表名，value是区间
	'''
	# name list
	b2b_12 = ['b2b'+ str(ele/2) for ele in range(100, 300, 2)]
	# insert other zone
	b2b_12.append('b2bother')
	b2b_12.insert(0, 'b2bother')
	b2b_12.insert(0, 'a')
	char_ls = [chr(i) for i in range(99,123)]

	num_ls = [str(ele) for ele in range(10)]
	name_ls = []
	name_ls.extend(num_ls)
	name_ls.extend(b2b_12)
	name_ls.extend(char_ls)
	print name_ls #生成key list
	# index list   区间列表
	char_indx = [chr(i) for i in range(99,123)]
	b2b_ls_indx = ['b2b-' + str(ele) for ele in range(100, 300, 2)]
	b2b_ls_indx.append('b2b-300')
	b2b_ls_indx.insert(0,'b')
	b2b_ls_indx.insert(0,'a')
	num_indx = [str(ele) for ele in range(10)]
	indx_ls = []
	indx_ls.extend(num_indx)
	indx_ls.extend(b2b_ls_indx)
	indx_ls.extend(char_indx)
	indx_ls.append('zzzzz')
	print indx_ls

	# 生成区间字典
	table_dict = {}
	for indx in range(len(name_ls)):
		if name_ls[indx] in table_dict:
			table_dict[name_ls[indx]].append((indx_ls[indx], indx_ls[indx + 1]))
		else:
			table_dict[name_ls[indx]] = [(indx_ls[indx], indx_ls[indx + 1])]

	return table_dict


if __name__ == '__main__':
	#print gen_table_dict()
	#print table_dict
	#dict = {'b2b78': [('b2b-156', 'b2b-158')]}
	dict = gen_table_dict()
	#create_sub_tables(table_dict)
	#dist_part_table(dict)
	#t1 = time.clock()
	test(dict, num_of_threads=4)
	#out_part_table(table_dict)
	#t2 = time.clock()
	#print 'Time total used=%fs'%(t2-t1)


