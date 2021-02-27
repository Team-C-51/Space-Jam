from tkinter import *
import sounddevice as sd
f=Tk()
f.title("Try")
f.geometry("1024x1024")
f.config(bg="yellow")
l1=Label(f,text="Duration of song in Seconds")
l1.grid(row=0,column=0)
txt=0
rec=0
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
e1=Entry(f,width=30)
e1.grid(row=0,column=1)
e1.insert(0,"in seconds")
b1=Button(f,text="press",command=click)
b1.grid(row=0,column=2)
b2=Button(f,text="Click",command=click1)
b2.grid(row=1,column=1)
f.mainloop()
