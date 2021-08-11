import pymysql
import tkinter
import numpy as np
from tkinter import messagebox 
from tkinter import ttk
from tkinter import Scrollbar
from tkinter.filedialog import askdirectory,askopenfilename
import itertools
import shlex
from decimal import Decimal
import pandas as pd
from tabulate import tabulate
import webbrowser
from matplotlib.figure import Figure
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot as plt
import xlrd



#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#connect database

#get atomic number and atomic name  
def getAtom():
    number_name=dict()
    with open('original data/atom.txt','r') as f: 
        for line in f.readlines():
            curLine=line.strip().split(" ")
            number_name[int(curLine[0])]=curLine[1]
    return number_name
    

#get electron configuration
def getShell():
    number_shell=dict()
    with open('original data/shell.txt','r') as f:
        for line in f.readlines():        
            curLine=line.strip().split(" ")
            curLine=['0' if i=='' else i for i in curLine]         
            if len(curLine)==30:
                pass
            else:
                for i in range(30-len(curLine)):
                    curLine.append('0')
            temp=dict()
            temp['K']=float(curLine[1])
            temp['L1'],temp['L2'],temp['L3']=float(curLine[2]),float(curLine[3]),float(curLine[4])
            temp['M1'],temp['M2'],temp['M3'],temp['M4'],temp['M5']=float(curLine[5]),float(curLine[6]),float(curLine[7]),float(curLine[8]),float(curLine[9])
            temp['N1'],temp['N2'],temp['N3'],temp['N4'],temp['N5'],temp['N6'],temp['N7']=float(curLine[10]),float(curLine[11]),float(curLine[12]),float(curLine[13]),float(curLine[14]),float(curLine[15]),float(curLine[16])
            temp['O1'],temp['O2'],temp['O3'],temp['O4'],temp['O5'],temp['O6'],temp['O7']=float(curLine[17]),float(curLine[18]),float(curLine[19]),float(curLine[20]),float(curLine[21]),float(curLine[22]),float(curLine[23])
            temp['P1'],temp['P2'],temp['P3'],temp['P4'],temp['P5']=float(curLine[24]),float(curLine[25]),float(curLine[26]),float(curLine[27]),float(curLine[28])
            temp['Q1']=float(curLine[29])
            for key in temp:
                if temp[key]==0:
                    temp[key]=None
            number_shell[int(curLine[0])]=temp
    return number_shell  
        
  
#get electrons energies
def getEnergies():  
    number_energies=dict()
    with open('original data/energies.txt','r') as f:      
        for line in f.readlines():        
            curLine=line.strip().split(" ")
            curLine=['0' if i=='' else i for i in curLine]         
            if len(curLine)==30:
                pass
            else:
                for i in range(30-len(curLine)):
                    curLine.append('0')
            temp=dict()
            temp['K']=float(curLine[1])
            temp['L1'],temp['L2'],temp['L3']=float(curLine[2]),float(curLine[3]),float(curLine[4])
            temp['M1'],temp['M2'],temp['M3'],temp['M4'],temp['M5']=float(curLine[5]),float(curLine[6]),float(curLine[7]),float(curLine[8]),float(curLine[9])
            temp['N1'],temp['N2'],temp['N3'],temp['N4'],temp['N5'],temp['N6'],temp['N7']=float(curLine[10]),float(curLine[11]),float(curLine[12]),float(curLine[13]),float(curLine[14]),float(curLine[15]),float(curLine[16])
            temp['O1'],temp['O2'],temp['O3'],temp['O4'],temp['O5'],temp['O6'],temp['O7']=float(curLine[17]),float(curLine[18]),float(curLine[19]),float(curLine[20]),float(curLine[21]),float(curLine[22]),float(curLine[23])
            temp['P1'],temp['P2'],temp['P3'],temp['P4'],temp['P5']=float(curLine[24]),float(curLine[25]),float(curLine[26]),float(curLine[27]),float(curLine[28])
            temp['Q1']=float(curLine[29])
            for key in temp:
                if temp[key]==0:
                    temp[key]=None
            number_energies[int(curLine[0])]=temp
    return number_energies


#get barkla and orbital notation
def getNotation():
    barkla_orbital=dict()
    with open('original data/notation.txt','r') as f:
        for line in f.readlines():
            curLine=line.strip().split(" ")
            barkla_orbital[curLine[0]]=curLine[1]+' '+curLine[2]
    return barkla_orbital


