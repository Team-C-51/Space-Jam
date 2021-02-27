from tkinter import *
import pandas as pd
import sklearn as sk
import math as m
import sounddevice as sd
f=Tk()
f.title("Try")
f.geometry("1024x1024")
f.config(bg="yellow")
l1=Label(f,text="Duration of song in Seconds")
l1.grid(row=0,column=0)
txt=0
rec=0
name=0
def click():
    global txt
    txt=e1.get()
    txt=int(txt)
    mini=txt//60
    sec=txt-mini*60
    l1.configure(text=str(mini)+" mins"+str(sec)+" Seconds")
    e1.delete(0,END)
l2 =Label(f,text="To record your song click:")
l2.grid(row=1,column=0)
def click1():
    global rec
    Fs=16000
    d=txt+2
    l2.config(text="Start Speaking")
    rec=sd.rec(int(d*Fs),Fs,1,blocking=True)
    sd.wait()
    def click2():
        global rec
        sd.play(rec,Fs)
    b3=Button(f,text="Wanna hear yourself",command=click2)
    b3.grid(row=1,column=2)
    l2.config(text="Thanks")
def click2():
    name=e2.get()
    e2.delete(0,END)
    l3.config(text=name)
def click3():
    fan_fall=int(e3.get())
    e3.delete(0,END)
    l4.config(text=str(fan_fall))
def click4():
    theme=e4.get()
    e4.delete(0,END)
    l5.config(text=theme)
def click5():
    f=open("shape of you",'r')
    sent1=e5.get()
    sent2=f.read()
    wds1=sent1.split()
    wds2=sent2.split()
    totalwords=set(wds1).union(set(wds2))
    wdd1=dict.formkeys(total,0)
    wdd2=dict.formkeys(total,0)
    for word in sen1:
        wdd1[word]+=1
    for word in sen2:
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
            idfdict[word]=m.log(n/(float(val)+1))
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
    print(sim)
    
e1=Entry(f,width=30)
e1.grid(row=0,column=1)
e1.insert(0,"in seconds")
b1=Button(f,text="press",command=click)
b1.grid(row=0,column=2)
b2=Button(f,text="Click",command=click1)
b2.grid(row=1,column=1)
l3=Label(f,text="Enter your name:")
l3.grid(row=2,column=0)
e2=Entry(f,width=30)
e2.grid(row=2,column=1)
b3=Button(f,text="Click to enter",command=click2)
b3.grid(row=2,column=2)
l4=Label(f,text="Enter fan following in numbers:")
l4.grid(row=3,column=0)
e3=Entry(f,width=30)
e3.grid(row=3,column=1)
b4=Button(f,text="Click to enter",command=click3)
b4.grid(row=3,column=2)
l5=Label(f,text="Enter theme of your song:")
l5.grid(row=4,column=0)
e4=Entry(f,width=30)
e4.grid(row=4,column=1)
b5=Button(f,text="Click to enter",command=click4)
b5.grid(row=4,column=2)
l6=Label(f,text="Enter Lyrics:")
l6.grid(row=4,column=0)
e5=Entry(f,width=30)
e5.grid(row=4,column=1)
b6=Button(f,text="Click to enter",command=click5)
b6.grid(row=4,column=2)
f.mainloop()
