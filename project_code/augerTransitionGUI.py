#all about Auger Transitions GUI
from getDatabase import getAtom
import tkinter
from tkinter import messagebox 
from tkinter import ttk
from tkinter import Scrollbar
from tkinter.filedialog import askdirectory
import itertools
import shlex
from decimal import Decimal
import pandas as pd
from tabulate import tabulate


def augerTransitionGUI(index):
    global lastChoice
    lastChoice=''
    atom_number=index+3
    auger_window=tkinter.Tk()
    auger_window.geometry("1200x680")
    number_name=getAtom()
    atom_name=number_name[atom_number]
    auger_window.title('Auger Transitions for %s'%atom_name)
    auger_window.focus_force()
    
    
    
if __name__ == "__main__":
    lastChoice=0
    augerTransitionGUI(1)