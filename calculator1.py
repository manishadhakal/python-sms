from tkinter import *
from tkinter import ttk

def buttonclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def buttoncleardisplay():
    global operator
    operator=""
    text_input.set("")

def buttonequalsinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator = ""

win=Tk()
win.title("Calculator")
operator=""
text_input=StringVar()

txtdisplay=Entry(win,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)

button7=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:buttonclick(7))
button7.grid(row=1,column=0)
button8=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:buttonclick(8))
button8.grid(row=1,column=1)
button9=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:buttonclick(9))
button9.grid(row=1,column=2)
Addition=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:buttonclick("+"))
Addition.grid(row=1,column=3)

button4=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:buttonclick(4))
button4.grid(row=2,column=0)
button5=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:buttonclick(5))
button5.grid(row=2,column=1)
button6=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:buttonclick(6))
button6.grid(row=2,column=2)
Subtraction=Button(win,pady=16,padx=16,bd=8,fg="black",font=('arial',20,'bold',),text="-",bg="powder blue",command=lambda:buttonclick("-"))
Subtraction.grid(row=2,column=3)

button1=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:buttonclick(1))
button1.grid(row=3,column=0)
button2=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:buttonclick(2))
button2.grid(row=3,column=1)
button3=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:buttonclick(3))
button3.grid(row=3,column=2)
Multiplication=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:buttonclick("*"))
Multiplication.grid(row=3,column=3)

button0=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:buttonclick(0))
button0.grid(row=4,column=0)
buttonclear=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=buttoncleardisplay)
buttonclear.grid(row=4,column=1)
buttonnequals=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=buttonequalsinput).grid(row=4,column=2)
Division=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:buttonclick("/")).grid(row=4,column=3)

win.mainloop()