from tkinter import *
from tkinter import messagebox

root = Tk()


def popup():
    messagebox.showerror('wrong', 'This is the wrong door >:(')


def correct():
    messagebox.showinfo('correct', 'this is the correct door :)')


def three():
    cald = Toplevel()
    cool = Toplevel()
    nand = Toplevel()
    buttons = Button(cool, text='Click the correct door to win the game', pady=100, padx=20, command=popup).pack()
    buttons2 = Button(cald, text='Click the correct door to win the game', pady=100, padx=20, command=correct).pack()
    buttons2 = Button(nand, text='Click the correct door to win the game', pady=100, padx=20, command=popup).pack()


def two():
    cald = Toplevel()
    cool = Toplevel()
    buttons = Button(cool, text='Click the correct door to win the game', pady=100, padx=20, command=popup).pack()
    buttons2 = Button(cald, text='Click the correct door to win the game', pady=100, padx=20, command=correct).pack()


def myclick():
    tki = Toplevel()
    button2 = Button(tki, text='two doors', command=two).pack()
    button3 = Button(tki, text='three doors',command=three).pack()


def clickbait():
    messagebox.showwarning('HACKED', 'OH NO, YOU ARE HACKED >:)')


def clickedddd():
    tki = Toplevel()
    button12222 = Button(tki, text='YOU WON THE LOTTERY SO CLICK TO GET YOUR PRIZE',command=clickbait).pack()


button1 = Button(root, text='click to play door_game 2.0', command=myclick).pack()
button2 = Button(root, text='click here to see a visual advertisement',command=clickedddd).pack()

mainloop()
