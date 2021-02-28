from tkinter import *
import pandas as pd
import sklearn as sk
import math as m
import sounddevice as sd
import speech_recognition as sr
import pyaudio
import matplotlib.pyplot as plt
import numpy 
from matplotlib import pyplot
f=Tk()
f.title("Try")
f.geometry("500x300")
bg=PhotoImage(file="TVBP6Y.png")
l=Label(f,image=bg)
l.place(x=0,y=0)
l1=Label(f,text="Duration of song in Seconds")
l1.grid(row=0,column=0)
txt=0
rec=0
name=0
score=0
def click():
    global score
    global txt
    txt=e1.get()
    txt=int(txt)
    mini=txt//60
    sec=txt-mini*60
    l1.configure(text=str(mini)+" mins"+str(sec)+" Seconds")
    e1.delete(0,END)
    if 200<txt<=220:
        score+=15
    elif 220<txt<=240:
        score+=13
    elif 180<txt<=200:
        score+=11
    elif 160<txt<=180:
        score+=9
    elif 260<txt<=300:
        score+=7
    elif 240<txt<=260:
        score+=9
    else:
        score+=5
l2 =Label(f,text="To record your song click:")
l2.grid(row=1,column=0)
def click1():
    global score
    global rec
    Fs=16000
    d=txt+2
    l2.config(text="Start Speaking")
    rec=sd.rec(int(d*Fs),Fs,1,blocking=True)
    sd.wait()
    plt.plot(rec); plt.title('Recorded Sound')
    def click2():
        global rec
        sd.play(rec,Fs)
    def click3():
        global rec
        rec=numpy.arange(1, 100, 0.5)
        signalAmplitude = numpy.sin(rec) 
        pyplot.plot(rec, signalAmplitude, color ='green') 
        pyplot.xlabel('Time') 
        pyplot.ylabel('Amplitude') 
        pyplot.title("Signal")  
        pyplot.magnitude_spectrum(signalAmplitude, color ='green')
        pyplot.title("Magnitude Spectrum of the Signal") 
        pyplot.show()
    b3=Button(f,text="Wanna hear yourself",command=click2)
    b3.grid(row=1,column=2)
    b4=Button(f,text="Your amplitute variations graph:",command=click3)
    b4.grid(row=1,column=3)
    l2.config(text="Thanks")
def click2():
    name=e2.get()
    e2.delete(0,END)
    l3.config(text=name)
def click3():
    global score
    fan_fall=int(e3.get())
    e3.delete(0,END)
    l4.config(text=str(fan_fall))
    if 200000000<=fan_fall:
        score+=35
    elif 50000000<=fan_fall<200000000:
        score+=33
    elif 5000000<=fan_fall<50000000:
        score+=31
    elif 500000<=fan_fall<5000000:
        score+=28
    elif 150000<=fan_fall<500000:
        score+=24
    elif 50000<=fan_fall<150000:
        score+=20
    elif 20000<=fan_fall<50000:
        score+=15
    elif 5000<=fan_fall<20000:
        score+=10
    elif 1000<=fan_fall<5000:
        score+=8
    else:
        score+=5
def click4():
    global score
    theme=e4.get()
    e4.delete(0,END)
    l5.config(text=theme)
    if theme=="pop":
        score+=5
    elif theme=="love":
        score+=4.5
    elif theme=="sad":
        score+=4
    elif theme=="rock":
        score+=3.5
    else:
        score+=3
