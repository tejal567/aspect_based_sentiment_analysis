import os
import pickle

cats_dump = pickle.load(open('cats_dump.p','r'))
cats_pol = pickle.load(open('cats_pol.p','r'))

list1=[u'food', u'ambience', u'price', u'restaurant', u'service']
count = dict(zip(list1,[0,0,0,0,0]))
value = dict(zip(list1,[0,0,0,0,0]))

for dump,pol in zip(cats_dump.iterkeys(), cats_pol.iterkeys()):
	# print cats_pol[pol]
	if len(cats_pol[pol]):
		for i,j in zip(cats_pol[pol],cats_dump[dump]):
			# print i,j
			count[j] += 1
			value[j] += i

print count
print value