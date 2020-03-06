from tkinter import *
def buttonClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def buttonClearDisplay():
    global operator
    operator=""
    text_input.set=("")
def buttonEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator = ""

win=Tk()
win.title("calculator")
operator=""
text_input=StringVar()
#entry box
textDisplay=Entry(win,font=('arial','20','bold'),textvariable=text_input,bd=40,width=15,
                  bg="powder blue",justify='right')
button9=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="9",bg="powder blue",command=lambda:buttonClick(9))
button8=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="8",bg="powder blue",command=lambda:buttonClick(8))
button7=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="7",bg="powder blue",command=lambda:buttonClick(7))
Addition=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="+",bg="powder blue",command=lambda:buttonClick("+"))

#entrybox2
button6=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="6",bg="powder blue",command=lambda:buttonClick(6))
button5=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="5",bg="powder blue",command=lambda:buttonClick(5))
button4=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="4",bg="powder blue",command=lambda:buttonClick(4))
substraction=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="-",bg="powder blue",command=lambda:buttonClick("-"))
#entrybox3
button3=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="3",bg="powder blue",command=lambda:buttonClick(3))
button2=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="2",bg="powder blue",command=lambda:buttonClick(2))
button1=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="1",bg="powder blue",command=lambda:buttonClick(1))
multiply=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="*",bg="powder blue",command=lambda:buttonClick("*"))

#entrybox4
button0=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="0",bg="powder blue",command=lambda:buttonClick(0))
buttonclear=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="c",bg="powder blue",command=buttonClearDisplay)
buttonEquals=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="=",bg="powder blue",command=buttonEqualsInput)
division=Button(win,padx=16,pady=16,bd=8,fg="black",font=('arial','20','bold'),
            text="/",bg="powder blue",command=lambda:buttonClick("/"))
#grid
textDisplay.grid(columnspan=4)
button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)
Addition.grid(row=1,column=3)

button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)
substraction.grid(row=2,column=3)

button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)
multiply.grid(row=3,column=3)

button0.grid(row=4,column=0)
buttonclear.grid(row=4,column=1)
buttonEquals.grid(row=4,column=2)
division.grid(row=4,column=3)
win.mainloop()

