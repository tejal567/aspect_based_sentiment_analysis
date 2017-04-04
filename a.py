import os
import sys
text=[]
txt = open('./database/Restaurants_Train.xml', 'r')
sent=[]
sentence = {}
id = 0
for line in txt:
	if '<sentence id' in line:
		#print '\n'+line	
		#print "going to sent:",line
		line = line.strip()
		sent.append(line)
		id = line[14:len(line)-2]
	if '<text>' in line:
		
		line = line.replace('</text>', '')
		line = line.replace('<text>','')
		line = line.replace('pound', 'kilo')
		line = line.replace('#','')
		#print "going to text::",line
		line=line.strip()
		text.append(line)
		sentence[id] = line