from tkinter import *
from random import *
abc="QWERTYUIPASDFGHJKLZXCVBNMQWqwertyuiopasdfghjklzxcvbnm123456789@"
nomore=""
num=[1,2,3,4,5,6,7,8,9]
k=Tk()
k.config(bg="black")
def enc():
	tk=Tk()
	tk.geometry("650x650")
	tk.title('ENCRYPTION')
	tk.config(bg="black")
	Label(tk,text='ENTER YOUR PASSWORD\n',fg="white",bg="black",font="Arial 10 ").pack()
	z=Entry(tk)
	z.pack()
	Label(tk,text='\n',fg="white",bg="black",font="Arial 10 ").pack()
	
	def en():
		
		p=str(z.get())

		
		v=''	
		for l in p:
			if choice([0,1]):
			    v+=str(ord(l)+choice(num)-7*3)+choice(abc)
			else :
			    v+=str(ord(l)+choice(num)-7*3)+nomore
		with open("mn.txt","a") as f:
			
			f.write(v)
			f.write(' = ')
			f.write(p)
			f.write('\n')
			
		Label(tk,text='\nEncripted Value\n',fg="white",bg="black",font="Arial 10 ").pack()
		Label(tk,text=v,fg="white",bg="black",font="Arial 10 ").pack()
		Label(tk,text='\nPlz Save It',fg="white",bg="black",font="Arial 10 ").pack()
		
	Button(tk,text="click",command=en,fg="white",bg="black",font="Arial 10 ",width=10).pack()
	
	tk.mainloop()


def dec():
	tk2=Tk()
	tk2.geometry("650x650")
	tk2.title('DECRIPTION')
	tk2.config(bg="black")
	def dec1():
		with open('mn.txt','r') as r:
			
			g=e.get()
			while 1:
				m=r.readline().split()
				
				
				
				if m!=[]:
					if m[0]==g:
						Label(tk2,text='\nYour Password Is\n',fg="white",bg="black",font="Arial 10 ").pack()
						Label(tk2,text=m[2],fg="white",bg="black",font="Arial 10 ").pack()
						
						break
				else:
				    Label(tk2,text='\n\nNot Valid!',fg="white",bg="black",font="Arial 10 ").pack()
				    break	
	Label(tk2,text='ENTER ENCRYPTED VALUE\n ',fg="white",bg="black",font="Arial 10 ").pack()				
	e=Entry(tk2)
	e.pack()
	Label(tk2,text='\n',fg="white",bg="black",font="Arial 10 ").pack()
	Button(tk2,text='Click',command=dec1,fg="white",bg="black",font="Arial 10 ",width=10).pack()
	tk2.mainloop()
Button(k,text='Encryption',command=enc,fg="light green",bg="black",font="Arial 15 bold",width=10).place(x=150,y=800)
Button(k,text='Decription',command=dec,fg="light green",bg="black",font="arial 15 bold",width=10).place(x=150,y=950)
k.mainloop()
	