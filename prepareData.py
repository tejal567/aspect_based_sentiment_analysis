txt = open('./database/Restaurants_Train.xml', 'r')

def polarity(pol):
	if pol == 'negative':
		return -1
	if pol == 'positive':
		return 1
	return 0

class sentence():
	def __init__(self):
		self.id1 = 0
		self.text = ''
		self.aspects = []
	def asp_pol(self, c , pol):
		print c
		print polarity(pol)
		self.aspects.append((c,polarity(pol)))

sent = sentence()
new1 = False

sentences = []

for line in txt:
	line = line.strip()
	if '</aspectTerms>' in line:
		new1 = False
	if new1:
		line = line.replace('<aspectTerm term="','')
		line = line.replace('" polarity="', ' ')
		line = line[:line.find('"')]
		x = line.split(" ")
		print x
		print x[-2],x[-1]
		sent.asp_pol(x[-2],x[-1])
	if '<sentence id' in line:
		sent = sentence()
		line = line.strip()
		line = line.replace('<sentence id="','')
		line = line.replace('">','')
		x = int(line)
		sent.id1 = x
	if '<text>' in line:
		line = line.replace('<text>','')
		line = line.replace('</text>','')
		sent.text = line
	if '<aspectTerms>' in line:
		new1 = True
	if '</sentence>' in line:
		sentences.append(sent)

train_label = []

for sent in sentences:
	we = []
	x = sent.text.split(' ')
	for xi in sent.aspects:
		_,pol = xi
		train_label.append(pol)

train_x = []
maxi = 0
for sent in sentences:
	x = sent.text.split(' ')
	for xi in sent.aspects:
		c,pol = xi
		t = sent.text+" "+c.replace('(','').replace('.','')
		# print t
		train_x.append(str(t))
		maxi = max(maxi,len(t.split(' ')))