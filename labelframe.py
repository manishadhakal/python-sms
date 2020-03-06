import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title("labelframe and padding")
win.configure(background='skyblue')
labelframe=tkinter.LabelFrame(win, text='Enter Your Details')
labelframe.grid(row=0,column=0,padx=500,pady=70)
labels=['what is your name ?',
        'What is your age ?',
        'What is your gender ?',
        'what is your address ?',
        'country',
        'city']
for i in range(len(labels)):
    cur_label= 'label'+ str(i)
    cur_label=ttk.Label(labelframe, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tkinter.W,padx=10,pady=10)

# entry box
name_var=tkinter.StringVar()
user_info={
        'name':tkinter.StringVar(),
       'age':tkinter.StringVar(),
        'gender':tkinter.StringVar(),
       'address':tkinter.StringVar(),
       'country':tkinter.StringVar(),
       'city':tkinter.StringVar()
    }
counter=0

for i in user_info:
    cur_entrybox= 'entry'+ i
    cur_entrybox=ttk.Entry(labelframe, width=20 ,textvariable=user_info[i])
    cur_entrybox.grid(row=counter, column=1,padx=10,pady=10)
    counter+=1
def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('address').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('city').get())


submit_btn=ttk.Button(win,text='Submit' ,command=submit)
submit_btn.grid(row=1, columnspan=2)

win.mainloop()
