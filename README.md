# Aspect_Based_Sentiment_Analysis

Additional Tools required:  
-- Stanford CoreNLP  
-- NLTK (WordNet)  

This repository contains all the codes required for Aspect Based Sentiment Analysis,  
a.py -> gets sentences from XML file. Name the file you want to run on in a.py.
Before running code download stanford corenlp server, extract it and place it inside corenlp-server directory. [Here is the link](http://nlp.stanford.edu/software/stanford-corenlp-full-2014-08-27.zip) 
1. Run corenlp.py which comes with Stanford CoreNLP Parser,  
2. Then in another terminal run client.py.
3. Run aspect_term_extracter.py  
4. Run pol.py. gives polarity of the aspect terms extracted from above step  
5. Run categorizer.py . Gives categories of the aspect terms.  
6. Run catpol.py. Gives polarity of the categories.  
7. Atlast run makeXML which creates an XML file with the sentences, aspect terms, polarities, categories and their polarities.  
