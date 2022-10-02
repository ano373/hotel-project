import tkinter



def show(frame):
    tkinter.Frame.tkraise(frame)


lof=[]
window= tkinter.Tk()
window.geometry("1000x600")

f1=tkinter.Frame(window, bg="blue")
lof.append(f1)
f2=tkinter.Frame(window, bg ="green")
lof.append(f2)
f3=tkinter.Frame(window, bg ="yellow")
lof.append(f3)

for i in lof:
    i.place(relx=0, rely=0, relheight=1, relwidth=1)

#=============main manu============
tkinter.Label(f1, text='main menu', font = ("Arial", 50)).place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
tkinter.Button(f1, text='check in', font = ("Arial", 25), command=lambda : show(f2)).place(relx=0.18, rely=0.17, height=103, width=566)
tkinter.Button(f1, text='show list', font = ("Arial", 25), command=lambda : show(f3)).place(relx=0.18, rely=0.33, height=93, width=566)


#=============check in=============
tkinter.Label(f2, text='check in', font = ("Arial", 50)).place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
tkinter.Button(f2, text='go back', font = ("Arial", 25), command=lambda : show(f1)).place(relx=0.18, rely=0.17, height=103, width=566)

#=============show list=============
tkinter.Label(f3, text='list of guests', font = ("Arial", 50)).place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
tkinter.Button(f3, text='go back', font = ("Arial", 25), command=lambda : show(f1)).place(relx=0.18, rely=0.17, height=103, width=566)



show(f1)
window.mainloop()

# try :
#     f=open("txt.txt")
# except FileNotFoundError:
#     print("")