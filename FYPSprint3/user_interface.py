"""
Implement a GUI for viewing car data extracted using car_crawler.py
"""

from tkinter import *
from tkinter.messagebox import showinfo


class MyFrame(Frame):
    def __init__(self):
        self.get_entries()

    def get_entries(self):
        top = Tk()
        top.title('Echo')

        Label(top, text="Enter car Make:").pack(side=TOP)
        ent = Entry(top)
        ent.pack(side=TOP)
        Label(top, text="Enter car Model:").pack(side=TOP)
        ent2 = Entry(top)
        ent2.pack(side=TOP)

        btn = Button(top, text="Search", command=(lambda: self.reply(ent.get(), ent2.get())))
        btn.pack(side=LEFT)

        top.mainloop()

    def reply(self, name1, name2):
        #showinfo(title='Reply', message='Hello %s %s!' % (name1, name2))
        return name1, name2
