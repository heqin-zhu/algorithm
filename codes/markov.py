from random import randint
import re


class markov:
	def __init__(self,txt):
		self.words= self.clean(txt)
		self.dic = self.getDic(self.words)
	def clean(self,text):
	    text = text.replace("\n", " "); 
	    text = text.replace("\"", ""); 
	 
	    # 保证每个标点符号都和前面的单词在一起 
	    # 这样不会被剔除，保留在马尔可夫链中 
	    punctuation = [',', '.', ';',':'] 
	    for symbol in punctuation: 
	        text = text.replace(symbol, symbol+" "); 
	 
	    return  re.split(' +',text)
		
	def  getDic(self,words):
		dic = {}
		end = len(words)
		for i in range(1,end):
			if words[i-1] not in dic:
				dic[words[i-1]] = {words[i]:1}
			elif words[i] not in dic[words[i-1]]:
				dic[words[i-1]][words[i]] = 1
			else: dic[words[i-1]][words[i]] +=1
		return dic
	def getSum(self,dic):
		if '%size' not in dic:
			dic['%size'] = sum(list(dic.values()))
		return dic['%size']
	def nextWord(self,word):
		k = randint(1,self.getSum(self.dic[word]))
		for i,j in self.dic[word].items():
			k-=j
			if k<=0:return i
	def genSentence(self,begin = 'I',length = 30):
		li = [begin]
		nextWord= begin
		for  i in range(1,length):
			nextWord= self.nextWord(nextWord)
			li.append(nextWord)
		return ' '.join(li)
