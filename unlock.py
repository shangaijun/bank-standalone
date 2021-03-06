#!/usr/bin/python

"""
If your credit is locked,that means your credit's status is l or L
This program could unlock your credit's status to unlock(U)
"""

def unlock(file):
	new_informations = []
	f_personinfo = open(file)
	informations = f_personinfo.readlines()
	f_personinfo.close()
	
	new_informations.append(informations[0].strip())

	for infor in informations[1:]:
		infor = infor.strip()
		infor_s = infor.split()

		if infor_s[4].lower() == "l":
			infor_s[4] = "U"
			new_informations.append('\t'.join(infor_s))
			continue
		new_informations.append(infor)

	f_personinfo = open(file,'w')
	f_personinfo.write("\n".join(new_informations))
	f_personinfo.flush()
	f_personinfo.close()
	
if __name__ == "__main__":
	unlock('person.info')
