"""
creates custom gui to copy custom text templates to clipboard
Author: Maxwell Fusco
Language: Python 3.8
"""
from tkinter import *
import os
import subprocess
from math import sqrt, ceil

class TextTemplate:
    def __init__(self):
        self.root = Tk()
        self.responses = TextTemplate.generate_responses()
        self.frame = Frame(self.root)
        self.row, self.column = self.generateDimensions()
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.grid=Frame(self.frame)
        self.grid.grid(sticky=N+S+E+W, column=self.column, row=self.row, columnspan=2)
        Grid.rowconfigure(self.frame, self.row, weight=1)
        Grid.columnconfigure(self.frame, self.column, weight=1)

        for x in range(self.row):
            for y in range(self.column):
                if len(self.responses) <= x * self.row + y:
                    break
                response = self.responses[x * self.row + y]
                button = Button(self.frame, text=response[1], command=lambda:subprocess.run("pbcopy", universal_newlines=True, input=response[2]))
                button.grid(row=x, column=y, sticky=N+S+E+W)
                #button.pack(expand=FALSE, fill=X, side=TOP)

        self.root.mainloop()

    @staticmethod
    def generate_responses():
        responses = []
        for filename in os.listdir(os.getcwd()):
            if filename in ('TextTemplate.py','.git','..','.'):
                continue
            responses.append(TextTemplate.generate_response(filename))
        return responses

    @staticmethod
    def generate_response(filename):
        file_tup = []
        with open(filename) as file:
            for i, line in enumerate(file):
                if i == 0:
                    file_tup.append(int(line.strip()))
                    file_tup.append(filename[:-4])
                else:
                    if len(file_tup) == 3:
                        file_tup[2] += line
                    else:
                        file_tup.append(line)
        return tuple(file_tup)

    def generateDimensions(self):
        row = ceil(sqrt(len(self.responses)))
        col = ceil(len(self.responses)/row)
        return row, col

text_template = TextTemplate()
