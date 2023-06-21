from tkinter import *
from tkinter import messagebox
import time
import random
import os
#GUI environment making
root =Tk()
root.title("Hangman")
root.geometry("850x450+200+100")
root.resizable(width=False,height=False)
us=Label(root,text='Used letters:',font="Virdisa 12")
us.place(x=20,y=300)
used=Label(root,text='',font="Virdisa 12 italic bold")
used.place(x=120,y=300)
lbl1=Label(root,text='Word: ',font="Castellar 16 bold",bd=6,justify=LEFT)
lbl1.place(x=20,y=10)
en_box=Label(root,text='',bg='yellow',font="Virdisa 16 bold",fg='blue',width=50,bd=6,justify=LEFT,relief='sunken')
en_box.place(x=120,y=10)
hint_box=Label(root,text='Hint:',bg='white',font="Castellar 14 bold",width=50,bd=6,justify=LEFT)
hint_box.place(x=20,y=60)
lbl=Label(root,text='Lives left:',font="Castellar 14 bold",bd=6,justify=LEFT)
lbl.place(x=80,y=100)
lives_left=Label(root,text='9',fg='red',font="Arial 14 bold",bd=6,bg='white',justify=RIGHT)
lives_left.place(x=280,y=100)
result=Label(root,text='',font='Roboto 20 bold',bd=8,justify=CENTER)
result.place(x=20,y=350)
#defining the various processes
def display():
	#starting
	used.config(text='')
	result.config(text='',relief='flat',bg='silver')
	lives_left.config(text='9')
	full_set=[]
	fp=open('Hangman_word_and_keys.txt','r+')
	for i in fp.readlines():
		full_set.append(i.strip("\n"))
	#choosing the word
	n=len(full_set)
	temp=range(n)
	ch=random.choice(temp)
	w_k=full_set[ch].split(",")
	#creating blank set
	guess_set=[]
	for i in range(len(w_k[0])):
		if w_k[0][i]==' ':
			guess_set.append(' ')
		else:
			guess_set.append('_')
	guess_word=''
	for i in guess_set:
		guess_word+=i+' '
	en_box.config(text=guess_word)
	hint_box.config(text="Hint: "+w_k[1])
	btn=[]
	for i in range(65,91):
		btn.append(Button(width=4,bg='orange',text=chr(i),bd=6,command=lambda x=chr(i):enterLetter(x,guess_set,w_k)))
		n=65
	pos=0
	btntext=chr(n)
	for i in range(2):
		for j in range(13):
			btn[pos].place(x=100+j*50,y=140+i*70)
			n+=1
			pos+=1
			btntext=chr(n)
def enterLetter(x,guess_set,w_k):
	if x in w_k[0] and x not in guess_set:
		for i in range(len(w_k[0])):
			if w_k[0][i]==x:
				guess_set[i]=x
		used_letter=used['text']
		used.config(text=used_letter+" "+x)
		guess_word=''
		for i in guess_set:
			guess_word+=i+' '
			en_box.config(text=guess_word)
		if '_' not in guess_set:
			win()
	elif x in guess_set:
		pass
	elif x in used['text']:
		pass
	else:
		used_letter=used['text']
		used.config(text=used_letter+" "+x)
		hang(w_k)
def win():
        result.config(text="Congratulations!!Word guessed correctly!",relief='raised',bg='gold')
        end()
def hang(w_k):
	lives=int(lives_left['text'])-1
	lives_left.config(text=str(lives))
	if lives==0:
		result.config(text="All lives lost!!Better luck next time!",relief='raised',bg='grey')
		en_box.config(text=w_k[0])
		end()
##
def end():
	mg=messagebox.askyesno('End','Play again?')
	if mg==True:
		display()
	else:
		root.destroy()
display()



root.mainloop()
