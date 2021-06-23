import pymysql
import tkinter
from tkinter import messagebox 
from tkinter import ttk


db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='atom_shell',
    charset='utf8'
)

#cursor = db.cursor(pymysql.cursors.DictCursor)


def getAtom():
    cursor = db.cursor()
    sql = 'SELECT * FROM atom'
    cursor.execute(sql)
    results = cursor.fetchall()
    #all_number=[]
    #all_name=[]
    number_name=dict()
    for row in results:
        atom_number = row[0]
        atom_name = row[1]
        #all_number.append(atom_number)
        #all_name.append(atom_name)
        number_name[atom_number]=atom_name

    return number_name

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
    #print(number_shell)
    return number_shell

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
        en_o1,en_o2,en_o3,en_o4,en_o5,en_o6=row[17],row[18],row[19],row[20],row[21],row[22]
        en_p1,en_p2,en_p3,en_p4,en_p5=row[23],row[24],row[25],row[26],row[27]
        en_q1=row[28] 
        temp['K']=en_k
        temp['L1'],temp['L2'],temp['L3']=en_l1,en_l2,en_l3
        temp['M1'],temp['M2'],temp['M3'],temp['M4'],temp['M5']=en_m1,en_m2,en_m3,en_m4,en_m5
        temp['N1'],temp['N2'],temp['N3'],temp['N4'],temp['N5'],temp['N6'],temp['N7']=en_n1,en_n2,en_n3,en_n4,en_n5,en_n6,en_n7
        temp['O1'],temp['O2'],temp['O3'],temp['O4'],temp['O5'],temp['O6']=en_o1,en_o2,en_o3,en_o4,en_o5,en_o6
        temp['P1'],temp['P2'],temp['P3'],temp['P4'],temp['P5']=en_p1,en_p2,en_p3,en_p4,en_p5           
        temp['Q1']=en_q1
        number_energies[atom_number]=temp
    #print(number_energies)
    return number_energies
    
    


#def main():
   #atom_number,atom_name=getAtom()
   #number_name=dict()
   #for i in range(len(atom_number)):
       #number_name[atom_number[i]]=atom_name[i]


def calculateAuger(number):
    number_name=getAtom()
    number_shell=getShell()
    number_energies=getEnergies()
    print(number_name[number])
    print(number_shell[number])
    print(number_energies[number])

def commandTable():
    #messagebox.showinfo( "Auger Transitions", "Hello Runoob")
    auger_window=tkinter.Tk()
    auger_window.geometry("1000x680")
    auger_window.title('Auger Transition')
    auger_window.focus_force()
    #table = ttk.Treeview(auger_window)
    table = ttk.Treeview(auger_window,height=1,columns=['1','2'],show='headings')
    table.column('1', width=200) 
    table.column('2', width=100) 
    table.heading('1', text='Auger Transition')
    table.heading('2', text='Auger Energies')
    table.insert('',0,values=('KL1L1',55))
    #table.insert('',1,values=('KL1L1',55))

    table.place(x=10,y=10)
    
    auger_window.mainloop()
    
        

def rootGUI():
   number_name=getAtom()
   root=tkinter.Tk() 
   root.geometry("1000x680")
   root.title('All Atom')
         
   for i in range(91):
       atom_name=number_name[i+3]
       if i<=10:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+i*80, y=10) 
       elif i<=20:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-10)*80, y=70)
       elif i<=30:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-20)*80, y=130)
       elif i<=40:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-30)*80, y=190)
       elif i<=50:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-40)*80, y=250)
       elif i<=60:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-50)*80, y=310)
       elif i<=70:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-60)*80, y=370)
       elif i<=80:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-70)*80, y=430)
       elif i<=90:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-80)*80, y=490)
       elif i<=100:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = commandTable).place(x=50+(i-80)*80, y=550)
             
   root.mainloop()


   
if __name__ == "__main__":
    #number_name=getAtom()
    #number_shell=getShell()
    #number_energies=getEnergies()
    #calculateAuger(3)
    rootGUI()
    
    

    
        
        
    