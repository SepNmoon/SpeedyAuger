#all about the root GUI
from getDatabase import getAtom
from augerTransitionGUI import augerTransitionGUI
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



#rootGUI
def rootGUI():
    
    number_name=getAtom() #dict
    root=tkinter.Tk() 
    root.geometry("1000x680")
    #root.resizable(0,0)
    root.title('All Atom')
    tkinter.Button(root,text='1 H',width=5,height=2,bg='Gray').place(x=30,y=10) #1
    tkinter.Button(root,text='2 He',width=5,height=2,bg='Gray').place(x=880,y=10) #18
    uncover_atom=dict()
    uncover_atom[94],uncover_atom[95],uncover_atom[96],uncover_atom[97],uncover_atom[98],uncover_atom[99],uncover_atom[100],uncover_atom[101],uncover_atom[102]='Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No'
    uncover_atom[103],uncover_atom[104],uncover_atom[105],uncover_atom[106],uncover_atom[107]='Lr','Rf','Db','Sg','Bh'
    uncover_atom[108],uncover_atom[109],uncover_atom[110],uncover_atom[111],uncover_atom[112]='Hs','Mt','Ds','Rg','Cn'
    uncover_atom[113],uncover_atom[114],uncover_atom[115],uncover_atom[116],uncover_atom[117],uncover_atom[118]='Nh','Fl','Mc','Lv','Ts','Og'
    for i in range(25):
        if i<=8:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+94,'name':uncover_atom[i+94]},width=5,height=2,bg='Gray').place(x=380+i*50, y=520)
        else:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+94,'name':uncover_atom[i+94]},width=5,height=2,bg='Gray').place(x=130+(i-9)*50, y=370)  
         
    for i in range(91):
        atom_name=number_name[i+3]
        if i==0 or i==1:     
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(x=30+i*50, y=70)
        elif i<=7:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(x=630+(i-2)*50, y=70)
        elif i==8 or i==9:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(x=30+(i-8)*50, y=130)
        elif i<=15:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(x=630+(i-10)*50, y=130)
        elif i==16 or i==17:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(x=30+(i-16)*50, y=190)
        elif i<=27:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='PowderBlue').place(x=30+(i-16)*50, y=190)
        elif i<=33:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(x=30+(i-16)*50, y=190)
        elif i==34 or i==35:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(x=30+(i-34)*50, y=250)
        elif i<=45:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='PowderBlue').place(x=30+(i-34)*50, y=250)
        elif i<=51:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(x=30+(i-34)*50, y=250)
        elif i==52 or i==53:
            tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(x=30+(i-52)*50, y=310)
        elif i>=54 and i<=67:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='LightGreen').place(x=30+(i-52)*50, y=460)
        elif i<=77:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='PowderBlue').place(x=130+(i-68)*50, y=310)
        elif i<=83:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(x=130+(i-68)*50, y=310)
        elif i==84 or i==85:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(x=30+(i-84)*50, y=370)
        else:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='LightGreen').place(x=30+(i-84)*50, y=520)
        
           
    root.mainloop()



if __name__ == "__main__":
    rootGUI()
    