from nltk.corpus import wordnet
import pickle


aspect_list=pickle.load(open('aspect_dump_new.p','rb'))
polarities = pickle.load(open('polarities.p','r'))


def polarity(pol):
	if pol == 'negative':
		return -1
	if pol == 'positive':
		return 1
	return 0


list1=[u'food', u'ambience', u'price', u'restaurant', u'service']
cats_dict= dict()
cats_pol = dict()
for _,sid in zip(polarities.iterkeys(),aspect_list.iterkeys()):
	aspects = aspect_list[sid]
	pol = polarities[sid]
	print aspects,pol
	cats_dict[sid] = []
	cats_pol[sid] = []
	for word,p in zip(aspects, pol.iterkeys()):
		acc = 0
		cat = ''
		#print word
		for wo in list1:
			w1 = wordnet.synsets(word)
			w2 = wordnet.synsets(wo)
			if len(w1) == 0 or len(w2) == 0:
				continue
			word1 = w1[0]
			word2 = w2[0]
			s = word1.wup_similarity(word2)
			if s > acc:
				acc = s
				cat = wo
		if cat not in cats_dict[sid] and acc > 0.4:
			cats_dict[sid].append(cat)
			temp = pol[p]
			print temp
			if temp in cats_pol[sid]:
				cats_pol[sid] += polarity(temp)
			else:
				cats_pol[sid].append(polarity(temp))
			print sid,word,cat,acc

#print cats_dict
pickle.dump(cats_dict,open('cats_dump.p','wb'))
pickle.dump(cats_pol,open('cats_pol.p','wb'))