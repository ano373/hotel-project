import tkinter as tk
import tkinter.font as tkFont
import tkinter
import os
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import dictlist as dictlist
import pymysql
from tkinter import *

def show(frame):
    Frame.tkraise(frame)

window= Tk()
window.geometry("963x788")
window.title("Hotel Managment")
# Button(f5,text='Go back',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",command=lambda : show(f1)).place(relx=0, rely=0.88, height=90, width=200)
row_selected = False
room_no = -1
id_guest = -1


def table_update(rows):

    tree.delete(*tree.get_children())
    for n, _dict in enumerate(rows, 1):
        _list = []
        for key in fieldnames:
            _list.append(_dict[key])
        tree.insert('', 'end', n, values=_list)


def search():
    q = ent_search.get()
    if (len(q) == 0):
        messagebox.showwarning(title='WARNING!', message='Enter a name or room number please !')
    else:
        query = "SELECT NAME,ROOM_REG,DAY_NUM,PAY,BILL FROM guests WHERE NAME LIKE '%" + q + "%' OR ROOM_REG LIKE '%" + q + "%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        table_update(rows)


def clear():
    ent_search.delete(0, END)
    query = "SELECT NAME,ROOM_REG,DAY_NUM,PAY,BILL FROM guests"
    cursor.execute(query)
    rows = cursor.fetchall()
    table_update(rows)


