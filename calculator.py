# Create GUI application using tkinter to develop a calculator

from tkinter import *
root = Tk()
root.title('Calculator')
root.geometry('300x400+300+120')
root.resizable(FALSE, FALSE)
# Number --- Function
def number1():
    x='1'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number2():
    x='2'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number3():
    x='3'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number4():
    x='4'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number5():
    x='5'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number6():
    x='6'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number7():
    x='7'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number8():
    x='8'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number9():
    x='9'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
def number0():
    x='0'
    if(display.get() == '0'):
        display.delete(0, 'end')
        display.insert(0, x)
    else:
        length = len(display.get())
        display.insert(length, x)
# Operator -- function
def numberp():
    x='.'
    if(display.get()=='0'):
        display.delete(0,'end')
        display.insert(0,x)
    else:
        length=len(display.get())
        display.insert(length,x)
def opetatorP():
    x='+'
    if(display.get()!='0'):
        length = len(display.get())
        display.insert(length,x)
def opetatorS():
    x='-'
    if(display.get()!='0'):
        length = len(display.get())
        display.insert(length,x)
def opetatorM():
    x='*'
    if(display.get()!='0'):
        length = len(display.get())
        display.insert(length,x)
def opetatorD():
    x='/'
    if(display.get()!='0'):
        length = len(display.get())
        display.insert(length,x)
def funE():
    try:
        if(display.get()!='0'):
            value=display.get()
            result=eval(value)
            display.delete(0,'end')
            display.insert(0,result)
    except(SyntaxError):
        display.delete(0,'end')
        display.insert(0,'Error')
# clear or Del -- Button
def clr():
    display.delete(0,'end')
    display.insert(0,'0')
def Del():
    if display.get()!=0:
        length= len(display.get())
        display.delete(length-1,'end')
        if(length==1):
            display.insert(0,'0')
display = Entry(font='calibiri 14 bold',width=20,bd=6,justify=RIGHT)
display.insert(0,'0')
display.place(x=35,y=10)

#Number -- Button
button1 = Button(root , text = '1', width = 7, bd = 7, command=number1)
button1.place(x = 25,y = 215)
button2 = Button(root, text = '2', width = 7, bd = 7, command=number2)
button2.place(x = 110, y = 215)
button3 = Button(root, text = '3', width = 7, bd = 7, command=number3)
button3.place(x=195, y=215)
button4 = Button(root, text = '4', width = 7, bd = 7, command=number4)
button4.place(x=25, y=260)
button5 = Button(root, text = '5', width = 7, bd = 7, command=number5)
button5.place(x=110, y=260)
button6 = Button(root, text = '6', width = 7, bd = 7, command=number6)
button6.place(x=195, y=260)
button7 = Button(root, text = '7', width = 7, bd = 7, command=number7)
button7.place(x=25, y=305)
button8 = Button(root, text = '8', width = 7, bd = 7, command=number8)
button8.place(x=110, y=305)
button9 = Button(root, text = '9', width = 7, bd = 7, command=number9)
button9.place(x=195, y=305)
button0 = Button(root, text = '0', width = 7, bd = 7, command=number0)
button0.place(x= 25, y = 350)
# Operator Button
buttonp = Button(root, text = '.', width = 7, bd = 7, command = numberp)
buttonp.place(x = 110, y = 350)
buttonE = Button(root, text = '=', width = 7, bd = 7, command = funE)
buttonE.place(x = 195, y = 350)
buttonCLR = Button(root, text = 'CL',font = 'calibiri 14 bold', width = 5, bd = 3,bg = 'blue', command = clr)
buttonCLR.place(x = 25, y = 155)
buttonExit = Button(root, text = 'Off', font = 'calibiri 14 bold', width = 5, bd = 3, bg = 'white', command = root.quit)
buttonExit.place(x = 195, y = 155)
button_add = Button(root, font = 'calibiri 14 bold', text = '+', height = 3, width = 5, bd = 3, command = opetatorP)
button_add.place(x = 195, y = 65)
button_sub = Button(root, font = 'calibiri 14 bold', text = '-', width = 5, bd = 3, command = opetatorS)
button_sub.place(x = 110, y = 65)
button_mul = Button(root, font = 'calibiri 14 bold', text = 'x', width = 5, bd = 3, command = opetatorM)
button_mul.place(x = 25, y = 65)
button_div = Button(root, font = 'calibiri 14 bold', text = '/', width = 12, bd = 3, command = opetatorD)
button_div.place(x = 25, y = 110)
button_del = Button(root, font = 'calibiri 14 bold', text = '←', width = 5, bd = 3, bg = 'red', command = Del)
button_del.place(x = 110, y = 155)
root.mainloop()