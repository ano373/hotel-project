import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import dictlist as dictlist
import pymysql
from tkinter import *

# .................. frame style fun............
def frame_style(labelframe):
    labelframe.configure(relief=GROOVE,
                         font="arial",
                         foreground="black",
                         background="#ffffff",
                         highlightbackground="#123456",
                         highlightcolor="black",
                         width=60)

# ...........insert database into table.............
def table_update(rows):
    tree.delete(*tree.get_children())
    for n, _dict in enumerate(rows, 1):
        _list = []
        for key in fieldnames:
            _list.append(_dict[key])
        tree.insert('', 'end', n, values=_list)


def search():
     q =  searched_text.get()
     query = "SELECT NAME,ROOM_REG,BILL FROM guests WHERE NAME LIKE '%"+q+"%' OR ROOM_REG LIKE '%"+q+"%'"
     cursor.execute(query)
     rows = cursor.fetchall()
     table_update(rows)

def clear():
    query = "SELECT NAME,ROOM_REG,BILL FROM guests"
    cursor.execute(query)
    rows = cursor.fetchall()
    table_update(rows)

def getrow(event):
    rowid = tree.identify_row(event.y)
    item = tree.item(tree.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])

def update_guest():
    guest_name = t1.get()
    guest_room = t2.get()
    guest_bill = t3.get()

    if messagebox.askyesno("confirm update?","are you sure you want to update the guest's data?"):
        query= "UPDATE guests  SET NAME = %s, BILL =%s WHERE ROOM_REG = %s"
        cursor.execute(query,(guest_name,guest_bill,guest_room))
        db.commit()
        clear()

    else:
        pass
def checkout_guest():
    guest_room = t2.get()
    guest_name = t1.get()
    if messagebox.askyesno("confirm checkout?","are you sure (" + guest_name + ") want to CHECKOUT?"):
     query = "DELETE FROM guests WHERE ROOM_REG = " + guest_room
     cursor.execute(query)
     db.commit()
     clear()
    else:
        pass

# .............data conn.................
db = pymysql.connect(host='localhost',
                     user='ano',
                     password='1234a',
                     database='hotel_db',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

# .............. fechall data.............
sql = " SELECT NAME,ROOM_REG,BILL FROM guests"
cursor.execute(sql)
rows = cursor.fetchall()

# ................main window.............
root = Tk()
searched_text = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
root.geometry("780x541+504+123")
root.title("HOTEL MANAGEMENT")

# .........list of all guests frame.........
tableframe = LabelFrame(root, text="Guest list")
Label(root,text='Data Management',font = ("prototype",30,"bold"), bg = "#9e6960",anchor="w",fg="#ffffff").place(relx=0, rely=0, relheight=0.10, relwidth=1)
searchframe = LabelFrame(root, text="Search")
Dataframe = LabelFrame(root, text="Guest Data")
tableframe.pack(fill="both", expand="yes", padx=20, pady=55)
searchframe.pack(fill="both", expand="yes", padx=20, pady=10)
Dataframe.pack(fill="both", expand="yes", padx=20, pady=10)
frame_style(tableframe)
frame_style(searchframe)
frame_style(Dataframe)

root.update()

# ........... treeview table..................
tree = ttk.Treeview(tableframe, columns=(1, 2, 3), show="headings", height=5)
tree.pack()

# ...............table headings............
tree.heading(1, text="NAME")
tree.heading(2, text="ROOM NO")
tree.heading(3, text="BILL")
tree.bind('<Double 1>',getrow)

fieldnames = ['NAME', 'ROOM_REG', 'BILL']
table_update(rows)

# search section
ent = Entry(searchframe,textvariable=searched_text)
ent.pack(side=tkinter.LEFT,padx=6)
search_btn=Button(searchframe,text="Search",command=search)
search_btn.pack(side=tkinter.LEFT,padx=6)
clear_btn=Button(searchframe,text="Clear",command=clear)
clear_btn.pack(side=tkinter.LEFT,padx=6)

# guest data section
def gridplace(lbl_name,row,column,txtvar):
    lbl = Label(Dataframe,text=lbl_name)
    lbl.grid(row=row,column=column,padx=5,pady=3)
    ent = Entry(Dataframe,textvariable=txtvar)
    ent.grid(row=row,column=column+1,padx=5,pady=3)

gridplace("NAME",0,0,t1)
gridplace("ROOM_REG",1,0,t2)
gridplace("BILL",2,0,t3)

update_btn=Button(Dataframe, text="Update", command=update_guest)
checkout_btn=Button(Dataframe,text="Check Out",command=checkout_guest)

update_btn.grid(row=4, column=1, padx=5, pady=3)
checkout_btn.grid(row=4,column=2,padx=5,pady=3)
root.mainloop()


