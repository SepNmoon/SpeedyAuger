import pymysql
import tkinter
import numpy as np
from tkinter import messagebox 
from tkinter import ttk
from tkinter import Scrollbar
from tkinter.filedialog import askdirectory
import itertools
import shlex
from decimal import Decimal
import pandas as pd
from tabulate import tabulate
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#connect database
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='atom_shell',
    charset='utf8'
)

#get atomic number and atomic name
def getAtom():
    cursor = db.cursor()
    sql = 'SELECT * FROM atom'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_name=dict()
    for row in results:
        atom_number = row[0]
        atom_name = row[1]
        number_name[atom_number]=atom_name
    return number_name


#get electron configuration
def getShell():
    cursor = db.cursor()
    sql = 'SELECT * FROM shell'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_shell=dict()
    for row in results:
        temp=dict()
        atom_number = row[0]
        ele_k=row[1]
        ele_l1,ele_l2,ele_l3=row[2],row[3],row[4]
        ele_m1,ele_m2,ele_m3,ele_m4,ele_m5=row[5],row[6],row[7],row[8],row[9]
        ele_n1,ele_n2,ele_n3,ele_n4,ele_n5,ele_n6,ele_n7=row[10],row[11],row[12],row[13],row[14],row[15],row[16]
        ele_o1,ele_o2,ele_o3,ele_o4,ele_o5,ele_o6=row[17],row[18],row[19],row[20],row[21],row[22]
        ele_p1,ele_p2,ele_p3,ele_p4,ele_p5=row[23],row[24],row[25],row[26],row[27]
        ele_q1=row[28]
        temp['K']=ele_k
        temp['L1'],temp['L2'],temp['L3']=ele_l1,ele_l2,ele_l3
        temp['M1'],temp['M2'],temp['M3'],temp['M4'],temp['M5']=ele_m1,ele_m2,ele_m3,ele_m4,ele_m5
        temp['N1'],temp['N2'],temp['N3'],temp['N4'],temp['N5'],temp['N6'],temp['N7']=ele_n1,ele_n2,ele_n3,ele_n4,ele_n5,ele_n6,ele_n7
        temp['O1'],temp['O2'],temp['O3'],temp['O4'],temp['O5'],temp['O6']=ele_o1,ele_o2,ele_o3,ele_o4,ele_o5,ele_o6
        temp['P1'],temp['P2'],temp['P3'],temp['P4'],temp['P5']=ele_p1,ele_p2,ele_p3,ele_p4,ele_p5
        temp['Q1']=ele_q1
        number_shell[atom_number]=temp
    return number_shell


#get electrons energies
def getEnergies():
    cursor = db.cursor()
    sql = 'SELECT * FROM energies'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_energies=dict()
    for row in results:
        temp=dict()
        atom_number = row[0]
        en_k=row[1]
        en_l1,en_l2,en_l3=row[2],row[3],row[4]
        en_m1,en_m2,en_m3,en_m4,en_m5=row[5],row[6],row[7],row[8],row[9]
        en_n1,en_n2,en_n3,en_n4,en_n5,en_n6,en_n7=row[10],row[11],row[12],row[13],row[14],row[15],row[16]
        en_o1,en_o2,en_o3,en_o4,en_o5,en_o6,en_o7=row[17],row[18],row[19],row[20],row[21],row[22],row[23]
        en_p1,en_p2,en_p3,en_p4,en_p5=row[24],row[25],row[26],row[27],row[28]
        en_q1=row[29] 
        temp['K']=en_k
        temp['L1'],temp['L2'],temp['L3']=en_l1,en_l2,en_l3
        temp['M1'],temp['M2'],temp['M3'],temp['M4'],temp['M5']=en_m1,en_m2,en_m3,en_m4,en_m5
        temp['N1'],temp['N2'],temp['N3'],temp['N4'],temp['N5'],temp['N6'],temp['N7']=en_n1,en_n2,en_n3,en_n4,en_n5,en_n6,en_n7
        temp['O1'],temp['O2'],temp['O3'],temp['O4'],temp['O5'],temp['O6'],temp['O7']=en_o1,en_o2,en_o3,en_o4,en_o5,en_o6,en_o7
        temp['P1'],temp['P2'],temp['P3'],temp['P4'],temp['P5']=en_p1,en_p2,en_p3,en_p4,en_p5           
        temp['Q1']=en_q1
        number_energies[atom_number]=temp
    return number_energies


