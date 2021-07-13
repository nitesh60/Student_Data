# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:48:50 2021

@author: Nitesh
"""
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile
from tkinter import *
import tkinter as tk
from tkinter import Button
import os
from PIL import ImageTk, Image
import pymysql


  
root = tk.Tk()
#change the backgroung
root.config(bg='white')
#changing the diamention width*height+position of window you want to strt
root.geometry('1350x650+00+00')
#changing title
root.title('RESULT')
#creating variable
sid = tk.StringVar()
sid1 = tk.StringVar()
sid2 = tk.StringVar()
sid3 = tk.IntVar()
sid4 = tk.StringVar()
sid5 = tk.StringVar()
sid6 = tk.IntVar()
sid7 = tk.IntVar()
sid8 = tk.IntVar()
sid9 = tk.IntVar()
sid10 = tk.IntVar()
sid11 = tk.IntVar()
sid12 = tk.StringVar()
#waiting function
def clear():
  sid.set('')
  sid1.set('')
  sid2.set('')
  sid3.set('')
  sid4.set('')
  sid5.set('')
  sid6.set(0)
  sid7.set(0)
  sid8.set(0)
  sid9.set(0)
  sid10.set(0)
  sid11.set(0)
  
def connect_db():
  #opening connection to the db
  db = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '12345',
                       database = 'results'
                       )
  
  cursor = db.cursor()
  return db, cursor  
  
def logout():
    ask = tk.messagebox.askyesno('confirmation','do you really want to quit')
    if ask >0:
        root.destroy()

def save_file():
  db,cursor = connect_db()
  query = f"insert into info values('{sid.get()}','{sid1.get()}','{sid2.get()}',{sid3.get()},'{sid4.get()}',{sid5.get()},{sid6.get()},{sid7.get()},{sid8.get()},{sid9.get()},{sid10.get()},{sid11.get()})"
  #for pemanent changes
  cursor.execute(query)
  db.commit()
  db.close()
    
  
def save():
 calculate() 
 present = 'no'
 #check roll no. entere or not
 if sid3.get() == 0:
   tk.messagebox.showerror('Warning','Roll number can not be zero')
 else:
   db,cursor = connect_db()
   query = f"SELECT * FROM info WHERE Roll_no = {sid3.get()}"
   cursor.execute(query)
   is_present = cursor.fetchone()
   #print(is_present())
   if is_present != None:
     present = 'yes'
   if present == 'yes':
     ask = tk.messagebox.askyesno('Update','do you really want to update a record')
     if ask>0:
       save_file()
       tk.messagebox.showinfo('Success',"Record updated sucessfully")
   else:
     save_file()
     tk.messagebox.showinfo('Success',"Record save sucessfully")
   
    
def search():
  present = 'no'
  if sid3.get() == 0:
   tk.messagebox.showerror('Warning','Roll number can not be zero')
  else:
    db,cursor = connect_db()
    query = f"select * from info where  Roll_no = {sid3.get()}"
    cursor.execute(query)
    is_present = cursor.fetchone()
    if is_present!= None:
      present = 'yes'
    if present == 'yes':
      sid.set(is_present[0])
      sid1.set(is_present[1])
      sid2.set(is_present[2])
      sid3.set(is_present[3])
      sid4.set(is_present[4])
      sid5.set(is_present[5])
      sid6.set(is_present[6])
      sid7.set(is_present[7])
      sid8.set(is_present[8])
      sid9.set(is_present[9])
      sid10.set(is_present[10])
      sid11.set(is_present[11])
       
    else:
     clear()
     tk.messagebox.showinfo('Warning','Record is not found')
     
     
def calculate():
  ml = sid6.get()
  r = sid7.get()
  ai = sid8.get()
  ds = sid9.get()
  total = ml+r+ai+ds
  sid10.set(total)
  percentage = (total/400)*100
  sid11.set(percentage) 
  
#create frames
#top frame
top_frame = tk.Frame(root,bg = 'maroon')
top_frame.place(x=5,y=5,width=1340,height=150)
#left frame
left_frame = tk.Frame(root,bg = 'maroon')
left_frame.place(x=5,y=160,width=665,height=330)
#right frame
right_frame = tk.Frame(root,bg = 'maroon')
right_frame.place(x=678,y=160,width=666,height=330)
#buttom frame
button_frame = tk.Frame(root,bg = 'maroon')
button_frame.place(x=5,y=495,width=1340,height=150)
#main title
main_title = tk.Label(top_frame,text='RESULT 2.0',font=('Times New Roman',35,'bold'),bg='maroon',fg='white')
main_title.pack(pady=50)
#main_title.grid(row= 0,column=0,padx=5,pady=5)
#to get title in center

left_title = tk.Label(left_frame,text = "S_Info",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
left_title.grid(row= 0,column=0,padx=5,pady=5)#rows and column

side_label = tk.Label(left_frame,text = "F_name",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_label.grid(row= 1,column=0,padx=5,pady=5)
side_entry = tk.Entry(left_frame,textvariable = sid,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_entry.grid(row= 1,column=1,padx=5,pady=5)

side_label2 = tk.Label(left_frame,text = "L_name",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_label2.grid(row= 2,column=0,padx=5,pady=5)
side_entry2 = tk.Entry(left_frame,textvariable = sid1,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_entry2.grid(row= 2,column=1,padx=5,pady=5)

side_label3 = tk.Label(left_frame,text = "Class",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_label3.grid(row= 3,column=0,padx=5,pady=5)
side_entry3 = tk.Entry(left_frame,textvariable = sid2,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_entry3.grid(row= 3,column=1,padx=5,pady=5)

side_label4 = tk.Label(left_frame,text = "Roll_no",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_label4.grid(row= 4,column=0,padx=5,pady=5)
side_entry4 = tk.Entry(left_frame,textvariable = sid3,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_entry4.grid(row= 4,column=1,padx=5,pady=5)

side_label4 = tk.Label(left_frame,text = "Email_id",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_label4.grid(row= 5,column=0,padx=5,pady=5)
side_entry4 = tk.Entry(left_frame,textvariable = sid4,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_entry4.grid(row= 5,column=1,padx=5,pady=5)

side_label4 = tk.Label(left_frame,text = "Phone_no",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_label4.grid(row= 6,column=0,padx=5,pady=5)
side_entry4 = tk.Entry(left_frame,textvariable = sid5,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_entry4.grid(row= 6,column=1,padx=5,pady=5)

right_title = tk.Label(right_frame,text = "S_Marks",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
right_title.grid(row= 0,column=0,padx=5,pady=5)

side_r_label = tk.Label(right_frame,text = "ML_marks",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_label.grid(row= 1,column=0,padx=5,pady=5)
side_r_entry = tk.Entry(right_frame,textvariable = sid6,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_entry.grid(row= 1,column=1,padx=5,pady=5)

side_r_label2 = tk.Label(right_frame,text = "R_marks",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_label2.grid(row= 2,column=0,padx=5,pady=5)
side_r_entry2 = tk.Entry(right_frame,textvariable = sid7,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_entry2.grid(row= 2,column=1,padx=5,pady=5)

side_r_label3 = tk.Label(right_frame,text = "AI_marks",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_label3.grid(row= 3,column=0,padx=5,pady=5)
side_r_entry3 = tk.Entry(right_frame,textvariable = sid8,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_entry3.grid(row= 3,column=1,padx=5,pady=5)

side_r_label4 = tk.Label(right_frame,text = "DS_marks",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_label4.grid(row= 4,column=0,padx=5,pady=5)
side_r_entry4 = tk.Entry(right_frame,textvariable = sid9,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_entry4.grid(row= 4,column=1,padx=5,pady=5)

side_r_label5 = tk.Label(right_frame,text = "Total",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_label5.grid(row= 5,column=0,padx=5,pady=5)
side_r_entry5 = tk.Entry(right_frame,textvariable = sid10,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_entry5.grid(row= 5,column=1,padx=5,pady=5)

side_r_label6 = tk.Label(right_frame,text = "Percentage",font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_label6.grid(row= 6,column=0,padx=5,pady=5)
side_r_entry6 = tk.Entry(right_frame,textvariable = sid11,font=('Times New Roman',20,'bold'),bg='maroon',fg='white')
side_r_entry6.grid(row= 6,column=1,padx=5,pady=5)
 

#create button 
close_button = tk.Button(button_frame, text = 'Quit',font=('Times New Roman',20,'bold'),bg='maroon',fg='white',command = logout)
close_button.grid(row = 1, column = 0,padx=5,pady=5)

clear_button = tk.Button(button_frame, text = 'Clear',font=('Times New Roman',20,'bold'),bg='maroon',fg='white',command=clear)
clear_button.grid(row = 1, column = 1,padx=5,pady=5)

save_button = tk.Button(button_frame, text = 'Save',font=('Times New Roman',20,'bold'),bg='maroon',fg='white',command=save)
save_button.grid(row = 1, column = 2,padx=5,pady=5)

#search bar
search_button = tk.Button(button_frame, text = 'search',font=('Times New Roman',20,'bold'),bg='maroon',fg='white',command=search)
search_button.grid(row = 1, column = 5,padx=5,pady=5)

root.mainloop()#keepig the windows open continously