import pickle
import a
aspect=pickle.load(open('aspect_dump_new.p', 'rb'))
txt = open('./database/Restaurants_Train.xml', 'r')
aspect_xml = {}
id = 0
freq_xml = {}
count = 0
for line in txt:
	if '<sentence id' in line:
		line = line.strip()
		id = line[14:len(line)-2]
		aspect_xml[id] = []
	if '<aspectTerm term' in line:
		line = line.strip()
		term = ""
		for i in range (18,len(line)):
			if line[i] == '\"':
				break
			term = term + line[i]
		term = term.lower()
		if ' ' in term:
			count += 1
		aspect_xml[id].append(term)
		if term in freq_xml:
			freq_xml[term] = freq_xml[term] + 1
		else:
			freq_xml[term] = 1

accurate = 0
false_positive = 0
false_negative = 0
for sid in aspect_xml.keys():
	false_negative = false_negative + len(list(set(aspect_xml[sid]) - set(aspect[sid])))
	false_positive = false_positive + len(list(set(aspect[sid]) - set(aspect_xml[sid])))
	#print sid,list(set(aspect_xml[sid]) - set(aspect[sid]))
	accurate = accurate + len(list(set(aspect[sid]) & set(aspect_xml[sid])))

print "aspect_xml=",len(freq_xml.keys())
print count
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