def getrow(event):
    rowid = tree.identify_row(event.y)
    item = tree.item(tree.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    curitem = tree.focus()
    global room_no,row_selected
    room_no = tree.set(curitem,1)
    row_selected = True
    query = "SELECT ID FROM guests WHERE ROOM_REG = " + room_no
    cursor.execute(query)
    global id_guest
    id_guest = cursor.fetchone()
    id_guest = id_guest["ID"]
    print(id_guest)


def update_guest():
    check = True
    if (row_selected == False):
        messagebox.showwarning(title='WARNING!', message="please select a colomb")
        check = False

    if updateoptions.get() == "Choose":
        messagebox.showwarning(title='WARNING!', message='pls choose an option from the option list')
        check = False

    if len(entery_updated.get()) == 0:
        messagebox.showwarning(title='WARNING!', message='Edit box is empty !')
        entery_updated.configure(bg="#EE0000")
        check = False


    if updateoptions.get() == "Room number" or updateoptions.get() == "number of days":
        try:
            int(entery_updated.get())
            if updateoptions.get() == "number of days" and len(entery_updated.get()) != 2:
                entery_updated.configure(bg="#EE0000")
                check = False
                messagebox.showwarning(title='WARNING!', message='you cant stay more than 99 days !')

        except ValueError:
            messagebox.showwarning(title='WARNING!', message='Enter a vaild number please !')
            entery_updated.configure(bg="#EE0000")
            check = False

    if updateoptions.get() == "Payment method":
        s = entery_updated.get()
        c = ["card","cash"]
      # if s in c :
             #entery_updated.configure(bg="#EE0000")
             #check = False
             #messagebox.showwarning(title='WARNING!', message='enter a vaild payment method !')



    if check:
        if messagebox.askyesno("confirm update?", "are you sure you want to update the guest's data?"):
            try:
                entery_updated.configure(bg="#ffffff")
               # updatelist = ["Room number", 'number of days', 'Payment method']
                if updateoptions.get() == "Room number":
                    sql = "UPDATE guests SET ROOM_REG = '%d' WHERE ID = '%d'" % \
                     (int(entery_updated.get()),id_guest)
                    cursor.execute(sql)
                    db.commit()
                    messagebox.showinfo(title='info', message='updated successfully !')
                    entery_updated.delete(0, END)
                    clear()

                elif updateoptions.get() == "number of days":
                    sql = "UPDATE guests SET DAY_NUM = '%d' WHERE ID = '%d'" % \
                    (int(entery_updated.get()),id_guest)
                    cursor.execute(sql)
                    db.commit()
                    messagebox.showinfo(title='info', message='updated successfully !')
                    entery_updated.delete(0, END)
                    clear()

                elif updateoptions.get() == "Payment method":
                    sql = "UPDATE guests SET PAY = '%s' WHERE ID = '%d'" % \
                    (entery_updated.get(),id_guest)
                    cursor.execute(sql)
                    db.commit()
                    messagebox.showinfo(title='info', message='updated successfully !')
                    entery_updated.delete(0, END)
                    clear()


            except:
                db.rollback()

        else:
             pass


def checkout_guest():
    guest_room = t2.get()
    guest_name = t1.get()
    if (len(guest_room) == 0 & len(guest_name) == 0):
        messagebox.showwarning(title='error', message="please select a coulomb")
    else:
        if messagebox.askyesno("confirm checkout?", "are you sure (" + guest_name + ") want to CHECKOUT?"):
            query = "DELETE FROM guests WHERE ROOM_REG = " + guest_room
            cursor.execute(query)
            db.commit()
            clear()
            global row_selected
            row_selected = False
            os.system("feedback.py")

        else:
            pass

root = Frame(window,  bg ="#ffffff")
# root.configure(bg="white")
searched_text = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()


# .............data conn.................
db = pymysql.connect(host='localhost',
                     user='root',
                     database='hotel_db',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

# .............. fechall data.............
sql = " SELECT NAME,ROOM_REG,DAY_NUM,PAY,BILL FROM guests"
cursor.execute(sql)
rows = cursor.fetchall()

root.update()

# ........... treeview table..................
tree = ttk.Treeview(root, columns=(0, 1, 2, 3, 4), show="headings", height=3)
tree.place(x=25, y=90, width=887, height=370)

fieldnames = ['NAME', 'ROOM_REG', 'DAY_NUM', 'PAY', 'BILL']
# ...............table headings............
for i in range(5):
    tree.column(i, width=150, anchor=tk.CENTER)
    tree.heading(i, text=fieldnames[i])

tree.bind('<Double 1>', getrow)

table_update(rows)


tk.Label(root, text='Data Management', font=("prototype", 30, "bold"), bg="#9e6960", anchor="w",
         fg="#ffffff").place(relx=0, rely=0, relheight=0.10, relwidth=1)

Button(root, text='Go back', font=("Forte", 25), bg="#9e6960", fg="#ffffff").\
                             place(relx=0, rely=0.88, height=90,width=200)
btn_search = tk.Button(root)
btn_search["bg"] = "#9e6960"
btn_search["font"] = ("Forte", 24)
btn_search["fg"] = "white"
btn_search["justify"] = "center"
btn_search["text"] = "Search"
btn_search.place(x=280, y=480, width=195, height=54)
btn_search["command"] = search

btn_clear = tk.Button(root)
btn_clear["bg"] = "#9e6960"
btn_clear["font"] = ("Forte", 24)
btn_clear["fg"] = "white"
btn_clear["justify"] = "center"
btn_clear["text"] = "Clear"
btn_clear.place(x=490, y=480, width=216, height=54)
btn_clear["command"] = clear

ent_search = tk.Entry(root, textvariable=searched_text)
ent_search["font"] = ("Forte", 24)
ent_search["fg"] = "#333333"
ent_search["justify"] = "center"
ent_search["text"] = ""
ent_search.place(x=70, y=480, width=198, height=56)

btn_checkout = tk.Button(root)
btn_checkout["bg"] = "#9e6960"
btn_checkout["font"] = ("Forte", 24)
btn_checkout["fg"] = "white"
btn_checkout["justify"] = "center"
btn_checkout["text"] = "Checkout"
btn_checkout.place(x=670, y=670, width=203, height=67)
btn_checkout["command"] = checkout_guest

Label(root, text="options :", bg="#ffffff", font=("prototype", 20)).place(x=310, y=550, width=121, height=41)
updatelist = ["Room number", 'number of days', 'Payment method']
opt = StringVar()
updateoptions = ttk.Combobox(root, values=updatelist, state="readonly", height=6, font=("Arial", 12), textvariable=opt)
updateoptions.place(x=440, y=550, width=135, height=42)
updateoptions.set("Choose")

entery_updated = Entry(root, font=("Arial", 20), borderwidth=2)
entery_updated.place(x=330, y=600, width=209, height=39)

btn_update = Button(root, text='Update', font=("Forte", 25), bg="#9e6960", fg="#ffffff", activeforeground="#ffffff",
                    activebackground="#9e6960", command=update_guest)
btn_update.place(x=360, y=650, width=140, height=49)

root.place(relx=0, rely=0, relheight=1, relwidth=1)
show(root)
window.mainloop()
