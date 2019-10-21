#import modules
 
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("650x480")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below",fg="steel blue",font=( 'Bradley Hand ITC' ,20, 'bold' )).place(x=200,y=0)
    username_lable = Label(register_screen, text="Username",font=( 'Bradley Hand ITC' ,17, 'bold' ),)
    username_lable.place(x=300,y=50)
    username_entry = Entry(register_screen, font=( 20 ),bd=2,textvariable=username)
    username_entry.place(x=300,y=100)
    password_lable = Label(register_screen, text="Password",font=( 'Bradley Hand ITC' ,17, 'bold' ))
    password_lable.place(x=300,y=150)
    password_entry = Entry(register_screen,font=( 20),bd=2, textvariable=password, show='*')
    password_entry.place(x=300,y=200)
    Label(register_screen, text="").place(x=300,y=250)
    Button(register_screen, text="Register", width=10, height=1, bg='brown',fg='white', command = register_user).place(x=300,y=300)
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("650x480")
    Label(login_screen, text="Please enter details below to login",font=( 'Bradley Hand ITC' ,17, 'bold' )).place(x=130,y=0)
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen,font=( 'Bradley Hand ITC' ,17,'bold' ), text="Username").place(x=250,y=50)
    username_login_entry = Entry(login_screen,font=(17) ,textvariable=username_verify)
    username_login_entry.place(x=250,y=100)
    Label(login_screen,font=( 'Bradley Hand ITC' ,17, 'bold' ), text="Password").place(x=250,y=150)
    password_login_entry = Entry(login_screen,font=(17 ), textvariable=password_verify, show= '*')
    password_login_entry.place(x=250,y=200)
    Button(login_screen, text="Login", width=10, height=1,bg='brown',fg='white', command = login_verify).place(x=275,y=250)
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    messagebox.showinfo("Registration","Registration Success")
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
#=========================================================================================================================================================
def login_sucess():     
    messagebox.showinfo("Login","Login Sucess") 
    def datasave():
        conn = sqlite3.connect('lpggas.db')
        c= conn.cursor()
        m='Male'
        f='Female'
        mn='Subsidised'
        yr='Normal'
        nm=name.get()
        ph=phone.get()
        st=state.get()
        ad=address.get()
        if var.get()==1 and var1.get()==1 :
            c.execute('INSERT INTO lpggas (name,phone,gender,program,state,address) VALUES(?,?,?,?,?,?)' ,(nm,ph,m,mn,st,ad))
            conn.commit()
        if var.get()==2 and var1.get()==1 :
            c.execute('INSERT INTO lpggas (name,phone,gender,program,state,address) VALUES(?,?,?,?,?,?)', (nm,ph,f,mn,st,ad))
            conn.commit()
        if var.get()==1 and var2.get()==2 :
            c.execute('INSERT INTO lpggas (name,phone,gender,program,state,address) VALUES (?,?,?,?,?,?)',(nm,ph,m,yr,st,ad))
            conn.commit()
        if var.get()==2 and var2.get()==2 :
            c.execute('INSERT INTO lpggas (name,phone,gender,program,state,address) VALUES (?,?,?,?,?,?)', (nm,ph,f,yr,st,ad))
            conn.commit()
        messagebox.showinfo("Succesful","Data Submitted Succesfully Your lpg cylinder will deliver soon")
        delete_login_success()
        
    
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("850x600")
    login_success_screen.title("Registration Form")

    label_0 = Label(login_success_screen, text="Registration form",width=30,font=("bold", 20),fg='steel blue')
    label_0.place(x=250,y=53)

    name = StringVar()
    phone = IntVar()
    label_1 = Label(login_success_screen, text="FullName",width=20,font=("bold", 10))
    label_1.place(x=250,y=130)

    entry_1 = Entry(login_success_screen,textvariable=name)
    entry_1.place(x=440,y=130)

    label_2 = Label(login_success_screen, text="Phone no",width=20,font=("bold", 10))
    label_2.place(x=250,y=180)

    entry_2 = Entry(login_success_screen,textvariable=phone)
    entry_2.place(x=440,y=180)

    label_3 = Label(login_success_screen, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=250,y=230)
    var = IntVar()
    Radiobutton(login_success_screen, text="Male",padx = 5, variable=var, value=1).place(x=445,y=230)
    Radiobutton(login_success_screen, text="Female",padx = 20, variable=var, value=2).place(x=500,y=230)

    label_4 = Label(login_success_screen, text="State",width=20,font=("bold", 10))
    label_4.place(x=250,y=280)
    list1 = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"];
    state=StringVar()
    droplist=OptionMenu(login_success_screen,state, *list1)
    droplist.config(width=30)
    state.set('State') 
    droplist.place(x=440,y=280)

    label_4 = Label(login_success_screen, text="Program",width=20,font=("bold", 10))
    label_4.place(x=240,y=330)
    var1 = IntVar()
    Checkbutton(login_success_screen, text="Subsidised", variable=var1).place(x=400,y=330)
    var2 = IntVar()
    Checkbutton(login_success_screen, text="Normal", variable=var2).place(x=500,y=330)

    label_5 = Label(login_success_screen, text="Address",width=20,font=("bold", 10))
    label_5.place(x=250,y=380)
    address=StringVar()
    entry_5 = Entry(login_success_screen,textvariable=address,width=40)
    entry_5.place(x=440,y=380)

    Button(login_success_screen, text='Submit',width=20,bg='brown',fg='white',command=datasave).place(x=400,y=480)

    login_success_screen.mainloop()
    
#==========================================================================================================================================================

# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("100x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("100x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()



def delete_login_success():
    login_success_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1300x800")
    main_screen.title("Account Login")
    lblinfo = Label(font=( 'aria' ,30, 'bold' ),text="LPG GAS SYSTEM",fg="steel blue",bd=10).pack()
    i=ImageTk.PhotoImage(Image.open("1.jpg"))
    Label(image=i,height=700,width=1600).pack()
    #lblinfo.place(x=400,y=10)
    b=Button(text="Login", height="2", width="30", command = login)
    b.place(x=550,y=200)
    c=Button(text="Register", height="2", width="30", command=register)
    c.place(x=550,y=250)
    main_screen.mainloop()
 
 
main_account_screen()
