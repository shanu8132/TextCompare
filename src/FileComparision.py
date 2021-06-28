from tkinter import *
import difflib
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import os.path

def get_filepath1():
    
    file1 = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    
    if file1 == "":
        file1 = None
        showinfo("Error", "Please select both the files to compare")
    
    else:
        first_path.set(file1)
        

def get_filepath2():
    
    file2 = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    
    if file2 == "":
        file2 = None
        showinfo("Error", "Please select both the files to compare")
    
    else:
        second_path.set(file2)
        

def diffreport():
    
    if(first_path.get()==""):
        showinfo("Error","Please select both the files to compare")
    elif(second_path.get()==""):
        showinfo("Error","Please select both the files to compare")
    else:
        first_file = first_path.get()
        second_file = second_path.get()
        
        ff = open(first_file,'r').readlines()
        sf = open(second_file,'r').readlines()
    
       
        diff = difflib.HtmlDiff().make_file(ff,sf,first_file, second_file)
    
        #with open('Report.html','w') as f:
        with open(os.path.join(os.path.expanduser('~'),'Documents/Report.html'),'w') as f:
            f.write(diff)
            f.close()
            showinfo("Success", "Check the Report.html file at Documents Folder")
    #print(f"First File = {first_path.get()} Second File = {second_path.get()}")
    
    

def About():
    showinfo("About","Text Compare Software is used to generate the HTML Report of the differences in the content of two files")

def Email():
    showinfo("Email","Contact Me on : shanu8132@gmail.com")

def Github():
    showinfo("Github","github.com/shanu8132")


window = Tk()
#window.configure(bg="#FF8976")
window.geometry("400x270")
window.maxsize(400,255)
window.minsize(400,255)
window.title("Text Compare")
window.wm_iconbitmap("1.ico")

bgImage = PhotoImage(file = "background5.png")
Label(window,image=bgImage).place(relwidth=1,relheight=1)


first_path=StringVar()
second_path = StringVar()

l1 = Label(window,text="First File: ",font="cambria 12 bold",bg="#FF8976")
l1.grid(row=1,column=2,padx=20,pady=20)

f1= Entry(window, textvariable=first_path,bd=4)
f1.grid(row=1,column=3,ipadx=25)

b2 = Button(text="Browse",command=get_filepath1,width=6,font="cambria 10 bold").grid(row=1,column=4,padx=10)

l2 = Label(window,text="Second File: ",font="cambria 12 bold",bg="#FF8976")
l2.grid(row=2,column=2,padx=20,pady=10)

f2 = Entry(window,textvariable=second_path,bd=4)
f2.grid(row=2,column=3,ipadx=25)

b3 = Button(text="Browse",command=get_filepath2,width=6,font="cambria 10 bold").grid(row=2,column=4,padx=10)

b1 = Button(text="Generate Comparision Report",font="cambria 10 bold",command = diffreport).grid(row=7,column=3)

MenuBar = Menu(window)

FileMenu = Menu(MenuBar,tearoff=0)
FileMenu.add_command(label="About",command=About)
FileMenu.add_command(label="Exit",command=exit)
MenuBar.add_cascade(label="Help",menu=FileMenu)

ContactMenu = Menu(MenuBar,tearoff=0)
ContactMenu.add_command(label="Email",command=Email)
ContactMenu.add_command(label="Github",command=Github)
MenuBar.add_cascade(label="Contact",menu=ContactMenu)

window.config(menu=MenuBar)


window.mainloop()