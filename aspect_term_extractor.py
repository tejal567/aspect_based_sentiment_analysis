import pickle
import re
import string
import a

sentence=pickle.load(open('sentence_dump.p','rb'))
noun = ["NN", "NNS", "NNP", "NNPS"]
asdict = {}
adjective = ["JJ", "JJR", "JJS"]
freq = {}
used_adj = []
single_asdict = {}

def extractor(words = {}, sid=0):
	aspect_terms=[]
	for word in words.keys():
		if words[word]['pos_tag'] in noun:
			asd = 0
			for char in word:
				if not re.search('[a-zA-Z]', char):
					asd = 1
					break
			if asd == 1:
				#print word,"asd"
				continue
			word1 = word.lower()
			aspect_terms.append(word1)
			if word1 in freq:
				freq[word1] = freq[word1] + 1
			else:
				freq[word1] = 1
	return aspect_terms

def change_order():
	for sid in a.sentence.keys():
		#print a.sentence[sid]
		a.sentence[sid] = a.sentence[sid].replace(',',' ')
		a.sentence[sid] = a.sentence[sid].replace('.',' ')
		a.sentence[sid] = a.sentence[sid].replace("'",' ')
		a.sentence[sid] = a.sentence[sid].replace(':',' ')
		a.sentence[sid] = a.sentence[sid].replace('!',' ')
		a.sentence[sid] = a.sentence[sid].replace('?',' ')
		a.sentence[sid] = a.sentence[sid].replace('"',' ')
		a.sentence[sid] = a.sentence[sid].replace('(',' ')
		a.sentence[sid] = a.sentence[sid].replace(')',' ')
		a.sentence[sid] = a.sentence[sid].replace('-',' ')
		a.sentence[sid] = a.sentence[sid].replace('+',' ')
		a.sentence[sid] = a.sentence[sid].lower()
		words = a.sentence[sid].split()
		l = [""] * len(words)
		for i in range (0,len(words)):
			if words[i][len(words[i])-2:len(words[i])] == "'s":
				words[i] = words[i][0:len(words[i])-2]
				#print words[i]
		for word in asdict[sid]:
			if word in words:
				#print words.index(word),word
				l[words.index(word)] = word
		asdict[sid] = []
		x = ""
		for word in l:
			if word != "":
				x = x + word + " "
				
			else:
				if x == "":
					continue
				z = x[0:len(x)-1]
				
				
				y = z.split()
				asdict[sid].append(y[len(y) - 1])
				for key in y:
					freq[key] -= 1
				if y[len(y) - 1] in freq:
					freq[y[len(y) - 1]] = freq[y[len(y) - 1]] + 1
				else:
					freq[y[len(y) - 1]] = 1 
				x = ""
		if x!= "":
			z = x[0:len(x)-1]
			
			y = z.split()
			asdict[sid].append(y[len(y) - 1])
			for key in y:
				freq[key] -= 1
			if y[len(y) - 1] in freq:
				freq[y[len(y) - 1]] = freq[y[len(y) - 1]] + 1
			else:
				freq[y[len(y) - 1]] = 1

def change_order1():
	for sid in a.sentence.keys():
		#print a.sentence[sid]
		a.sentence[sid] = a.sentence[sid].replace(',',' ')
		a.sentence[sid] = a.sentence[sid].replace('.',' ')
		a.sentence[sid] = a.sentence[sid].replace("'",' ')
		a.sentence[sid] = a.sentence[sid].replace(':',' ')
		a.sentence[sid] = a.sentence[sid].replace('!',' ')
		a.sentence[sid] = a.sentence[sid].replace('?',' ')
		a.sentence[sid] = a.sentence[sid].replace('"',' ')
		a.sentence[sid] = a.sentence[sid].replace('(',' ')
		a.sentence[sid] = a.sentence[sid].replace(')',' ')
		a.sentence[sid] = a.sentence[sid].replace('-',' ')
		a.sentence[sid] = a.sentence[sid].replace('+',' ')
		a.sentence[sid] = a.sentence[sid].lower()
		words = a.sentence[sid].split()
		l = [""] * len(words)
		for i in range (0,len(words)):
			if words[i][len(words[i])-2:len(words[i])] == "'s":
				words[i] = words[i][0:len(words[i])-2]
				#print words[i]
		for word in asdict[sid]:
			if word in words:
				#print words.index(word),word
				l[words.index(word)] = word
		asdict[sid] = []
		x = ""
		for word in l:
			if word != "":
				x = x + word + " "
				
			else:
				if x == "":
					continue
				z = x[0:len(x)-1]
				
				
				y = z.split()
				asdict[sid].append(z)
				for key in y:
					freq[key] -= 1
				
				x = ""
		if x!= "":
			z = x[0:len(x)-1]
			
			y = z.split()
			asdict[sid].append(z)
			for key in y:
				freq[key] -= 1

