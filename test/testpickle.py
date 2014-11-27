#!/usr/bin/env python

import pickle

pk = open('person.info','r')
data1 = pickle.load(pk)
pk.close()
print data1
