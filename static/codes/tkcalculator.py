from tkinter import *


def insert(event):
    text = event.widget.cget("text")

    if text=='C':
        data.set('')
        root.update()

    elif text=='=':
        if data.get().isdigit():
            value = int(data.get())

        else:

            try:
                value = eval(data.get())
            except Exception as e:
                value = 'ERROR!'


        data.set(value)

        root.update()

    else:
        data.set(data.get() + text)
        root.update()



class button():

    def __init__(self, master, text, font):
        self.text = text
        self.font = font
        self.master = master

    def createbutton(self):
        b = Button(self.master, text=self.text, font=self.font)
        b.pack(side=LEFT)
        b.bind('<Button-1>', insert)



root = Tk()

root.geometry('250x478')

root.title('CALCULATOR BY HARSH')

root.minsize(250,478)


root.maxsize(250,478)

data = StringVar()

entry = Entry(root, textvariable=data, font="comicsanms 22 bold")
entry.pack(fill=X, pady=10, padx=8)

frame1 = Frame(root)

frame2 = Frame(root)

frame3 = Frame(root)

for i in range(9, 6, -1):

    button1 = button(frame1, f'{i}', "comicsanms 30 bold")
    button1.createbutton()

bplus = button(frame1, '+', "comicsanms 30 bold")

bplus.createbutton()

frame1.pack()


for i in range(6, 3, -1):
    button1 = button(frame2, f'{i}', "comicsanms 30 bold")
    button1.createbutton()

bminus = button(frame2, '-', "comicsanms 36 bold")
bminus.createbutton()

frame2.pack()


for i in range(3, 0, -1):
    button1 = button(frame3, f'{i}', "comicsanms 30 bold")

    button1.createbutton()

bmulti = button(frame3, '*', "comicsanms 30 bold")

bmulti.createbutton()

frame3.pack()

frame4 = Frame(root)

bzero = button(frame4, '0', "comicsanms 29 bold")

bzero.createbutton()

bpoint = button(frame4, '.', "comicsanms 30 bold")

bpoint.createbutton()

bdev = button(frame4, '/', "comicsanms 30 bold")

bdev.createbutton()

bequal = button(frame4, '=', "comicsanms 34 bold")

bequal.createbutton()

frame4.pack()

frame5 = Frame(root)

bclear = Button(frame5, text='C', font="comicsanms 36 bold")

bclear.bind('<Button-1>', insert)

bclear.pack(side=LEFT, padx=15)

bdoub = Button(frame5, text='00', font="comicsanms 36 bold")

bdoub.bind('<Button-1>', insert)

bdoub.pack(side=LEFT, padx=15)

frame5.pack()




root.mainloop()