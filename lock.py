#!/usr/bin/python

"""
If you input wrong password for three times,use this script to lock the account 
"""
def islock(file):
	f_person = open(file)
	informations = f_person.readlines()
	f_person.close()

	for info in informations[1:]:
		info_s = info.strip().split()	
		if (info_s[4].lower() == "l"):
			return True
		else:
			return False

	

def lock(file):
	new_informations = []
	f_personinfo = open(file)
	informations = f_personinfo.readlines()
	f_personinfo.close()
	
	new_informations.append(informations[0].strip())

	for infor in informations[1:]:
		infor = infor.strip()
		infor_s = infor.split()

		infor_s[4] = "L"
		new_informations.append('\t'.join(infor_s))

	f_personinfo = open(file,'w')
	f_personinfo.write("\n".join(new_informations))
	f_personinfo.flush()
	f_personinfo.close()
	
if __name__ == "__main__":
	lock('person.info')
	print islock('person.info')