def getRange():
    number_range=dict()
    with open('original data/energies_range.txt','r') as f:
        for line in f.readlines():
            curLine=line.strip().split(" ")
            temp=dict()
            temp['Max']=float(curLine[1])
            temp['Min']=float(curLine[2])
            number_range[int(curLine[0])]=temp
    return number_range
    

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#get cross section data
def getCrossSection(number,photon_energy):
    photon_shell_cross=dict()
    shell_cross=dict()
    with open('Scofield_csv_database/%d.csv'%number,'r') as f:
        f.readline()
        for line in f.readlines():
            if number<=4:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                photon_shell_cross[float(curLine[0])]=temp  
            elif number<=10:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                photon_shell_cross[float(curLine[0])]=temp  
            elif number<=12:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=18:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=20:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['4s1/2']=float(curLine[8])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=30:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=36:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=38:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['5s1/2']=float(curLine[13])
                photon_shell_cross[float(curLine[0])]=temp
            elif number==46:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=48:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['5s1/2']=float(curLine[15])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=54:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['5s1/2']=float(curLine[15])
                temp['5p1/2']=float(curLine[16])
                temp['5p3/2']=float(curLine[17])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=56:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['5s1/2']=float(curLine[15])
                temp['5p1/2']=float(curLine[16])
                temp['5p3/2']=float(curLine[17])
                temp['6s1/2']=float(curLine[18])
                photon_shell_cross[float(curLine[0])]=temp
            elif number==57:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['5s1/2']=float(curLine[15])
                temp['5p1/2']=float(curLine[16])
                temp['5p3/2']=float(curLine[17])
                temp['5d3/2']=float(curLine[18])
                temp['5d5/2']=float(curLine[19])
                temp['6s1/2']=float(curLine[20])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=70 and number!=64:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['4f5/2']=float(curLine[15])
                temp['4f7/2']=float(curLine[16])
                temp['5s1/2']=float(curLine[17])
                temp['5p1/2']=float(curLine[18])
                temp['5p3/2']=float(curLine[19])
                temp['6s1/2']=float(curLine[20])   
                photon_shell_cross[float(curLine[0])]=temp
            elif number==64 or (number<=80 and number!=77):
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['4f5/2']=float(curLine[15])
                temp['4f7/2']=float(curLine[16])
                temp['5s1/2']=float(curLine[17])
                temp['5p1/2']=float(curLine[18])
                temp['5p3/2']=float(curLine[19])
                temp['5d3/2']=float(curLine[20])
                temp['5d5/2']=float(curLine[21])
                temp['6s1/2']=float(curLine[22])
                photon_shell_cross[float(curLine[0])]=temp
            elif number==77:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['4f5/2']=float(curLine[15])
                temp['4f7/2']=float(curLine[16])
                temp['5s1/2']=float(curLine[17])
                temp['5p1/2']=float(curLine[18])
                temp['5p3/2']=float(curLine[19])
                temp['5d3/2']=float(curLine[20])
                temp['5d5/2']=float(curLine[21])
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=86:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['4f5/2']=float(curLine[15])
                temp['4f7/2']=float(curLine[16])
                temp['5s1/2']=float(curLine[17])
                temp['5p1/2']=float(curLine[18])
                temp['5p3/2']=float(curLine[19])
                temp['5d3/2']=float(curLine[20])
                temp['5d5/2']=float(curLine[21])
                temp['6s1/2']=float(curLine[22])
                temp['6p1/2']=float(curLine[23])
                temp['6p3/2']=float(curLine[24])
                photon_shell_cross[float(curLine[0])]=temp
            elif number==87 or number==88:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['4f5/2']=float(curLine[15])
                temp['4f7/2']=float(curLine[16])
                temp['5s1/2']=float(curLine[17])
                temp['5p1/2']=float(curLine[18])
                temp['5p3/2']=float(curLine[19])
                temp['5d3/2']=float(curLine[20])
                temp['5d5/2']=float(curLine[21])
                temp['6s1/2']=float(curLine[22])
                temp['6p1/2']=float(curLine[23])
                temp['6p3/2']=float(curLine[24])
                temp['7s1/2']=float(curLine[25])
                photon_shell_cross[float(curLine[0])]=temp
            elif number==89 or number==90:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['4f5/2']=float(curLine[15])
                temp['4f7/2']=float(curLine[16])
                temp['5s1/2']=float(curLine[17])
                temp['5p1/2']=float(curLine[18])
                temp['5p3/2']=float(curLine[19])
                temp['5d3/2']=float(curLine[20])
                temp['5d5/2']=float(curLine[21])
                temp['6s1/2']=float(curLine[22])
                temp['6p1/2']=float(curLine[23])
                temp['6p3/2']=float(curLine[24])
                temp['6d3/2']=float(curLine[25]) 
                temp['6d5/2']=float(curLine[26])
                temp['7s1/2']=float(curLine[27]) 
                photon_shell_cross[float(curLine[0])]=temp
            elif number<=93:
                curLine=line.strip().split(",")
                temp=dict()
                temp['1s1/2']=float(curLine[1])
                temp['2s1/2']=float(curLine[2])
                temp['2p1/2']=float(curLine[3])
                temp['2p3/2']=float(curLine[4])
                temp['3s1/2']=float(curLine[5])
                temp['3p1/2']=float(curLine[6])
                temp['3p3/2']=float(curLine[7])
                temp['3d3/2']=float(curLine[8])
                temp['3d5/2']=float(curLine[9])
                temp['4s1/2']=float(curLine[10])
                temp['4p1/2']=float(curLine[11])
                temp['4p3/2']=float(curLine[12])
                temp['4d3/2']=float(curLine[13])
                temp['4d5/2']=float(curLine[14])
                temp['4f5/2']=float(curLine[15])
                temp['4f7/2']=float(curLine[16])
                temp['5s1/2']=float(curLine[17])
                temp['5p1/2']=float(curLine[18])
                temp['5p3/2']=float(curLine[19])
                temp['5d3/2']=float(curLine[20])
                temp['5d5/2']=float(curLine[21])
                temp['5f5/2']=float(curLine[22])
                temp['5f7/2']=float(curLine[23])  
                temp['6s1/2']=float(curLine[24])
                temp['6p1/2']=float(curLine[25])
                temp['6p3/2']=float(curLine[26])
                temp['6d3/2']=float(curLine[27]) 
                temp['6d5/2']=float(curLine[28])
                temp['7s1/2']=float(curLine[29])
                photon_shell_cross[float(curLine[0])]=temp
                  
                   
    #print(photon_shell_cross)
    

    if photon_energy in photon_shell_cross:
        shell_cross=photon_shell_cross[photon_energy]
    elif photon_energy>1 and photon_energy<1.5:
        start_cross=photon_shell_cross[1]
        end_cross=photon_shell_cross[1.5]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-1)/(1.5-1))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>1.5 and photon_energy<2:
        start_cross=photon_shell_cross[1.5]
        end_cross=photon_shell_cross[2]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-1.5)/(2-1.5))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>2 and photon_energy<3:
        start_cross=photon_shell_cross[2]
        end_cross=photon_shell_cross[3]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-2)/(3-2))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>3 and photon_energy<4:
        start_cross=photon_shell_cross[3]
        end_cross=photon_shell_cross[4]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-3)/(4-3))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>4 and photon_energy<5:
        start_cross=photon_shell_cross[4]
        end_cross=photon_shell_cross[5]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-4)/(5-4))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>5 and photon_energy<6:
        start_cross=photon_shell_cross[5]
        end_cross=photon_shell_cross[6]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-5)/(6-5))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>6 and photon_energy<8:
        start_cross=photon_shell_cross[6]
        end_cross=photon_shell_cross[8]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-6)/(8-6))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>8 and photon_energy<10:
        start_cross=photon_shell_cross[8]
        end_cross=photon_shell_cross[10]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-8)/(10-8))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>10 and photon_energy<15:
        start_cross=photon_shell_cross[10]
        end_cross=photon_shell_cross[15]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-10)/(15-10))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>15 and photon_energy<20:
        start_cross=photon_shell_cross[15]
        end_cross=photon_shell_cross[20]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-15)/(20-15))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>20 and photon_energy<30:
        start_cross=photon_shell_cross[20]
        end_cross=photon_shell_cross[30]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-20)/(30-20))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>30 and photon_energy<40:
        start_cross=photon_shell_cross[30]
        end_cross=photon_shell_cross[40]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-30)/(40-30))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>40 and photon_energy<50:
        start_cross=photon_shell_cross[40]
        end_cross=photon_shell_cross[50]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-40)/(50-40))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>50 and photon_energy<60:
        start_cross=photon_shell_cross[50]
        end_cross=photon_shell_cross[60]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-50)/(60-50))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>60 and photon_energy<80:
        start_cross=photon_shell_cross[60]
        end_cross=photon_shell_cross[80]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-60)/(80-60))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>80 and photon_energy<100:
        start_cross=photon_shell_cross[80]
        end_cross=photon_shell_cross[100]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-80)/(100-80))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>100 and photon_energy<150:
        start_cross=photon_shell_cross[100]
        end_cross=photon_shell_cross[150]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-100)/(150-100))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>150 and photon_energy<200:
        start_cross=photon_shell_cross[150]
        end_cross=photon_shell_cross[200]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-150)/(200-150))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>200 and photon_energy<300:
        start_cross=photon_shell_cross[200]
        end_cross=photon_shell_cross[300]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-200)/(300-200))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>300 and photon_energy<400:
        start_cross=photon_shell_cross[300]
        end_cross=photon_shell_cross[400]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-300)/(400-300))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>400 and photon_energy<500:
        start_cross=photon_shell_cross[400]
        end_cross=photon_shell_cross[500]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-400)/(500-400))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>500 and photon_energy<600:
        start_cross=photon_shell_cross[500]
        end_cross=photon_shell_cross[600]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-500)/(600-500))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>600 and photon_energy<800:
        start_cross=photon_shell_cross[600]
        end_cross=photon_shell_cross[800]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-600)/(800-600))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>800 and photon_energy<1000:
        start_cross=photon_shell_cross[800]
        end_cross=photon_shell_cross[1000]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-800)/(1000-800))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>1000 and photon_energy<1500:
        start_cross=photon_shell_cross[1000]
        end_cross=photon_shell_cross[1500]
        for shell in start_cross:
            shell_cross[shell]=((photon_energy-1000)/(1500-1000))*(end_cross[shell]-start_cross[shell])+start_cross[shell]
    elif photon_energy>1500:
        start_cross=photon_shell_cross[1000]
        end_cross=photon_shell_cross[1500]
        for shell in start_cross:
            shell_cross[shell]=((end_cross[shell]-start_cross[shell])/(1500-1000))*(photon_energy-1500)+end_cross[shell]
        


    norm_shell_cross=dict()
    for shell in shell_cross:
        norm_shell_cross[shell]=(shell_cross[shell]/max(shell_cross.values()))*100
            
    #print(norm_shell_cross)
    return norm_shell_cross,shell_cross
            

  
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
    number_shell=getShell()
    shell_electrons=number_shell[number]
    #print(shell_electrons)
    
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
    
    mult_array=[]
    for transition in transition_energies:
        temp=shlex.shlex(transition,posix=True)
        temp.whitespace += ','
        temp.whitespace_split = True
        temp=list(temp)

        mult=shell_electrons[temp[0]]*shell_electrons[temp[1]]*shell_electrons[temp[2]]      
        mult=Decimal(mult).quantize(Decimal('0.0000'))
        mult_array.append(mult)
    #print(mult_array)
    max_mult=max(mult_array)
    #print(max_mult)
    
    norm_array=[]
    for mult in mult_array:
        norm=(100*mult)/max_mult
        norm=Decimal(norm).quantize(Decimal('0.0'))
        norm_array.append(norm)
    #print(norm_array)
        
        
        
    return transition_energies,norm_array

