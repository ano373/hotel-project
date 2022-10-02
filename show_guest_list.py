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
root.geometry("780x541+504+123")
root.title("HOTEL MANAGEMENT")

# .........list of all guests frame.........
tableframe = LabelFrame(root, text="Guest list")
searchframe = LabelFrame(root, text="Search")
Dataframe = LabelFrame(root, text="Guest Data")
tableframe.pack(fill="both", expand="yes", padx=20, pady=10)
searchframe.pack(fill="both", expand="yes", padx=20, pady=10)
Dataframe.pack(fill="both", expand="yes", padx=20, pady=10)
frame_style(tableframe)
frame_style(searchframe)
frame_style(Dataframe)

root.update()

# ........... treeview table..................
tree = ttk.Treeview(tableframe, columns=(1, 2, 3), show="headings", height=tableframe.winfo_height())
tree.pack()

# ...............table headings.............
tree.heading(1, text="NAME")
tree.heading(2, text="ROOM NO")
tree.heading(3, text="BILL")

# ...........insert database into table.............
# Dict's are unordered,
# therfore you need a list of fieldnames in your desired order
fieldnames = ['NAME', 'ROOM_REG', 'BILL']

for n, _dict in enumerate(rows, 1):
    _list = []
    for key in fieldnames:
        _list.append(_dict[key])
    tree.insert('', 'end', n, values=_list)





root.mainloop()

