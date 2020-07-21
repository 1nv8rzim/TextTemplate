"""
creates custom gui to copy custom text templates to clipboard
Author: Maxwell Fusco
Language: Python 3.8
"""
import tkinter
import os
import subprocess
from math import sqrt, ceil

class TextTemplate:
    def __init__(self):
        self.root = tkinter.Tk()
        self.responses = TextTemplate.generate_responses()
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        self.row, self.column = self.generateDimensions()

        self.grid = tkinter.Frame(self.frame)
        self.grid.grid(sticky=N+S+E+W, columns=self.column, rows=self.row, columnspan=2)

        for x in range(self.row):
            for y in range(self.column):
                if len(self.responses) <= x * self.row + y:
                    break
                button = tkinter.Button(grid)
                response = self.responses[x * self.row + y]
                button.grid(row=x, column=y, text=response[1], command=lambda:subprocess.run("pbcopy", universal_newlines=True, input=response[2]))

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
        row = ciel(sqrt(len(self.responses)))
        col = ceil(len(self.reponses)/row)
        return row, col

text_template = TextTemplate()
