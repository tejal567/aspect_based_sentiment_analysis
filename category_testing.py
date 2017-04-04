import pickle
import a
category=pickle.load(open('cats_dump.p', 'rb'))
txt = open('./database/Restaurants_Train.xml', 'r')
asdf = ['restaurant']
category_xml = {}
id = 0
freq_xml = {}
for line in txt:
	if '<sentence id' in line:
		line = line.strip()
		id = line[14:len(line)-2]
		category_xml[id] = []
	if '<aspectCategory category' in line:
		line = line.strip()
		term = ""
		for i in range (26,len(line)):
			if line[i] == '\"':
				break
			term = term + line[i]
		term = term.lower()
		category_xml[id].append(term)
		if term in freq_xml:
			freq_xml[term] = freq_xml[term] + 1
		else:
			freq_xml[term] = 1

accurate = 0
false_positive = 0
false_negative = 0
for sid in category_xml.keys():
	xc = list(set(category_xml[sid]) - set(asdf))
	yc = list(set(category[sid]) - set(asdf))
	false_negative = false_negative + len(list(set(xc) - set(yc)))
	false_positive = false_positive + len(list(set(yc) - set(xc)))
	accurate = accurate + len(list(set(xc) & set(yc)))
	# false_negative = false_negative + len(list(set(category_xml[sid]) - set(category[sid])))
	# false_positive = false_positive + len(list(set(category[sid]) - set(category_xml[sid])))
	# accurate = accurate + len(list(set(category[sid]) & set(category_xml[sid])))

print "category_xml=",len(freq_xml.keys())
#print category_xml
print "accurate=",accurate
print "false_positive=",false_positive
print "false_negative=",false_negative
accurate = float(accurate)
precision = (accurate/(accurate+false_positive))
recall = (accurate/(accurate+false_negative))
fscore = (2*precision*recall)/(precision+recall)
print "precision=",precision
print "recall=",recall
print "fscore=",fscore