#get barkla and orbital notation
def getNotation():
    cursor = db.cursor()
    sql = 'SELECT * FROM notation'
    cursor.execute(sql)
    results = cursor.fetchall()
    barkla_orbital=dict()
    for row in results:
        barkla_notation = row[0]
        orbital_notation=row[1]
        barkla_orbital[barkla_notation]=orbital_notation   
    return barkla_orbital


def getRange():
    cursor = db.cursor()
    sql = 'SELECT * FROM energies_range'
    cursor.execute(sql)
    results = cursor.fetchall()
    number_range=dict()
    for row in results:
        atom_number=row[0]
        max_value=row[1]
        min_value=row[2]
        temp=dict()
        temp['Max']=max_value
        temp['Min']=min_value
        number_range[atom_number]=temp
    return number_range
            
    
    
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#All about AugerTransitionGUI

#Button command in Auger Transition Window
def updateTable(table,value,position):
    for index in range(position):
        index+=1
        ke_result=table.set(index,'#2')
        ke_result=float(ke_result)
        result=Decimal(value-ke_result).quantize(Decimal('0.00'))
        if result<0:
            table.set(index,'#3','Not Accessible')
        else:
            table.set(index,'#3',result)

                
def clickConvertButtonAT(select,table,position,inputEntry,auger_window,lastLabel):
    global lastChoice
    lastLabel['text']='Values in table calculated for: %s'%lastChoice    
    inputValue=inputEntry.get()  
    selectChoice=select.get()

    if (selectChoice=='No selection' and inputValue=='') or (selectChoice!='No selection' and inputValue!=''):
        tkinter.messagebox.showinfo(title='ERROR',message='Please input or select',parent=auger_window)
    elif selectChoice=='No selection' and inputValue!='':        
        try:           
            inputValue=float(inputValue)            
        except:
            tkinter.messagebox.showinfo(title='ERROR',message='Please input valid value',parent=auger_window)
        else:
            updateTable(table,inputValue,position)
            lastChoice=inputValue
                   
    elif selectChoice!='No selection' and inputValue=='': 
        if selectChoice=='Mg 1253.6(eV)':           
            selectValue=1253.6
            lastChoice='Mg 1253.6(eV)'
        elif selectChoice=='Al 1486.7(eV)':
            selectValue=1486.7
            lastChoice='Al 1486.7(eV)'
        elif selectChoice=='Ag 2984.3(eV)':
            selectValue=2984.3
            lastChoice='Ag 2984.3(eV)'
        elif selectChoice=='Cr 5414.9(eV)':
            selectValue=5414.9
            lastChoice='Cr 5414.9(eV)'
        elif selectChoice=='Ga 9251.74(eV)':
            selectValue=9251.74   
            lastChoice='Ga 9251.74(eV)'
        updateTable(table,selectValue,position)
        
 
        
        
        
def clickClearButtonAT(inputEntry,select,table,position):
    inputEntry.delete(0,'end')
    select.current(5)
    for index in range(position):
        index+=1
        table.set(index,'#3','')    




        
