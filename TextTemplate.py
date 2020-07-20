"""
creates custom gui to copy custom text templates to clipboard
Author: Maxwell Fusco
Language: Python 3.8
"""
import tkinter
import os

class TextTemplate:
    def __init__(self):
        self.root = tkinter.Tk()
        self.responses = TextTemplate.generate_responses()

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

text_template = TextTemplate()
