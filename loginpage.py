from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter.ttk import Combobox

def reset_password():
    if mailentry.get()=='':
        messagebox.showerror('Error','Please enter email address to reset password')
    else:
        con = pymysql.connect(host='localhost',user='sai',password='****',database='register')
        cur = con.cursor()
        cur.execute('select * from student where email=%s',mailentry.get())
        row = cur.fetchone()
        if row==None:
            messagebox.showerror('Error','Please enter valid email address')
        else:
            con.close()
            def change_password():
                if securityquestionCombo.get()=='Select' or answerEntry.get()=='' or newpasswordEntry.get()=='':
                    messagebox.showerror('Error','All fields are required')
                else:
                    con = pymysql.connect(host='localhost',user='sai',password='****',database='register')
                    cur = con.cursor()
                    cur.execute('select * from student where email=%s and question=%s and answer=%s',
                                (mailentry.get(),securityquestionCombo.get(),answerEntry.get()))
                    row = cur.fetchone()
                    if row==None:
                        messagebox.showerror('Error','Security question or answer is incorrect',parent=root2)
                    else:
                        cur.execute('update student set password=%s where email=%s',
                                   (newpasswordEntry.get(),mailentry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success','Password changed successfully',parent=root2)
                        securityquestionCombo.current(0)
                        answerEntry.delete(0,END)
                        newpasswordEntry.delete(0,END)
                        root2.destroy()


            root2 = Toplevel()
            root2.title('Forgot password')
            root2.geometry('470x560+400+60')
            root2.config(bg='white')
            root2.focus_force()
            root2.grab_set()
            forgetLabel = Label(root2,text='Forget',font=('times new roman',22,'bold'),bg='white')
            forgetLabel.place(x=128,y=10)
            forgetpassLabel = Label(root2,text='Password',font=('times new roman',22,'bold'),bg='white',fg='green')
            forgetpassLabel.place(x=225,y=10)

            passwordimage = PhotoImage(file='pass.png')
            passimageLabel = Label(root2,image=passwordimage,bg='white')
            passimageLabel.place(x=170,y=70)

            securityquestionLabel = Label(root2,text='Security Question',font=('times new roman',19,'bold'),
                                          bg='white')
            securityquestionLabel.place(x=60,y=220)
            securityquestionCombo=Combobox(root2,font=('times new roman',19),state='readonly',width=28)
            securityquestionCombo['values'] = ('Select',
                                       'Your first pet name?',
                                       'Your birth place?',
                                       'Your best friend name?',
                                       'Your favourite teacher?',
                                       'Your favorite hobby?')
            securityquestionCombo.place(x=60,y=260)
            securityquestionCombo.current(0)

            answerLabel = Label(root2,text='Answer',font=('times new roman',19,'bold'),bg='white')
            answerLabel.place(x=60,y=310)
            answerEntry = Entry(root2,font=('times new roman',19),bg='white',width=30)
            answerEntry.place(x=60,y=350)

            newpasswordLabel = Label(root2,text='New Password',font=('times new roman',19,'bold'),bg='white')
            newpasswordLabel.place(x=60,y=400)
            newpasswordEntry = Entry(root2,font=('times new roman',19),bg='white',width=30)
            newpasswordEntry.place(x=60,y=440)

            changepassButton = Button(root2,text='Change Password',font=('arial',17,'bold'),bg='green',
                                      fg='white',cursor='hand2',activebackground='green',
                                      activeforeground='white',command=change_password)
            changepassButton.place(x=130,y=500)

            root2.mainloop()




def register_window():
    window.destroy()
    import register

def signin():
    if mailentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost',user='sai',password='****',database='register')
            cur = con.cursor()
            cur.execute('select * from student where email=%s and password=%s',(mailentry.get(),passwordentry.get()))
            row = cur.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Email / Password')
            else:
                messagebox.showinfo('Success','Welcome')
            con.close()

        except Exception as e:
            messagebox.showerror('Error',f'Error is due to {e}')




window = Tk()

window.geometry('900x600+50+50')
window.title('Login page')

bgloginimage = PhotoImage(file='loginbg.png')
bgloginLabel = Label(window,image=bgloginimage)
bgloginLabel.place(x=0,y=0)

frame = Frame(window,width=560,height=320,bg='white')
frame.place(x=180,y=140)

userimage = PhotoImage(file='user.png')
userimageLabel = Label(frame,image=userimage,bg='white')
userimageLabel.place(x=10,y=50)

mailLabel = Label(frame,text='Email',font=('arial',22,'bold'),bg='white')
mailLabel.place(x=220,y=32)
mailentry = Entry(frame,font=('arial',22),bg='white')
mailentry.place(x=220,y=70)

passwordLabel = Label(frame,text='Password',font=('arial',22,'bold'),bg='white')
passwordLabel.place(x=220,y=120)
passwordentry = Entry(frame,font=('arial',22),bg='white',show='*')
passwordentry.place(x=220,y=160)

regButton = Button(frame,text='Register new Account?',font=('arial',12),bd=0,bg='white',cursor='hand2',
                   activebackground='white',command=register_window)
regButton.place(x=220,y=200)

forgotButton = Button(frame,text='Forgot Password?',font=('arial',12),bd=0,bg='white',fg='red',cursor='hand2',
                      activebackground='white',activeforeground='red',command=reset_password)
forgotButton.place(x=410,y=200)

loginButton = Button(frame,text='Login',font=('arial',18,'bold'),fg='white',bg='gray20',cursor='hand2',
                     activebackground='gray20',activeforeground='white',command=signin)
loginButton.place(x=450,y=240)



window.mainloop()
