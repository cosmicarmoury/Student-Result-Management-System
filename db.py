

from tkinter import*
from PIL import Image,ImageTk #pip istall pillow
from course import coursec
from student import studentc
from result import resultc
from report import reportc
from tkinter import messagebox
import  os


class projectDB:
    def __init__(self,root) :
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#E0EEEE")
        self.logo_dash=ImageTk.PhotoImage(file="picsforp/logo.png")


        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("segoe ui semibold",20,"bold"),bg="#698B69",fg="black").place(x=0,y=0,relwidth=1,height=50)
        mframe=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="#EED5B7")
        mframe.place(x=10,y=70,width=1340,height=80)
        btn1=Button(mframe,text="COURSE",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn2=Button(mframe,text="STUDENT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_stu).place(x=240,y=5,width=200,height=40)
        btn3=Button(mframe,text="RESULT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_res).place(x=460,y=5,width=200,height=40)
        btn4=Button(mframe,text="VIEW RESULT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn5=Button(mframe,text="LOGOUT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn6=Button(mframe,text="EXIT",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",cursor="hand2",command=self.exit).place(x=1120,y=5,width=200,height=40)
        
        self.bg_img=ImageTk.PhotoImage(file="picsforp/t1.jpg")
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=150,y=210,width=1000,height=480)

        self.lbl_course=Label(self.root, text="Total Courses\n [0]",font=("segoe ui semibold",20),bd=10,relief=RIDGE,bg="#698B69",fg="black").place(x=200,y=530,width=300,height=100)
       

        self.lbl_stu=Label(self.root, text="Total Students\n [0]",font=("segoe ui semibold",20),bd=10,relief=RIDGE,bg="#698B69",fg="black").place(x=510,y=530,width=300,height=100)
       

        self.lbl_result=Label(self.root, text="Total Results\n [0]",font=("segoe ui semibold",20),bd=10,relief=RIDGE,bg="#698B69",fg="black").place(x=820,y=530,width=300,height=100)
       

        footer=Label(self.root,text="SRMS-Student Result Management System\n Contact Us For Any Technical Issue: 98xxxxxx07",font=("segoe ui semibold",15,),bg="#698B69",fg="black").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=coursec(self.new_win) 

    
    def add_report(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=reportc(self.new_win) 


    def add_stu(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=studentc(self.new_win) 

    def add_res(self):
        self.new_win=Toplevel(self.root)   
        self.new_obj=resultc(self.new_win) 
    
    def logout(self):
        op=messagebox.askyesno("Confirm","Do You Really Want To Logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op=messagebox.askyesno("Confirm","Do You Really Want To Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            









if __name__=="__main__":
    root=Tk()
    obj=projectDB(root)
    root.mainloop()
