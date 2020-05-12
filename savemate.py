from pytube import YouTube
from tkinter import *
from tkinter import messagebox

class body:
    def __init__(self):
        self.root = Tk()
        self.root.title("SaveMate v1.0.0")
        self.root.geometry("450x240")
        self.root.resizable(False, False)
        self.root.configure(background='#525252')

        try:
            self.root.iconbitmap('savemate.ico')
        except:
            None
        
        self.yt = None

        Label(self.root, text="SaveMate", font=("Segoe", 16), bg='#525252', fg='#ffffff').pack(side = "top")

        self.T = Text(self.root, height=1, width=52, bg='#737373', fg='#ffffff')
        self.T.pack()
        
        self.listbox = Listbox(self.root, width=70, bg='#737373', fg='#ffffff')
        self.listbox.pack()
        
        self.listbox.insert(END, 'Paste a URL into the box above to begin')

        frame = Frame(self.root)
        frame.pack(side=BOTTOM)

        about = Button(self.root, text="About", bg='#525252', fg='#ffffff', command=self.about)
        about.pack(in_=frame, side=LEFT)

        search = Button(self.root, text="Search", bg='#525252', fg='#ffffff', command=self.get)
        search.pack(in_=frame, side=LEFT)

        download = Button(self.root, text="Download", bg='#525252', fg='#ffffff', command=self.save)
        download.pack(in_=frame, side=LEFT)

        clear = Button(self.root, text="Clear", bg='#525252', fg='#ffffff', command=self.clear)
        clear.pack(in_=frame, side=LEFT)

    def about(self):
        messagebox.showinfo(title='about',message='© Xuriun™ 2020 \n Developed by Sam Bennett')

    def clear(self):
            try:
                self.listbox.delete(0,'end')
                self.T.delete(0, END)
            except:
                None
            

    def get(self):
        try:
            try:
                self.listbox.delete(0,'end')
            except:
                None
            self.yt = YouTube(self.T.get("1.0","end-1c"))
            for x in range(len(yt.streams)):
                self.listbox.insert(END, str(yt.streams[x]) + str(x))
        except:
            try:
                self.listbox.delete(0,'end')
            except:
                None
            self.listbox.insert(END, 'An error occured, Link is Invalid')

    def save(self):
        n = int(self.listbox.get(self.listbox.curselection())[-1])
        self.yt.streams[n].download()
        self.listbox.delete(0,'end')
        self.listbox.insert(END, 'Download Complete')
        

    def show(self):
        self.root.mainloop()


try:
    yt = YouTube('https://youtu.be/9bZkp7q19f0')
    body().show()
except:
    messagebox.showerror(title='An Error Occured', message='Could not connect to internet. \nCheck connection and try again.')