def click5():
    global score
    sent1=e5.get()
    sent2="The club isnt the best place to find a lover So the bar is where I go (Mm, mm) Me and my friends at the table doing shots Drinking fast, and then we talk slow (Mm, mm) You come over and start up a conversation with just me And trust me, Ill give it a chance now (Mm, mm) Take my hand, stop Put Van the Man on the jukebox And then we start to dance And now Im singing like Girl, you know I want your love Your love was handmade for somebody like me Come on now, follow my lead I may be crazy, dont mind me Say Boy, let's not talk too much Grab on my waist and put that body on me Come on now, follow my lead Come, come on now, follow my lead (Mm, mm) Im in love with the shape of you We push and pull like a magnet do Although my heart is falling too Im in love with your body Last night you were in my room And now my bed sheets smell like you Every day discovering something brand new Oh, Im in love with your body Oh I, oh I, oh I, oh I Oh, Im in love with your body Oh I, oh I, oh I, oh Oh, Im in love with your body Oh  , oh I, oh I, oh I Oh, Im in love with your body Every day discovering something brand new Im in love with the shape of you One week in we let the story begin Were going out on our first date (Mm, mm) But you and me are thrifty So go all-you-can-eat Fill up your bag, and I fill up a plate (Mm, mm) We talk for hours and hours about the sweet and the sour And how your family is doing okay (Mm, mm) And leave and get in a taxi, then kiss in the back seat Tell the driver make the radio play And Im singing like Girl, you know I want your love Your love was handmade for somebody like me Come on now, follow my lead I may be crazy, dont mind me Say Boy, let's not talk too much Grab on my waist and put that body on me Come on now, follow my lead Come, come on now, follow my lead (Mm, mm) Im in love with the shape of you We push and pull like a magnet do Although my heart is falling too Im in love with your body Last night you were in my room And now my bed sheets smell like you Every day discovering something brand new Oh, Im in love with your body Oh I, oh I, oh I, oh I Oh, Im in love with your body Oh I, oh I, oh I, oh I Oh, Im in love with your body Oh I, oh I, oh I, oh I Oh, Im in love with your body Every day discovering something brand new Im in love with the shape of you Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Im in love with the shape of you We push and pull like a magnet do Although my heart is falling too Im in love with your body Last night you were in my room And now my bed sheets smell like you Every day discovering something brand new Oh, Im in love with your body Come on, be my baby, come on (Come on, be my baby, come on) I'm in love with your body Come on, be my baby, come on (Come on, be my baby, come on) Oh, I'm in love with your body Come on, be my baby, come on (Come on, be my baby, come on) Im in love with your body Every day discovering something brand new Im in love with the shape of you"
    wds1=sent1.split()
    wds2=sent2.split()
    total=list(set(wds1).union(set(wds2)))
    wdd1=dict.fromkeys(total,0)
    wdd2=dict.fromkeys(total,0)
    for wds in wds1:
        wdd1[wds]+=1
    for wds in wds2:
        wdd2[wds]+=1
    def computeTF(worddict,sen):
        tfdict={}
        leng=len(sen)
        for wds,value in worddict.items():
            tfdict[wds]=value/float(leng)
        return tfdict
    tf1=computeTF(wdd1,sent1)
    tf2=computeTF(wdd2,sent2)
    def computeIDF(doclist):
        idfdict={}
        n=len(doclist)
        idfdict=dict.fromkeys(doclist[0].keys(),0)
        for wds,val in idfdict.items():
            idfdict[wds]=m.log(n/(float(val)+1))
        return idfdict
    idfs=computeIDF([wdd1,wdd2])
    def computeTFIDF(TF,IDF):
        tfidf={}
        for wds,val in TF.items():
            tfidf[wds]=val*idfs[wds]
        return tfidf
    TS1=computeTFIDF(tf1,idfs)
    TS2=computeTFIDF(tf2,idfs)
    v=0
    w=0
    sum=0
    for i in total:
        sum+=TS1[i]*TS2[i]
        v+=TS1[i]**2
        w+=TS2[i]**2
    sim=sum/((v**0.5)*(w**0.5))
    l6.config(text=str(sim))
    if 0.8<sim<=1:
        score+= sim*50
    elif 0.5<sim<=0.8:
        score+= (sim+0.1)*50
    elif 0.3<sim<=0.5:
        score+= (sim+0.15)*50
    else:
        score+=(sim+0.175)*50
    
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
l5=Label(f,text="Choose from the theme:- pop,rock,love,sad:")
l5.grid(row=4,column=0)
e4=Entry(f,width=30)
e4.grid(row=4,column=1)
b5=Button(f,text="Click to enter",command=click4)
b5.grid(row=4,column=2)
l6=Label(f,text="Type Lyrics:")
l6.grid(row=5,column=0)
e5=Entry(f,width=30)
e5.grid(row=5,column=1)
e5.config(text="Don't enter anyting here")
b6=Button(f,text="Enter to check",command=click5)
b6.grid(row=5,column=2)
def click6():
    global score
    l7=Label(f,text="The probability of your song being a hit is: "+str(score)+"%")
    l7.grid(row=7,column=1)
    score=0
b8=Button(f,text="If you have submitted all the data,then click",command=click6)
b8.grid(row=6,column=0,columnspan=3)
f.mainloop()
