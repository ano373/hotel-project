from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import tkinter.font as tkFont
import dictlist as dictlist
import os


def show(frame):
    Frame.tkraise(frame)

#db_conn = pymysql.connect(host="localhost", user="root", password="", database="hotel_db")
db_conn = pymysql.connect(host='localhost',
                     user='root',
                     database='hotel_db',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db_conn.cursor()

war_red='#f75957'
white='#ffffff'
lof=[]
window= Tk()
window.geometry("963x788")
window.title("Hotel Managment")

#*********************  Inserting functions  ***********************************
def table_update(rowss):
   tree.delete(*tree.get_children())
   for n, _dict in enumerate(rowss, 1):
      _list = []
      for key in fieldnames:
         _list.append(_dict[key])
      tree.insert('', 'end',n, values=_list)


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
   print(rows)
   table_update(rows)


def getrow(event):
   rowid = tree.identify_row(event.y)
   item = tree.item(tree.focus())
   t1.set(item['values'][0])
   t2.set(item['values'][1])
   t3.set(item['values'][2])
   curitem = tree.focus()
   global room_no, row_selected
   room_no = tree.set(curitem, 1)
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

   if updateoptionss.get() == "Choose":
      messagebox.showwarning(title='WARNING!', message='pls choose an option from the option list')
      check = False

   if len(entery_updateds.get()) == 0:
      messagebox.showwarning(title='WARNING!', message='Edit box is empty !')
      entery_updateds.configure(bg="#EE0000")
      check = False

   if updateoptionss.get() == "Room number" or updateoptionss.get() == "number of days":
      try:
         int(entery_updateds.get())
         if updateoptionss.get() == "number of days" and len(entery_updateds.get()) != 2:
            entery_updateds.configure(bg="#EE0000")
            check = False
            messagebox.showwarning(title='WARNING!', message='you cant stay more than 99 days !')

      except ValueError:
         messagebox.showwarning(title='WARNING!', message='Enter a vaild number please !')
         entery_updateds.configure(bg="#EE0000")
         check = False

   if updateoptionss.get() == "Payment method":
      s = entery_updateds.get()
      c = ["card", "cash"]
   # if s in c :
   # entery_updated.configure(bg="#EE0000")
   # check = False
   # messagebox.showwarning(title='WARNING!', message='enter a vaild payment method !')

   if check:
      if messagebox.askyesno("confirm update?", "are you sure you want to update the guest's data?"):
         try:
            entery_updateds.configure(bg="#ffffff")
            # updatelist = ["Room number", 'number of days', 'Payment method']
            if updateoptionss.get() == "Room number":
               sql = "UPDATE guests SET ROOM_REG = '%d' WHERE ID = '%d'" % \
                     (int(entery_updateds.get()), id_guest)
               cursor.execute(sql)
               db_conn.commit()
               messagebox.showinfo(title='info', message='updated successfully !')
               entery_updateds.delete(0, END)
               clear()

            elif updateoptionss.get() == "number of days":
               sql = "UPDATE guests SET DAY_NUM = '%d' WHERE ID = '%d'" % \
                     (int(entery_updateds.get()), id_guest)
               cursor.execute(sql)
               db_conn.commit()
               messagebox.showinfo(title='info', message='updated successfully !')
               entery_updateds.delete(0, END)
               clear()

            elif updateoptionss.get() == "Payment method":
               sql = "UPDATE guests SET PAY = '%s' WHERE ID = '%d'" % \
                     (entery_updateds.get(), id_guest)
               cursor.execute(sql)
               db_conn.commit()
               messagebox.showinfo(title='info', message='updated successfully !')
               entery_updateds.delete(0, END)
               clear()


         except:
            db_conn.rollback()

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
         db_conn.commit()
         clear()
         global row_selected
         row_selected = False
         os.system("feedback.py")

      else:
         pass
#.........................................................................

def delete(num):
  if num==1:
     E1.delete(0, END)
     E2.delete(0, END)
     E3.delete(0, END)
     E4.delete(0, END)
     E5.delete(0, END)
     E6.delete(0, END)
     E7.delete(0, END)
     # E8.delete(0, END)
     E9.delete(0, END)
     E10.delete(0, END)
     Co1.set("Choose")
     Co2.set("Choose")
     Co3.set("Choose")
     Co4.set("Egypt")
  elif num==2:
     wk_E1.delete(0, END)
     wk_E2.delete(0, END)
     wk_E3.delete(0, END)
     wk_E4.delete(0, END)
     wk_E5.delete(0, END)
     wk_E6.delete(0, END)
     joboptions.set("Choose")




def check_name(name,entry):
   n=name.get()
   l=len(name.get())
   if len(n)==0:
      messagebox.showwarning(title='WARNING!', message='Name box is empty !')
      entry.configure(bg='#f75957')
      return False
   for i in range(0,l):
      if n[i].isdigit()==True:
            messagebox.showwarning(title='WARNING!',message='Enter a valid Name!')
            entry.configure(bg='#f75957')
            return False
   entry.configure(bg='#ffffff')
   return True


def check_age(age,entry):
   try:
      if len(age.get())==0:
         messagebox.showwarning(title='WARNING!', message='Age box is empty!')
         entry.configure(bg='#f75957')
         return False

      a=int(age.get())

      if a<100 and a>=16:
         entry.configure(bg='#ffffff')
         return True
      else:
         messagebox.showwarning(title='WARNING!', message='Enter a valid age!')
         entry.configure(bg='#f75957')
         return False
   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid age!')
      entry.configure(bg='#f75957')
      return False

def check_addr():
   if len(addr.get())==0 and Co4.get()=="Egypt":
      messagebox.showwarning(title='WARNING!', message='Address box is empty')
      E3.configure(bg=war_red)
      return False
   E3.configure(bg=white)
   return True

def check_email(e_mail,entery):
   c=0
   e=e_mail.get()
   if len(e_mail.get())==0:
      messagebox.showwarning(title='WARNING!', message='Email box is empty')
      entery.configure(bg=war_red)
      return False
   for i in range(0,len(e_mail.get())):
      if e[i]=='@':
         c+=1
   if e.endswith(".com",0,len(e)):
      c+=1
   if c==2:
      entery.configure(bg=white)
      return True
   else :
      messagebox.showwarning(title='WARNING!', message='invalid Email !')
      entery.configure(bg=war_red)
      return False

def check_mobile(mobile,entery):
   try:
      if len(mobile.get()) == 0:
         messagebox.showwarning(title='WARNING!', message='Mobile phone box is empty!')
         entery.configure(bg=war_red)
         return False

      m = int(mobile.get())

      if len(mobile.get())==11 and (mobile.get()).startswith("01"):
         entery.configure(bg=white)
         return True
      else:
         messagebox.showwarning(title='WARNING!', message='Enter a valid phone number!')
         entery.configure(bg=war_red)
         return False
   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid phone number!')
      entery.configure(bg=war_red)
      return False

def check_nat_id():
   try:
      if len(na_id.get()) == 0 and Co4.get()=="Egypt":
         messagebox.showwarning(title='WARNING!', message='National ID box is empty!')
         E6.configure(bg=war_red)
         return False
      elif len(na_id.get()) == 0 and Co4.get()!="Egypt":
         return False

      nat=int(na_id.get())

      if len(na_id.get())==14 and Co4.get()=="Egypt" :
         E6.configure(bg=white)
         return True
      elif len(na_id.get())!=14 and Co4.get()=="Egypt":
         messagebox.showwarning(title='WARNING!', message='Enter a valid National ID!')
         E6.configure(bg=war_red)
         return False
      elif Co4.get()!="Egypt":
         return False
   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid National ID!')
      E6.configure(bg=war_red)
      return False

def check_number_of_persons():
   try:
      if len(p_num.get()) == 0:
         messagebox.showwarning(title='WARNING!', message='Persons number box is empty!')
         E7.configure(bg=war_red)
         return False

      p = int(p_num.get())

      if p>0:
         E7.configure(bg=white)
         return True
      else:
         messagebox.showwarning(title='WARNING!', message='Enter a valid Persons number !')
         E7.configure(bg=war_red)
         return False
   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid Persons number !')
      E7.configure(bg=war_red)
      return False

# def check_register_room_number():
#    try:
#       if len(room_num.get()) == 0:
#          messagebox.showwarning(title='WARNING!', message='Register room number box is empty!')
#          E8.configure(bg=war_red)
#          return False
#
#       r = int(room_num.get())
#
#       if r>0 and r<=250:
#          E8.configure(bg=white)
#          return True
#       else:
#          messagebox.showwarning(title='WARNING!', message='Enter a valid Register room number !')
#          E8.configure(bg=war_red)
#          return False
#    except ValueError:
#       messagebox.showwarning(title='WARNING!', message='Enter a valid Register room number !')
#       E8.configure(bg=war_red)
#       return False

def check_reserved_days():
   try:
      if len(days.get()) == 0:
         messagebox.showwarning(title='WARNING!', message='Reserved days box is empty!')
         E9.configure(bg=war_red)
         return False

      d = int(days.get())

      if d>0 and d<=30:
         E9.configure(bg=white)
         return True
      else:
         messagebox.showwarning(title='WARNING!', message='Enter a valid days !')
         E9.configure(bg=war_red)
         return False
   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid days !')
      E9.configure(bg=war_red)
      return False

def check_room_sys():
   if len(combo1.get())==0 or combo1.get()=='Choose':
      messagebox.showwarning(title='WARNING!', message='Please choose your Room system from Room system box !')
      return False

   return True


def check_payment():
   if len(combo2.get()) == 0 or combo2.get() == 'Choose':
      messagebox.showwarning(title='WARNING!', message='Please choose your payment method from payment method box !')
      return False

   return True


def  room_system_calculation():
   total=0
   standard=75
   rs=combo1.get() #room sys

   if rs=="Single" :
      total=standard * int(days.get())
      return total

   elif rs=="Double":
      standard+=25
      total = standard * int(days.get())
      return total
   elif rs=="Triple":
      standard+=50
      total = standard * int(days.get())
      return total
   elif rs=="Quad":
      standard+=100
      total = standard * int(days.get())
      return total
   elif rs=="King":
      standard+=200
      total = standard * int(days.get())
      return total
   elif rs=="Queen":
      standard+=175
      total = standard * int(days.get())
      return total
   elif rs=="Studio":
      standard-=25
      total = standard * int(days.get())
      return total

# def check_reserved_room():
#    sql = "SELECT ROOM_REG FROM guests WHERE ROOM_REG=%s" % (int(room_num.get()))
#    try:
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     if result[0]==int(room_num.get()):
#        messagebox.showinfo(title='Info', message='this room is already reserved please pick another room')
#        return False
#
#    except:
#       db_conn.rollback()
#    return True

def add_none_registered_rooms():
   c=0
   sql = "SELECT ROOM_REG FROM guests"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      # print(results)
      list1=[]
      results_for_combobox = [result[0] for result in results]
      for x in range(1,251):
         if x not in results_for_combobox:
         # Add itmes in combobox through Loop code
           list1.append(str(x))
           # Co3['values'] = tuple(list(Co3['values']) + [str(x)])

         elif x in results_for_combobox:
            continue
      Co3['values']=list1

   except:
      db_conn.rollback()

def  check_reserved_room():
   if room_num.get()=="Choose":
      messagebox.showwarning(title='WARNING!', message='pls choose a room !')
      return False
   return True


def check_passport():
   if Co4.get()!="Egypt":
      if len(passp_id.get())==0:
         messagebox.showwarning(title='WARNING!', message='passport ID box is empty !')
         E10.configure(bg=war_red)
         return False
      elif len(passp_id.get())!=9:
         messagebox.showwarning(title='WARNING!', message='passport ID is invalid !')
         E10.configure(bg=war_red)
         return False
      else:
       return True

   return False

def insert_guest():
   if check_name(name,E1) and check_age(age,E2) and check_addr() and check_email(email,E4) \
           and check_mobile(mobile,E5) and check_number_of_persons() \
            and check_reserved_days() and check_room_sys()\
           and check_payment() and check_reserved_room():
      bill=room_system_calculation()
      nat=""
      pp=""
      ad=""
      check=True
      if check_passport() and  Co4.get()!="Egypt":
         nat="Null"
         ad="Null"
         pp=passp_id.get()
      elif check_nat_id() and Co4.get()=="Egypt":
         nat=na_id.get()
         ad=addr.get()
         pp="Null"
      else:
         check=False

      if check==True:
         if messagebox.askyesno(title='Confirmation', message='Do you really want to submit ?'):

            sql = "INSERT INTO guests (NAME, \
                     AGE,ADDRESS, EMAIL,PHONE,NAT_ID,ROOM_REG,P_NO,ROOM_SYS,DAY_NUM,PAY,COUNTRY,PASSP_ID,BILL) \
                     VALUES ('%s', '%d', '%s', '%s' , '%s', '%s', '%d', '%d', '%s', '%d', '%s','%s','%s', '%d')" % \
                  (name.get(), int(age.get()), ad, email.get(), mobile.get(), nat, int(room_num.get()),
                   int(p_num.get()), combo1.get(), int(days.get()), combo2.get(), combo3.get(), pp, bill)

            try:

               cursor.execute(sql)
               db_conn.commit()
               messagebox.showinfo(title='Info', message='Submited Successfully !')
               sql = "SELECT ID FROM guests WHERE ROOM_REG=%s" % (int(room_num.get()))
               cursor.execute(sql)
               result = cursor.fetchone()
               msg = 'your ID is ' + str(result[0])
               messagebox.showinfo(title='Info', message=msg)
               add_none_registered_rooms()
            except:

               db_conn.rollback()

            # db_conn.close()

            delete(1)




#****************** End  ************************




#********************* Searching functions ***********************************
def search_for_a_guest():

   if len(search_entery.get())==0:
      search_entery.configure(bg="#f75957")
      messagebox.showwarning(title='WARNING!', message='search box is empty !')


   elif search_box.get()=="ID" or search_box.get()=="Room number" or search_box.get()=="National ID" :
      try:
         int(search_entery.get())
         if search_box.get()=="National ID" and len(search_entery.get())!=14:
            messagebox.showwarning(title='WARNING!', message='pls enter a vaild National ID!')

      except ValueError:
         messagebox.showwarning(title='WARNING!', message='Enter a vaild number please !')



   if search_box.get()=="Choose":
      messagebox.showwarning(title='WARNING!', message='pls choose an option from the search list')



   search_entery.configure(bg="#ffffff")
   check = False
   result=""

   if search.get()=="ID":
     try:
        sql = "SELECT * FROM guests WHERE ID='%s'" % ( int(s_num.get()))
        cursor.execute(sql)
        result = cursor.fetchone()

        if cursor.rowcount==0:
           check=False
           messagebox.showwarning(title='WARNING!', message='Enter a vaild guest info !')
        else:
           check=True


     except:
        db_conn.rollback()

   elif search.get()=="Room number":
      try:
         sql = "SELECT * FROM guests WHERE ROOM_REG='%s'" % (int(s_num.get()))
         cursor.execute(sql)
         result = cursor.fetchone()

         if cursor.rowcount == 0:
            check = False
            messagebox.showwarning(title='WARNING!', message='Enter a vaild guest info !')
         else:
            check = True

      except:
         db_conn.rollback()

   elif search.get() == "National ID":
      try:
         sql = "SELECT * FROM guests WHERE NAT_ID='%s'" % (int(s_num.get()))
         cursor.execute(sql)
         result = cursor.fetchone()

         if cursor.rowcount == 0:
            check = False
            messagebox.showwarning(title='WARNING!', message='Enter a vaild guest info !')
         else:
            check = True

      except:
         db_conn.rollback()
   elif search.get() == "Passport ID":
      if search_box.get()=="Passport ID" and len(search_entery.get())!=9:
         messagebox.showwarning(title='WARNING!', message='Enter a vaild passport ID  please !')

      try:
         sql = "SELECT * FROM guests WHERE PASSP_ID='%s'" % (s_num.get())
         cursor.execute(sql)
         result = cursor.fetchone()

         if cursor.rowcount == 0:
            check = False
            messagebox.showwarning(title='WARNING!', message='Enter a vaild guest info !')

         elif len(result[13]) ==0 :
            check=False
            messagebox.showwarning(title='WARNING!', message="Enter a vaild guest info !")
         # elif  result[13]=="Null":
         #    check = False
         #    messagebox.showwarning(title='WARNING!', message="Enter a vaild guest info !")

         else:
            check = True

      except:
         db_conn.rollback()


   # elif search.get()=="Email":
   #    try:
   #       sql = "SELECT * FROM guests WHERE EMAIL='%s'" % ( s_num.get())
   #       cursor.execute(sql)
   #       result = cursor.fetchone()
   #       if cursor.rowcount == 0:
   #          check = False
   #          messagebox.showwarning(title='WARNING!', message='Enter a vaild guest info !')
   #       else:
   #          check = True
   #       # else:
   #       #
   #       #    for i in range(0, 13):
   #       #       info_list.append(result[i])
   #       # print(info_list)
   #    except:
   #       db_conn.rollback()


   if check==True:
      show(f4)
      Label(f4, text='Guest info', font=("Forte", 50, "bold"), bg="#9e6960", fg="#ffffff", anchor="w").place(relx=0, rely=0,relheight=0.10, relwidth=1)

      Label(f4, text="ID :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.15, height=40,
                                                                                       width=400)
      Label(f4, text=result[0], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.15, height=40,
                                                                                        width=400)

      Label(f4, text="Name :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.20, height=40,width=400)
      Label(f4, text=result[1], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.20, height=40,width=400)

      Label(f4, text="Age :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.25, height=40,
                                                                                       width=400)
      Label(f4, text=result[2], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.25, height=40,
                                                                                        width=400)
      Label(f4, text="Address  :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.30, height=40,
                                                                                       width=400)
      Label(f4, text=result[3], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.30, height=40,
                                                                                        width=400)
      Label(f4, text="Email :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.35, height=40,
                                                                                       width=400)
      Label(f4, text=result[4], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.35, height=40,
                                                                                        width=400)
      Label(f4, text="Mobile phone :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.40, height=40,
                                                                                       width=400)
      Label(f4, text=result[5], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.40, height=40,
                                                                                        width=400)
      Label(f4, text="National ID :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.45, height=40,
                                                                                       width=400)
      Label(f4, text=result[6], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.45, height=40,
                                                                                        width=400)
      Label(f4, text="Registered room :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.50, height=40,
                                                                                       width=400)
      Label(f4, text=result[7], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.50, height=40,
                                                                                        width=400)
      Label(f4, text="number of persons :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.55, height=40,
                                                                                       width=400)
      Label(f4, text=result[8], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.55, height=40,
                                                                                        width=300)
      Label(f4, text="Room system :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.60, height=40,
                                                                                       width=400)
      Label(f4, text=result[9], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.60, height=40,
                                                                                        width=400)
      Label(f4, text="Number of registered days  :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.65, height=40,
                                                                                       width=400)
      Label(f4, text=result[10], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.65, height=40,
                                                                                        width=400)
      Label(f4, text="The used Payment Method :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.70, height=40,
                                                                                       width=400)
      Label(f4, text=result[11], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.70, height=40,
                                                                                        width=200)
      Label(f4, text="Country :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.75,
                                                                                               height=40,
                                                                                               width=400)
      Label(f4, text=result[12], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.75,
                                                                                             height=40, width=400)
      Label(f4, text="Passport ID :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.80,
                                                                                               height=40,
                                                                                               width=400)
      Label(f4, text=result[13], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.80,
                                                                                             height=40, width=400)
      Label(f4, text="His/Her Bill :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.85, height=40,
                                                                                       width=400)
      Label(f4, text=result[14], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.85,height=40,width=400)



   Button(f4, text='go back', font=("Forte", 25), bg="#9e6960", fg="#ffffff", activeforeground="#ffffff",activebackground="#9e6960", command=lambda: show(f3)).place(relx=0, rely=0.88, height=103, width=200)


def search_for_a_worker():

   if len(wk_search_entery.get())==0:
      wk_search_entery.configure(bg="#f75957")
      messagebox.showwarning(title='WARNING!', message='search box is empty !')


   elif wk_search_box.get()=="ID" or wk_search_box.get()=="Room number" or wk_search_box.get()=="National ID" :
      try:
         int(wk_search_entery.get())
         if wk_search_box.get()=="National ID" and len(wk_search_entery.get())!=14:
            messagebox.showwarning(title='WARNING!', message='pls enter a vaild National ID!')

      except ValueError:
         messagebox.showwarning(title='WARNING!', message='Enter a vaild number please !')



   if wk_search_box.get()=="Choose":
      messagebox.showwarning(title='WARNING!', message='pls choose an option from the search list')



   wk_search_entery.configure(bg="#ffffff")
   check = False
   result=""

   if wk_search.get()=="ID":
     try:
        sql = "SELECT * FROM workers WHERE ID='%s'" % (int(wk_sr_num.get()))
        cursor.execute(sql)
        result = cursor.fetchone()

        if cursor.rowcount==0:
           check=False
           messagebox.showwarning(title='WARNING!', message='Enter a vaild worker info !')
        else:
           check=True


     except:
        db_conn.rollback()


   elif wk_search.get() == "National ID":
      try:
         sql = "SELECT * FROM workers WHERE NAT_ID='%s'" % (int(wk_sr_num.get()))
         cursor.execute(sql)
         result = cursor.fetchone()

         if cursor.rowcount == 0:
            check = False
            messagebox.showwarning(title='WARNING!', message='Enter a vaild worker info !')
         else:
            check = True

      except:
         db_conn.rollback()



   # elif search.get()=="Email":
   #    try:
   #       sql = "SELECT * FROM guests WHERE EMAIL='%s'" % ( s_num.get())
   #       cursor.execute(sql)
   #       result = cursor.fetchone()
   #       if cursor.rowcount == 0:
   #          check = False
   #          messagebox.showwarning(title='WARNING!', message='Enter a vaild guest info !')
   #       else:
   #          check = True
   #       # else:
   #       #
   #       #    for i in range(0, 13):
   #       #       info_list.append(result[i])
   #       # print(info_list)
   #    except:
   #       db_conn.rollback()


   if check==True:
      show(f9)
      Label(f9, text='Guest info', font=("Forte", 50, "bold"), bg="#9e6960", fg="#ffffff", anchor="w").place(relx=0, rely=0,relheight=0.10, relwidth=1)

      Label(f9, text="ID :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.15, height=40,
                                                                                       width=400)
      Label(f9, text=result[0], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.15, height=40,
                                                                                        width=400)

      Label(f9, text="Name :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.20, height=40,width=400)
      Label(f9, text=result[1], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.20, height=40,width=400)

      Label(f9, text="Age :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.25, height=40,
                                                                                       width=400)
      Label(f9, text=result[2], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.25, height=40,
                                                                                        width=400)
      Label(f9, text="Address  :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.30, height=40,
                                                                                       width=400)
      Label(f9, text=result[3], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.30, height=40,
                                                                                        width=400)
      Label(f9, text="Email :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.35, height=40,
                                                                                       width=400)
      Label(f9, text=result[4], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.35, height=40,
                                                                                        width=400)
      Label(f9, text="Mobile phone :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.40, height=40,
                                                                                       width=400)
      Label(f9, text=result[5], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.40, height=40,
                                                                                        width=400)
      Label(f9, text="National ID :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.45, height=40,
                                                                                       width=400)
      Label(f9, text=result[6], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.45, height=40,
                                                                                        width=400)
      Label(f9, text="JOB :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.50, height=40,
                                                                                       width=400)
      Label(f9, text=result[7], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.50, height=40,
                                                                                        width=400)
      Label(f9, text="Salary :", anchor="e", bg="#ffffff", font=("prototype", 20)).place(relx=0.05, rely=0.55, height=40,
                                                                                       width=400)
      Label(f9, text=result[8], anchor="w", bg="#ffffff", font=("Comic Sans MS", 20)).place(relx=0.50, rely=0.55, height=40,
                                                                                        width=300)



   Button(f9, text='go back', font=("Forte", 25), bg="#9e6960", fg="#ffffff", activeforeground="#ffffff",activebackground="#9e6960", command=lambda: show(f8)).place(relx=0, rely=0.88, height=103, width=200)
#****************** End ************************

#********************* Inserting new worker functions ***********************************


# def check_wk_name():
#    n=wk_name.get()
#    l=len(wk_name.get())
#    if len(n)==0:
#       messagebox.showwarning(title='WARNING!', message='Name box is empty !')
#       wk_E1.configure(bg='#f75957')
#       return False
#    for i in range(0,l):
#       if n[i].isdigit()==True:
#             messagebox.showwarning(title='WARNING!',message='Enter a valid Name!')
#             wk_E1.configure(bg='#f75957')
#             return False
#    wk_E1.configure(bg='#ffffff')
#    return True


# def check_wk_age():
#    try:
#       if len(wk_age.get())==0:
#          messagebox.showwarning(title='WARNING!', message='Age box is empty!')
#          wk_E2.configure(bg='#f75957')
#          return False
#
#       a=int(wk_age.get())
#
#       if a<100 and a>0:
#          wk_E2.configure(bg='#ffffff')
#          return True
#       else:
#          messagebox.showwarning(title='WARNING!', message='Enter a valid age!')
#          wk_E2.configure(bg='#f75957')
#          return False
#    except ValueError:
#       messagebox.showwarning(title='WARNING!', message='Enter a valid age!')
#       wk_E2.configure(bg='#f75957')
#       return False
#

# def check_wk_email():
#    c=0
#    e=wk_email.get()
#    if len(wk_email.get())==0:
#       messagebox.showwarning(title='WARNING!', message='Email box is empty')
#       wk_E4.configure(bg=war_red)
#       return False
#    for i in range(0,len(wk_email.get())):
#       if e[i]=='@':
#          c+=1
#    if e.endswith(".com",0,len(e)):
#       c+=1
#    if c==2:
#       wk_E4.configure(bg=white)
#       return True
#    else :
#       messagebox.showwarning(title='WARNING!', message='invalid Email !')
#       wk_E4.configure(bg=war_red)
#       return False
#
# def check_wk_mobile():
#    try:
#       if len(wk_mobile.get()) == 0:
#          messagebox.showwarning(title='WARNING!', message='Mobile phone box is empty!')
#          wk_E5.configure(bg=war_red)
#          return False
#
#       m = int(wk_mobile.get())
#
#       if len(wk_mobile.get())==11 and (wk_mobile.get()).startswith("01"):
#          wk_E5.configure(bg=white)
#          return True
#       else:
#          messagebox.showwarning(title='WARNING!', message='Enter a valid phone number!')
#          wk_E5.configure(bg=war_red)
#          return False
#    except ValueError:
#       messagebox.showwarning(title='WARNING!', message='Enter a valid phone number!')
#       wk_E5.configure(bg=war_red)
#       return False
def check_wk_addr():
   if len(wk_addr.get())==0 :
      messagebox.showwarning(title='WARNING!', message='Address box is empty')
      wk_E3.configure(bg=war_red)
      return False
   wk_E3.configure(bg=white)
   return True

def check_wk_nat_id():
   try:
      if len(wk_na_id.get()) == 0 :
         messagebox.showwarning(title='WARNING!', message='National ID box is empty!')
         wk_E6.configure(bg=war_red)
         return False

      nat=int(wk_na_id.get())

      if len(wk_na_id.get())==14  :
         wk_E6.configure(bg=white)
         return True
      elif len(wk_na_id.get())!=14 :
         messagebox.showwarning(title='WARNING!', message='Enter a valid National ID!')
         wk_E6.configure(bg=war_red)
         return False

   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid National ID!')
      wk_E6.configure(bg=war_red)
      return False

def check_job_chooser():
   if joboptions.get()=="Choose":
      messagebox.showwarning(title='WARNING!', message='Choose a job from Job box chooser!')
      return False

   return True

def calculate_salary():
   standard=4000
   total=0
   # jobslist = ["Cleaner", "Room survice", "Chief", "Cooker", "Dishes cleaner", "Receptionist", "Guard","Manager"]
   if job.get()=="Cleaner":
      total=standard-500
      return total

   elif job.get()=="Room survice":
      total = standard + 500
      return total

   elif job.get() == "Chief":
      total = standard + 2000
      return total

   elif job.get() == "Cooker":
      total = standard + 700
      return total

   elif job.get() == "Dishes cleaner":
      total = standard -500
      return total

   elif job.get() == "Receptionist":
      total = standard + 0
      return total

   elif job.get() == "Guard":
      total = standard + 200
      return total

   elif job.get() == "Manager":
      total = standard + 3000
      return total



def inserting_new_worker():
   if  check_name(wk_name,wk_E1) and check_age(wk_age,wk_E2) and check_wk_addr() and check_email(wk_email,wk_E4) \
           and check_mobile(wk_mobile,wk_E5) and check_wk_nat_id():
      salary=calculate_salary()
      if messagebox.askyesno(title='Confirmation', message='Do you really want to submit ?'):

         sql = "INSERT INTO workers (NAME, \
                          AGE,ADDRESS, EMAIL,PHONE,NAT_ID,JOB,SALARY) \
                          VALUES ('%s', '%d', '%s', '%s' , '%s', '%s', '%s', '%d')" % \
               (wk_name.get(),int(wk_age.get()),wk_addr.get(),wk_email.get(),wk_mobile.get(),wk_na_id.get(),job.get(),salary)


         try:

            cursor.execute(sql)
            db_conn.commit()
            messagebox.showinfo(title='Info', message='Submited Successfully !')
            sql = "SELECT ID FROM workers WHERE NAT_ID=%s" % (wk_na_id.get())
            cursor.execute(sql)
            result = cursor.fetchone()
            msg = 'your ID is ' + str(result[0])
            messagebox.showinfo(title='Info', message=msg)

         except:

            db_conn.rollback()

         # db_conn.close()

         delete(2)


#****************** End ************************

#********************* updating worker functions ***********************************


def update_worker_info():

   check = True
   result=""


   if len(wk_id.get())==0:
      messagebox.showwarning(title='WARNING!', message='ID box is empty !')
      entery_id.configure(bg="#f75957")
      check = True
   elif len(wk_id.get())>0:
      try:
         sql = "SELECT * FROM workers WHERE ID='%s'" % (int(wk_id.get()))
         cursor.execute(sql)
         result = cursor.fetchone()

         if cursor.rowcount == 0:
            check = False
            messagebox.showwarning(title='WARNING!', message='Enter a vaild worker ID !')
         else:
            check = True


      except:
         db_conn.rollback()





   if updateoptions.get() == "Choose":
      messagebox.showwarning(title='WARNING!', message='pls choose an option from the option list')
      check = False

   # updatelist = ["Salary", 'phone number', 'Address', 'Email']
   if len(entery_updated.get())==0:
      messagebox.showwarning(title='WARNING!', message='Edit box is empty !')
      entery_updated.configure(bg=war_red)
      check = False
   elif updateoptions.get()=="Salary" or updateoptions.get()=="phone number":
      try:
         int(entery_updated.get())
         if updateoptions.get()=="phone number" and len(entery_updated.get()) !=11:
            entery_updated.configure(bg=war_red)
            check = False
            messagebox.showwarning(title='WARNING!', message='Enter a vaild phone number please !')

      except ValueError:
         messagebox.showwarning(title='WARNING!', message='Enter a vaild number please !')
         entery_updated.configure(bg=war_red)
         check = False




   if check :


      entery_id.configure(bg="#ffffff")
      entery_updated.configure(bg="#ffffff")
      if updateoptions.get() == "Salary":
         try:
            if messagebox.askyesno(title='Confirmation', message='Do you really want to update ?'):
               sql = "UPDATE workers SET SALARY = '%d' WHERE ID = '%d'" % (int(entery_updated.get()), int(wk_id.get()))
               cursor.execute(sql)
               db_conn.commit()
               messagebox.showinfo(title='info', message='updated successfully !')
               entery_id.delete(0, END)
               entery_updated.delete(0, END)

            else:
               pass


         except:
            db_conn.rollback()

      elif updateoptions.get() == "Email":
         if check_email(wk_update_entery,entery_updated) :
            try:
               if messagebox.askyesno(title='Confirmation', message='Do you really want to update ?'):
                  sql = "UPDATE workers SET 	EMAIL = '%s' WHERE ID = '%d'" % (entery_updated.get(), int(wk_id.get()))

                  cursor.execute(sql)

                  db_conn.commit()

                  messagebox.showinfo(title='info', message='updated successfully !')
                  entery_id.delete(0, END)
                  entery_updated.delete(0, END)

               else:
                  pass



            except:

               db_conn.rollback()
         else :
            entery_updated.configure(bg=war_red)




      elif updateoptions.get() == "phone number":
         if check_mobile(wk_update_entery,entery_updated):
            try:
               if messagebox.askyesno(title='Confirmation', message='Do you really want to update ?'):
                  sql = "UPDATE workers SET PHONE = '%s' WHERE ID = '%d'" % (entery_updated.get(), int(wk_id.get()))

                  cursor.execute(sql)

                  db_conn.commit()

                  messagebox.showinfo(title='info', message='updated successfully !')
                  entery_id.delete(0, END)
                  entery_updated.delete(0, END)
               else:
                  pass

            except:

               db_conn.rollback()
         else:
            entery_updated.configure(bg=war_red)



      elif updateoptions.get() == "Address":

         try:
            if messagebox.askyesno(title='Confirmation', message='Do you really want to update ?'):
               sql = "UPDATE workers SET ADDRESS = '%s' WHERE ID = '%d'" % (entery_updated.get(), int(wk_id.get()))

               cursor.execute(sql)

               db_conn.commit()

               messagebox.showinfo(title='info', message='updated successfully !')
               entery_id.delete(0, END)
               entery_updated.delete(0, END)
            else:
               pass



         except:

            db_conn.rollback()


def delete_worker():
   check = True
   result = ""

   if len(wk_id.get()) == 0:
      messagebox.showwarning(title='WARNING!', message='ID box is empty !')
      entery_id.configure(bg="#f75957")
      check = True
   elif len(wk_id.get()) > 0:
      try:
         sql = "SELECT * FROM workers WHERE ID='%s'" % (int(wk_id.get()))
         cursor.execute(sql)
         result = cursor.fetchone()

         if cursor.rowcount == 0:
            check = False
            messagebox.showwarning(title='WARNING!', message='Enter a vaild worker ID !')
         else:
            check = True


      except:
         db_conn.rollback()

   if check:
      try:
         sql = "DELETE FROM workers WHERE ID ='%d'" % (int(wk_id.get()))
         cursor.execute(sql)
         db_conn.commit()
         messagebox.showinfo(title='info', message='Deleted successfully !')

      except:
         db_conn.rollback()


#****************** End ************************


#*********************** Main project ***************************

f1=Frame(window, bg="#ffffff") # Main menu
lof.append(f1)
f2=Frame(window, bg = "#ffffff")  # Check in
lof.append(f2)
f3=Frame(window,  bg ="#ffffff")# searching for a guest
lof.append(f3)
f4=Frame(window,  bg ="#ffffff")# the result of searching for a guest
lof.append(f4)
f5=Frame(window,  bg ="#ffffff")# HR Managment frame
lof.append(f5)
f6=Frame(window,  bg ="#ffffff")# inserting a new worker
lof.append(f6)
f7=Frame(window,  bg ="#ffffff")# managing workers frame
lof.append(f7)
f8=Frame(window,  bg ="#ffffff")# searching for a worker
lof.append(f8)
f9=Frame(window,  bg ="#ffffff")# the result of searching for a worker
lof.append(f9)
root=Frame(window,  bg ="#ffffff")# guest data managment frame
lof.append(root)


for i in lof:
    i.place(relx=0, rely=0, relheight=1, relwidth=1)

#============================================= main manu =================================
Label(f1,text='Main Menu',font = ("Forte", 50,"bold"), bg = "#9e6960",fg="#ffffff").place(relx=0, rely=0, relheight=0.15, relwidth=1)
Button(f1,text='Check in',font = ("Forte", 30),bg = "#9e6960",fg="#ffffff",command=lambda : show(f2)).place(relx=0.23, rely=0.17, height=103, width=566)
Button(f1,text='Get info of a guest ',font = ("Forte", 30),fg="#ffffff",bg = "#9e6960",command=lambda : show(f3)).place(relx=0.23, rely=0.31, height=93, width=566)
Button(f1,text='Guest data managment ',font = ("Forte", 30),fg="#ffffff",bg = "#9e6960",command=lambda : show(root)).place(relx=0.23, rely=0.44, height=93, width=566)
Button(f1,text='HR Managment section ',font = ("Forte", 30),fg="#ffffff",bg = "#9e6960",command=lambda : show(f5)).place(relx=0.23, rely=0.58, height=93, width=566)


#=======================================================   Check in  ====================================================
Label(f2,text='Check in form',font = ("prototype",35,"bold"), bg = "#9e6960",anchor="w",fg="#ffffff").place(relx=0, rely=0, relheight=0.10, relwidth=1)

Label(f2,text="Name :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.15, height=40, width=320)
name=StringVar()
E1=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=name)
E1.place(relx=0.37, rely=0.15,height=34, relwidth=0.43)

Label(f2,text="Age :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.20, height=40, width=320)
age=StringVar()
E2=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=age)
E2.place(relx=0.37,rely=0.20,height=34, width=150)

Label(f2,text="Address :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.25, height=40, width=320)
addr=StringVar()
E3=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=addr)
E3.place(relx=0.37,rely=0.25,height=34, relwidth=0.43)

Label(f2,text="Email :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.30, height=40, width=320)
email=StringVar()
E4=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=email)
E4.place(relx=0.37, rely=0.30,height=34, relwidth=0.43)

Label(f2,text="Mobile phone :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.35, height=40, width=320)
mobile=StringVar()
E5=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=mobile)
E5.place(relx=0.37,rely=0.35,height=34, relwidth=0.43)

Label(f2,text="National ID :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.40, height=40, width=320)
na_id=StringVar()
E6=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=na_id)
E6.place(relx=0.37,rely=0.40,height=34, relwidth=0.43)

Label(f2,text="persons number :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.45, height=40, width=320)
p_num=StringVar()
E7=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=p_num)
E7.place(relx=0.37,  rely=0.45,height=34, width=150)

Label(f2,text="Register room number :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.50, height=40, width=320)
room_num=StringVar()

Co3=ttk.Combobox(f2,state="readonly",height=5,font = ("Arial", 20),textvariable=room_num)
add_none_registered_rooms()
Co3.place(relx=0.37,  rely=0.50,height=34, width=150)
Co3.set("Choose")

Label(f2,text="Room system :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.55, height=40, width=320)
roomlist=["Single","Double","Triple","Quad","Queen","King","Studio"]
combo1=StringVar()
Co1=ttk.Combobox(f2,values=roomlist,state="readonly",height=5,font = ("Arial", 20),textvariable=combo1)
Co1.place(relx=0.37,  rely=0.55,height=34, width=200)
Co1.set("Choose")

Label(f2,text="Reserved days :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.60, height=40, width=320)
days=StringVar()
E9=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=days)
E9.place(relx=0.37,rely=0.60,height=34, width=150)

Label(f2,text="Payment method :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.65, height=40, width=320)
paylist=["CASH","CREDIT CARD","HIBREAD"]
combo2=StringVar()
Co2=ttk.Combobox(f2,values=paylist,state="readonly",height=5,font = ("Arial", 20),textvariable=combo2)
Co2.place(relx=0.37,  rely=0.65,height=34, width=230)
Co2.set("Choose")

Label(f2,text="Country :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.70, height=40, width=320)
countrylist=["Egypt","USA","UK","Suadi Arbia","France","Germany","Italy","Japan","Malysia","Sudan","Lebanon","UAE","Kwait"]
combo3=StringVar()
Co4=ttk.Combobox(f2,values=countrylist,state="readonly",height=6,font = ("Arial", 20),textvariable=combo3)
Co4.place(relx=0.37,  rely=0.70,height=34, width=230)
Co4.set("Egypt")

Label(f2,text="Passpost ID :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.75, height=40, width=320)
passp_id=StringVar()
E10=Entry(f2,font = ("Arial", 20),borderwidth=2,textvariable=passp_id)
E10.place(relx=0.37,rely=0.75,height=34, width=180)


Button(f2,text='Submit',font = ("prototype", 25), bg = "#9e6960",fg="#ffffff",command=insert_guest,activeforeground="#ffffff",activebackground="#9e6960").place(relx=0.40, rely=0.85, height=90, width=200)


Button(f2,text='Go back',font = ("prototype", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=lambda : show(f1)).place(relx=0, rely=0.88, height=103, width=200)

#============================================= Get info of a guest ======================================================
Label(f3,text='Get info of a guest',font = ("Forte", 35), bg = "#9e6960",anchor="w",fg="#ffffff").place(relx=0, rely=0, relheight=0.10, relwidth=1)

Label(f3,text="Choose the way of searching :",anchor="w",bg="#ffffff", font=("prototype",25)).place(relx=0.05, rely=0.40, height=40, width=450)

search=StringVar()
search_list=['ID','Room number','National ID','Passport ID']
search_box=ttk.Combobox(f3,values=search_list,state="readonly",height=5,font = ("Arial", 20),textvariable=search)
search_box.place(relx=0.55,rely=0.40,height=34, width=230)
search_box.set("Choose")

s_num=StringVar()
search_entery=Entry(f3,font = ("Arial", 20),borderwidth=2,textvariable=s_num)
search_entery.place(relx=0.30,rely=0.55,height=34, width=400)

Button(f3,text='Search',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",command= search_for_a_guest).place(relx=0.40, rely=0.70, height=90, width=200)


Button(f3,text='Go back',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",command=lambda : show(f1)).place(relx=0, rely=0.88, height=90, width=200)


#============================================= HR Managment screen ======================================================
Label(f5,text='HR Managment',font = ("Forte", 35), bg = "#9e6960",fg="#ffffff").place(relx=0, rely=0, relheight=0.15, relwidth=1)

Button(f5,text='ADD new worker',font = ("Forte", 30),bg = "#9e6960",fg="#ffffff",command=lambda : show(f6)).place(relx=0.23, rely=0.17, height=103, width=566)
Button(f5,text='Update workers info ',font = ("Forte", 30),fg="#ffffff",bg = "#9e6960",command=lambda : show(f7)).place(relx=0.23, rely=0.31, height=93, width=566)
Button(f5,text='Get info of a worker ',font = ("Forte", 30),fg="#ffffff",bg = "#9e6960",command=lambda : show(f8)).place(relx=0.23, rely=0.45, height=93, width=566)


Button(f5,text='Go back',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",command=lambda : show(f1)).place(relx=0, rely=0.88, height=90, width=200)



#============================================= ADD new worker ======================================================
Label(f6,text='ADD New Worker Form',font = ("Forte", 35), bg = "#9e6960",anchor='w',fg="#ffffff").place(relx=0, rely=0, relheight=0.12, relwidth=1)

Label(f6,text="Name :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.15, height=40, width=320)
wk_name=StringVar()
wk_E1=Entry(f6,font = ("Arial", 20),borderwidth=2,textvariable=wk_name)
wk_E1.place(relx=0.37, rely=0.15,height=34, relwidth=0.43)

Label(f6,text="Age :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.20, height=40, width=320)
wk_age=StringVar()
wk_E2=Entry(f6,font = ("Arial", 20),borderwidth=2,textvariable=wk_age)
wk_E2.place(relx=0.37,rely=0.20,height=34, width=150)

Label(f6,text="Address :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.25, height=40, width=320)
wk_addr=StringVar()
wk_E3=Entry(f6,font = ("Arial", 20),borderwidth=2,textvariable=wk_addr)
wk_E3.place(relx=0.37,rely=0.25,height=34, relwidth=0.43)

Label(f6,text="Email :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.30, height=40, width=320)
wk_email=StringVar()
wk_E4=Entry(f6,font = ("Arial", 20),borderwidth=2,textvariable=wk_email)
wk_E4.place(relx=0.37, rely=0.30,height=34, relwidth=0.43)

Label(f6,text="Mobile phone :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.35, height=40, width=320)
wk_mobile=StringVar()
wk_E5=Entry(f6,font = ("Arial", 20),borderwidth=2,textvariable=wk_mobile)
wk_E5.place(relx=0.37,rely=0.35,height=34, relwidth=0.43)

Label(f6,text="National ID :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.40, height=40, width=320)
wk_na_id=StringVar()
wk_E6=Entry(f6,font = ("Arial", 20),borderwidth=2,textvariable=wk_na_id)
wk_E6.place(relx=0.37,rely=0.40,height=34, relwidth=0.43)

Label(f6,text="JOB :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.45, height=40, width=320)
jobslist=["Cleaner","Room survice","Chief","Cooker","Dishes cleaner","Receptionist","Guard","Manager"]
job=StringVar()
joboptions=ttk.Combobox(f6,values=jobslist,state="readonly",height=6,font = ("Arial", 20),textvariable=job)
joboptions.place(relx=0.37,  rely=0.45,height=34, width=230)
joboptions.set("Choose")

Button(f6,text='Submit',font = ("prototype", 25), bg = "#9e6960",fg="#ffffff",command=inserting_new_worker,activeforeground="#ffffff",activebackground="#9e6960").place(relx=0.40, rely=0.60, height=90, width=200)


Button(f6,text='Go back',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=lambda : show(f5)).place(relx=0, rely=0.88, height=90, width=200)
Button(f6,text='Main menu',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=lambda : show(f1)).place(relx=0.25, rely=0.88, height=90, width=200)

#============================================='Update workers info ' ======================================================
Label(f7,text='ADD New Worker Form',font = ("Forte", 35), bg = "#9e6960",anchor='w',fg="#ffffff").place(relx=0, rely=0, relheight=0.12, relwidth=1)

Label(f7,text="Id of the worker :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.15, height=40, width=320)
wk_id=StringVar()
entery_id=Entry(f7,font = ("Arial", 20),borderwidth=2,textvariable=wk_id)
entery_id.place(relx=0.37, rely=0.15,height=34, width=200)

Label(f7,text="update options :",anchor="e",bg="#ffffff", font=("prototype",20)).place(relx=0, rely=0.20, height=40, width=320)
updatelist=["Salary",'phone number','Address','Email']
opt=StringVar()
updateoptions=ttk.Combobox(f7,values=updatelist,state="readonly",height=6,font = ("Arial", 20),textvariable=opt)
updateoptions.place(relx=0.37,  rely=0.20,height=34, width=230)
updateoptions.set("Choose")

wk_update_entery=StringVar()
entery_updated=Entry(f7,font = ("Arial", 20),borderwidth=2,textvariable=wk_update_entery)
entery_updated.place(relx=0.30, rely=0.35,height=34, width=400)

Button(f7,text='Update',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=update_worker_info).place(relx=0.25, rely=0.50, height=90, width=200)
Button(f7,text='Delete',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=delete_worker).place(relx=0.50, rely=0.50, height=90, width=200)



Button(f7,text='Go back',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=lambda : show(f5)).place(relx=0, rely=0.88, height=90, width=200)
Button(f7,text='Main menu',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=lambda : show(f1)).place(relx=0.25, rely=0.88, height=90, width=200)

#============================================= Get info of a worker ======================================================
Label(f8,text='Get info of a worker',font = ("Forte", 35), bg = "#9e6960",anchor="w",fg="#ffffff").place(relx=0, rely=0, relheight=0.10, relwidth=1)

Label(f8,text="Choose the way of searching :",anchor="w",bg="#ffffff", font=("prototype",25)).place(relx=0.05, rely=0.40, height=40, width=450)

wk_search=StringVar()
wk_search_list=['ID','National ID']
wk_search_box=ttk.Combobox(f8,values=wk_search_list,state="readonly",height=5,font = ("Arial", 20),textvariable=wk_search)
wk_search_box.place(relx=0.55,rely=0.40,height=34, width=230)
wk_search_box.set("Choose")

wk_sr_num=StringVar()
wk_search_entery=Entry(f8,font = ("Arial", 20),borderwidth=2,textvariable=wk_sr_num)
wk_search_entery.place(relx=0.30,rely=0.55,height=34, width=400)

Button(f8,text='Search',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",command= search_for_a_worker).place(relx=0.40, rely=0.70, height=90, width=200)


Button(f8,text='Go back',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",command=lambda : show(f5)).place(relx=0, rely=0.88, height=90, width=200)
Button(f7,text='Main menu',font = ("Forte", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=lambda : show(f1)).place(relx=0.25, rely=0.88, height=90, width=200)
#====================================guest data manganment====================================================

#.............. frame bar.............................
Label(root, text='Data Management', font=("prototype", 30, "bold"), bg="#9e6960", anchor="w",
         fg="#ffffff").place(relx=0, rely=0, relheight=0.10, relwidth=1)

Button(root, text='Go back', font=("Forte", 25), bg="#9e6960", fg="#ffffff").\
                             place(relx=0, rely=0.88, height=90,width=200)
#.................used var.............
row_selected = False
room_no = -1
id_guest = -1
searched_text = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()




btn_search = Button(root)
btn_search["bg"] = "#9e6960"
btn_search["font"] = ("Forte", 24)
btn_search["fg"] = "white"
btn_search["justify"] = "center"
btn_search["text"] = "Search"
btn_search.place(x=280, y=480, width=195, height=54)
btn_search["command"] = search

btn_clear = Button(root)
btn_clear["bg"] = "#9e6960"
btn_clear["font"] = ("Forte", 24)
btn_clear["fg"] = "white"
btn_clear["justify"] = "center"
btn_clear["text"] = "Clear"
btn_clear.place(x=490, y=480, width=216, height=54)
btn_clear["command"] = clear

ent_search = Entry(root, textvariable=searched_text)
ent_search["font"] = ("Forte", 24)
ent_search["fg"] = "#333333"
ent_search["justify"] = "center"
ent_search["text"] = ""
ent_search.place(x=70, y=480, width=198, height=56)

btn_checkout = Button(root)
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
updateoptionss = ttk.Combobox(root, values=updatelist, state="readonly", height=6, font=("Arial", 12), textvariable=opt)
updateoptionss.place(x=440, y=550, width=135, height=42)
updateoptionss.set("Choose")

entery_updateds = Entry(root, font=("Arial", 20), borderwidth=2)
entery_updateds.place(x=330, y=600, width=209, height=39)

btn_update = Button(root, text='Update', font=("Forte", 25), bg="#9e6960", fg="#ffffff", activeforeground="#ffffff",
                    activebackground="#9e6960", command=update_guest)
btn_update.place(x=360, y=650, width=140, height=49)

# .............. fechall data.............
sql = " SELECT NAME,ROOM_REG,DAY_NUM,PAY,BILL FROM guests"
cursor.execute(sql)
rows = cursor.fetchall()

root.update()

# ........... treeview table..................
tree = ttk.Treeview(root, columns=('0', '1', '2', '3', '4'), show="headings", height=3)
tree.place(x=25, y=90, width=887, height=370)

fieldnames = ['NAME', 'ROOM_REG', 'DAY_NUM', 'PAY', 'BILL']
# ...............table headings............
for i in range(5):
    tree.column(i, width=150, anchor=CENTER)
    tree.heading(i, text=fieldnames[i])

tree.bind('<Double 1>', getrow)

table_update(rows)


#==========================================================================================================================

show(f1)
window.mainloop()

# try:
#    int(name.get())
# except ValueError:
#