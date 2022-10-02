from tkinter import Label, messagebox

import pymysql

db_conn = pymysql.connect(host='localhost',
                             user='ano',
                             password='1234a',
                             database='hotel_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db_conn.cursor()


def delete():
   E1.delete(0, END)
   E2.delete(0, END)
   E3.delete(0, END)
   E4.delete(0, END)
   E5.delete(0, END)
   E6.delete(0, END)
   E7.delete(0, END)
   # E8.delete(0, END)
   E9.delete(0, END)
   Co1.set("Choose")
   Co2.set("Choose")
   Co3.set("Choose")


def check_name():
   n=name.get()
   l=len(name.get())
   if len(n)==0:
      messagebox.showwarning(title='WARNING!', message='Name box is empty !')
      E1.configure(bg='#f75957')
      return False
   for i in range(0,l):
      if n[i].isdigit()==True:
            messagebox.showwarning(title='WARNING!',message='Enter a valid Name!')
            E1.configure(bg='#f75957')
            return False
   E1.configure(bg='#ffffff')
   return True


def check_age():
   try:
      if len(age.get())==0:
         messagebox.showwarning(title='WARNING!', message='Age box is empty!')
         E2.configure(bg='#f75957')
         return False

      a=int(age.get())

      if a<100 and a>0:
         E2.configure(bg='#ffffff')
         return True
      else:
         messagebox.showwarning(title='WARNING!', message='Enter a valid age!')
         E2.configure(bg='#f75957')
         return False
   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid age!')
      E2.configure(bg='#f75957')
      return False

def check_addr():
   if len(addr.get())==0:
      messagebox.showwarning(title='WARNING!', message='Address box is empty')
      E3.configure(bg=war_red)
      return False
   E3.configure(bg=white)
   return True

def check_email():
   c=0
   e=email.get()
   if len(email.get())==0:
      messagebox.showwarning(title='WARNING!', message='Email box is empty')
      E4.configure(bg=war_red)
      return False
   for i in range(0,len(email.get())):
      if e[i]=='@':
         c+=1
   if e.endswith(".com",0,len(e)):
      c+=1
   if c==2:
      E4.configure(bg=white)
      return True
   else :
      messagebox.showwarning(title='WARNING!', message='invalid Email !')
      E4.configure(bg=war_red)
      return False

def check_mobile():
   try:
      if len(mobile.get()) == 0:
         messagebox.showwarning(title='WARNING!', message='Mobile phone box is empty!')
         E5.configure(bg=war_red)
         return False

      m = int(mobile.get())

      if len(mobile.get())==11 and (mobile.get()).startswith("01"):
         E5.configure(bg=white)
         return True
      else:
         messagebox.showwarning(title='WARNING!', message='Enter a valid phone number!')
         E5.configure(bg=war_red)
         return False
   except ValueError:
      messagebox.showwarning(title='WARNING!', message='Enter a valid phone number!')
      E5.configure(bg=war_red)
      return False

def check_nat_id():
   try:
      if len(na_id.get()) == 0:
         messagebox.showwarning(title='WARNING!', message='National ID box is empty!')
         E6.configure(bg=war_red)
         return False

      nat=int(na_id.get())

      if len(na_id.get())==14 :
         E6.configure(bg=white)
         return True
      else:
         messagebox.showwarning(title='WARNING!', message='Enter a valid National ID!')
         E6.configure(bg=war_red)
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
         E9.configure(bg=red)
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
   elif rs=="Trible":
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


def insert_guest():
   if check_name() and check_age() and check_addr() and check_email() \
           and check_mobile() and check_nat_id() and check_number_of_persons() \
            and check_reserved_days() and check_room_sys()\
           and check_payment() :
      bill=room_system_calculation()

      if messagebox.askyesno(title='Confirmation',message='Do you really want to submit ?'):

         sql = "INSERT INTO guests (NAME, \
                  AGE,ADDRESS, EMAIL,PHONE,NAT_ID,ROOM_REG,P_NO,ROOM_SYS,DAY_NUM,PAY,BILL) \
                  VALUES ('%s', '%d', '%s', '%s' , '%s', '%s', '%d', '%d', '%s', '%d', '%s', '%d')" % \
               (name.get(), int(age.get()), addr.get(), email.get(), mobile.get(), na_id.get(), int(room_num.get()),
                int(p_num.get()), combo1.get(), int(days.get()), combo2.get(), bill)

         try:

            cursor.execute(sql)
            db_conn.commit()
            messagebox.showinfo(title='Info',message='Submited Successfully !')
            sql = "SELECT ID FROM guests WHERE NAT_ID=%s" % (na_id.get())
            cursor.execute(sql)
            result = cursor.fetchone()
            msg='your ID is '+ str(result[0])
            messagebox.showinfo(title='Info', message=msg)
            add_none_registered_rooms()
         except:

            db_conn.rollback()

         # db_conn.close()

         delete()


#=======================================================check in====================================================
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

Button(f2,text='Submit',font = ("prototype", 25), bg = "#9e6960",fg="#ffffff",command=insert_guest,activeforeground="#ffffff",activebackground="#9e6960").place(relx=0.40, rely=0.77, height=90, width=200)


Button(f2,text='go back',font = ("prototype", 25), bg = "#9e6960",fg="#ffffff",activeforeground="#ffffff",activebackground="#9e6960",command=lambda : show(f1)).place(relx=0, rely=0.88, height=103, width=200)






