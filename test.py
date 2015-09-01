

import sep_offer_info
'''
f = open('memberIds.txt', 'r')
tt = open('tt.txt', 'w')

while True:
	member = f.readline()
	if len(member) == 0:
		break
	else:
		table_name = sep_offer_info.det_table(member.split()[0])
		tt.write(table_name + ' '+ member)

f.close()
tt.close()

'''

'''
dict = {'b2bother': [('b', 'b2b-100'), ('b2b-300', 'c')]}

sep_offer_info.part_table(dict)
'''

