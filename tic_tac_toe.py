from tkinter import *
from tkinter import messagebox
plyr1 = 0
plyr2 = 0
x = 0
y=''
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []

class tic_tac:
    def __init__(self):
        root = Tk()
        root.title('Tic Tac Toe')
        root.geometry("600x700+400+20")
        def state():
            if(len(pe.get())> 0 and len(pe2.get())>1):
                pe.config(state = DISABLED)
                pe2.config(state = DISABLED)
            else:
                messagebox.showinfo('Name','Enter the Player Name')
        p1 = Label(root, text = ' Player 1', font = 'Times 18 bold')
        p1.place(x = 10, y = 10)
        pe = Entry(root, bd = 3)
        pe.place(x = 150, y = 15)
        p2 = Label(root, text = ' Player 2', font = 'Times 18 bold')
        p2.place(x = 10, y = 50)
        pe2 = Entry(root, bd = 3)
        pe2.place(x = 150, y = 55)
        sub = Button(root, text = 'Submit', bd = 5, width = 10,font = 'bold',command = state)
        sub.place(x = 300, y = 45)


        def val(num):
            global x, y
            global plyr1,plyr2
            if num == 1:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'
                l7.append(y)
                l4.append(y)
                l1.append(y)
                b1.config(text = y)
                x = x + 1
                b1.config(state=DISABLED)
            if num == 2:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'
                l1.append(y)
                l5.append(y)
                b2.config(text = y)
                x = x + 1
                b2.config(state = DISABLED)
            if num == 3:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'
                l1.append(y)
                l6.append(y)
                l8.append(y)
                b3.config(text = y)
                x = x + 1
                b3.config(state=DISABLED)
            if num == 4:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'
                l4.append(y)
                l2.append(y)
                b4.config(text = y)
                x = x + 1
                b4.config(state=DISABLED)
            if num == 5:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'
                l7.append(y)
                l2.append(y)
                l5.append(y)
                b5.config(text = y)
                l8.append(y)
                x = x + 1
                b5.config(state=DISABLED)
            if num == 6:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'
                l2.append(y)
                l6.append(y)
                b6.config(text = y)
                x = x + 1
                b6.config(state=DISABLED)
            if num == 7:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'

                l4.append(y)
                l8.append(y)

                l3.append(y)
                b7.config(text = y)
                x = x + 1
                b7.config(state=DISABLED)
            if num == 8:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'

                l3.append(y)
                l5.append(y)
                b8.config(text = y)
                x = x + 1
                b8.config(state=DISABLED)
            if num == 9:
                if x % 2 == 0:
                    y = 'X'
                elif x % 2 != 0:
                    y = 'O'

                l3.append(y)
                l7.append(y)
                l6.append(y)
                b9.config(text = y)
                x = x + 1
                b9.config(state=DISABLED)
            if(len(l1) == 3):
                for i in l1:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result',pe.get()+' win')
                    root.destroy()
                    


                for i in l1:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    

            if (len(l2) == 3):
                for i in l2:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result', pe.get() + ' win')
                    root.destroy()
                    
                for i in l2:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    
            if (len(l3) == 3):
                for i in l3:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result', pe.get() + ' win')
                    root.destroy()
                for i in l3:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    

            if (len(l4) == 3):
                for i in l4:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result', pe.get() + ' win')
                    root.destroy()
                    
                for i in l4:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    

            if (len(l5) == 3):
                for i in l5:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result', pe.get() + ' win')
                    root.destroy()
                    
                for i in l5:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    

            if (len(l6) == 3):
                for i in l6:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result', pe.get() + ' win')
                    root.destroy()
                    
                for i in l6:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    

            if (len(l7) == 3):
                for i in l7:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result', pe.get() + ' win')
                    root.destroy()
                    
                for i in l7:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    

            if (len(l8) == 3):
                for i in l8:
                    if i == 'X':
                        flagx = 1
                    else:
                        flagx = 0
                        break
                if flagx == 1:
                    messagebox.showinfo('Game Result', pe.get() + ' win')
                    root.destroy()
                    
                for i in l8:
                    if i == 'O':
                        flago = 1
                    else:
                        flago = 0
                        break
                if flago == 1:
                    messagebox.showinfo('Game Result', pe2.get() + ' win')
                    root.destroy()
                    
                if x == 9:
                    messagebox.showinfo('Game Result', 'Game Draw')
                    root.destroy()
                    

        b1 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(1))
        b1.place(x = 10, y = 100)
        b2 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(2))
        b2.place(x = 190, y = 100)
        b3 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(3))
        b3.place(x = 370, y = 100)
        b4 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(4))
        b4.place(x = 10, y = 290)
        b5 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(5))
        b5.place(x = 190, y = 290)
        b6 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(6))
        b6.place(x = 370, y = 290)

        b7 = Button(root, height  = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(7))
        b7.place(x = 10, y = 480)
        b8 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(8))
        b8.place(x = 190, y = 480)
        b9 = Button(root, height = 5, width = 10, bd = 5, font = 'times 20 bold', command =lambda :val(9))
        b9.place(x = 370, y = 480)
        root.mainloop()
obj = tic_tac()