def delete_false():
	z = []
	for word in freq.keys():
		if ' ' in word:
			continue
		if freq[word] < 10:
			z.append(word)
	x = freq.keys()
	for sid in asdict.keys():
		asdict[sid] = list(set(asdict[sid])-set(z))

def store_adjv():
	for sid in a.sentence.keys():
		a.sentence[sid] = a.sentence[sid].replace(',',' ')
		a.sentence[sid] = a.sentence[sid].replace('.',' ')
		a.sentence[sid] = a.sentence[sid].replace("'",' ')
		a.sentence[sid] = a.sentence[sid].replace(':',' ')
		a.sentence[sid] = a.sentence[sid].replace('!',' ')
		a.sentence[sid] = a.sentence[sid].replace('?',' ')
		a.sentence[sid] = a.sentence[sid].replace('"',' ')
		a.sentence[sid] = a.sentence[sid].replace('(',' ')
		a.sentence[sid] = a.sentence[sid].replace(')',' ')
		a.sentence[sid] = a.sentence[sid].replace('-',' ')
		a.sentence[sid] = a.sentence[sid].replace('+',' ')
		x = a.sentence[sid].lower()
		words = x.split()
		for aspect in asdict[sid]:
			to_use = aspect
			if ' ' in aspect:
				to_use = aspect.split(' ')[0]
			#print to_use
			#print words
			ind = words.index(to_use)
			distance = 1000
			ad = ""
			for y in sentence[sid].keys():
				#print word
				if sentence[sid][y]['pos_tag'] in adjective:
					#print " hi"
					word = y.lower()
					if word in words and abs(words.index(word) - ind) < distance:
						distance = abs(words.index(word) - ind)
						ad = word
						#print "sd"
			if ad not in used_adj and len(ad) > 0:
				used_adj.append(ad)

def create_single():
	#print asdict
	for sid in asdict.keys():
		single_asdict[sid] = []
		#print asdict['42'],sid
		for aspect in asdict[sid]:
			if ' ' not in aspect:
				single_asdict[sid].append(aspect)
			else:
				x = aspect.split()
				for y in x:
					single_asdict[sid].append(y)
	#print asdict

def infrequent_aspects():
	for sid in a.sentence.keys():
		x = a.sentence[sid].lower()
		words = x.split()
		for word in words:
			if word in used_adj:
				ind = words.index(word)
				distance = 1000
				ad = ""
				for y in sentence[sid].keys():
					if sentence[sid][y]['pos_tag'] in noun:
						word1 = y.lower()
						asd = 0
						for char in word1:
							if not re.search('[a-zA-Z]', char):
								asd = 1
								break
						if asd == 1:
							#print word,"asd"
							continue
						if word1 in words and abs(words.index(word1) - ind) < distance:
							distance = abs(words.index(word1) - ind)
							ad = word1
				if ad not in single_asdict[sid] and len(ad)>0:
					asdict[sid].append(ad)
					#print ad


if __name__ == "__main__":
	for sid in sentence.keys():
		aspects=extractor(sentence[sid], sid)
		asdict[sid]=aspects
	#single_asdict = asdict
	#change_order()
	
	delete_false()
	store_adjv()
	create_single()
	infrequent_aspects()
	print freq
	#print used_adj
	pickle.dump(asdict,open('aspect_dump_new.p','wb'))