
from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image,ImageTk #pip istall pillow
class resultc:
    def __init__(self,root) :
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1270x480+80+170")
        self.root.config(bg="#E0EEEE")
        self.root.focus_force()

        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_fmarks=StringVar()
        self.var_roll=StringVar()
      
        self.roll_list=[]
        self.fetch_rollno()
        


        title=Label(self.root,text="Add Student Result Details",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=15,width=1200,height=50)
        #widgets========================================
        lbl_select=Label(self.root,text="Select Student",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=50,y=220)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=50,y=280)
        lbl_fullm=Label(self.root,text="Full Marks",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=50,y=340)
        self.txt_st=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("segoe ui semibold",16,"bold"),state='readonly',justify=CENTER,)
        self.txt_st.place(x=280,y=100,width=200)
        self.txt_st.set("Select")
        btn_search=Button(self.root,text="Search",font=("segoe ui semibold",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.search).place(x=500,y=100,width=100,height=28)
       
       
        self.bg_img=ImageTk.PhotoImage(file="picsforp/res.jpg")
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=650,y=100,width=450,height=275)


        txt_name=Entry(self.root,textvariable=self.var_name,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black",state='readonly').place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black",state='readonly').place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=280,y=280,width=320)
        txt_fmarks=Entry(self.root,textvariable=self.var_fmarks,font=("segoe ui semibold",20,"bold"),bg="#9BCD9B",bd=2.5,fg="black").place(x=280,y=340,width=320)
 

        #==========button=========================================================
        btn_add=Button(self.root,text="Submit",font=("segoe ui semibold",15,"bold"),bg="lightyellow",activebackground="white",fg="black",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("segoe ui semibold",15,"bold"),bg="red",fg="black",activebackground="white",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)

        #=====fetch================================================================

    def fetch_rollno (self):
          con=sqlite3.connect(database="project.db")
          cur=con.cursor()
          try:
            
                cur.execute("select rollno from student")
                rows=cur.fetchall()
                
                if len(rows)>0:
                    for row in rows:
                       self.roll_list.append(row[0])

               # print(v)
               
          except Exception as ex:
                messagebox.showerror("Error",f"Error due to{str(ex)}")

    
    def search(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
              cur.execute("select name,course from student where rollno=?", (self.var_roll.get(),))
              row=cur.fetchone()
              if row!=None:
                 self.var_name.set(row[0])
                 self.var_course.set(row[1])
                 #self.coursetable.delete(*self.coursetable.get_children())
                 #self.coursetable.insert('',END,values=row)
                  
              else:
               messagebox.showerror("Error","No record found", parent=self.root)
             
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to{str(ex)}")

    def add(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
             if self.var_name.get()=="":
                messagebox.showerror("Error","Please First Search Student Record",parent=self.root)
             else:
                per=(int(self.var_marks.get())*100)/int(self.var_fmarks.get())
                cur.execute("select* from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","Result Already Present",parent=self.root)
                else:
                    cur.execute("Insert into result (roll,name,course,marks,fmarks,per) values(?,?,?,?,?,?)",
                                (self.var_roll.get(),
                                self.var_name.get(),self.var_course.get(),self.var_marks.get(), self.var_fmarks.get(),
                                str(per)
                                ))
                               
                    con.commit()
                    messagebox.showinfo("Success","Result added successfully",parent=self.root)
                  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")

    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),self.var_course.set(""),self.var_marks.set(""), self.var_fmarks.set("")




if __name__=="__main__":
    root=Tk()
    obj=resultc(root)
    root.mainloop()