def clickExportButtonAT(auger_window,transition_table,atom_name,position):
    
    if transition_table.set(1,'#3')=='':
        tkinter.messagebox.showinfo(title='ERROR',message='Please input or select',parent=auger_window)
    else:
        reminderBox=tkinter.messagebox.askquestion('Confirmation','Do you want to continue?',parent=auger_window)
        if reminderBox=='yes':
            file_path=askdirectory(parent=auger_window)
            if file_path!='':  
 
                table_header = ['Auger Transition', 'Auger Energies (KE)', 'Auger Energies (BE)']
                table_data=[]
                for p in range(position):
                    temp=[]
                    temp.append(transition_table.set(p+1,'#1'))
                    temp.append(transition_table.set(p+1,'#2'))
                    temp.append(transition_table.set(p+1,'#3'))
                    table_data.append(temp)

                select_value=float(transition_table.set(1,'#2'))+float(transition_table.set(1,'#3'))
                select_value=Decimal(select_value).quantize(Decimal('0.00'))
                select_value=str(select_value)
                file_path=file_path+'/'+'auger_transition_'+atom_name+'_'+select_value+'.txt'              
                with open(file_path,"w") as f:
                    f.write(tabulate(table_data, headers=table_header))                  
            else:
                pass        
        else:
            pass
        
   



    
#Calculate Auger energies for transitions
def calculateAuger(number):
    #read from database
    number_energies=getEnergies()
    current_energies=number_energies[number]
    next_energies=number_energies[number+1]
    nonNone_energies=dict()
    for e in current_energies:
        if current_energies[e]!=None:
            nonNone_energies[e]=current_energies[e]
    transition_array=[]
    for i in itertools.combinations_with_replacement(nonNone_energies.keys(), 3): 
        temp=','.join(i)
        transition_array.append(temp)
    transition_array_copy=transition_array.copy()
    for t in transition_array_copy:
        temp=shlex.shlex(t,posix=True)
        temp.whitespace += ','
        temp.whitespace_split = True
        temp=list(temp)
        if temp[0]==temp[1]:
            transition_array.remove(t)
        elif number<=10:
            if temp[0]=='L1' or temp[0]=='L2' or temp[0]=='L3':
                transition_array.remove(t)
        elif number<=18:
            if temp[0]=='M1' or temp[0]=='M2' or temp[0]=='M3':
                transition_array.remove(t)
        elif number<=36:
            if temp[0]=='N1' or temp[0]=='N2' or temp[0]=='N3':
                transition_array.remove(t)
        elif number<=54:
            if number==45 and (temp[0]=='O1' or temp[1]=='O1' or temp[2]=='O1'):
                transition_array.remove(t)
                
            if temp[0]=='O1' or temp[0]=='O2' or temp[0]=='O3':
                transition_array.remove(t)
                       
        elif number<=86:
            if number==76 and (temp[0]=='P1' or temp[1]=='P1' or temp[2]=='P1'):
                transition_array.remove(t)
            if number==57 and (temp[0]=='O4' or temp[1]=='O4' or temp[2]=='O4' or temp[0]=='O5' or temp[1]=='O5' or temp[2]=='O5'):
                transition_array.remove(t)
            if number==64 and (temp[0]=='O4' or temp[1]=='O4' or temp[2]=='O4' or temp[0]=='O5' or temp[1]=='O5' or temp[2]=='O5'):
                transition_array.remove(t)
            if temp[0]=='P1' or temp[0]=='P2' or temp[0]=='P3':
                transition_array.remove(t)
        elif number==93 and (temp[0]=='P4' or temp[1]=='P4' or temp[2]=='P4' or temp[0]=='P5' or temp[1]=='P5' or temp[2]=='P5'):
            transition_array.remove(t)
    
    transition_energies=dict()
    for transition in transition_array:
        temp=shlex.shlex(transition,posix=True)
        temp.whitespace += ','
        temp.whitespace_split = True
        temp=list(temp)
        vacancy=temp[0]
        inter1=temp[1]
        inter2=temp[2]
        energies=current_energies[vacancy]-0.5*(current_energies[inter1]+next_energies[inter1])-0.5*(current_energies[inter2]+next_energies[inter2])
        energies=Decimal(energies).quantize(Decimal('0.00'))
 
        if energies>=10:
           transition_energies[transition]=energies
    return transition_energies


    
