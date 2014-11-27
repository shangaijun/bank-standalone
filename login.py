#!/usr/bin/env python

import getpass
import sys
import lock

def login():
	if(lock.islock('person.info') == True):
		print "Your account is locked,please contact BANK to unlock"
		sys.exit()
	else:
		pass
	f_sec = open("person.info")
	informations=f_sec.readlines()
	f_sec.close()
	counter=0
	while True:
		user_input=raw_input("Please input your account: ").strip()
		pass_input = getpass.getpass("Please input your password: ")
		counter+=1
		for info in informations[1:]:
			r_user,r_pass=info.strip().split()[0:2]
			print r_user,r_pass
			if (user_input == r_user) and  (pass_input == r_pass):
				return True
			else:
				print "Wrong account or password,please input again"
			
		if(counter>=3):
			lock.lock('person.info')
			print "You use wrong account or password for 3 times,I will lock your account,please contact with BANK"
			sys.exit()
	




if __name__=='__main__':
	print login()
