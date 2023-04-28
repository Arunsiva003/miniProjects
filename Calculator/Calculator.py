from tkinter import *

window = Tk()

def button(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('ZeroDivisionError')
    except ArithmeticError:
        equation_label.set("Math Error!")
    except:
        equation_label.set('invalid')

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

def oneclear():
    global equation_text
    equation_text = str(equation_text)[0:len(equation_text) - 1]
    equation_label.set(equation_text)

equation_text = ""
equation_label = StringVar()
window.geometry('420x560')
window.config(bg='black')

frame = Frame(window, bg='brown', bd=10, relief=RAISED)
frame.pack()

entrylabel = Label(frame, textvariable=equation_label, font=('consolas', 20), bg='black', fg='red', width=22,
                   height=2)
entrylabel.grid(row=0, columnspan=4)

button1 = Button(frame, text=1, command=lambda: button(1), width=8, height=4, font=35, bd=3)
button1.grid(row=1, column=0)
button2 = Button(frame, text=2, command=lambda: button(2), width=8, height=4, font=35, bd=3)
button2.grid(row=1, column=1)
button3 = Button(frame, text=3, command=lambda: button(3), width=8, height=4, font=35, bd=3)
button3.grid(row=1, column=2)
button4 = Button(frame, text=4, command=lambda: button(4), width=8, height=4, font=35, bd=3)
button4.grid(row=2, column=0)
button5 = Button(frame, text=5, command=lambda: button(5), width=8, height=4, font=35, bd=3)
button5.grid(row=2, column=1)
button6 = Button(frame, text=6, command=lambda: button(6), width=8, height=4, font=35, bd=3)
button6.grid(row=2, column=2)
button7 = Button(frame, text=7, command=lambda: button(7), width=8, height=4, font=35, bd=3)
button7.grid(row=3, column=0)
button8 = Button(frame, text=8, command=lambda: button(8), width=8, height=4, font=35, bd=3)
button8.grid(row=3, column=1)
button9 = Button(frame, text=9, command=lambda: button(9), width=8, height=4, font=35, bd=3)
button9.grid(row=3, column=2)
button0 = Button(frame, text=0, command=lambda: button(0), width=8, height=4, font=35, bd=3)
button0.grid(row=4, column=0)
plusbutton = Button(frame, text='+', command=lambda: button('+'), width=8, height=4, font=35, bd=3)
plusbutton.grid(row=1, column=3)
minusbutton = Button(frame, text='-', command=lambda: button('-'), width=8, height=4, font=35, bd=3)
minusbutton.grid(row=2, column=3)
multiplybutton = Button(frame, text='*', command=lambda: button('*'), width=8, height=4, font=35, bd=3)
multiplybutton.grid(row=3, column=3)
divbutton = Button(frame, text='/', command=lambda: button('/'), width=8, height=4, font=35, bd=3)
divbutton.grid(row=4, column=3)
dotbutton = Button(frame, text='.', command=lambda: button('.'), width=8, height=4, font=35, bd=3)
dotbutton.grid(row=4, column=1)
equalbutton = Button(frame, text='=', command=equals, width=8, height=4, font=35, bd=3)
equalbutton.grid(row=4, column=2)
clearbutton = Button(frame, text='clear', command=clear, width=8, height=4, font=35, bd=3)
clearbutton.grid(row=5, column=2)
delbutton = Button(frame, text='Del', command=oneclear, width=8, height=4, font=35, bd=3)
delbutton.grid(row=5, column=3)
openbrac = Button(frame, text=')', command=lambda: button(')'), width=8, height=4, font=35, bd=3)
openbrac.grid(row=5, column=1)
closebrac = Button(frame, text='(', command=lambda: button('('), width=8, height=4, font=35, bd=3)
closebrac.grid(row=5, column=0)

window.mainloop()