#AugerGUI
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
    
    #calculate energies for transitions
    transition_energies=calculateAuger(atom_number)
    

    #transition table
    if len(transition_energies)<=30:
        table_row=len(transition_energies)
    else:
        table_row=27
    transition_table=ttk.Treeview(auger_window,height=table_row,columns=['1','2','3'],show='headings')
    transition_table.column('1', width=200) 
    transition_table.column('2', width=200) 
    transition_table.column('3', width=200) 
    transition_table.heading('1', text='Auger Transition')
    transition_table.heading('2', text='Auger Energies (KE)')
    transition_table.heading('3', text='Auger Energies (BE)')
    position=0

    for t in transition_energies:
        transition_table.insert('',position,iid=position+1,values=(t,transition_energies[t],''))
        position+=1
    transition_table.place(x=550,y=90)
    ybar=Scrollbar(transition_table,orient='vertical', command=transition_table.yview,bg='Gray')
    transition_table.configure(yscrollcommand=ybar.set)
    ybar.place(relx=0.95, rely=0.02, relwidth=0.035, relheight=0.958)
    
    
    #Add convert function
    selectButton=ttk.Combobox(auger_window)    
    selectButton.place(x=550,y=30)
    selectButton['value']=('Mg 1253.6(eV)','Al 1486.7(eV)','Ag 2984.3(eV)','Cr 5414.9(eV)','Ga 9251.74(eV)','No selection')
    selectButton.current(5)
    
    orLabel=tkinter.Label(auger_window,text='or')
    orLabel.place(x=750,y=30)
    
    inputEntry=tkinter.Entry(auger_window)
    inputEntry.place(x=800,y=30)
    
    unitLabel=tkinter.Label(auger_window,text='(eV)')
    unitLabel.place(x=950,y=30)
    
    lastLabel=tkinter.Label(auger_window,text='Values in table calculated for: %s'%lastChoice)
    lastLabel.place(x=930,y=65)
    
    convertButton=tkinter.Button(auger_window,text='Convert',bg='Orange',command=lambda: clickConvertButtonAT(selectButton,transition_table,position,inputEntry,auger_window,lastLabel))
    convertButton.place(x=1000,y=30)
    
    clearButton=tkinter.Button(auger_window,text='Clear',command=lambda: clickClearButtonAT(inputEntry,selectButton,transition_table,position))
    clearButton.place(x=1065,y=30)
    
    
    exportButton=tkinter.Button(auger_window,text='Export',bg='LightBlue',command=lambda: clickExportButtonAT(auger_window,transition_table,atom_name,position))
    exportButton.place(x=1140,y=30)
    

    auger_window.mainloop()


#----------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------- 
#All about rangeGUI 
def clickExportButtonRG(range_window,transition_table,position,rangeMin,rangeMax,selectKE,selectBE,selectValue):
    reminderBox=tkinter.messagebox.askquestion('Confirmation','Do you want to continue?',parent=range_window)
    rangeMin=str(rangeMin)
    rangeMax=str(rangeMax)
    selectValue=str(selectValue)
    if reminderBox=='yes':
        file_path=askdirectory(parent=range_window)
        if file_path!='':
            table_header=['Atom','Auger Transition','Auger Energy']
            table_data=[]
            for p in range(position):
                temp=[]
                temp.append(transition_table.set(p+1,'#1'))
                temp.append(transition_table.set(p+1,'#2'))
                temp.append(transition_table.set(p+1,'#3'))
                table_data.append(temp)
            
            if selectKE==True:
                file_path=file_path+'/'+'Auger_transitions_'+'from_'+rangeMin+'_to_'+rangeMax+'_KE_'+sortOrder+'.txt'
            elif selectBE==True:               
                file_path=file_path+'/'+'Auger_transitions_'+'from_'+rangeMin+'_to_'+rangeMax+'_BE_'+selectValue+sortOrder+'.txt'
            with open(file_path,'w') as f:
                f.write(tabulate(table_data,headers=table_header))
        
        
        else:
            pass
    else:
        pass
    

