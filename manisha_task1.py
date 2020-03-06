import tkinter
from tkinter import ttk
from tkinter import messagebox
win=tkinter.Tk()
win.title("messagebox")
win.configure(background='skyblue')
labelframe=tkinter.LabelFrame(win, text='Enter Your Details')
labelframe.grid(row=0,column=0,padx=100,pady=70)
name_lables1=ttk.Label(labelframe,text='what is your name?',font=('Helvetico',14,'bold'))
age_labels2=ttk.Label(labelframe,text='what is your age?',font=('Helvetico',14,'bold'))
email_lables3=ttk.Label(labelframe,text='what is your email?',font=('Helvetico',14,'bold'))
address_lables4=ttk.Label(labelframe,text='what is your address?',font=('Helvetico',14,'bold'))

#var
name_var=tkinter.StringVar()
age_var=tkinter.StringVar()
email_var=tkinter.StringVar()
address_var=tkinter.StringVar()

#Entrybox
name_entrybox=ttk.Entry(labelframe,width=50,textvariable=name_var)
age_entrybox=ttk.Entry(labelframe,width=50,textvariable=age_var)
email_entrybox=ttk.Entry(labelframe,width=50,textvariable=age_var)
address_entrybox=ttk.Entry(labelframe,width=50,textvariable=age_var)


#grid
name_lables1.grid(row=0,column=0,padx=5,pady=5,sticky=tkinter.W)
age_labels2.grid(row=0,column=1,padx=5,pady=5,sticky=tkinter.W)
email_lables3.grid(row=0,column=2,padx=5,pady=5,sticky=tkinter.W)
address_lables4.grid(row=0,column=3,padx=5,pady=5,sticky=tkinter.W)


name_entrybox.grid(row=1,column=0,padx=5,pady=5,sticky=tkinter.W)
age_entrybox.grid(row=1,column=1,padx=5,pady=5,sticky=tkinter.W)
email_entrybox.grid(row=1,column=2,padx=5,pady=5,sticky=tkinter.W)
address_entrybox.grid(row=1,column=3,padx=5,pady=5,sticky=tkinter.W)



def submit():
    name=name_var.get()
    email=email_var.get()
    address=address_var.get()
    age=age_var.get()
    if email=='':
        messagebox.showerror('ERROR','PLEASE ENTRY BOTH DETAILS')
    else:
        try:
            age=int(email)
        except ValueError:
            messagebox.showerror('Error','Please Enter the @ ')
        else:
            if age<18:
                messagebox.showerror('Warning','You are not above 18,Please visit this content own risk ')
                print(f"{name}:{age}:{email}:{address}")



button=ttk.Button(win,text='SUBMIT',command=submit)
button.grid(row=1,columnspan=2)



win.mainloop()