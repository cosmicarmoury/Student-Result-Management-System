from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image,ImageTk #pip istall pillow


class studentc:
    def __init__(self,root) :
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x480+80+170")
        self.root.config(bg="#E0EEEE")
        self.root.focus_force()

        title=Label(self.root,text="Manage Student Details",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=15,width=1200,height=35)

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gend=StringVar()
        self.var_dob=StringVar()
        self.var_cont=StringVar()
        self.var_c=StringVar()
        self.var_city=StringVar()
        self.var_state=StringVar()
        self.var_address=StringVar()

        




        lbl_rollno=Label(self.root,text="Roll No",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=10,y=110)
        lbl_email=Label(self.root,text="Email",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=10,y=160)
        lbl_gend=Label(self.root,text="Gender",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=10,y=210)
        lbl_state=Label(self.root,text="State",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=10,y=260)
        lbl_address=Label(self.root,text="Address",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=10,y=310)

        
        lbl_dob=Label(self.root,text="D.O.B",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=390,y=60)
        lbl_cont=Label(self.root,text="Contact",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=390,y=110)
        lbl_city=Label(self.root,text="City",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=390,y=260)
        lbl_c=Label(self.root,text="Course",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=390,y=210)

        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black")
        self.txt_roll.place(x=160,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=160,y=110,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=160,y=160,width=200)

        self.txt_gend=ttk.Combobox(self.root,textvariable=self.var_gend,values=("Select","Male","Female","Other"),font=("segoe ui semibold",16,"bold"),state='readonly',justify=CENTER,)
        self.txt_gend.place(x=160,y=210,width=200)
        self.txt_gend.current(0)
        self.txt_address=Text(self.root,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black")
        self.txt_address.place(x=160,y=310,width=545,height=60)

        self.course_list=[]
        self.fetch_c()

        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=500,y=60,width=200)
        txt_cont=Entry(self.root,textvariable=self.var_cont,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=500,y=110,width=200)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=160,y=260,width=200)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("segoe ui semibold",16,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=500,y=260,width=200)
        self.txt_c=ttk.Combobox(self.root,textvariable=self.var_c,values=self.course_list,font=("segoe ui semibold",16,"bold"),state='readonly',justify=CENTER,)
        self.txt_c.place(x=500,y=210,width=200)
        self.txt_c.set("Select")





        self.btn_add=Button(self.root,text="Save",font=("segoe ui semibold",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("segoe ui semibold",15,"bold"),bg="#4caf50",fg="black",cursor="hand2", command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("segoe ui semibold",15,"bold"),bg="#f44336",fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("segoe ui semibold",15,"bold"),bg="#607d8b",fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

#=============SEARCH=====================================================================================================
        self.var_s=StringVar()
        lbl_search_rollno=Label(self.root,text="Roll No",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=730,y=60)
        txt_search_rollno=Entry(self.root,textvariable=self.var_s,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=("segoe ui semibold",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.search).place(x=1080,y=60,width=120,height=28)
        
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=110,width=470,height=340)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)



        self.coursetable=ttk.Treeview(self.C_Frame,columns=("rollno","name","email","gender","dob","contact","course","state","city","address"), xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.coursetable.xview)
        scrolly.config(command=self.coursetable.yview)

        self.coursetable.heading("rollno",text="Roll No")
        self.coursetable.heading("name",text="Name")
        self.coursetable.heading("email",text="Email")
        self.coursetable.heading("gender",text="Gender")
        self.coursetable.heading("dob",text="DOB")
        self.coursetable.heading("contact",text="Contact")
        self.coursetable.heading("course",text="Course")
        self.coursetable.heading("state",text="State")
        self.coursetable.heading("city",text="City")
        self.coursetable.heading("address",text="Address")
        self.coursetable["show"]='headings'
        self.coursetable.column("rollno",width=100)
        self.coursetable.column("name",width=100)
        self.coursetable.column("email",width=100)
        self.coursetable.column("gender",width=100)
        self.coursetable.column("dob",width=100)
        self.coursetable.column("contact",width=100)
        self.coursetable.column("course",width=100)
        self.coursetable.column("state",width=100)
        self.coursetable.column("city",width=100)
        self.coursetable.column("address",width=200)
        
        self.coursetable.pack(fill=BOTH,expand=1)
        self.coursetable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
      

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gend.set("Select")
        self.var_dob.set("")
        self.var_cont.set("")
        self.var_c.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        
    
        self.txt_address.delete("1.0",END)
       
        self.txt_roll.config(state=NORMAL)
        self.var_s.set("")

    def delete(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try: 
             if self.var_roll.get()=="":
                messagebox.showerror("error","please select rollno from the list",parent=self.root)
             else:
                  cur.execute("select* from student where rollno=?",(self.var_roll.get(),))
                  row=cur.fetchone()
                  if row==None:
                     messagebox.showerror("error","Please select student from the list",parent=self.root)
                  else:
                      op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                      if op==True:
                          cur.execute("delete from student where rollno=?",(self.var_roll.get(),))
                          con.commit()
                          messagebox.showinfo("Successfully Deleted","Successfully Deleted",parent=self.root)
                          self.clear()

                    



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

              

        
        



    
    
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.coursetable.focus()
        content=self.coursetable.item(r)
        row=content["values"]
       # print(row)
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gend.set(row[3])
        self.var_dob.set(row[4])
        self.var_cont.set(row[5])
        self.var_c.set(row[6])
        self.var_state.set(row[7])
        self.var_city.set(row[8])
        
    
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[9])

    def add(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
             if self.var_roll.get()=="":
                messagebox.showerror("error","Roll No is required",parent=self.root)
             else:
                cur.execute("select* from student where rollno=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("error","Roll No already exists",parent=self.root)
                else:
                    cur.execute("Insert into student(rollno,name,email,gender,dob,contact,course,state,city,address) values(?,?,?,?,?,?,?,?,?,?)",
                                (self.var_roll.get(),
                                self.var_name.get(),self.var_email.get(),self.var_gend.get(), self.var_dob.get(),
                                self.var_cont.get(),self.var_c.get(),self.var_state.get(),self.var_city.get(),
                                self.txt_address.get("1.0",END)))
                               
                    con.commit()
                    messagebox.showinfo("Success","Student added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")



    def update(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
             if self.var_roll.get()=="":
                messagebox.showerror("error","Roll No is required",parent=self.root)
             else:
                cur.execute("select* from student where rollno=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("error","Select roll no from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,course=?,state=?,city=?,address=? where rollno=?",
                               ( 
                                self.var_name.get(),self.var_email.get(),self.var_gend.get(), self.var_dob.get(),
                                self.var_cont.get(),self.var_c.get(),self.var_state.get(),self.var_city.get(),
                                self.txt_address.get("1.0",END),self.var_roll.get(),))
                    con.commit()
                    messagebox.showinfo("Success"," Updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
      
      
    def show(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
            
                cur.execute("select* from student ")
                rows=cur.fetchall()
                self.coursetable.delete(*self.coursetable.get_children())
                for row in rows:
                    self.coursetable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    def fetch_c(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
            
                cur.execute("select name  from course ")
                rows=cur.fetchall()
                
                if len(rows)>0:
                    for row in rows:
                       self.course_list.append(row[0])

               # print(v)
               
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")



  
    def search(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
              cur.execute("select * from student where rollno=?", (self.var_s.get(),))
              row=cur.fetchone()
              if row!=None:
                 self.coursetable.delete(*self.coursetable.get_children())
                 self.coursetable.insert('',END,values=row)
                  
              else:
               messagebox.showerror("Error","No record found", parent=self.root)
             
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to{str(ex)}")



    

    
             
                 

                    

       


if __name__=="__main__":
    root=Tk()
    obj= studentc(root)
    root.mainloop()
