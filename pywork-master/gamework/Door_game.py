from tkinter import *
from tkinter import messagebox

root = Tk()
tki = Toplevel()


# this is my advertisement
# this is danger door
def popup():
    render = messagebox.showerror('WARNING', 'This is the wrong door')
    if render == "ok":
        render = "You have picked wrong door :("
        Label(root, text=render, fg="white", bg="blue").pack()
        quit()


# this is safe door
def safedoor():
    render1 = messagebox.showinfo('you have found the right door :)', 'This is the correct door click ok to continue')
    if render1 == 'ok':
        render1 = 'You have won this game :)'
        Label(tki, text=render1, fg="white", bg="blue").pack()
        quit()


button = Button(root, text='Click the correct button to win the game', command=popup, fg="white", bg="blue",pady=100,padx=20).pack()
destroy = Button(root,text="click to exit",command=root.destroy).pack()

button2 = Button(tki, text='Click the correct button to win the game', command=safedoor, fg="white", bg="blue",pady=100,padx=20).pack()
destroy1 = Button(tki,text="click to exit",command=tki.destroy).pack()
mainloop()