def clickPlotForElement(v,selectPlotButton,inputEntry2,auger_window,transition_energies,norm_array,atom_number,nonNone_value,excitationEntry):
    showKineticPlot=False
    showBindingPlot=False
    if v.get()==0:
        tkinter.messagebox.showinfo(title='ERROR',message='Please select binding energies or kinetic energies',parent=auger_window)
    elif v.get()==2:    
        try:
            selectExcitation=float(excitationEntry.get())
        except:
            tkinter.messagebox.showinfo(title='ERROR',message='Please input valid excitation energy',parent=auger_window)
        else:
            showKineticPlot=True
                
        
    elif v.get()==1:
        if (selectPlotButton.get()=='No selection' and inputEntry2.get()=='') or (selectPlotButton.get()!='No selection' and inputEntry2.get()!=''):
            tkinter.messagebox.showinfo(title='ERROR',message='Please input or select',parent=auger_window)
        elif selectPlotButton.get()=='No selection' and inputEntry2.get()!='':
            try:                  
                selectPhoton=float(inputEntry2.get())            
            except:
                tkinter.messagebox.showinfo(title='ERROR',message='Please input valid value',parent=auger_window)
            else:
                showBindingPlot=True
        elif selectPlotButton.get()!='No selection' and inputEntry2.get()=='':
            showBindingPlot=True
            if selectPlotButton.get()=='Mg 1253.6(eV)':           
                selectPhoton=1253.6
            elif selectPlotButton.get()=='Al 1486.7(eV)':
                selectPhoton=1486.7
            elif selectPlotButton.get()=='Ag 2984.3(eV)':
                selectPhoton=2984.3
            elif selectPlotButton.get()=='Cr 5414.9(eV)':
                selectPhoton=5414.9
            elif selectPlotButton.get()=='Ga 9251.74(eV)':
                selectPhoton=9251.74    
    
    
    if showKineticPlot==True:
        if len(transition_energies)<=10:
            fontSize=10
        else:
            fontSize=7
        plot_window=tkinter.Toplevel()
        plot_window.geometry("680x680")
        figure, ax = plt.subplots(1,1)
        x_value=transition_energies.values()
        y_height=norm_array
        y_min=np.zeros(len(norm_array))
        
        plt.vlines(x_value,y_min,y_height)
        index=0
        for key in transition_energies:
            new_key=key.replace(',','')
            plt.text(transition_energies[key],norm_array[index],new_key,size=fontSize)
            index+=1
        
        norm_shell_cross,shell_cross=getCrossSection(atom_number,selectExcitation)        
        kinetic_core=[]
        
        for shell in nonNone_value:
            kinetic_core.append(selectExcitation-nonNone_value[shell])
        
        shell_list=list(norm_shell_cross.keys())
        norm_cross_list=list(norm_shell_cross.values())
        #print(norm_shell_cross)
        #print(nonNone_value)
        #print(kinetic_core)
        
        #barkla_orbital=getNotation()
        core_x_values=[]
        core_y_height=[]
        text=[]
        
        index=0
        for y in kinetic_core:
            if y>0:
                core_x_values.append(y)
                core_y_height.append(norm_cross_list[index])
                text.append(shell_list[index])
            index+=1
        #print(core_x_values)
        #print(core_y_height)
        #print(text)
        core_y_min=np.zeros(len(core_x_values))
        plt.vlines(core_x_values,core_y_min,core_y_height,color='red')
        index=0
        for t in text:
            plt.text(core_x_values[index],core_y_height[index],t)
            index+=1
        
        
        plt.xlabel('Kinetic Energy')
        plt.ylabel('Normalized Intensity')
        plt.close()        
        canvas =FigureCanvasTkAgg(figure, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)
        
        toolbar = NavigationToolbar2Tk(canvas, plot_window)
        toolbar.update()
        canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH,expand=tkinter.YES)

        
        plot_window.mainloop()
    
    elif showBindingPlot==True:
        if len(transition_energies)<=10:
            fontSize=10
        else:
            fontSize=7
        plot_window=tkinter.Toplevel()
        plot_window.geometry("680x680")
        x_value=[]
        y_height=[]
        positive_transitions=[]
        index=0
        for key in transition_energies:
            if (selectPhoton-float(transition_energies[key]))>=0:                
                x_value.append(Decimal(selectPhoton-float(transition_energies[key])).quantize(Decimal('0.00')))
                y_height.append(norm_array[index])
                positive_transitions.append(key)
            index+=1
        
        figure, ax = plt.subplots(1,1)
        y_min=np.zeros(len(x_value))        
        plt.vlines(x_value,y_min,y_height)
        index=0
        for transition in positive_transitions:
            new_transition=transition.replace(',','')
            plt.text(x_value[index],y_height[index],new_transition,size=fontSize)
            index+=1
        
        norm_shell_cross,shell_cross=getCrossSection(atom_number,selectPhoton)
        core_x_values=list(nonNone_value.values())
        core_y_height=list(norm_shell_cross.values())
        core_y_min=np.zeros(len(core_x_values))
        plt.vlines(core_x_values,core_y_min,core_y_height,color='red')
        index=0
        for shell in norm_shell_cross:
            plt.text(core_x_values[index],core_y_height[index],shell)
            index+=1
        
        
        plt.gca().invert_xaxis() 
        plt.xlabel('Binding Energy')
        plt.ylabel('Normalized Intensity')
        plt.close()        
        canvas =FigureCanvasTkAgg(figure, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)
        
        toolbar = NavigationToolbar2Tk(canvas, plot_window)
        toolbar.update()
        canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH,expand=tkinter.YES)

        plot_window.mainloop()
        
        



def selectPlot(auger_window,v,selectPlotButton,orLabel2,inputEntry2,excitationEntry,excitationLabel):   
    if v.get()==1:
        selectPlotButton.place(x=140,y=10)
        orLabel2.place(x=250,y=10)
        inputEntry2.place(x=275,y=10)  
        excitationEntry.place_forget()
        excitationLabel.place_forget()
    else:
        selectPlotButton.place_forget()
        orLabel2.place_forget()
        inputEntry2.place_forget()
        excitationEntry.place(x=150,y=35)
        excitationLabel.place(x=230,y=35)
        
    
#AugerGUI
def augerTransitionGUI(index):
    global lastChoice
    lastChoice=''
   
    atom_number=index+3
    
    #auger window
    #auger_window=tkinter.Tk()
    auger_window=tkinter.Toplevel()
    auger_window.geometry("1200x680")
    number_name=getAtom()
    atom_name=number_name[atom_number]
    auger_window.title('Auger Transitions for %s'%atom_name)
    auger_window.focus_force()
    
    #read from database
    number_energies=getEnergies()
    barkla_orbital=getNotation()
    #number_shell=getShell()
    
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
    core_table.place(x=10,y=60)
    

    #calculate energies and norm mult for transitions
    transition_energies,norm_array=calculateAuger(atom_number)


    #transition table
    if len(transition_energies)<=30:
        table_row=len(transition_energies)
    else:
        table_row=26
    transition_table=ttk.Treeview(auger_window,height=table_row,columns=['1','2','3','4'],show='headings')
    transition_table.column('1', width=150) 
    transition_table.column('2', width=150) 
    transition_table.column('3', width=150) 
    transition_table.column('4', width=150) 
    transition_table.heading('1', text='Auger Transition')
    transition_table.heading('2', text='Auger Energies (KE)')
    transition_table.heading('3', text='Auger Energies (BE)')
    transition_table.heading('4', text='Norm Mult')
    position=0
    

    for t in transition_energies:
        transition_table.insert('',position,iid=position+1,values=(t,transition_energies[t],'',norm_array[position]))
        position+=1
    transition_table.place(x=550,y=120)
    ybar=Scrollbar(transition_table,orient='vertical', command=transition_table.yview,bg='Gray')
    transition_table.configure(yscrollcommand=ybar.set)
    ybar.place(relx=0.95, rely=0.02, relwidth=0.035, relheight=0.958)
    
    
    citationLabel1=tkinter.Label(auger_window,text="*W.A.Coghlan, R.E.Clausing, ")
    citationLabel1.place(x=550,y=5)
    citationLabel2=tkinter.Label(auger_window,text="Auger catalog calculated transition energies listed by energy and element,",font=('Times',10,'italic'))
    citationLabel2.place(x=713,y=6)
    citationLabel3=tkinter.Label(auger_window,text="Atomic Data and Nuclear Data Tables, Volume 5, Issue 4, 1973, Pages 317-469, ISSN 0092-640X,")
    citationLabel3.place(x=550,y=25)
    
   
    linkLabel1 = tkinter.Label(auger_window, text='https://doi.org/10.1016/S0092-640X(73)80005-1', fg='blue',font=('Arial', 10,'italic','underline'))
    linkLabel1.place(x=550, y=46)
 

    def open_url(event):
        webbrowser.open("https://doi.org/10.1016/S0092-640X(73)80005-1", new=0)
       
    linkLabel1.bind("<Button-1>", open_url)
        
    #Add convert function
    selectButton=ttk.Combobox(auger_window)    
    selectButton.place(x=550,y=70)
    selectButton['value']=('Mg 1253.6(eV)','Al 1486.7(eV)','Ag 2984.3(eV)','Cr 5414.9(eV)','Ga 9251.74(eV)','No selection')
    selectButton.current(5)
    
    orLabel=tkinter.Label(auger_window,text='or')
    orLabel.place(x=750,y=70)
    
    inputEntry=tkinter.Entry(auger_window)
    inputEntry.place(x=800,y=70)
    
    unitLabel=tkinter.Label(auger_window,text='(eV)')
    unitLabel.place(x=950,y=70)
    
    lastLabel=tkinter.Label(auger_window,text='Values in table calculated for: %s'%lastChoice)
    lastLabel.place(x=930,y=97)
    
    convertButton=tkinter.Button(auger_window,text='Convert',bg='Orange',command=lambda: clickConvertButtonAT(selectButton,transition_table,position,inputEntry,auger_window,lastLabel))
    convertButton.place(x=1000,y=70)
    
    clearButton=tkinter.Button(auger_window,text='Clear',command=lambda: clickClearButtonAT(inputEntry,selectButton,transition_table,position))
    clearButton.place(x=1065,y=70)
    
    
    exportButton=tkinter.Button(auger_window,text='Export',bg='LightBlue',command=lambda: clickExportButtonAT(auger_window,transition_table,atom_name,position))
    exportButton.place(x=1140,y=70)
    
    selectPlotButton=ttk.Combobox(auger_window,width=12) 
    selectPlotButton['value']=('Mg 1253.6(eV)','Al 1486.7(eV)','Ag 2984.3(eV)','Cr 5414.9(eV)','Ga 9251.74(eV)','No selection')
    selectPlotButton.current(5)
    orLabel2=tkinter.Label(auger_window,text='or')
    inputEntry2=tkinter.Entry(auger_window,width=10)
    
    excitationEntry=tkinter.Entry(auger_window,width=10)
    excitationLabel=tkinter.Label(auger_window,text='hv')

    
    v=tkinter.IntVar()    
    plotBindingButton=tkinter.Radiobutton(auger_window,text='Binding Energies',value=1,variable=v,command=lambda: selectPlot(auger_window,v,selectPlotButton,orLabel2,inputEntry2,excitationEntry,excitationLabel))
    plotBindingButton.place(x=5,y=10)
    plotKineticButton=tkinter.Radiobutton(auger_window,text='Kinetic Energies',value=2,variable=v,command=lambda: selectPlot(auger_window,v,selectPlotButton,orLabel2,inputEntry2,excitationEntry,excitationLabel))
    plotKineticButton.place(x=5,y=30)
    plotButton=tkinter.Button(auger_window,text='Plot',bg='Pink',command=lambda: clickPlotForElement(v,selectPlotButton,inputEntry2,auger_window,transition_energies,norm_array,atom_number,nonNone_value,excitationEntry))
    plotButton.place(x=360,y=10)
    

    auger_window.mainloop()


