import pandas as pd
import sklearn as sk
import math as m
sent1=input("Enter the 1st song")
sent2=input("Enter the 2nd song")
wds1=sent1.split()
wds2=sent2.split()
totalwords=set(wds1).union(set(wds2))
wdd1=dict.formkeys(total,0)
wdd2=dict.formkeys(total,0)
for word in wds1:
  wdd1[word]+=1
for word in wds2:
  wdd2[word]+=1
def computeTF(worddict,sen):
  tfdict={}
  leng=len(sen)
  for word,count in worddict.items():
    ifdict[word]=count/float(leng)
  return ifdict
tf1=computeTF(wdd1,sen1)
tf2=computeTF(wdd2,sen2)
def computeIDF(doclist):
  idfdict={}
  n=len(doclist)
  idfdict=dict.formkeys(doclist[0].keys(),0)
  for word,val in idfdict.items():
    idfdict[word]=m.log(n/(float(val)+1)))
  return idfdict
idfs=computeTDF([wdd1,wdd2])
def computeTFIDF(TF,IDF):
  tfidf={}
  for word,val in TF.items():
    ifidf[word]=val*idfs[word]
  return ifidf
TS1=computeTFIDF(tf1,idfs)
TS2=computeTFIDF(tf2,idfs)
v=0
w=0
sum=0
for i in totalwords:
  sum+=TS1[i]*TS2[i]
  v+=TS1[i]**2
  w+=TS2[i]**2
sim=sum/((v**0.5)*(w**0.5))
