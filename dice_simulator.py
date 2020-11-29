from tkinter import *
import random
root = Tk()
root.geometry("750x750+300+0")
root.title('Dice Simulator')
def dice():
    def one():
        l1 = Label(box, text='*', font='calibiri 50 bold',bg = 'white')
        l1.place(x = 200, y = 78)
    def two():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y=46)
        l2 = Label(box, text = '*', font = 'calibiri 50 bold', bg = 'white')
        l2.place(x = 246, y = 127)


    def three():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=203, y=16)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=145, y=122)
        l3 = Label(box, text = '*', font='calibiri 50 bold', bg='white')
        l3.place(x = 258, y = 122)

    def four():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y=16)
        l2 = Label(box, text = '*', font = 'calibiri 50 bold', bg = 'white')
        l2.place(x = 141, y = 124)
        l3 = Label(box, text = '*', font = 'calibiri 50 bold', bg = 'white')
        l3.place(x = 272, y = 16)
        l4 = Label(box, text = '*', font = 'calibiri 50 bold', bg = 'white')
        l4.place(x = 272, y = 124)
    def five():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y=16)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=141, y=124)
        l3 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l3.place(x=272, y=16)
        l4 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l4.place(x=272, y=124)
        l5 = Label(box, text = '*', font = 'calibiri 50 bold', bg = 'white')
        l5.place(x = 200, y = 68)

    def six():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y=16)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=141, y=124)
        l3 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l3.place(x=272, y=16)
        l4 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l4.place(x=272, y=124)
        l5 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l5.place(x=210, y=16)
        l6 = Label(box, text = '*', font = 'calibiri 50 bold', bg = 'white')
        l6.place(x = 210, y = 124)
    def ones():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x = 200, y = 300)
    def twos():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y = 268)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=246, y=349)
    def threes():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=203, y=238)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=145, y=344)
        l3 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l3.place(x=258, y=344)
    def fours():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y=238)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=141, y=346)
        l3 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l3.place(x=272, y=238)
        l4 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l4.place(x=272, y=346)
    def fives():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y=238)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=141, y=346)
        l3 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l3.place(x=272, y=238)
        l4 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l4.place(x=272, y=346)
        l5 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l5.place(x=200, y=290)
    def sixes():
        l1 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l1.place(x=141, y=238)
        l2 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l2.place(x=141, y=346)
        l3 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l3.place(x=272, y=238)
        l4 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l4.place(x=272, y=346)
        l5 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l5.place(x=210, y=238)
        l6 = Label(box, text='*', font='calibiri 50 bold', bg='white')
        l6.place(x=210, y=346)
    box = Text(root,height = 50, width = 50)
    a = random.randint(1,6)
    if(a == 1):
        one()
    if(a == 2):
        two()
    if(a == 3):
        three()
    if(a == 4):
        four()
    if(a == 5):
        five()
    if(a == 6):
        six()
    b = random.randint(1,6)
    if(b == 1):
        ones()
    if(b == 2):
        twos()
    if(b == 3):
        threes()
    if(b == 4):
        fours()
    if(b == 5):
        fives()
    if(b == 6):
        sixes()
    for k in range(0,2):
        for i in range(0,8):
            box.insert(INSERT,'            ')
            for j in range(0,6):

                if ((i == 0) or (i == 7)):
                    box.insert(INSERT,'=====')
                if(i>=1 and i<7):
                    if((j == 0)or (j == 5)):
                        box.insert(INSERT,'||')
                        box.insert(INSERT,'                     ')
                    else:
                        box.insert(INSERT,' ')
            box.insert(INSERT,'\n')
    box.place(x = 165, y = 120)
    box.config(state=DISABLED)
dice_button = Button(root, text = 'play', width = 10, height = 5,bd = 10, command = dice)
dice_button.place(x = 300, y = 0)
root.mainloop()