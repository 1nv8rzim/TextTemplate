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
        self.responses = TextTemplate.generate_reponses()

    @staticmethod
    def generate_reponses():
        responses = []
        for filename in os.listdir(os.getcwd()):
            if filename == 'TextTemplate.py':
                continue
            reponses.append(TextTemplate.generate_reponses(filename))
        return responses.sort()

    @staticmethod
    def generate_reponse(filename):
        file_tup = []
        with open(filename) as file:
            for i, line in enumerate(file):
                if i == 0:
                    file_tup.append(int(file.readline().strip()))
                    file_tup.append(filename)
                else:
                    if len(file_tup) == 3:
                        file_tup[2] += line
                    else:
                        file_tup.append(line)
        return tuple(file_tup)
        
                        