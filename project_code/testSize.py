import tkinter

def rootGUI(): 
    number_name=getAtom() #dict
    root=tkinter.Tk() 
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    #root.resizable(0,0)
    print(root.winfo_screenwidth())
    print(root.winfo_screenheight())
    #root.geometry("%dx%d" % (width, height))
    root.geometry("1000x680")
    root.title('All Atom')
    button=tkinter.Button(root,text='test')
    button.place(relx=0.9,rely=0.5)

    root.mainloop()
    
rootGUI()