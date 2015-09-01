# -*- coding: utf-8 -*-

import sys
import time
import json


def read_input(file):
	for line in file:
		yield line.rstrip()



def output_result(current_company, done_cat, done_count):
	for indx in range(len(done_cat)):
		print "%s\t%s\t%f" % (current_company, done_cat[indx], done_count[indx])


def plan1():
	current_company = None
	current_no = 0
	current_cat = ''
	company_total = 0
	done_cat = []
	done_count = []
	t1 = time.clock()
	for line in read_input(sys.stdin):
		ls = line.split(',')
		company = ls[0]
		cat = ls[1]
		level = int(ls[3])
		if company == current_company:
			if current_cat == cat:
				current_no += level
			else:
				done_cat.append(current_cat)
				done_count.append(current_no)
				# 在每个公司的每个cat计算完之后计算总数
				company_total += current_no
				current_cat = cat
				current_no = level
		else:
			if current_company:
				# update
				done_cat.append(current_cat)
				done_count.append(current_no)
				# 在每个公司的每个cat计算完之后计算总数
				company_total += current_no
				done_count = [ele / float(company_total) for ele in done_count]
				print sum(done_count)
				output_result(current_company, done_cat, done_count)
			print '---------------------------------------------------'
			done_cat = []
			done_count = []
			current_company =company
			current_cat = cat
			company_total = 0
			current_no = level
	done_count = [ele / float(company_total) for ele in done_count]
	print sum(done_count)
	output_result(current_company, done_cat, done_count)
	t2 = time.clock()
	print 'Time total used=%fs'%(t2-t1)


def plan2():
	f = open('to_mysql.txt', 'a')
	current_company = None
	company_total = 0
	company_dict = {}
	t1 = time.clock()
	for line in read_input(sys.stdin):
		ls = line.split(',')
		company = ls[0]
		cat = ls[1]
		level = int(ls[3])
		if company == current_company:
			if cat in company_dict:
				company_dict[cat] += level
				company_total += level
			else:
				company_dict[cat] = level
				company_total += level
		else:
			if current_company:
				# 在每个公司的每个cat计算完之后计算总数
				for key in company_dict:
					f.write(current_company + ' ' + key + ' ' + str(company_dict[key] / float(company_total)) + '\n')
					#print current_company, key, company_dict[key] / float(company_total)
				company_dict['memberid'] = current_company
				json.dump(company_dict, open('to_mongodb.json', 'a'))
			print '---------------------------------------------------'
			company_dict = {}
			current_company =company
			company_dict[cat] = level
			company_total = level
	for key in company_dict:
		f.write(current_company + ' ' + key + ' ' + str(company_dict[key] / float(company_total)) + '\n')
	json.dump(company_dict, open('to_mongodb.json', 'a'))
		#print current_company, key, company_dict[key] / float(company_total)
	f.close()
	t2 = time.clock()

	print 'Time total used=%fs'%(t2-t1)

#plan1()
plan2()


