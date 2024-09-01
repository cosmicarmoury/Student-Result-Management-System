from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image,ImageTk #pip istall pillow
import sqlite3 #pip install sqlite3
import os 

class register:
    def __init__(self,root) :
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#E0EEEE")
        self.bg=ImageTk.PhotoImage(file="newim/i2.jpg")
        self.bg2=ImageTk.PhotoImage(file="newim/YY.jpg")
        self.bg3=ImageTk.PhotoImage(file="newim/i4.jpg")
        


        bg=Label(self.root,image=self.bg).place(x=150,y=0)
        bg2=Label(self.root,image=self.bg2).place(x=80,y=100,width=400,height=500)
        bg3=Label(self.root,image=self.bg3).place(x=130,y=310,height=40)
        frame1=LabelFrame(self.root,bg="#E0EEEE")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=50,y=30)
       # btn1=Button(mframe,text="COURSE",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
       # btn2=Button(mframe,text="STUDENT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_stu).place(x=240,y=5,width=200,height=40)
       # btn3=Button(mframe,text="RESULT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_res).place(x=460,y=5,width=200,height=40)
       # btn4=Button(mframe,text="VIEW RESULT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
       # btn5=Button(mframe,text="LOGOUT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2").place(x=900,y=5,width=200,height=40)
       # btn6=Button(mframe,text="EXIT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2").place(x=1120,y=5,width=200,height=40)
        self.var_fname=StringVar()

        lbl_name=Label(frame1,text="First Name",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black").place(x=50,y=110)
        lbl_sname=Label(frame1,text="Last Name",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black").place(x=370,y=110)
        lbl_con=Label(frame1,text="Contact No.",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black").place(x=50,y=200)
        lbl_em=Label(frame1,text="Email",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black").place(x=370,y=200)
        lbl_pass=Label(frame1,text="Password",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black").place(x=50,y=290)
        lbl_cpass=Label(frame1,text="Confirm Password",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black").place(x=370,y=290)



        self.txt_name=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_name.place(x=50,y=150,width=150)
        self.txt_sname=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_sname.place(x=370,y=150,width=150)
        self.txt_con=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_con.place(x=50,y=240,width=150)
        self.txt_em=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_em.place(x=370,y=240,width=150)
        self.txt_pass=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_pass.place(x=50,y=330,width=150)
        self.txt_cpass=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_cpass.place(x=370,y=330,width=150)


        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree To The Terms And Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("segoe ui semibold",10),bg="lightgray").place(x=50,y=390)
        btn_reg=Button(frame1,text="Register",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.reg_data).place(x=50,y=440,width=200,height=40)
        btn2=Button(self.root,text="Sign In",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.login_widow).place(x=170,y=400,width=200,height=40)

    def login_widow(self):
        self.root.destroy()
        os.system("python login.py")
    
    def clear(self):
        self.txt_name.delete(0,END)
        self.txt_sname.delete(0,END)
        self.txt_em.delete(0,END)
        self.txt_con.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_cpass.delete(0,END)

    def reg_data(self):
        if self.txt_name.get()=="" or self.txt_sname.get()=="" or self.txt_em.get() ==""  or self.txt_con.get()=="" or self.txt_pass.get()=="" or self.txt_cpass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        
      
        elif self.txt_pass.get()!=self.txt_cpass.get():
            messagebox.showerror("Error","Password And Confirm Password Should Be Same",parent=self.root)
        

        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree To Our Terms And Conditions",parent=self.root)


        else:
            try:
                con=sqlite3.connect(database="project.db")
                cur=con.cursor()
                cur.execute("select * from member where Email=?",(self.txt_em.get(),))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already Exists",parent=self.root)
                
                else:
                    cur.execute("INSERT INTO member(FName ,LName , Email ,ContactNo , Password , CPassword) Values(?,?,?,?,?,?)",(self.txt_name.get(),
                              self.txt_sname.get(),
                              self.txt_em.get(),
                              self.txt_con.get(),
                              self.txt_pass.get(),
                              self.txt_cpass.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful!")
                    self.clear()
                    self.login_widow()

            except Exception as ex:
               messagebox.showerror("Error",f"Error due to{str(ex)}")



root=Tk()
obj=register(root)
root.mainloop()
