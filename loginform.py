from tkinter import *
from functools import partial
from turtle import bgcolor, width

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('500x200+100+50')  
tkWindow.title('GUI loginform')
tkWindow.configure (bg="green")


#username label and text entry box
usernameLabel = Label(tkWindow,  width="16",bg="green",fg="white", text="Identifiant").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, width="40", textvariable=username).grid(row=0, column=1, padx=10,pady=10)  

#password label and password entry box
passwordLabel = Label(tkWindow, width="16",bg="green",fg="white",   text="Mot_de_passe").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow,width="40", textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow,width="13",fg="white", bg="#07870d", text="Soumettre", command=validateLogin).grid(row=4, column=0, padx=10,pady=20)  

tkWindow.mainloop()