def clickSortButtonRG(transition_table,position,descending):
    global sortOrder
    
    position_energies=dict()
    for p in range(position):
        p+=1
        position_energies[p]=float(transition_table.set(p,'#3'))

    if descending==True:
        sortOrder='descending'
        sort_position=sorted(position_energies.items(),key=lambda x:x[1],reverse=True)
    else:
        sortOrder='ascending'
        sort_position=sorted(position_energies.items(),key=lambda x:x[1],reverse=False)
    
    new_table=[]
    for i in sort_position:
        p=i[0]
        temp=[]
        temp.append(transition_table.set(p,'#1'))
        temp.append(transition_table.set(p,'#2'))
        temp.append(transition_table.set(p,'#3'))
        new_table.append(temp)
    
    for p in range(position):
        p+=1              
        transition_table.set(p,'#1',new_table[p-1][0])
        transition_table.set(p,'#2',new_table[p-1][1])
        transition_table.set(p,'#3',new_table[p-1][2])
 

def clickNumberButtonRG(all_transitions,transition_table,position):
    global sortOrder
    sortOrder='by_number'
    new_table=[]
    for atom_name in all_transitions:   
        current_transitions=all_transitions[atom_name]
        for transition in current_transitions:
            temp=[]
            temp.append(atom_name)
            temp.append(transition)
            temp.append(current_transitions[transition])
            new_table.append(temp)
    
        
        
    for p in range(position):
        p+=1
        transition_table.set(p,'#1',new_table[p-1][0])
        transition_table.set(p,'#2',new_table[p-1][1])
        transition_table.set(p,'#3',new_table[p-1][2])

    
    
      

def augerRangeGUI(selectBE,selectKE,fromEntry,toEntry,selectValue,fromAll,fromSome):
    range_window=tkinter.Tk()
    range_window.geometry("1200x680")
    
    number_range=getRange()
    number_name=getAtom()


    rangeMin=min(float(fromEntry.get()),float(toEntry.get()))
    rangeMax=max(float(fromEntry.get()),float(toEntry.get()))
    correctAtom=[]
    
    if fromAll==True:
        if selectKE==True:
            for number in number_range:
                temp=number_range[number]
                if temp['Max']<rangeMin or temp['Min']>rangeMax:
                    pass
                else:
                    correctAtom.append(number)
        elif selectBE==True:
            for number in number_range:
                temp=number_range[number]
                temp_min=selectValue-temp['Max']
                temp_max=selectValue-temp['Min']
                if temp_max<rangeMin or temp_min>rangeMax:
                    pass
                else:
                    correctAtom.append(number)
        print(correctAtom)
    elif fromSome==True:
        correctAtom=unique_array

    all_transitions=dict()  
    transitions_length=0
    for number in correctAtom:        
        temp=dict()
        atom_name=number_name[number]
        current_transitions=calculateAuger(number)
        if selectKE==True:           
            for t in current_transitions:
                if current_transitions[t]>=rangeMin and current_transitions[t]<=rangeMax:
                    transitions_length+=1
                    temp[t]=current_transitions[t]
                    all_transitions[atom_name]=temp
        elif selectBE==True:            
            for t in current_transitions:
                if (selectValue-float(current_transitions[t]))>=rangeMin and (selectValue-float(current_transitions[t]))<=rangeMax:
                    transitions_length+=1
                    temp[t]=Decimal(selectValue-float(current_transitions[t])).quantize(Decimal('0.00'))                    
                    all_transitions[atom_name]=temp

    if transitions_length>0:
        
        if transitions_length<=30:
            table_row=transitions_length
        else:
            table_row=30
        
        transition_table=ttk.Treeview(range_window,height=table_row,columns=['1','2','3'],show='headings')
        transition_table.column('1',width=100) 
        transition_table.column('2',width=200) 
        transition_table.column('3',width=200) 
        transition_table.heading('1', text='Atom')
        transition_table.heading('2', text='Auger Transition')
        transition_table.heading('3', text='Auger Energies')
        transition_table.pack()    
    
        position=0
        for atom_name in all_transitions:
            current_transitions=all_transitions[atom_name]
            for t in current_transitions:            
                transition_table.insert('',position,iid=position+1,values=(atom_name,t,current_transitions[t]))
                position+=1
    

        

        ybar=Scrollbar(transition_table,orient='vertical', command=transition_table.yview,bg='Gray')
        transition_table.configure(yscrollcommand=ybar.set)
        ybar.place(relx=0.95, rely=0.02, relwidth=0.035, relheight=0.958)
    
        descendingButton=tkinter.Button(range_window,text='Descending order (energies)',bg='LightPink',command=lambda: clickSortButtonRG(transition_table,position,descending=True))
        descendingButton.place(x=900,y=50)
        ascendingButton=tkinter.Button(range_window,text='Ascending order (energies)',bg='LightBlue',command=lambda: clickSortButtonRG(transition_table,position,descending=False))
        ascendingButton.place(x=900,y=100)
        numberButton=tkinter.Button(range_window,text='Sort by atomic number',bg='LightGreen',command=lambda: clickNumberButtonRG(all_transitions,transition_table,position))
        numberButton.place(x=900,y=150)
    
        exportButton=tkinter.Button(range_window,text='Export',bg='Yellow',command=lambda: clickExportButtonRG(range_window,transition_table,position,rangeMin,rangeMax,selectKE,selectBE,selectValue))
        exportButton.place(x=900,y=300)
    else:
        tkinter.messagebox.showinfo(title='REMINDER',message='No relevant results',parent=range_window)
    
    range_window.mainloop()  



