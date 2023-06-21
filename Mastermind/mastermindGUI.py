import random
from tkinter import *
from tkinter import messagebox
import time
##Creating the code
def create_code():
    t=list(range(10))
    global code
    code=''
    for i in range(3):
        ran=random.choice(t)
        t.remove(ran)
        code+=str(ran)
    return code
code=create_code()
#creating window
root=Tk()
root.geometry("480x500")
root.resizable(width=False,height=False)
root.title('Mastermind')
root.config(bg='cyan')
#creating display interface--labels
displbl1=Label(root,text='Your Guess: ',bg='cyan',font='Arial 14 underline',relief='flat',justify=LEFT)
displbl1.place(x=20,y=20)
en=Label(root,text='',font='Castellar 14 bold',fg='red',bg='yellow',bd=6,width=16,relief='sunken',justify=CENTER)
en.place(x=180,y=20)
displbl2=Label(root,text='Previous guesses(cows,bulls):',bg='cyan',font='Arial 10 italic',bd=6,fg='purple')
displbl2.place(x=20,y=410)
prg=Label(root,text='',font='Arial 10 bold',bg='cyan',fg='brown')
prg.place(x=10,y=430)
displbl3=Label(root,text='Cows:',bg='cyan',font='Century 16 bold underline')
displbl3.place(x=20,y=340)
Cows=Label(root,text='',font='Century 16',bg='cyan',bd=6,fg='red')
Cows.place(x=100,y=335)
displbl4=Label(root,text='Bulls:',bg='cyan',font='Century 16 bold underline')
displbl4.place(x=280,y=340)
Bulls=Label(root,text='',bg='cyan',font='Century 16',bd=6,fg='red')
Bulls.place(x=350,y=335)
displbl5=Label(root,text='Turns:',bg='cyan',font='Century 16 bold underline')
displbl5.place(x=20,y=380)
turns=Label(root,text=0,bg='cyan',font='Robotto')
turns.place(x=100,y=382)
#Creating interactive interface ::::: buttons
btn=[]
for i in range(10):
    btn.append(Button(root,text=str(i),font='Times',width=5,relief='raised',bg='gold',bd=5,command=lambda x=i:clicked(x)))
pos = 0
for i in range(3):
    for j in range(3):
        btn[pos].place(x=80*j+100,y=50*i+100)
        pos+=1
btn[pos].place(x=100,y=250)
##Erase button
def Erase():
    if len(en['text'])>0:
        st=en['text']
        en.config(text=st[:len(st)-1])
er=Button(root,text='<--',font='Times',width=5,relief='raised',bg='silver',bd=5,command= Erase)
er.place(x=180,y=250)
##Submit button
def Submit():
    if en['text']==code:
        win()
    elif len(set(en['text']))==3:
        c=0
        b=0
        for i in range(len(en['text'])):
            if en['text'][i]==code[i]:
                b+=1
            elif (en['text'][i]!=code[i]) and en['text'][i] in code:
                c+=1
        Bulls.config(text=b)
        Cows.config(text=c)
        if len(prg['text'])%77==0 and len(prg['text'])>0:
            prg.config(text=prg['text']+'\n')
        prg.config(text=prg['text']+'|'+en['text']+'('+str(c)+','+str(b)+')')
        en.config(text='')
        turns.config(text=turns['text']+1)
sub=Button(root,text='Submit',font='Times 14 underline bold',width=5,relief='raised',fg='red',bg='silver',bd=5,command= Submit)
sub.place(x=260,y=250)
def clicked(x):
    if len(en['text'])<3:
        st=en['text']+str(x)
        en.config(text=st)
def win():
    msg=messagebox.askyesno('Exit','Congratulations!\nYou guessed the code in '+str(turns['text']+1)+' turns!\nPlay Again?')
    if msg==True:
        code=create_code()
        en.config(text='')
        turns.config(text=0)
        Cows.config(text='')
        Bulls.config(text='')
        prg.config(text='')
    else:
        root.destroy()
root.option_add('*font','Castellar 16 bold')
messagebox.showinfo('Gameplay','\n1)The code is of 3 digits without any repetition.\
                    \n2)Cows indicate no. of digits in your guess which are present in the code but at incorrect position.\
                    \n3).Bulls indicate no. of digits in your guess which are at correct position.\
                    \n4)Press "<--" to erase.\
                    \n5)Press "Submit" to submit your guess.\
                    \n\tHappy Guessing!!')
root.mainloop()
