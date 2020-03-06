from tkinter import*
from tkinter import ttk
import sqlite3
win=Tk()
class Student:
    def __init__(self,win):
        self.win=win
        self.win.title('student Management System(@SaGa Technology')
        self.win.geometry("1350x700+0+0")
        title=Label(self.win,text='Student Management System',bd=10,relief=GROOVE,font=('Times new roman',40,'bold'),bg='skyblue',fg='black')
        title.pack(side=TOP,fill=X)
        self.Rollno_var=StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.contact_var = StringVar()
        self.email_var = StringVar()
       # address_var=StringVar()
        self.gender_var = StringVar()
        self.dob_var = StringVar()

#manage Frame
        manage_frame=Frame(self.win,bd=5,relief=RIDGE,bg='skyblue')
        manage_frame.place(x=20,y=100,width=450,height=600)

#show Frame

#Manage Title
        manage_title=Label(manage_frame,text='Manage Student',bg='skyblue',font=('Times new roman',20,'bold'),fg='black')
        manage_title.grid(row=0,columnspan=2,pady=10)
#manage_label1
    #rollno
        manage_labelRollno=Label(manage_frame,text='Roll No:',bg='skyblue',font=('Times new roman',14,'bold'),fg='black')
        manage_labelRollno.grid(row=1,column=0,pady=15,padx=10,sticky='W')
    # firstname
        manage_labelname=Label(manage_frame,text='First Name:',bg='skyblue',font=('Times new roman',14,'bold'),fg='black')
        manage_labelname.grid(row=1,column=0,pady=15,padx=10,sticky='W')
    #lastname
        manage_labellastname=Label(manage_frame, text='Last Name:', bg='skyblue', font=('Times new roman', 14, 'bold'),
                             fg='black')
        manage_labellastname.grid(row=2, column=0, pady=15, padx=10, sticky='W')

    #datetofbirth
        manage_labeldob = Label(manage_frame, text='Date Of Birth:', bg='skyblue', font=('Times new roman', 14, 'bold'),
                                 fg='black')
        manage_labeldob.grid(row=3, column=0, pady=15, padx=10, sticky='W')
    #gender
        manage_labelgender = Label(manage_frame, text='Gender:', bg='skyblue', font=('Times new roman', 14, 'bold'),
                                    fg='black')
        manage_labelgender.grid(row=4, column=0, pady=15, padx=10, sticky='w')

    #contactnum
        manage_labelcontact = Label(manage_frame, text='Contact No:', bg='skyblue', font=('Times new roman', 14, 'bold'),
                                 fg='black')
        manage_labelcontact.grid(row=5, column=0, pady=15, padx=10, sticky='W')
    #email
        manage_labelemail = Label(manage_frame, text='Email:', bg='skyblue', font=('Times new roman', 14, 'bold'),
                                 fg='black')
        manage_labelemail.grid(row=6, column=0, pady=15, padx=10, sticky='W')
    #address
        manage_labeladdress = Label(manage_frame, text='Address:', bg='skyblue', font=('Times new roman', 14, 'bold'),
                                     fg='black')
        manage_labeladdress.grid(row=7, column=0, pady=15, padx=10, sticky='W')
    #manageEntrybox
        manage_entryRollno = Entry(manage_frame, textvariable=self.Rollno_var,
                                      font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entryRollno.grid(row=1, column=2, pady=15, padx=10, sticky='w')

        manage_entryfirstname=Entry(manage_frame,textvariable=self.firstname_var,font=('Times new roman', 14, 'bold'),bd=5,relief=RIDGE)
        manage_entryfirstname.grid(row=1, column=2, pady=15, padx=10, sticky='w')

        manage_entrylastname = Entry(manage_frame,textvariable=self.lastname_var, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entrylastname.grid(row=2, column=2, pady=15, padx=10, sticky='w')

        manage_entrydob = Entry(manage_frame,textvariable=self.dob_var, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entrydob.grid(row=3, column=2, pady=15, padx=10, sticky='w')

        manage_comboboxgender=ttk.Combobox(manage_frame,textvariable=self.gender_var,width=16,font=('Times new roamn',14,'bold'),state='readonly')
        manage_comboboxgender['values']=['Male','female','Others']
        manage_comboboxgender.grid(row=4,column=2,padx=20,pady=10,sticky='W')

        manage_entrycontact = Entry(manage_frame,textvariable=self.contact_var, font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entrycontact.grid(row=5, column=2, pady=15, padx=10, sticky='w')

        manage_entryEmail = Entry(manage_frame, textvariable=self.email_var,font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        manage_entryEmail.grid(row=6, column=2, pady=15, padx=10, sticky='w')

        self.manage_entryaddress= Text(manage_frame,width=20,height=2.5,font=('Times new roman', 14, 'bold'), bd=5, relief=RIDGE)
        self.manage_entryaddress.grid(row=7, column=2, pady=11, padx=5, sticky='w')


#buttonFrame
        ButtonFrame=Frame(manage_frame,bd=4,bg='skyblue',relief=RIDGE)
        ButtonFrame.place(x=5,y=500,width=430)


        addbutton=Button(ButtonFrame,command=self.add_student,text='Add',width=12)
        addbutton.grid(row=0,column=0,padx=4,pady=3)

        deletebutton = Button(ButtonFrame, text='DELETE', width=12)
        deletebutton.grid(row=0, column=1, padx=4, pady=3)

        updatebutton = Button(ButtonFrame,command=self.update_data, text='UPDATE', width=12)
        updatebutton.grid(row=0, column=2, padx=4, pady=3)

        clearbutton = Button(ButtonFrame,command=self.clear_data, text='Clear', width=12)
        clearbutton.grid(row=0, column=3, padx=4, pady=3)

    #showframe
        show_frame=Frame(self.win,bd=5,relief=RIDGE,bg='skyblue')
        show_frame.place(x=480,y=100,width=850,height=550)
        show_labelsearch=Label(show_frame,text='Search By:',bg='skyblue',font=('Times new roman',14,'bold'),fg='black')
        show_labelsearch.grid(row=0,column=0,padx=20,pady=10,sticky='W')

        show_comboboxsearch = ttk.Combobox(show_frame, width=16, font=('Times new roamn', 14, 'bold'),
                                             state='readonly')
        show_comboboxsearch['values'] = ['name', 'email', 'lastname']
        show_comboboxsearch.grid(row=0, column=1, padx=20, pady=10, sticky='W')

        show_entrysearch=Entry(show_frame,font=('Times new roman',14,'bold'),bd=5,relief=RIDGE)
        show_entrysearch.grid(row=0,column=2,padx=20,pady=10,sticky='W')

        searchbutton=Button(show_frame,text='SEARCH',width=12)
        searchbutton.grid(row=0,column=3,padx=4,pady=3,sticky='W')

        showallbutton=Button(show_frame,text='SHOW ALL',width=12)
        showallbutton.grid(row=0,column=4,padx=4,pady=3,sticky='W')

        showtable_Frame=Frame(show_frame,bg='skyblue',relief=RIDGE,bd=5)
        showtable_Frame.place(x=10,y=70,height=450,width=700)

        scroll_x=Scrollbar(showtable_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(showtable_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(showtable_Frame,columns=('Rollno','name','lastname','dob','contact','gender','email','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('Rollno',text='Roll No')
        self.student_table.heading('name',text='NAME')
        self.student_table.heading('lastname',text='LASTNAME')
        self.student_table.heading('dob',text='DOB')
        self.student_table.heading('contact',text='CONTACT')
        self.student_table.heading('email',text='EMAIL')
        self.student_table.heading('gender',text='GENDER')
        self.student_table.heading('address',text='ADDRESS')
        self.student_table['show']='headings'
        self.student_table.pack()
        self.student_table.column('Rollno',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('lastname',width=100)
        self.student_table.column('contact',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('address',width=100)
        self.student_table.pack(fill='both',expand=1)
        self.student_table.bind('<ButtonRelease-1>',self.get_cursor)

        self.fetch_data()


    # con= sqlite3.connect('student.db')
    # cur=con.cursor()
    # cur.execute('CREATE TABLE student(firstname text,lastanme text,contact text,email text,address text,dob text,gender text)')
    # con.commit()
    # con.close()



    def add_student(self):
       con=sqlite3.connect('student.db')
       cur=con.cursor()
       cur.execute("INSERT INTO student values(?,?,?,?,?,?,?)",( self.Rollno_var.get(),
                                                                 self.firstname_var.get(),
                                                                 self.lastname_var.get(),
                                                                 self.gender_var.get(),
                                                                 self.email_var.get(),
                                                                 self.contact_var.get(),
                                                                 self.dob_var.get(),
                                                                 self.manage_entryaddress.get(1.0,END)))
       con.commit()
       self.fetch_data()
       self.clear_data()
       con.close()
    def fetch_data(self):
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        cur.execute('select * from student')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
            con.close()
    def clear_data(self):
        self.Rollno_var.set('')
        self.firstname_var.set('')
        self.lastname_var.set('')
        self.dob_var.set('')
        self.contact_var.set('')
        self.manage_entryaddress.delete(1.0,END)
        self.email_var.set('')
        self.gender_var.set('')

    def get_cursor(self,event):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.Rollno_var.set(row[0])
        self.firstname_var.set(row[1])
        self.lastname_var.set(row[2])
        self.dob_var.set(row[3])
        self.contact_var.set(row[4])
        self.email_var.set(row[5])
        self.manage_entryaddress.delete(1.0,END)
        self.manage_entryaddress.insert(END,row[6])
        self.gender_var.set(row[7])

    def update_data(self):
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        cur.execute('update student set Rollno=?,firstname=?,lastanme=?,contact=?,dob=?,email=?,address=?,gender=?',(
                                                                                                             self.Rollno_var.get(),
                                                                                                             self.firstname_var.get(),
                                                                                                             self.lastname_var.get(),
                                                                                                             self.dob_var.get(),
                                                                                                             self.contact_var.get(),
                                                                                                             self.email_var.get(),
                                                                                                             self.gender_var.get(),
                                                                                                             self.manage_entryaddress.get(1.0,END)))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()



ob=Student(win)
win.mainloop()