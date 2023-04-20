import tkinter as tk
from tkinter import *
import time
import sys, os

class LogicSouls(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Logic Souls')
        self.resizable(0, 0)
        self.geometry('500x500')
        self['bg'] = 'black'
        self.kolakowski = [1, 2, 2]
        self.counter = 2
        self.loser = False

        #value = next number in the sequence
        #pointer = run time limit for current run 
        #counter = current run length 

        # label
        self.label = Label(
            self,
            text = 'GET READY!',
            font=('Digital-7', 60),
            bg = 'black',
            fg = 'white'
            )

        self.label.pack(expand=True)

        self.score = Label(
            self, 
            text = str(self.counter -2),
            font = ('Digital-7', 30),
            bg = 'black',
            fg = 'white'
        )

        self.score.pack(expand = True)

        self.bind('<Key>', self.key_pressed)


        # schedule an update every 1 second
        self.label.after(1000, self.update)



    def generate_next_kolakoski(self):

        x = self.kolakowski[self.counter]
        if self.counter % 2 == 0:
            if x == 1:
                self.kolakowski.append(1)
            if x == 2:
                self.kolakowski.append(1)
                self.kolakowski.append(1)
        if self.counter % 2 == 1:
            if x == 1:
                self.kolakowski.append(2)
            if x == 2:
                self.kolakowski.append(2)
                self.kolakowski.append(2)
        self.counter += 1 
        



    def update(self):
        """ update the label every 1 second """
        if not self.loser:
            if self.counter >= 22:
                self.label.configure(font = ('texgyrechorus', 60))
            if self.counter >= 71:
                self.label.configure(font = ('clean', 60))
            if self.counter >= 202:
                self.label.configure(font = ('mincho', 60))
            if self.counter >= 1002:
                self.label.configure(font = ('latin modern typewriter', 60))


            self.label.configure(fg = 'white')
            self.generate_next_kolakoski()
            self.label.configure(text=str(self.kolakowski[self.counter]))
            self.score.configure(text = str(self.counter -2))
        else:
            self.label.configure(fg = 'red', text = 'YOU LOSE')
            self.loser = True
            self.label.after(500, self.game_over)


        self.loser = True
        # schedule another timer
        self.label.after(1000, self.update)

    def key_pressed(self, event):
        if event.char == str(self.kolakowski[self.counter]):
            self.label.configure(fg = 'green')
            self.loser = False
        else:
            self.label.configure(fg = 'red', text = 'YOU LOSE')
            self.loser = True
            self.label.after(500, self.game_over)

    def game_over(self):
        time.sleep(1)
        sys.exit(1)

if __name__ == "__main__":
    root = LogicSouls()
    root.mainloop()