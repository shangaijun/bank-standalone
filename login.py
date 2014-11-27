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
	f_sec = open("sec.db")
	r_user,r_pass=f_sec.readline().split()
	counter=0
	while True:
		#user_input=getpass.getuser("Please input your username: ")
		user_input=raw_input("Please input your username: ").strip()
		pass_input = getpass.getpass("Please input your password: ")
		if (user_input == r_user) and  (pass_input == r_pass):
			return True
		else:
			print "Wrong username or password,please try again"
			counter+=1
			
		if(counter>=3):
			lock.lock('person.info')
			print "You use wrong username or password for 3 times,I will lock your account,please contact with BANK"
			sys.exit()
	




if __name__=='__main__':
	print login()
