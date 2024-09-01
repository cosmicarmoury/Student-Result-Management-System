from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image,ImageTk #pip istall pillow
class coursec:
    def __init__(self,root) :
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x480+80+170")
        self.root.config(bg="#E0EEEE")
        self.root.focus_force()

        title=Label(self.root,text="Manage Course Details",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=15,width=1200,height=35)

        self.var_c=StringVar()
        self.var_d=StringVar()
        self.var_ch=StringVar()
        self.var_id=StringVar()
    

        


   
        lbl_coursename=Label(self.root,text="Course Name",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=60)
        lbl_duaration=Label(self.root,text="Duration",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=110)
        lbl_changes=Label(self.root,text="Charges",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=160)
        lbl_des=Label(self.root,text="Description",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=210)

        self.txt_coursename=Entry(self.root,textvariable=self.var_c,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black")
        self.txt_coursename.place(x=185,y=60,width=200)
        txt_duaration=Entry(self.root,textvariable=self.var_d,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=185,y=110,width=200)
        txt_changes=Entry(self.root,textvariable=self.var_ch,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=185,y=160,width=200)
        self.txt_des=Text(self.root,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black")
        self.txt_des.place(x=185,y=210,width=500,height=100)

        self.btn_add=Button(self.root,text="Save",font=("segoe ui semibold",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("segoe ui semibold",15,"bold"),bg="#4caf50",fg="black",cursor="hand2", command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("segoe ui semibold",15,"bold"),bg="#f44336",fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("segoe ui semibold",15,"bold"),bg="#607d8b",fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        self.var_s=StringVar()
        lbl_search_coursename=Label(self.root,text="Course Name",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=720,y=60)
        txt_search_coursename=Entry(self.root,textvariable=self.var_s,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=895,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.search).place(x=1078,y=60,width=120,height=28)


        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=110,width=470,height=340)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)



        self.coursetable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.coursetable.xview)
        scrolly.config(command=self.coursetable.yview)
        self.coursetable.heading("cid",text="Course ID")
        self.coursetable.heading("name",text="Name")
        self.coursetable.heading("duration",text="Duration")
        self.coursetable.heading("charges",text="Charges")
        self.coursetable.heading("description",text="Description")
        self.coursetable["show"]='headings'
        self.coursetable.column("cid",width=50)
        self.coursetable.column("name",width=50)
        self.coursetable.column("duration",width=100)
        self.coursetable.column("charges",width=50)
        self.coursetable.column("description",width=100)
        self.coursetable.pack(fill=BOTH,expand=1)
        self.coursetable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def clear(self):
        self.show()
        self.var_c.set("")
        self.var_d.set("")
        self.var_ch.set("")
        self.var_s.set("")
        self.txt_des.delete('1.0',END)
        self.txt_coursename.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try: 
             if self.var_c.get()=="":
                messagebox.showerror("error","please select course from the list",parent=self.root)
             else:
                  cur.execute("select* from course where name=?",(self.var_c.get(),))
                  row=cur.fetchone()
                  if row==None:
                     messagebox.showerror("error","Course name already exists",parent=self.root)
                  else:
                      op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                      if op==True:
                          cur.execute("delete from course where name=?",(self.var_c.get(),))
                          con.commit()
                          messagebox.showinfo("Successfully Deleted","Successfully Deleted",parent=self.root)
                          self.clear()

                    



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

              

        
        



    
    
    def get_data(self,ev):
        self.txt_coursename.config(state='readonly')
        self.txt_coursename
        r=self.coursetable.focus()
        content=self.coursetable.item(r)
        row=content["values"]
       # print(row)
        self.var_c.set(row[1])
        self.var_d.set(row[2])
        self.var_ch.set(row[3])
        self.txt_des.delete('1.0',END)
        self.txt_des.insert(END,row[4])

    def add(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
             if self.var_c.get()=="":
                messagebox.showerror("error","Course name is required",parent=self.root)
             else:
                cur.execute("select* from course where name=?",(self.var_c.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("error","Course name already exists",parent=self.root)
                else:
                    cur.execute("Insert into course(name,duration,charges,description) values(?,?,?,?)",(self.var_c.get(),
                                self.var_d.get(),self.var_ch.get(),
                                self.txt_des.get("1.0",END)))
                    con.commit()
                    messagebox.showinfo("Success","Course added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")



    def update(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
             if self.var_c.get()=="":
                messagebox.showerror("error","Course name is required",parent=self.root)
             else:
                cur.execute("select* from course where name=?",(self.var_c.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("error","Select course from list",parent=self.root)
                else:
                    cur.execute("update course set duration =?,charges=?,description=? where name=?",
                               (    self.var_d.get(),self.var_ch.get(),
                                self.txt_des.get("1.0",END),
                                self.var_c.get()))
                    con.commit()
                    messagebox.showinfo("Success","Course updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
      
      
    def show(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
            
                cur.execute("select* from course ")
                rows=cur.fetchall()
                self.coursetable.delete(*self.coursetable.get_children())
                for row in rows:
                    self.coursetable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
    


  
    def search(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
              cur.execute(f"select * from course where name LIKE '%{self.var_s.get()}%'")
              rows=cur.fetchall()
              self.coursetable.delete(*self.coursetable.get_children())
              for row in rows:
                    self.coursetable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")


    

    
             
                 

                    

       


if __name__=="__main__":
    root=Tk()
    obj=coursec(root)
    root.mainloop()