#----------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------- 
#All about rangeGUI 
def clickExportButtonRG(range_window,table,position,rangeMin,rangeMax,selectKE,selectBE,selectValue,fromAll,fromSome,correctAtom,auger_range,core_state):
    number_name=getAtom()
    reminderBox=tkinter.messagebox.askquestion('Confirmation','Do you want to continue?',parent=range_window)
    rangeMin=str(rangeMin)
    rangeMax=str(rangeMax)
    selectValue=str(selectValue)
    if reminderBox=='yes':
        file_path=askdirectory(parent=range_window)
        if file_path!='':
            if auger_range==True and core_state==False:
                table_header=['Atom','Auger Transition','Auger Energy']
                table_data=[]
                for p in range(position):
                    temp=[]
                    temp.append(table.set(p+1,'#1'))
                    temp.append(table.set(p+1,'#2'))
                    temp.append(table.set(p+1,'#3'))
                    table_data.append(temp)
                if fromAll==True:
                    if selectKE==True:
                        file_path=file_path+'/'+'Auger_transitions_'+'from_'+rangeMin+'_to_'+rangeMax+'_KE_'+sortOrder+'.txt'
                    elif selectBE==True:               
                        file_path=file_path+'/'+'Auger_transitions_'+'from_'+rangeMin+'_to_'+rangeMax+'_BE_'+selectValue+'_'+sortOrder+'.txt'
                    with open(file_path,'w') as f:
                        f.write(tabulate(table_data,headers=table_header))
                elif fromSome==True:                    
                    name_str=''
                    for number in correctAtom:
                        name_str=name_str+number_name[number]
                    if selectKE==True:
                        file_path=file_path+'/'+'Auger_transitions_'+'from_'+rangeMin+'_to_'+rangeMax+'_KE_'+sortOrder+'_'+name_str+'.txt'
                    elif selectBE==True:               
                        file_path=file_path+'/'+'Auger_transitions_'+'from_'+rangeMin+'_to_'+rangeMax+'_BE_'+selectValue+'_'+sortOrder+'_'+name_str+'.txt'
                    with open(file_path,'w') as f:
                        f.write(tabulate(table_data,headers=table_header))
            elif auger_range==False and core_state==True:
                table_header=['Atom','Barkla Notation','Orbital Notation','Binding Energies']
                table_data=[]
                for p in range(position):
                    temp=[]
                    temp.append(table.set(p+1,'#1'))
                    temp.append(table.set(p+1,'#2'))
                    temp.append(table.set(p+1,'#3'))
                    temp.append(table.set(p+1,'#4'))
                    table_data.append(temp)
                if fromAll==True:
                    file_path=file_path+'/'+'Core_State_Energies_'+'from_'+rangeMin+'_to_'+rangeMax+'_'+sortOrder+'.txt'
                elif fromSome==True:
                    name_str=''
                    for number in unique_array:
                        name_str=name_str+number_name[number]
                    file_path=file_path+'/'+'Core_State_Energies_'+'from_'+rangeMin+'_to_'+rangeMax+'_'+sortOrder+'_'+name_str+'.txt'
                with open(file_path,'w') as f:
                    f.write(tabulate(table_data,headers=table_header))
                    
            elif auger_range==True and core_state==True:
                table_header=['Atom','Auger Transition/Notation','Auger Energies/Core State Energies']
                table_data=[]
                for p in range(position):
                    temp=[]
                    temp.append(table.set(p+1,'#1'))
                    temp.append(table.set(p+1,'#2'))
                    temp.append(table.set(p+1,'#3'))
                    table_data.append(temp)
                
                if fromAll==True:
                    if selectKE==True:
                        file_path=file_path+'/'+'Search_Both_'+'from_'+rangeMin+'_to_'+rangeMax+'_KE_'+sortOrder+'.txt'
                    elif selectBE==True:               
                        file_path=file_path+'/'+'Search_Both_'+'from_'+rangeMin+'_to_'+rangeMax+'_BE_'+selectValue+'_'+sortOrder+'.txt'
                    with open(file_path,'w') as f:
                        f.write(tabulate(table_data,headers=table_header))
                elif fromSome==True:                    
                    name_str=''
                    for number in correctAtom:
                        name_str=name_str+number_name[number]
                    if selectKE==True:
                        file_path=file_path+'/'+'Search_Both_'+'from_'+rangeMin+'_to_'+rangeMax+'_KE_'+sortOrder+'_'+name_str+'.txt'
                    elif selectBE==True:               
                        file_path=file_path+'/'+'Search_Both_'+'from_'+rangeMin+'_to_'+rangeMax+'_BE_'+selectValue+'_'+sortOrder+'_'+name_str+'.txt'
                    with open(file_path,'w') as f:
                        f.write(tabulate(table_data,headers=table_header))

        
        else:
            pass
    else:
        pass
    

def clickSortButtonRG(table,position,descending,auger_range,core_state):
    
    global sortOrder
    position_energies=dict()
    
    
    if auger_range==True:
        for p in range(position):
            p+=1
            position_energies[p]=float(table.set(p,'#3'))
          
    elif auger_range==False:
        for p in range(position):
            p+=1
            position_energies[p]=float(table.set(p,'#4'))
    
 
    
    if descending==True: 
        sortOrder='descending'
        sort_position=sorted(position_energies.items(),key=lambda x:x[1],reverse=True)
    else:
        sortOrder='ascending'
        sort_position=sorted(position_energies.items(),key=lambda x:x[1],reverse=False)
    
    
    new_table=[]
    if auger_range==True:        
        for i in sort_position:
            p=i[0]
            temp=[]
            temp.append(table.set(p,'#1'))
            temp.append(table.set(p,'#2'))
            temp.append(table.set(p,'#3'))
            new_table.append(temp)
        
        for p in range(position):
            p+=1              
            table.set(p,'#1',new_table[p-1][0])
            table.set(p,'#2',new_table[p-1][1])
            table.set(p,'#3',new_table[p-1][2])
    elif auger_range==False:
        for i in sort_position:
            p=i[0]
            temp=[]
            temp.append(table.set(p,'#1'))
            temp.append(table.set(p,'#2'))
            temp.append(table.set(p,'#3'))
            temp.append(table.set(p,'#4'))
            new_table.append(temp)
            
        for p in range(position):
            p+=1              
            table.set(p,'#1',new_table[p-1][0])
            table.set(p,'#2',new_table[p-1][1])
            table.set(p,'#3',new_table[p-1][2])
            table.set(p,'#4',new_table[p-1][3])


 

