import tkinter as tk
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog as fd
import os
#------CODE------
version=1.0
class Ptsd:
    pdflist={}
    trueorder=[]
    pdf_writer = PdfFileWriter()

    def readpdf(self):
        filetypes = (
        ('Pdf files', '*.pdf'),
        ('All files', '*.*')
    )
    
        filename = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
        self.listbox.config(state="normal")
        for i in filename:
                self.listbox.insert('end',os.path.basename(i))
                self.pdflist[os.path.basename(i)]=i
        
    def add(self):
        try:
            self.finallist.insert('end',self.listbox.get(self.listbox.curselection()))
            self.trueorder.append(self.pdflist[self.listbox.get(self.listbox.curselection())])
        except:
            pass
    def remove(self):
        try:
            self.trueorder.pop(self.finallist.curselection()[0])
            self.finallist.delete(self.finallist.curselection()[0])
        except:
            pass
    def merge(self):
        folderpath=fd.askdirectory()
        self.filepath=(f"{self.folderpath}/out.pdf")
        for path in self.trueorder:
            pdf_reader = PdfFileReader(path,strict=False)
            for page in range(pdf_reader.getNumPages()):
                # Add each page to the writer object
                self.pdf_writer.addPage(pdf_reader.getPage(page))
        try:
            with open((self.filepath), 'wb') as out:
                self.pdf_writer.write(out)
        except:
            f = open("out.pdft", "x")
            with open((self.filepath), 'wb') as out:
                self.pdf_writer.write(out)
        #merge and save pdf to there
        pass
    def print(self):
        os.system("start file:///"+(self.filepath))
    def quickprint(self):
        pass
#------GUI------
    def __init__(self):
        self.body=tk.Tk()
        self.body.configure(bg=self.colorthemes[0][0])
        mb=tk.Menu(self.body)
        mb.add_cascade(label="Select-Files",command=self.readpdf)
        mb.add_cascade(label="Quick-Print")
        mb.add_cascade(label="Print",command=self.print)
        self.body.config(menu=mb)
        self.body.minsize(500,300)
        self.body.maxsize(900,500)
    #------------------ 
    colorthemes=[
        #swanky
        ["#001f23",
         "#007a75",
         "#5b9489",
         "#fcbe8e",
         "#ff0021"],
        #rustic
        ["#2b4d59",
         "#39998e",
         "#ffdc7c",
         "#ffaa67",
         "#da674a"   
        ]
        
    ]
    #------------------
    def mainwin(self): 
        remove_button=tk.Button(self.body,command=self.remove,text="Remove",bg=self.colorthemes[0][1],activebackground=self.colorthemes[0][2])
        add_button=tk.Button(self.body,text="Add",command=self.add,bg=self.colorthemes[0][1],activebackground=self.colorthemes[0][2])
        self.listbox=tk.Listbox(self.body,background=self.colorthemes[0][2],foreground=self.colorthemes[1][3])
        self.finallist=tk.Listbox(self.body,background=self.colorthemes[0][2],foreground=self.colorthemes[1][3])
        merge_button=tk.Button(self.body,command=self.merge,text="Merge",bg=self.colorthemes[0][1],activebackground=self.colorthemes[0][2])
        # autoprint=tk.Button(self.body,text="Auto-Print",bg=self.colorthemes[0][1],activebackground=self.colorthemes[0][2])
        #----------placements-------------
        remove_button.place(relx=.5,rely=.5,relheight=.10,relwidth=.15,anchor="center")
        add_button.place(relx=.5,rely=.35,relheight=.10,relwidth=.15,anchor="center")
        merge_button.place(relx=.5,rely=.65,relheight=.10,relwidth=.15,anchor="center")
        self.listbox.place(relx=.05,rely=.08,relheight=.80,relwidth=.30,anchor="nw")
        self.finallist.place(relx=.65,rely=.08,relheight=.80,relwidth=.30,anchor="nw")
        # autoprint.place(relx=.55,rely=.89,relheight=.10,relwidth=.15,anchor="nw")
        self.body.mainloop()
        










