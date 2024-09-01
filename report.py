
from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image,ImageTk #pip istall pillow
class reportc:
    def __init__(self,root) :
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1270x480+80+170")
        self.root.config(bg="#E0EEEE")
        self.root.focus_force()

        
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_fullm=StringVar()
        self.var_roll=StringVar()

        
        
        self.var_search=StringVar()
        self.var_id=StringVar()

        title=Label(self.root,text=" View Student Result ",font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=10,y=15,width=1200,height=50)

        lbl_select=Label(self.root,text="Select Roll No",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black").place(x=280,y=100)

        txt_select=Entry(self.root,textvariable=self.var_search,font=("segoe ui semibold",16),bg="lightyellow",fg="black",bd=2.5).place(x=450,y=100,width=200)

        btn_search=Button(self.root,text="Search",font=("segoe ui semibold",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.search).place(x=660,y=100,width=100,height=28)
 
        btn_clear=Button(self.root,text="Clear",font=("segoe ui semibold",15,"bold"),bg="orange",fg="black",activebackground="white",cursor="hand2",command=self.clear).place(x=780,y=100,width=100,height=28)

#===============LABELS==========================================================================================
        lbl_roll=Label(self.root,text="Roll No",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black",bd=2.5,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black",bd=2.5,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black",bd=2.5,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black",bd=2.5,relief=GROOVE).place(x=600,y=230,width=170,height=50)
        lbl_fullm=Label(self.root,text="Full Marks",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black",bd=2.5,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("segoe ui semibold",16,"bold"),bg="#698B69",fg="black",bd=2.5,relief=GROOVE).place(x=900,y=230,width=150,height=50)
        
       
       
       
       
       
        self.roll=Label(self.root,font=("segoe ui semibold",16,"bold"),bg="lightgray",fg="black",bd=2.5,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("segoe ui semibold",16,"bold"),bg="lightgray",fg="black",bd=2.5,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("segoe ui semibold",16,"bold"),bg="lightgray",fg="black",bd=2.5,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks=Label(self.root,font=("segoe ui semibold",16,"bold"),bg="lightgray",fg="black",bd=2.5,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.fullm=Label(self.root,font=("segoe ui semibold",16,"bold"),bg="lightgray",fg="black",bd=2.5,relief=GROOVE)
        self.fullm.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("segoe ui semibold",16,"bold"),bg="lightgray",fg="black",bd=2.5,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        

        btn_del=Button(self.root,text="Delete",font=("segoe ui semibold",15,"bold"),bg="red",fg="black",activebackground="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=100,height=28)





    
    def search(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
              if self.var_search.get()=="":
                  messagebox.showerror("Error", "Roll No Is Required")

              else:
                  cur.execute("select * from result where roll=?", (self.var_search.get(),))
                  row=cur.fetchone()
                  if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.fullm.config(text=row[5])
                    self.per.config(text=row[6])
                 #self.coursetable.delete(*self.coursetable.get_children())
                 #self.coursetable.insert('',END,values=row)
                  
                  else:
                   messagebox.showerror("Error","No record found", parent=self.root)
             
            
             
        except Exception as ex:
          messagebox.showerror("Error",f"Error due to{str(ex)}")

    def  clear(self):
         self.var_id=""
         self.roll.config(text="")
         self.name.config(text="")
         self.course.config(text="")
         self.marks.config(text="")
         self.fullm.config(text="")
         self.per.config(text="")
         self.var_search.set("")



     
    def delete(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try: 
             if self.var_id=="":
                messagebox.showerror("Error","Search Student Result First",parent=self.root)
             else:
                  cur.execute("select * from result where rid=?",(self.var_id,))
                  row=cur.fetchone()
                  if row==None:
                     messagebox.showerror("error","Invalid Student Result",parent=self.root)
                  else:
                      op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                      if op==True:
                          cur.execute("delete from result where rid=?",(self.var_id,))
                          con.commit()
                          messagebox.showinfo("Successfully Deleted","Successfully Deleted",parent=self.root)
                          self.clear()
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=reportc(root)
    root.mainloop()