def clickNumberButtonRG(correct_energies,table,position,auger_range,core_state):
    global sortOrder
    barkla_orbital=getNotation()
    sortOrder='by_number'
    new_table=[]

    if auger_range==True:
        for atom_name in correct_energies: 
            current_transitions=correct_energies[atom_name]
            for transition in current_transitions:
                temp=[]
                temp.append(atom_name)
                temp.append(transition)
                temp.append(current_transitions[transition])
                new_table.append(temp)
                
        for p in range(position):
            p+=1
            table.set(p,'#1',new_table[p-1][0])
            table.set(p,'#2',new_table[p-1][1])
            table.set(p,'#3',new_table[p-1][2])
            
            
    elif auger_range==False:
        for atom_name in correct_energies:
            current_energies=correct_energies[atom_name]
            for shell in current_energies:
                temp=[]
                temp.append(atom_name)
                temp.append(shell)
                temp.append(barkla_orbital[shell])
                temp.append(current_energies[shell])
                new_table.append(temp)
        

        for p in range(position):
            p+=1               
            table.set(p,'#1',new_table[p-1][0])
            table.set(p,'#2',new_table[p-1][1])
            table.set(p,'#3',new_table[p-1][2])
            table.set(p,'#4',new_table[p-1][3])



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
    elif fromSome==True:
        correctAtom=unique_array

    all_transitions=dict()  
    transitions_length=0
    for number in correctAtom:        
        temp=dict()
        atom_name=number_name[number]
        current_transitions,norm_array=calculateAuger(number)
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
        
        if transitions_length<=29:
            table_row=transitions_length
        else:
            table_row=29
        
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
    
        descendingButton=tkinter.Button(range_window,text='Descending order (energies)',bg='LightPink',command=lambda: clickSortButtonRG(transition_table,position,descending=True,auger_range=True,core_state=False))
        descendingButton.place(x=900,y=50)
        ascendingButton=tkinter.Button(range_window,text='Ascending order (energies)',bg='LightBlue',command=lambda: clickSortButtonRG(transition_table,position,descending=False,auger_range=True,core_state=False))
        ascendingButton.place(x=900,y=100)
        numberButton=tkinter.Button(range_window,text='Sort by atomic number',bg='LightGreen',command=lambda: clickNumberButtonRG(all_transitions,transition_table,position,auger_range=True,core_state=False))
        numberButton.place(x=900,y=150)
    
        exportButton=tkinter.Button(range_window,text='Export',bg='Yellow',command=lambda: clickExportButtonRG(range_window,transition_table,position,rangeMin,rangeMax,selectKE,selectBE,selectValue,fromAll,fromSome,correctAtom,auger_range=True,core_state=False))
        exportButton.place(x=900,y=300)
        
        citationLabel1=tkinter.Label(range_window,text='*S.T.Perkins, D.E.Cullen, et al.,')
        citationLabel1.place(x=150,y=610)   
        citationLabel2=tkinter.Label(range_window,text='Tables and Graphs of Atomic Subshell and Relaxation Data Derived from the LLNL Evaluated Atomic Data Library (EADL), Z = 1--100, ',font=('Times',10,'italic'))
        citationLabel2.place(x=325,y=611)
        citationLabel3=tkinter.Label(range_window,text='Lawrence Livermore National Laboratory, UCRL-50400, Vol. 30,')
        citationLabel3.place(x=150,y=630)   
        linkLabel1 = tkinter.Label(range_window, text='https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl', fg='blue',font=('Arial', 10,'italic','underline'))
        linkLabel1.place(x=150, y=650)
        def open_url(event):
            webbrowser.open("https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl", new=0)
       
        linkLabel1.bind("<Button-1>", open_url)
    else:
        tkinter.messagebox.showinfo(title='REMINDER',message='No relevant results',parent=range_window)
    
    range_window.mainloop()  


def coreStateGUI(fromEntry,toEntry,fromAll,fromSome):
    range_window=tkinter.Tk()
    range_window.geometry("1200x680")
    
    rangeMin=min(float(fromEntry.get()),float(toEntry.get()))
    rangeMax=max(float(fromEntry.get()),float(toEntry.get()))
    
    number_energies=getEnergies()
    number_name=getAtom()
    barkla_orbital=getNotation()
    
    correct_core=dict()
    core_length=0
    if fromAll==True:
        for number in number_energies:
            temp=number_energies[number]
            temp2=dict()
            for key,value in temp.items():
                if value!=None:                   
                    if value<=rangeMax and value>=rangeMin:                       
                        temp2[key]=value
                        core_length+=1
                             
                else:
                    pass
            
            if temp2!={} and number!=94:
                atom_name=number_name[number]
                correct_core[atom_name]=temp2
    elif fromSome==True:
        for number in unique_array:
            temp=number_energies[number]
            temp2=dict()
            for key,value in temp.items():
                if value!=None:                   
                    if value<=rangeMax and value>=rangeMin:                       
                        temp2[key]=value
                        core_length+=1
                else:
                    pass
            if temp2!={} and number!=94:   
                atom_name=number_name[number]
                correct_core[atom_name]=temp2
    if len(correct_core)!=0:
        if core_length<=29:
            table_row=core_length
        else:
            table_row=29
        
        binding_table=ttk.Treeview(range_window,height=table_row,columns=['1','2','3','4'],show='headings')
        binding_table.column('1',width=100) 
        binding_table.column('2',width=150) 
        binding_table.column('3',width=150) 
        binding_table.column('4',width=160) 
        binding_table.heading('1', text='Atom')
        binding_table.heading('2', text='Barkla Notation')
        binding_table.heading('3', text='Orbital Notation')
        binding_table.heading('4', text='Binding Energies')
        position=0       
        binding_table.pack() 
        for name in correct_core:
            temp=correct_core[name]
            for shell in temp:
                binding_table.insert('',position,iid=position+1,values=(name,shell,barkla_orbital[shell],temp[shell]))
                position+=1
        ybar=Scrollbar(binding_table,orient='vertical', command=binding_table.yview,bg='Gray')
        binding_table.configure(yscrollcommand=ybar.set)
        ybar.place(relx=0.95, rely=0.02, relwidth=0.035, relheight=0.958)    
        
        descendingButton=tkinter.Button(range_window,text='Descending order (energies)',bg='LightPink',command=lambda: clickSortButtonRG(binding_table,position,descending=True,auger_range=False,core_state=True))
        descendingButton.place(x=900,y=50)
        ascendingButton=tkinter.Button(range_window,text='Ascending order (energies)',bg='LightBlue',command=lambda: clickSortButtonRG(binding_table,position,descending=False,auger_range=False,core_state=True))
        ascendingButton.place(x=900,y=100)
        numberButton=tkinter.Button(range_window,text='Sort by atomic number',bg='LightGreen',command=lambda: clickNumberButtonRG(correct_core,binding_table,position,auger_range=False,core_state=True))
        numberButton.place(x=900,y=150)
    
        exportButton=tkinter.Button(range_window,text='Export',bg='Yellow',command=lambda: clickExportButtonRG(range_window,binding_table,position,rangeMin,rangeMax,None,None,None,fromAll,fromSome,None,auger_range=False,core_state=True))
        exportButton.place(x=900,y=300)
        
        citationLabel1=tkinter.Label(range_window,text='*S.T.Perkins, D.E.Cullen, et al.,')
        citationLabel1.place(x=150,y=610)   
        citationLabel2=tkinter.Label(range_window,text='Tables and Graphs of Atomic Subshell and Relaxation Data Derived from the LLNL Evaluated Atomic Data Library (EADL), Z = 1--100, ',font=('Times',10,'italic'))
        citationLabel2.place(x=325,y=611)
        citationLabel3=tkinter.Label(range_window,text='Lawrence Livermore National Laboratory, UCRL-50400, Vol. 30,')
        citationLabel3.place(x=150,y=630)   
        linkLabel1 = tkinter.Label(range_window, text='https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl', fg='blue',font=('Arial', 10,'italic','underline'))
        linkLabel1.place(x=150, y=650)
        def open_url(event):
            webbrowser.open("https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl", new=0)
       
        linkLabel1.bind("<Button-1>", open_url)
    else:
        tkinter.messagebox.showinfo(title='REMINDER',message='No relevant results',parent=range_window)

    
    range_window.mainloop()

