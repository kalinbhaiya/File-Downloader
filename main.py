import os
from tkinter import *
import time
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import webbrowser as wb

class Downloader:

    def __init__(self, url,path):
        self.url = url
        self.path = path

    def download(self):

        download_link = requests.get(self.url)
        master = Tk()
        master.withdraw()
        with open(self.path, 'wb') as f:
            f.write(download_link.content)

class GUI:

    def __init__(self,master):
        self.master = master
        self.geometry = master.geometry('500x300')
        self.resizable = master.resizable(0,0)
        self.title = master.title('File Downloader')
        self.background = master.config(background='grey16')
        frame = Frame(master, background='red')
        self.label1 = Label(frame, text='Welcome To The File Downloader!', font='cursive 20 bold italic', fg='aqua', bd=0,
                            bg='black')
        self.label1.pack(pady=5, padx=5)
        frame.pack(side=TOP)

        def change_frame_color():
            colors = ['blue', 'green', 'yellow', 'red', 'orange', 'aqua', 'violet', 'purple', 'grey', 'black', 'indigo',
                      'pink']
            color = random.choice(colors)
            frame.config(background=color)
            frame.after(500, change_frame_color)
        change_frame_color()


        self.label2 = Label(master,text='Enter The URL : ',fg='white',bg='grey16',font='cursive 12 bold italic').place(x=40,y=80)
        self.entry1 = Entry(master,width=46,border=3)
        self.entry1.place(x=170,y=81)

        self.label3 = Label(master,text='Download To : ',fg='white',bg='grey16',font='cursive 12 bold italic').place(x=40,y=150)
        self.entry2 = Entry(master,width=46,border=3)
        self.entry2.place(x=170,y=151)
        self.browse = Button(master, text='Browse', bg='orange', fg='white', font='cursive 7 bold', cursor='hand2'
                             , activeforeground='grey', activebackground='black',command=self.browse1)
        self.browse.place(x=412,y=175)
        self.browse.bind('<Enter>',self.enter1)
        self.browse.bind('<Leave>',self.leave1)

        self.download = Button(master, text='DOWNLOAD!', bg='orange', fg='white', font='cursive 10 bold', cursor='hand2'
                            , activeforeground='grey', activebackground='black',command=self.download1)
        self.download.pack(side=BOTTOM,pady=10)
        self.download.bind('<Enter>',self.enter2)
        self.download.bind('<Leave>',self.leave2)

        self.menubar = Menu(master)
        self.menu1 = Menu(self.menubar,tearoff=0)
        self.menu1.add_command(label='Credits',command=self.credits)
        self.menu1.add_command(label='About Author',command=self.about)
        self.menu1.add_command(label='Source Code',command=self.source)
        self.menubar.add_cascade(label='Help',menu=self.menu1)
        self.master.config(menu=self.menubar)
        self.master.protocol('WM_DELETE_WINDOW',self.close)


    def credits(self):
        messagebox.showinfo('File Downloader','File Downloader made by Muhammad Muzammil Alam.')

    def about(self):
        messagebox.showinfo('File Downloader',"Author : \nMuhammad Muzammil Alam\
                                                 Author's E-mail Address : \nmuzammil.alam231@gmail.com\
                                                 Author's Github Profile : \nhttps://github.com/kalinbhaiya\
                                                 Author's Facebook Profile : \nhttps://www.facebook.com/profile.php?id=100052280166322 Author's Instagram Profile : \nhttps://www.instagram.com/m.muzammil1231/")

        wb.open_new_tab('https://github.com/kalinbhaiya')
        wb.open_new_tab('https://www.facebook.com/profile.php?id=100052280166322')
        wb.open_new_tab('https://www.instagram.com/m.muzammil1231/')

    def source(self):
        wb.open_new_tab('https://github.com/kalinbhaiya/File-Downloader/blob/main/main.py')

    def enter1(self,event):
        self.browse.config(bg='aqua',fg='orange',relief=GROOVE)

    def leave1(self,event):
        self.browse.config(bg='orange',fg='white',relief=RAISED)

    def enter2(self,event):
        self.download.config(bg='aqua',fg='orange',relief=GROOVE)

    def leave2(self,event):
        self.download.config(bg='orange',fg='white',relief=RAISED)

    def close(self):
        question = messagebox.askquestion('File Downloader','Do you want to exit?')
        if question == 'yes':
            sys.exit()
        else:
            pass


    def browse1(self):
        path = filedialog.asksaveasfilename()
        self.entry2.delete(0,END)
        self.entry2.insert(0,path)

    def download1(self):
        if self.entry1.get()=='' or self.entry2.get()=='':
            messagebox.showerror('File Downloader','It seems like you have entered invalid URL or invalid File Path!')

        else:
            try:
                file = Downloader(self.entry1.get(),self.entry2.get())
                file.download()
                question = messagebox.askquestion('File Downloader','Your File Has Been Downloaded Successfully! Do you want to open the file right now?')
                if question == 'yes':
                    os.startfile(self.entry2.get())
                else:
                    pass

            except requests.exceptions.ConnectionError:
                messagebox.showerror('File Downloader','Please check your internet connection and try again.')

            except FileNotFoundError:
                messagebox.showerror('File Downloader','Please enter a valid file path.')

            except requests.exceptions.MissingSchema:
                messagebox.showerror('File Downloader','Please enter a valid URL.')

app = Tk()
GUI(app)
app.mainloop()
