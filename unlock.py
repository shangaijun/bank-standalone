#!/usr/bin/python

def unlock(personinfo):
	f_personinfo = open(personinfo)
	informations =f_personinfo.readlines()[1:]
	f_personinfo.close()

	for infor in informations:
		infor_s = infor.split()	
		#print infor_s[4].lower()
		if infor_s[4].lower() == "l":
			#print "you are locked"
			infor_s[4] = "U"
	

unlock('person.info')
	