def bothSearchGUI(selectBE,selectKE,fromEntry,toEntry,selectValue,fromAll,fromSome):
    range_window=tkinter.Tk()
    range_window.geometry("1200x680")
    
    rangeMin=min(float(fromEntry.get()),float(toEntry.get()))
    rangeMax=max(float(fromEntry.get()),float(toEntry.get()))
    
    number_energies=getEnergies()
    number_name=getAtom()
    barkla_orbital=getNotation()
    number_range=getRange()
    
    correct_core=dict()
    core_length=0
    if fromAll==True:
        for number in number_energies:
            temp=number_energies[number]
            temp2=dict()
            for key,value in temp.items():
                if value!=None:                   
                    if value<=rangeMax and value>=rangeMin:                       
                        temp2[key]=value
                        core_length+=1
                             
                else:
                    pass
            
            if temp2!={} and number!=94:
                atom_name=number_name[number]
                correct_core[atom_name]=temp2
    elif fromSome==True:
        for number in unique_array:
            temp=number_energies[number]
            temp2=dict()
            for key,value in temp.items():
                if value!=None:                   
                    if value<=rangeMax and value>=rangeMin:                       
                        temp2[key]=value
                        core_length+=1
                else:
                    pass
            if temp2!={} and number!=94:   
                atom_name=number_name[number]
                correct_core[atom_name]=temp2

    
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
    elif fromSome==True:
        correctAtom=unique_array

    all_transitions=dict()  
    transitions_length=0
    for number in correctAtom:        
        temp=dict()
        atom_name=number_name[number]
        current_transitions,norm_array=calculateAuger(number)
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
    
    
    table_length=transitions_length+core_length
    
    if table_length>0:        
        if table_length<=29:
            table_row=table_length
        else:
            table_row=29
        
        table=ttk.Treeview(range_window,height=table_row,columns=['1','2','3'],show='headings')
        table.column('1',width=120) 
        table.column('2',width=200) 
        table.column('3',width=250) 
        table.heading('1', text='Atom')
        table.heading('2', text='Auger Transition / Notation')
        table.heading('3', text='Auger Energies / Core State Energies')
        table.pack()
        
        two_tables=dict()
        
       
     
        for number in number_name:
            name=number_name[number]
            if name in correct_core.keys() and name in all_transitions.keys():
                temp1=correct_core[name]
                temp2=all_transitions[name]
                temp3=dict()
                for key1 in temp1:
                    temp3[key1]=temp1[key1]
                for key2 in temp2:
                    temp3[key2]=temp2[key2]
                two_tables[name]=temp3
            elif name in correct_core.keys():
                two_tables[name]=correct_core[name]
            elif name in all_transitions.keys():
                two_tables[name]=all_transitions[name]
                
        
        position=0
        for atom_name in two_tables:
            current_transitions=two_tables[atom_name]
            for t in current_transitions:            
                table.insert('',position,iid=position+1,values=(atom_name,t,current_transitions[t]))
                position+=1
    

        

        ybar2=Scrollbar(table,orient='vertical', command=table.yview,bg='Gray')
        table.configure(yscrollcommand=ybar2.set)
        ybar2.place(relx=0.95, rely=0.02, relwidth=0.035, relheight=0.958)
        
    
    
    descendingButton=tkinter.Button(range_window,text='Descending order (energies)',bg='LightPink',command=lambda: clickSortButtonRG(table,position,descending=True,auger_range=True,core_state=True))
    descendingButton.place(x=900,y=50)
    ascendingButton=tkinter.Button(range_window,text='Ascending order (energies)',bg='LightBlue',command=lambda: clickSortButtonRG(table,position,descending=False,auger_range=True,core_state=True))
    ascendingButton.place(x=900,y=100)
    numberButton=tkinter.Button(range_window,text='Sort by atomic number',bg='LightGreen',command=lambda: clickNumberButtonRG(two_tables,table,position,auger_range=True,core_state=True))
    numberButton.place(x=900,y=150)
    
    exportButton=tkinter.Button(range_window,text='Export',bg='Yellow',command=lambda: clickExportButtonRG(range_window,table,position,rangeMin,rangeMax,selectKE,selectBE,selectValue,fromAll,fromSome,correctAtom,auger_range=True,core_state=True))
    exportButton.place(x=900,y=300)
    
    
    citationLabel1=tkinter.Label(range_window,text='*S.T.Perkins, D.E.Cullen, et al.,')
    citationLabel1.place(x=150,y=610)   
    citationLabel2=tkinter.Label(range_window,text='Tables and Graphs of Atomic Subshell and Relaxation Data Derived from the LLNL Evaluated Atomic Data Library (EADL), Z = 1--100, ',font=('Times',10,'italic'))
    citationLabel2.place(x=325,y=611)
    citationLabel3=tkinter.Label(range_window,text='Lawrence Livermore National Laboratory, UCRL-50400, Vol. 30,')
    citationLabel3.place(x=150,y=630)   
    linkLabel1 = tkinter.Label(range_window, text='https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl', fg='blue',font=('Arial', 10,'italic','underline'))
    linkLabel1.place(x=150, y=650)
    def open_url(event):
        webbrowser.open("https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl", new=0)
       
    linkLabel1.bind("<Button-1>", open_url)
    
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
    bothSearch=False
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
            elif v1.get()==3:
                bothSearch=True
            else:
                tkinter.messagebox.showinfo(title='ERROR',message='Please select Auger Transitions or core state energies',parent=root)
            if augerTran==True or coreState==True or bothSearch==True:
                if v3.get()==1:
                    fromAll=True
                elif v3.get()==2:                   
                    if len(unique_array)==0:                     
                        tkinter.messagebox.showinfo(title='ERROR',message='Please select elements',parent=root)  
                    else:
                        fromSome=True
                else:
                    tkinter.messagebox.showinfo(title='ERROR',message='Please select from all elements or from some elements',parent=root)
            if (augerTran==True or bothSearch==True) and (fromAll==True or fromSome==True):
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

    if augerTran==True and (fromAll==True or fromSome==True) and (selectBE==True or selectKE==True):
        augerRangeGUI(selectBE,selectKE,fromEntry,toEntry,selectValue,fromAll,fromSome)
    elif coreState==True and (fromAll==True or fromSome==True):
        coreStateGUI(fromEntry,toEntry,fromAll,fromSome)
    elif bothSearch==True and (fromAll==True or fromSome==True) and (selectBE==True or selectKE==True):
        bothSearchGUI(selectBE,selectKE,fromEntry,toEntry,selectValue,fromAll,fromSome)
        
                        
              
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
     
def clickCheckButtonSA2(element,elementArray2):
    elementArray2.append(element)
    elementArray2=sorted(elementArray2)
    unique_element=np.unique(elementArray2)
    resdata = []
    for ii in unique_element:
        resdata.append(elementArray2.count(ii))

    new_array=[]
    index=0
    for d in resdata:
        if d%2==0:
            pass
        else:
            new_array.append(unique_element[index])
        index+=1
    global unique_array2
    unique_array2=new_array    
            
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
        selectButton.place(relx=490/1000,rely=48.5/680)
        selectButton['value']=('Mg 1253.6(eV)','Al 1486.7(eV)','Ag 2984.3(eV)','Cr 5414.9(eV)','Ga 9251.74(eV)','No selection')
        selectButton.current(5)
        orLabel.place(relx=600/1000,rely=48/680)
        inputEntry.delete(0,'end')
        inputEntry.place(relx=620/1000,rely=48.5/680)
    else:
        selectButton.place_forget()
        orLabel.place_forget()
        inputEntry.place_forget()
        

def selectElements(selectAtomButton,v3):
    if v3.get()==2:
        selectAtomButton.place(relx=380/1000,rely=90/680)
    else:      
        selectAtomButton.place_forget()

           
def clickClearButtonSA(elementArray,elementCheck):    

    for number in elementCheck:
        elementCheck[number].deselect()
    
    for element in unique_array:
        clickCheckButtonSA(element,elementArray)

def clickClearButtonSA2(elementArray2,elementCheck):    

    for number in elementCheck:
        elementCheck[number].deselect()
    
    for element in unique_array2:
        clickCheckButtonSA2(element,elementArray2)    
    
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
    if v1.get()==1 or v1.get()==3:
        keSelect.place(relx=530/1000,rely=1/680)
        beSelect.place(relx=530/1000,rely=21.5/680)
    else:
        keSelect.place_forget()
        beSelect.place_forget()
        
    