#----------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------- 
#All about rootGUI 

def clickSearchButtonRT(root,fromEntry,toEntry,v2,selectButton,inputEntry,v1,v3):
    fromValue=fromEntry.get()
    toValue=toEntry.get()
    selectBE=False
    selectKE=False
    augerTran=False
    coreState=False
    fromAll=False
    fromSome=False
    if fromValue=='' or toValue=='':
        tkinter.messagebox.showinfo(title='ERROR',message='Please input values',parent=root)
    else:
        try:
            fromValue=float(fromValue)
            toValue=float(toValue)
        except:
            tkinter.messagebox.showinfo(title='ERROR',message='Please input valid values',parent=root)
        else:
            if v1.get()==1:
                augerTran=True
            elif v1.get()==2:
                coreState=True
            else:
                tkinter.messagebox.showinfo(title='ERROR',message='Please select Auger Transitions or core state energies',parent=root)
            if augerTran==True or coreState==True:
                if v3.get()==1:
                    fromAll=True
                elif v3.get()==2:                   
                    if len(unique_array)==0:                     
                        tkinter.messagebox.showinfo(title='ERROR',message='Please select elements',parent=root)  
                    else:
                        fromSome=True
                else:
                    tkinter.messagebox.showinfo(title='ERROR',message='Please select from all elements or from some elements',parent=root)
            if augerTran==True and (fromAll==True or fromSome==True):
                if v2.get()==1:
                    selectKE=True
                    selectValue=0
                elif v2.get()==2:
                    if (selectButton.get()=='No selection' and inputEntry.get()=='') or (selectButton.get()!='No selection' and inputEntry.get()!=''):
                        tkinter.messagebox.showinfo(title='ERROR',message='Please input or select',parent=root)
                    elif selectButton.get()!='No selection':
                        selectBE=True
                        if selectButton.get()=='Mg 1253.6(eV)':                              
                            selectValue=1253.6   
                        elif selectButton.get()=='Al 1486.7(eV)':
                            selectValue=1486.7  
                        elif selectButton.get()=='Ag 2984.3(eV)':
                            selectValue=2984.3  
                        elif selectButton.get()=='Cr 5414.9(eV)':
                            selectValue=5414.9 
                        elif selectButton.get()=='Ga 9251.74(eV)':
                            selectValue=9251.74   
                    elif inputEntry.get()!='':
                        try:
                            selectValue=float(inputEntry.get())
                        except:
                            tkinter.messagebox.showinfo(title='ERROR',message='Please input valid values',parent=root)
                        else:
                            selectBE=True
                else:
                    tkinter.messagebox.showinfo(title='ERROR',message='Please select by KE or BE',parent=root)
                    

    
    #if selectBE or selectKE:        
        #rangeGUI(selectBE,selectKE,fromEntry,toEntry,selectValue) 
    if augerTran==True and (fromAll==True or fromSome==True) and (selectBE==True or selectKE==True):
        augerRangeGUI(selectBE,selectKE,fromEntry,toEntry,selectValue,fromAll,fromSome)
        
                        
              
