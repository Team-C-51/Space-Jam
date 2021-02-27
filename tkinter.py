from tkinter import *
import matplotlib.pylot as plt
import sounddevice as sd
f=Tk()
f.title("Try")
f.geometry("1024x1024")
f.config(bg="red")
l1=Label(f,text="Duration of song in Seconds",bg="orange")
l1.grid(row=0,column=0)
def click():
    txt=e1.get()
    txt=int(txt)
    mini=txt//60
    sec=txt-mini*60
    l1.configure(text=str(mini)+" mins"+str(sec)+" Seconds")
    e1.delete(0,END)
def click1():
    plt.close("all")
    Fs=16000
    d=txt+10
    l2.config(text="Start Speaking")
    rec=sd.rec(int(d*Fs),Fs,1,blocking=True)
    sd.wait()
    l2.config(text="Thanks")
    def click2():
        sd.play(a,Fs)
    b3=Button(f,text="Wanna hear yourself",command=click2,bg="Yellow")
    b3.grid(row=1,column=2)
e1=Entry(f,width=30,bg="blue")
e1.grid(row=0,column=1)
e1.insert(0,"in seconds")
b1=Button(f,text="press",command=click,bg="yellow")
b1.grid(row=0,column=2)
#b2=Button(f,text="press",command=click1)
#b2.grid(row=2,column=3)
l2.Label(f,text="To record your song click:",bg="orange")
l2.grid(row=1,column=0)
b2=Button(f,text="Click",command=click1,bg="Yellow")
b2.grid(row=1,column=1)
f.mainloop()
