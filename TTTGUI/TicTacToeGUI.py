##necessary imports
import random
import time
from tkinter import *
from tkinter import messagebox
#creating gui
root=Tk()
root.title("Tic Tac Toe")
root.geometry("450x420")
root.resizable(width=False,height=False)
PL1=Label(root,text="Player 1: X",font="Castellar 12 bold underline",bg="silver",fg="blue",bd=12)
PL1.place(x=0,y=20)
PL2=Label(root,text="Player 2: O",font="Castellar 12 bold underline",bg="silver",fg="green",bd=12)
PL2.place(x=310,y=20)
turn=Label(root,text="",font="Castellar 12 bold underline",bg="yellow",fg="red",bd=6,width=40)
turn.place(x=0,y=0)
#creating boxes
#necessary functions
def display():
	box=[]
	for i in range(9):
		box.append(Button(text=str(i),width=15,height=6,bd=5,bg='silver',command=lambda x=i:clck(x,box)))
	pos=0
	for i in range(3):
		for j in range(3):
			box[pos].place(x=j*120+40,y=i*100+80)
			pos+=1
	ts=random.choice([0,1])
	if ts==1:
		turn.config(text="Player 1's turn:")
		messagebox.showinfo('Toss','Player 1 (X) plays first')
	else:
		turn.config(text="Player 2's turn:")
		messagebox.showinfo('Toss','Player 2 (O) plays first')
def turn_change():
	if turn['text']=="Player 1's turn:":
		turn.config(text="Player 2's turn:")
	else:
		turn.config(text="Player 1's turn:")
def clck(n,box):
	if box[n]['text'] not in ["X","O"]:
		if turn['text']=="Player 1's turn:":
			box[n].config(font='Arial 9 bold',text='X',bg='blue',fg='black',justify=LEFT)
		else:
			box[n].config(font='Arial 9 bold',text='O',bg='green',fg='black',justify=LEFT)
		check_win(box)
def check_win(box):
	for i in range(0,9,3):
		if box[i]['text']==box[i+1]['text'] and box[i]['text']==box[i+2]['text']:
			if box[i]['text']=='X':
				win(1,box)
			else:
				win(2,box)
	for i in range(3):
		if box[i]['text']==box[i+3]['text'] and box[i]['text']==box[i+6]['text']:
			if box[i]['text']=='X':
				win(1,box)
			else:
				win(2,box)
	if box[0]['text']==box[4]['text'] and box[0]['text']==box[8]['text']:
		if box[0]['text']=='X':
			win(1,box)
		else:
			win(2,box)
	if box[2]['text']==box[4]['text'] and box[2]['text']==box[6]['text']:
		if box[2]['text']=='X':
			win(1,box)
		else:
			win(2,box)
	bl=[]
	for i in range(9):
		bl.append(box[i]['text'])
	n=len(set(bl))
	if n==2:
		draw(box)
	turn_change()
def win(pl,box):
	msg=messagebox.askyesno('Exit','player '+str(pl)+' wins!!\nPlay again?')
	if msg==True:
		display()
		turn_change()
	else:
		root.destroy()
def draw(box):
	msg=messagebox.askyesno('Exit','Match drawn!!\nPlay again?')
	if msg==True:
		display()
		turn_change()
	else:
		root.destroy()
display()





root.mainloop()