def clickImportButtonRT(root,showPathText):
    global import_file_path
    import_file_path=askopenfilename(parent=root)
    showPathText.config(state='normal')
    showPathText.insert(0,import_file_path)
    showPathText.config(state='readonly')

def clickClearPathButton(showPathText,selectPhotonButton,v_plot):
    showPathText.config(state='normal')
    showPathText.delete(0, 'end')
    showPathText.config(state='readonly')
    selectPhotonButton.set('')
    global unique_array2
    
    for element in unique_array2:
        clickCheckButtonSA2(element,elementArray2)
      
    unique_array2=[]
    v_plot.set(0)
    

    
    
def clickPlotButtonRT(import_file_path,root,showPathText,selectPhotonButton,v_plot):
    
    if showPathText.get()=='':
        tkinter.messagebox.showinfo(title='ERROR',message='Please import file',parent=root)
    elif selectPhotonButton.get()=='':
        tkinter.messagebox.showinfo(title='ERROR',message='Please select photon energy',parent=root)
    elif len(unique_array2)==0:
        tkinter.messagebox.showinfo(title='ERROR',message='Please select element',parent=root)
    elif v_plot.get()==0:
        tkinter.messagebox.showinfo(title='ERROR',message='Please select range of x axis',parent=root)
    else:
        

        number_energies=getEnergies()
        number_name=getAtom()
        selectPhoton=float(selectPhotonButton.get())
        bindingData=[]
        intensityData=[]
        normal_intensity_data=[]
        with open(import_file_path,'r') as f:            
            for line in f.readlines():
                curLine=line.strip().split(" ")
                bindingData.append(float(curLine[0]))
                intensityData.append(float(curLine[1]))

        
        for intensity in intensityData:
            normal_intensity_data.append((intensity/max(intensityData))*100)
        plotGUI=tkinter.Toplevel()
        plotGUI.geometry('680x680')
        
    
        figure,ax=plt.subplots(1,1)
        
        max_cross_sections=[]
        for number in unique_array2:
            norm_shell_cross,shell_cross=getCrossSection(number,selectPhoton)
            max_cross_sections.append(max(shell_cross.values()))

        max_value=max(max_cross_sections)

        
          
        plt_color=['red','green','yellow','purple','c',
                   'lightcoral','olivedrab','darkorange','mediumorchid','aquamarine',
                   'indianred','greenyellow','orange','thistle','turquoise',
                   'brown','chartreuse','antiquewhite','plum','lightseagreen',
                   'firebrick','lawngreen','tan','violet','mediumturquoise',
                   'maroon','b','navajowhite','darkmagenta','lightcyan',
                   'darkred','indigo','blanchedalmond','m','paleturquoise',
                   'r','lavender','moccasin','fuchsia','darkslategray',
                   'salmon','honeydew','burlywood','orchid','teal',
                   'tomato','darkseagreen','wheat','mediumvioletred','cyan',
                   'coral','palegreen','darkgoldenrod','deeppink','cadetblue',
                   'orangered','lightgreen','goldenrod','hotpink','powderblue',
                   'lightsalmon','forestgreen','gold','palevioletred','lightblue',
                   'sienna','limegreen','khaki','crimson','deepskyblue',
                   'chocolate','darkgreen','darkkhaki','pink','skyblue',
                   'sandybrown','g','olive','lightpink','steelblue',
                   'peru','lime','y','darkviolet','aliceblue',
                   'black','seagreen','springgreen','mediumspringgreen','royalblue',
                   'grey']
        color_index=0
        for number in unique_array2:
            norm_shell_cross,shell_cross=getCrossSection(number,selectPhoton)
            current_energies=number_energies[number]
            nonNone_value=dict()
            for shell in current_energies:
                if current_energies[shell]!=None:
                    nonNone_value[shell]=current_energies[shell]
                    
            norm_cross_section=dict()
            for shell in shell_cross:
                norm_cross_section[shell]=(shell_cross[shell]/max_value)*100
 
                                  
            core_x_values=list(nonNone_value.values())
            core_y_height=list(norm_cross_section.values())
            core_y_min=np.zeros(len(core_x_values))
            plt.vlines(core_x_values,core_y_min,core_y_height,color=plt_color[color_index])
            index=0
            for shell in norm_shell_cross:
                plt.text(core_x_values[index],core_y_height[index],number_name[number]+''+shell)
                index+=1
            
            
            transition_energies,norm_array=calculateAuger(number)
            
            auger_values=[]
            norm_mults=[]
            shell_text=[]
            index=0
            for shell in transition_energies:
                auger_values.append(selectPhoton-float(transition_energies[shell]))
                norm_mults.append(norm_array[index])
                shell=shell.replace(',','')
                shell_text.append(shell)
                index+=1
            
            
            auger_x_values=[]
            auger_y_height=[]
            auger_shell_text=[]
            index=0
            for value in auger_values:
                if value>0:
                    auger_x_values.append(value)
                    auger_y_height.append(norm_mults[index])
                    auger_shell_text.append(shell_text[index])
                index+=1
            auger_y_min=np.zeros(len(auger_y_height))
            plt.vlines(auger_x_values,auger_y_min,auger_y_height,color=plt_color[color_index])

            index=0
            for t in auger_shell_text:
                plt.text(auger_x_values[index],auger_y_height[index],number_name[number]+t)
                index+=1
            color_index+=1
            


        plt.plot(bindingData,normal_intensity_data)
        
        plt.gca().invert_xaxis() 
        if v_plot.get()==2:
            plt.xlim([1000,0])
        
        plt.xlabel('Binding Energy')
        plt.ylabel('Normalized Intensity')
        plt.close()        
        canvas =FigureCanvasTkAgg(figure, master=plotGUI)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)
        
        toolbar = NavigationToolbar2Tk(canvas, plotGUI)
        toolbar.update()
        canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH,expand=tkinter.YES)
        plotGUI.mainloop()


        

        
        
def clickSelectElementButton(root):
    selectAtomGUI=tkinter.Tk()
    selectAtomGUI.geometry("750x450")
    
    number_name=getAtom()
    
    elementCheck={}
    global unique_array2
    global elementArray2
    for number in number_name:
        v=tkinter.IntVar()
        atom_name=number_name[number]
        elementCheck[number]=tkinter.Checkbutton(selectAtomGUI,text='%(number)d %(name)s'%{'number':number,'name':atom_name},variable=v,command=lambda element=number: clickCheckButtonSA2(element,elementArray2))
        
        if number in unique_array2:
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
            
    clearButton=tkinter.Button(selectAtomGUI,text='Clear',command=lambda:clickClearButtonSA2(elementArray2,elementCheck))
    clearButton.place(x=660,y=250)
    
        
     
        
 