def clickCheckButtonSA(element,elementArray):
    elementArray.append(element)
    elementArray=sorted(elementArray)
    unique_element=np.unique(elementArray)
    resdata = []
    for ii in unique_element:
        resdata.append(elementArray.count(ii))

    new_array=[]
    index=0
    for d in resdata:
        if d%2==0:
            pass
        else:
            new_array.append(unique_element[index])
        index+=1
    global unique_array
    unique_array=new_array            
            
def clickClearButtonRT(root,fromEntry,toEntry,v2,selectButton,orLabel,inputEntry,v1,v3):
    fromEntry.delete(0,'end')
    toEntry.delete(0,'end')
    v1.set(0)
    v2.set(0)
    v3.set(0)
    selectButton.place_forget()
    orLabel.place_forget()
    inputEntry.place_forget()
    
    global unique_array
    
    for element in unique_array:
        clickCheckButtonSA(element,elementArray)
      
    unique_array=[]
    

    
    

def selectRadioButton(v2,root,selectButton,orLabel,inputEntry):
    if v2.get()==2:
        selectButton.place(x=490,y=48.5)
        selectButton['value']=('Mg 1253.6(eV)','Al 1486.7(eV)','Ag 2984.3(eV)','Cr 5414.9(eV)','Ga 9251.74(eV)','No selection')
        selectButton.current(5)
        orLabel.place(x=600,y=48)
        inputEntry.delete(0,'end')
        inputEntry.place(x=620,y=48.5)
    else:
        selectButton.place_forget()
        orLabel.place_forget()
        inputEntry.place_forget()
        

def selectElements(selectAtomButton,v3):
    if v3.get()==2:
        selectAtomButton.place(x=380,y=90)
    else:      
        selectAtomButton.place_forget()

           
def clickClearButtonSA(elementArray,elementCheck):    

    for number in elementCheck:
        elementCheck[number].deselect()
    
    for element in unique_array:
        clickCheckButtonSA(element,elementArray)
    
    
def clickSelectAtomButton(root):
    selectAtomGUI=tkinter.Tk()
    selectAtomGUI.geometry("750x450")
    number_name=getAtom()
    
    elementCheck={}
    global elementArray
    global unique_array
    for number in number_name:
        v=tkinter.IntVar()
        atom_name=number_name[number]
        elementCheck[number]=tkinter.Checkbutton(selectAtomGUI,text='%(number)d %(name)s'%{'number':number,'name':atom_name},variable=v,command=lambda element=number: clickCheckButtonSA(element,elementArray))
        
        if number in unique_array:
            elementCheck[number].select()
        if number>=3 and number<10:   
            elementCheck[number].place(x=20,y=20+(number-3)*40)
        elif number>=10 and number<20:
            elementCheck[number].place(x=80,y=20+(number-10)*40)
        elif number>=20 and number<30:
            elementCheck[number].place(x=150,y=20+(number-20)*40)
        elif number>=30 and number<40:
            elementCheck[number].place(x=220,y=20+(number-30)*40)
        elif number>=40 and number<50:
            elementCheck[number].place(x=290,y=20+(number-40)*40)
        elif number>=50 and number<60:
            elementCheck[number].place(x=360,y=20+(number-50)*40)
        elif number>=60 and number<70:
            elementCheck[number].place(x=430,y=20+(number-60)*40)
        elif number>=70 and number<80:
            elementCheck[number].place(x=500,y=20+(number-70)*40)
        elif number>=80 and number<90:
            elementCheck[number].place(x=570,y=20+(number-80)*40)
        elif number>=90:
            elementCheck[number].place(x=640,y=20+(number-90)*40)

    clearButton=tkinter.Button(selectAtomGUI,text='Clear',command=lambda:clickClearButtonSA(elementArray,elementCheck))
    clearButton.place(x=660,y=250)
    
    
