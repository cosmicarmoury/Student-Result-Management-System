from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image,ImageTk #pip install pillow
import sqlite3 
import os
class log:
    def __init__(self,root) :
        self.root=root
        self.root.title("Sign In Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#E0EEEE")
        self.bg=ImageTk.PhotoImage(file="newim/i2.jpg")
        self.bg2=ImageTk.PhotoImage(file="newim/YY.jpg")
        self.bg3=ImageTk.PhotoImage(file="newim/i4.jpg")
        
        user_input=StringVar()

        bg=Label(self.root,image=self.bg).place(x=150,y=0)
        bg2=Label(self.root,image=self.bg2).place(x=80,y=100,width=400,height=500)
        bg3=Label(self.root,image=self.bg3).place(x=130,y=310,height=40)
        frame1=LabelFrame(self.root,bg="#E0EEEE")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="SIGN IN HERE",font=("segoe ui semibold",30,"bold"),bg="#698B69",fg="black").place(x=50,y=30)

        lbl_em=Label(frame1,text="Email",font=("segoe ui semibold",18,"bold"),bg="#698B69",fg="black").place(x=50,y=150)
        lbl_pass=Label(frame1,text="Password",font=("segoe ui semibold",18,"bold"),bg="#698B69",fg="black").place(x=50,y=270)

        self.txt_em=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_em.place(x=50,y=200,width=350,height=35)
        self.txt_pass=Entry(frame1,font=("segoe ui semibold",16),bg="#9BCD9B",fg="black",bd=2.5)
        self.txt_pass.place(x=50,y=320,width=350,height=35)

        btn_reg=Button(frame1,text="Register New Account?",font=("segoe ui semibold",6,"bold"),bg="lightgray",fg="black",activebackground="white",cursor="hand2",command=self.register).place(x=50,y=450,width=200,height=25)
        btn_log=Button(frame1,text="Login",font=("segoe ui semibold",15,"bold"),bg="#698B69",fg="black",activebackground="white",cursor="hand2",command=self.login).place(x=50,y=380,width=200,height=40)
    


    def register(self):
        self.root.destroy()
        import regg

    def login(self):
        if self.txt_em.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","Both Fields Are Required",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="project.db")
                cur=con.cursor()
                cur.execute("select * from member where Email=? and Password==?",(self.txt_em.get(),self.txt_pass.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid Username Or Password",parent=self.root)
                    
                
                else:
                
                    messagebox.showinfo("Success","Sign In Successful",parent=self.root)
                    self.root.destroy()
                    os.system("python db.py")
                    
                    
                    self.clear()
                con.close()



            except Exception as ex:
                messagebox.showerror("Error",f"Error due to{str(ex)}")




root=Tk()
obj=log(root)
root.mainloop()
