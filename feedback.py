from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import pymysql

# .............data conn.................
db = pymysql.connect(host='localhost',
                       user='root',
                       database='feedback',
                       charset='utf8mb4')
cursor = db.cursor()
rating_value = 0
cursor.execute("Select AVG(RATING) AS average from feedback;")
avg_rating=cursor.fetchone()

def checkout():
    sql = "INSERT INTO feedback (RATING,REVIEWS) VALUES (%s, %s)"
    val = (rating_value, text_box.get("1.0",END))
    cursor.execute(sql, val)
    db.commit()
    text_box.delete(1.0, END)
    messagebox.showinfo(title='have a nice day', message="thanks for your feedback!")
    root.destroy()


def change_btn_color():
    theme_color = "#9e6960"
    if rating_value == 2:
        btn_1["bg"] = theme_color
        btn_3["bg"] = theme_color
        btn_4["bg"] = theme_color
        btn_5["bg"] = theme_color
        btn_2["bg"] = "white"
    if rating_value == 1:
        btn_2["bg"] = theme_color
        btn_3["bg"] = theme_color
        btn_4["bg"] = theme_color
        btn_5["bg"] = theme_color
        btn_1["bg"] = "white"
    if rating_value == 3:
        btn_1["bg"] = theme_color
        btn_2["bg"] = theme_color
        btn_4["bg"] = theme_color
        btn_5["bg"] = theme_color
        btn_3["bg"] = "white"
    if rating_value == 4:
        btn_1["bg"] = theme_color
        btn_3["bg"] = theme_color
        btn_2["bg"] = theme_color
        btn_5["bg"] = theme_color
        btn_4["bg"] = "white"
    if rating_value == 5:
        btn_1["bg"] = theme_color
        btn_3["bg"] = theme_color
        btn_2["bg"] = theme_color
        btn_4["bg"] = theme_color
        btn_5["bg"] = "white"

def btn_2_command():
    global rating_value
    rating_value = 2
    change_btn_color()

def btn_3_command():
    global rating_value
    rating_value = 3
    change_btn_color()

def btn_4_command():
    global rating_value
    rating_value = 4
    change_btn_color()

def btn_5_command():
    global rating_value
    rating_value = 5
    change_btn_color()

def btn_1_command():
    global rating_value
    rating_value = 1
    change_btn_color()

root = Tk()
root.title("feedback")
# setting window size
width = 395
height = 259
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

btn_2 = Button(root, command=btn_2_command)
btn_2["bg"] = "#9e6960"
btn_2["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=16)
btn_2["font"] = ft
btn_2["fg"] = "#000000"
btn_2["justify"] = "center"
btn_2["text"] = "2"
btn_2.place(x=90, y=70, width=70, height=25)

btn_3 = Button(root)
btn_3["bg"] = "#9e6960"
btn_3["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=16)
btn_3["font"] = ft
btn_3["fg"] = "#000000"
btn_3["justify"] = "center"
btn_3["text"] = "3"
btn_3.place(x=160, y=70, width=70, height=25)
btn_3["command"] = btn_3_command

btn_4 = Button(root)
btn_4["bg"] = "#9e6960"
btn_4["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=16)
btn_4["font"] = ft
btn_4["fg"] = "#000000"
btn_4["justify"] = "center"
btn_4["text"] = "4"
btn_4.place(x=230, y=70, width=70, height=25)
btn_4["command"] = btn_4_command

btn_5 = Button(root)
btn_5["bg"] = "#9e6960"
btn_5["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=16)
btn_5["font"] = ft
btn_5["fg"] = "#000000"
btn_5["justify"] = "center"
btn_5["text"] = "5"
btn_5.place(x=300, y=70, width=70, height=25)
btn_5["command"] = btn_5_command

btn_1 = Button(root)
btn_1["bg"] = "#9e6960"
btn_1["borderwidth"] = "1px"
btn_1["disabledforeground"] = "#ffffff"
ft = tkFont.Font(family='Times', size=16)
btn_1["font"] = ft
btn_1["fg"] = "#000000"
btn_1["justify"] = "center"
btn_1["text"] = "1"
btn_1.place(x=20, y=70, width=70, height=25)
btn_1["command"] = btn_1_command

GLabel_423 = Label(root)
ft = tkFont.Font(family='Times', size=13)
GLabel_423["font"] = ft
GLabel_423["fg"] = "#333333"
GLabel_423["justify"] = "center"
GLabel_423["text"] = "rate your visit"
GLabel_423.place(x=0, y=30, width=137, height=33)

text_box = Text(root, font=("Helvetica", 13))
text_box.place(x=20, y=110, width=353, height=103)

checkout_btn = Button(root, text="checkout", command=checkout)
checkout_btn.place(x=160, y=220, width=70, height=25)

Glabel = Label(root)
ft = tkFont.Font(family='Times', size=10)
Glabel["font"] = ft
Glabel["fg"] = "#333333"
Glabel["justify"] = "center"
Glabel["text"] = "avg rating: "
Glabel.place(x=240, y=10, width=70, height=25)


rate_label = Label(root)
ft = tkFont.Font(family='Times', size=10)
rate_label["font"] = ft
rate_label["fg"] = "#333333"
rate_label["justify"] = "center"
rate_label["text"] = avg_rating
rate_label.place(x=300, y=10, width=62, height=30)

root.mainloop()
