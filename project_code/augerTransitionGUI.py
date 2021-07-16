#all about Auger Transitions GUI
from getDatabase import getAtom
from getDatabase import getEnergies
from getDatabase import getNotation
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
    
    #auger window
    auger_window=tkinter.Tk()
    auger_window.geometry("1200x680")
    number_name=getAtom()
    atom_name=number_name[atom_number]
    auger_window.title('Auger Transitions for %s'%atom_name)
    auger_window.focus_force()
    
    #read from database
    number_energies=getEnergies()
    barkla_orbital=getNotation()
    
    #nonNone energies for this atom
    current_energies=number_energies[atom_number]
    nonNone_value=dict()
    nonNone_orbital=[]
    for shell in current_energies:
        if current_energies[shell]!=None:
            nonNone_value[shell]=current_energies[shell]
            nonNone_orbital.append(barkla_orbital[shell])
    length=len(nonNone_value)
    
    #binding energies table
    core_table = ttk.Treeview(auger_window,height=length,columns=['1','2','3'],show='headings')
    core_table.column('1', width=150) 
    core_table.column('2', width=150) 
    core_table.column('3', width=150) 
    core_table.heading('1', text='Barkla Notation')
    core_table.heading('2', text='Orbital Notation')
    core_table.heading('3', text='Binding Energies')
    index=0
    for item in nonNone_value:
        core_table.insert('',index,values=(item,nonNone_orbital[index],nonNone_value[item]))
        index+=1
    core_table.place(x=10,y=70)
    
    
    auger_window.mainloop()
    
    
if __name__ == "__main__":
    lastChoice=0
    augerTransitionGUI(1)