def selectTranCoreButton(v1,keSelect,beSelect,v2):
    v2.set(0)
    if v1.get()==1:
        keSelect.place(x=530,y=1)
        beSelect.place(x=530,y=21.5)
    else:
        keSelect.place_forget()
        beSelect.place_forget()
        
    
 
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

   fromLabel=tkinter.Label(root,text='from')
   fromLabel.place(x=200,y=10)
   fromEntry=tkinter.Entry(root,width=13)
   fromEntry.place(x=240,y=10)
   toLabel=tkinter.Label(root,text='(eV)  to')
   toLabel.place(x=340,y=10)
   toEntry=tkinter.Entry(root,width=13)
   toEntry.place(x=400,y=10)
   unitLabel=tkinter.Label(root,text='(eV)')
   unitLabel.place(x=500,y=10)
   
   
   
   
   
   v1=tkinter.IntVar()
   v2=tkinter.IntVar()
   selectButton=ttk.Combobox(root,width=12)
   orLabel=tkinter.Label(root,text='or')
   inputEntry=tkinter.Entry(root,width=10) 
   keSelect=tkinter.Radiobutton(root,text='by kinetic energies',value=1,variable=v2,command=lambda: selectRadioButton(v2,root,selectButton,orLabel,inputEntry))
   beSelect=tkinter.Radiobutton(root,text='by binding energies',value=2,variable=v2,command=lambda: selectRadioButton(v2,root,selectButton,orLabel,inputEntry))
   transitionSelect=tkinter.Radiobutton(root, text='Auger Transitions',value=1,variable=v1,command=lambda: selectTranCoreButton(v1,keSelect,beSelect,v2))
   transitionSelect.place(x=150,y=40)
   coreStateSelect=tkinter.Radiobutton(root,text='Core State Energies',value=2,variable=v1,command=lambda: selectTranCoreButton(v1,keSelect,beSelect,v2))
   coreStateSelect.place(x=150,y=60.5)
   
   
   sep1 = ttk.Separator(root, orient='vertical')
   sep1.place(relx=0.3, rely=0.05, relheight=0.1, relwidth=0.0005)
   
   v3=tkinter.IntVar()
   allAtomSelect=tkinter.Radiobutton(root, text='From All Elements',value=1,variable=v3,command=lambda: selectElements(selectAtomButton,v3))
   allAtomSelect.place(x=320,y=40)
   selectAtomButton=tkinter.Button(root,text='Select Elements',command=lambda: clickSelectAtomButton(root))
   someAtomSelect=tkinter.Radiobutton(root,text='From Selected Elements',value=2,variable=v3,command=lambda: selectElements(selectAtomButton,v3))
   someAtomSelect.place(x=320,y=60.5)
   

   searchButton=tkinter.Button(root,text='Search',bg='Orange',command=lambda: clickSearchButtonRT(root,fromEntry,toEntry,v2,selectButton,inputEntry,v1,v3))
   searchButton.place(x=685,y=10)
   clearButton=tkinter.Button(root,text='Clear',command=lambda: clickClearButtonRT(root,fromEntry,toEntry,v2,selectButton,orLabel,inputEntry,v1,v3))
   clearButton.place(x=750,y=10)
    

   root.mainloop()
   
   
if __name__ == "__main__":
    
    lastChoice=0
    sortOrder='by_number'

    elementArray=[]
    unique_array=[]



    rootGUI()