#rootGUI
def rootGUI():    
   number_name=getAtom() #dict
   root=tkinter.Tk() 
   #screen_width=root.winfo_screenwidth()
   #screen_height=root.winfo_screenheight()
   root.geometry("1000x680")
   #root.geometry("%dx%d" % (screen_width, screen_height))
   #root.resizable(0,0)
   root.title('All Atom')
   tkinter.Button(root,text='1 H',width=5,height=2,bg='Gray').place(relx=30/1000,rely=10/680) #1
   tkinter.Button(root,text='2 He',width=5,height=2,bg='Gray').place(relx=880/1000,rely=10/680) #18
   uncover_atom=dict()
   uncover_atom[94],uncover_atom[95],uncover_atom[96],uncover_atom[97],uncover_atom[98],uncover_atom[99],uncover_atom[100],uncover_atom[101],uncover_atom[102]='Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No'
   uncover_atom[103],uncover_atom[104],uncover_atom[105],uncover_atom[106],uncover_atom[107]='Lr','Rf','Db','Sg','Bh'
   uncover_atom[108],uncover_atom[109],uncover_atom[110],uncover_atom[111],uncover_atom[112]='Hs','Mt','Ds','Rg','Cn'
   uncover_atom[113],uncover_atom[114],uncover_atom[115],uncover_atom[116],uncover_atom[117],uncover_atom[118]='Nh','Fl','Mc','Lv','Ts','Og'
   for i in range(25):
       if i<=8:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+94,'name':uncover_atom[i+94]},width=5,height=2,bg='Gray').place(relx=(380+i*50)/1000, rely=520/680)
       else:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+94,'name':uncover_atom[i+94]},width=5,height=2,bg='Gray').place(relx=(130+(i-9)*50)/1000, rely=370/680)  
         
   for i in range(91):
       atom_name=number_name[i+3]
       if i==0 or i==1:     
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(relx=(30+i*50)/1000, rely=70/680)
       elif i<=7:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(relx=(630+(i-2)*50)/1000, rely=70/680)
       elif i==8 or i==9:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(relx=(30+(i-8)*50)/1000, rely=130/680)
       elif i<=15:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(relx=(630+(i-10)*50)/1000, rely=130/680)
       elif i==16 or i==17:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(relx=(30+(i-16)*50)/1000, rely=190/680)
       elif i<=27:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='PowderBlue').place(relx=(30+(i-16)*50)/1000, rely=190/680)
       elif i<=33:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(relx=(30+(i-16)*50)/1000, rely=190/680)
       elif i==34 or i==35:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(relx=(30+(i-34)*50)/1000, rely=250/680)
       elif i<=45:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='PowderBlue').place(relx=(30+(i-34)*50)/1000, rely=250/680)
       elif i<=51:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(relx=(30+(i-34)*50)/1000, rely=250/680)
       elif i==52 or i==53:
           tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(relx=(30+(i-52)*50)/1000, rely=310/680)
       elif i>=54 and i<=67:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='LightGreen').place(relx=(30+(i-52)*50)/1000, rely=460/680)
       elif i<=77:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='PowderBlue').place(relx=(130+(i-68)*50)/1000, rely=310/680)
       elif i<=83:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Yellow').place(relx=(130+(i-68)*50)/1000, rely=310/680)
       elif i==84 or i==85:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='Salmon').place(relx=(30+(i-84)*50)/1000, rely=370/680)
       else:
          tkinter.Button(root,text='%(number)d %(name)s'%{'number':i+3,'name':atom_name},command = lambda text=i: augerTransitionGUI(text),width=5,height=2,bg='LightGreen').place(relx=(30+(i-84)*50)/1000, rely=520/680)

   fromLabel=tkinter.Label(root,text='from')
   fromLabel.place(relx=200/1000,rely=10/680)
   fromEntry=tkinter.Entry(root,width=13)
   fromEntry.place(relx=240/1000,rely=10/680)
   toLabel=tkinter.Label(root,text='(eV)  to')
   toLabel.place(relx=340/1000,rely=10/680)
   toEntry=tkinter.Entry(root,width=13)
   toEntry.place(relx=400/1000,rely=10/680)
   unitLabel=tkinter.Label(root,text='(eV)')
   unitLabel.place(relx=500/1000,rely=10/680)
   

   v1=tkinter.IntVar()
   v2=tkinter.IntVar()
   selectButton=ttk.Combobox(root,width=12)
   orLabel=tkinter.Label(root,text='or')
   inputEntry=tkinter.Entry(root,width=10) 
   keSelect=tkinter.Radiobutton(root,text='by kinetic energies',value=1,variable=v2,command=lambda: selectRadioButton(v2,root,selectButton,orLabel,inputEntry))
   beSelect=tkinter.Radiobutton(root,text='by binding energies',value=2,variable=v2,command=lambda: selectRadioButton(v2,root,selectButton,orLabel,inputEntry))
   transitionSelect=tkinter.Radiobutton(root, text='Auger Transitions',value=1,variable=v1,command=lambda: selectTranCoreButton(v1,keSelect,beSelect,v2))
   transitionSelect.place(relx=150/1000,rely=40/680)
   coreStateSelect=tkinter.Radiobutton(root,text='Core State Energies',value=2,variable=v1,command=lambda: selectTranCoreButton(v1,keSelect,beSelect,v2))
   coreStateSelect.place(relx=150/1000,rely=60.5/680)
   bothSelect=tkinter.Radiobutton(root,text='Both',value=3,variable=v1,command=lambda: selectTranCoreButton(v1,keSelect,beSelect,v2))
   bothSelect.place(relx=150/1000,rely=81/680)
   
   
   sep1 = ttk.Separator(root, orient='vertical')
   sep1.place(relx=0.3, rely=0.05, relheight=0.1, relwidth=0.0005)
   
   v3=tkinter.IntVar()
   allAtomSelect=tkinter.Radiobutton(root, text='From All Elements',value=1,variable=v3,command=lambda: selectElements(selectAtomButton,v3))
   allAtomSelect.place(relx=320/1000,rely=40/680)
   selectAtomButton=tkinter.Button(root,text='Select Elements',command=lambda: clickSelectAtomButton(root))
   someAtomSelect=tkinter.Radiobutton(root,text='From Selected Elements',value=2,variable=v3,command=lambda: selectElements(selectAtomButton,v3))
   someAtomSelect.place(relx=320/1000,rely=60.5/680)
   

   searchButton=tkinter.Button(root,text='Search',bg='Orange',command=lambda: clickSearchButtonRT(root,fromEntry,toEntry,v2,selectButton,inputEntry,v1,v3))
   searchButton.place(relx=685/1000,rely=10/680)
   clearButton=tkinter.Button(root,text='Clear',command=lambda: clickClearButtonRT(root,fromEntry,toEntry,v2,selectButton,orLabel,inputEntry,v1,v3))
   clearButton.place(relx=750/1000,rely=10/680)
   
   citationLabel1=tkinter.Label(root,text='*S.T.Perkins, D.E.Cullen, et al.,')
   citationLabel1.place(relx=150/1000,rely=590/680)
   
   citationLabel2=tkinter.Label(root,text='Tables and Graphs of Atomic Subshell and Relaxation Data Derived from the LLNL Evaluated',font=('Times',10,'italic'))
   citationLabel2.place(relx=325/1000,rely=591/680)
   
   citationLabel3=tkinter.Label(root,text='Atomic Data Library (EADL), Z = 1--100,',font=('Times',10,'italic'))
   citationLabel3.place(relx=150/1000,rely=610/680)
   
   citationLabel4=tkinter.Label(root,text='Lawrence Livermore National Laboratory, UCRL-50400, Vol. 30,')
   citationLabel4.place(relx=377/1000,rely=610/680)
   
   linkLabel1 = tkinter.Label(root, text='https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl', fg='blue',font=('Arial', 10,'italic','underline'))
   linkLabel1.place(relx=150/1000, rely=630/680)
 

   def open_url(event):
       webbrowser.open("https://www.osti.gov/biblio/10121422-tables-graphs-atomic-subshell-relaxation-data-derived-from-llnl-evaluated-atomic-data-library-eadl", new=0)
       
   linkLabel1.bind("<Button-1>", open_url)
   
   
   showPathText=tkinter.Entry(root,state='readonly')
   showPathText.place(relx=140/1000,rely=160/680)
   
   importButton=tkinter.Button(root,text='Import File (.txt or .csv)',bg='Pink',command=lambda: clickImportButtonRT(root,showPathText))
   importButton.place(relx=140/1000,rely=120/680)
   
   selectPhotonButton=ttk.Combobox(root,width=10)
   selectPhotonButton['value']=[1,1.5,2,3,4,5,6,8,10,15]
   selectPhotonButton.place(relx=295/1000,rely=125/680)
   
   selectElementButton=tkinter.Button(root,text='Select Elements',command=lambda: clickSelectElementButton(root))
   selectElementButton.place(relx=295/1000,rely=155/680)
   
   rangeLabel=tkinter.Label(root,text='Please select range of x axis:')
   rangeLabel.place(relx=380/1000,rely=100/680)
   
   v_plot=tkinter.IntVar()
   selectReferenceButton=tkinter.Radiobutton(root,text='Range of Reference Lines',variable=v_plot,value=1)
   selectReferenceButton.place(relx=400/1000,rely=125/680)
   
   selectDataButton=tkinter.Radiobutton(root,text='Range of Dataset',variable=v_plot,value=2)
   selectDataButton.place(relx=400/1000,rely=155/680)
   

   plotButton=tkinter.Button(root,text='Plot',bg='Gold',width=5,command=lambda: clickPlotButtonRT(import_file_path,root,showPathText,selectPhotonButton,v_plot))
   plotButton.place(relx=565/1000,rely=100/680)

   clearPathButton=tkinter.Button(root,text='Clear',width=5,command=lambda: clickClearPathButton(showPathText,selectPhotonButton,v_plot))
   clearPathButton.place(relx=565/1000,rely=155/680)

   
 

   
   

    

   root.mainloop()
   
   
if __name__ == "__main__":
    
    lastChoice=0
    sortOrder='by_number'

    elementArray=[]
    unique_array=[]
    elementArray2=[]
    unique_array2=[]
    
    import_file_path=''



    rootGUI()

