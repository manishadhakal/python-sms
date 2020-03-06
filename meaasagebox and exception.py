import tkinter
from tkinter import ttk
from tkinter import messagebox
win=tkinter.Tk()
win.title("messagebox exception")
labelframe=tkinter.LabelFrame(win, text='contact details')
labelframe.grid(row=0,column=0,padx=200,pady=50)
win.configure(background='skyblue')
#Label
name_lables1=ttk.Label(labelframe,text='what is your name?',font=('Helvetico',14,'bold'))
age_labels2=ttk.Label(labelframe,text='what is your age?',font=('Helvetico',14,'bold'))

#var
name_var=tkinter.StringVar()
age_var=tkinter.StringVar()

#Entrybox
name_entrybox=ttk.Entry(labelframe,width=50,textvariable=name_var)
age_entrybox=ttk.Entry(labelframe,width=50,textvariable=age_var)
#grid
name_lables1.grid(row=0,column=0,padx=5,pady=5,sticky=tkinter.W)
age_labels2.grid(row=0,column=1,padx=5,pady=5,sticky=tkinter.W)
name_entrybox.grid(row=1,column=0,padx=5,pady=5,sticky=tkinter.W)
age_entrybox.grid(row=1,column=1,padx=5,pady=5,sticky=tkinter.W)
def submit():
    name=name_var.get()
    age=age_var.get()
    if age=='' and name=='':
        messagebox.showerror('ERROR','PLEASE ENTRY BOTH DETAILS')
    else:
        try:
            age=int(age)
        except ValueError:
            messagebox.showerror('Error','Please Enter Interger Digit only')
        else:
            if age<18:
                messagebox.showerror('Warning','You are not above 18,Please visit this content own risk ')
                print(f"{name}:{age}")
button=ttk.Button(win,text='SUBMIT',command=submit)
button.grid(row=1,columnspan=2)


win.mainloop()
