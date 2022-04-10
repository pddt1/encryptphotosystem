from asyncio.windows_events import NULL
from platform import uname
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk,HORIZONTAL
from tkinter.constants import CENTER
from tkinter.font import BOLD
from unittest import result
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory
import threading


frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}


class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)  # this is the background
        main_frame.pack(fill="both", expand="true")
        self.title('Crypto Images System')
        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        title_styles = {"font": ("Trebuchet MS Bold", 12), "background": "blue"}


        frame_login = tk.Frame(main_frame, relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, text="Please enter your account below", bg="blue",fg="white")
        label_title.grid(row=0, column=1, columnspan=1)
        
        label_user = tk.Label(frame_login, text="Username:")
        label_user.grid(row=1, column=0)

        
        label_pw = tk.Label(frame_login,  text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.30)

        signup_btn = ttk.Button(frame_login, text="Register", command=lambda: get_signup())
        signup_btn.place(rely=0.70, relx=0.6)
        frame_login.grid_rowconfigure(1, minsize=40)
        def get_signup():
            SignupPage()

        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            if username=='' or password=='':
                tk.messagebox.showerror("Information","Fill the empty field!!!")
            else:
                # result = backend.login_verify(username, password)
                result=True
                if result==False:
                    tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")
                else:
                    global usname
                    usname=username
                    tk.messagebox.showinfo("Login Successful",
                                       "Welcome {}".format(username))
                    root.deiconify()
                    top.destroy()


class SignupPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.title("Crypto Images System")
        self.geometry("400x350")
        self.resizable(0, 0)

        self.title("Registration")


        
        label_title = tk.Label(main_frame, text="Please enter information of your account below", bg="blue",fg="white")
        label_title.grid(row=0, column=1, columnspan=1)
        label_user = tk.Label(main_frame, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(main_frame, text="Password:")
        label_pw.grid(row=2, column=0)

        label_pw = tk.Label(main_frame, text="Confirm Password:")
        label_pw.grid(row=3, column=0)

        label_rsakey = tk.Label(main_frame, font='BOLD', text="Public Key:")
        label_rsakey.grid(row=4, column=0)

        label_e = tk.Label(main_frame, text="E:")
        label_e.grid(row=5, column=0)

        label_n = tk.Label(main_frame, text="N:")
        label_n.grid(row=6, column=0)

        entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        entry_cfpw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_cfpw.grid(row=3, column=1)

        entry_e = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_e.grid(row=5, column=1)

        entry_n = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_n.grid(row=6, column=1)

        button = ttk.Button(main_frame, text="Register", command=lambda: signup())
        button.grid(row=8, column=1)
        
        col_count, row_count = main_frame.grid_size()
 
        
        for row in range(0,row_count):
           
            main_frame.grid_rowconfigure(row, minsize=30)

        def signup():
            # Creates a text file with the Username and password
            user = entry_user.get()
            pw = entry_pw.get()
            cfpw=entry_cfpw.get()
            e=entry_e.get()
            n=entry_n.get()
            if user=='' or pw=='' or cfpw=='' or e==0 or n==0:
               tk.messagebox.showerror("Fill the empty field!!!")
               
            elif pw != cfpw :
                tk.messagebox.showerror('Confirm password does not match')
            else:
                # result = backend.register_user(user,pw,n,e)
                result=True
                if result==False:
                    tk.messagebox.showerror("Information", "Username existed!!!")
                else:
                    tk.messagebox.showinfo("Information", "Register success")
                    SignupPage.destroy(self)

class MenuBar(tk.Menu):
    'contains 2 page Upload and Storage'
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        #to Switch pages
        self.add_command(label="Upload", command=lambda: parent.show_frame(uploadPage))
        self.add_command(label="Storage", command=lambda: parent.show_frame(storagePage))
        self.add_command(label="Share", command=lambda: parent.show_frame(sharePage))

class MyApp(tk.Tk):
    'to control the frames of apps'
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global top
        top=LoginPage()
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.resizable(0, 0)
        self.geometry("900x600")
        self.frames = {}
        pages = (uploadPage,storagePage,sharePage)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(uploadPage)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name): #show selected page from MenuBar 
        frame = self.frames[name]
        frame.tkraise()

class GUI(tk.Frame):
    'Background for each pages'
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
       
class uploadPage(GUI):  # inherits from the GUI class
    'Upload photo page'
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        frame1 = tk.LabelFrame(self, frame_styles, text="Upload photo")
        frame1.place(rely=0.05, relx=0.02, height=400, width=200)

        frame2 = tk.LabelFrame(self, frame_styles, text="Encrypted Image")
        frame2.place(rely=0.05, relx=0.25, height=400, width=650)

        self.progress = ttk.Progressbar(frame1, orient=HORIZONTAL,length=100,  mode='indeterminate')

        load_bar = tk.Frame(frame1, width=180, height=185)
        load_bar.grid(row=2, column=0, padx=5, pady=5)
        def open_file():
            return NULL
            # try:
            #     file_path = askopenfile(mode='r', filetypes=[('Image Files', '.jpg .png .jpge')])
            # except:
            #     tk.messagebox.showerror("Error", "Some thing wrong when choosing photo.")
            #     return
            # if file_path is None:
            #     return
            # def real_traitement():
            #     self.progress.grid(row=1,column=0)
            #     self.progress.start()
            #     try:
            #         image=Image.open(file_path.name)
            #     except:
            #         tk.messagebox.showerror("Error", "Some thing wrong with your photo.")
            #         return
            #     src_img=image
            #     result,url_image=backend.postImgae(src_img,usname)
            #     if result==False:
            #         tk.messagebox.showerror("Error", "Some thing wrong when uploading photo.")
            #         return
            #     size=(650,400)
            #     print(url_image)
            #     image=Image.open(url_image)
            #     image= image.resize(size,Image.ANTIALIAS)
            
            #     photo=ImageTk.PhotoImage(image)
            #     label= tk.Label(frame2, image=photo)
            #     label.image= photo
            #     label.grid(row=0,column=0, )
            #     self.progress.stop()
            #     self.progress.grid_forget()

            # 'post image'
            # threading.Thread(target=real_traitement).start()
            
        upload_img_btn = tk.Button(frame1, text='Upload Photo', command=lambda:open_file())
        upload_img_btn.grid(row=2, column=0)
        
           
    

class sharePage(GUI):
    'Show list of images from firebase'
    def __init__(self, parent, controller):
        
        GUI.__init__(self, parent)
        
        frame1 = tk.LabelFrame(self, frame_styles, text="Reciver")
        frame1.place(rely=0.05, relx=0.02, height=100, width=300)

        frame2 = tk.LabelFrame(self, frame_styles, text="My images")
        frame2.place(rely=0.05, relx=0.4, height=400, width=500)

        scrollbar = tk.Scrollbar(frame2)
        scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

        mylist = tk.Listbox(frame2,selectmode = "multiple", yscrollcommand = scrollbar.set,width=80 )
        global receiver
        receiver = tk.StringVar()
        tk.Label(frame1, text="Please enter username of receiver", bg="blue",fg="white").pack(side="top")
        re=tk.Entry(frame1, textvariable=receiver)
        tk.Label(frame2, text="Choose the images you want to share", bg="blue",fg="white").pack(side="top",fill = tk.BOTH)
        re.pack(side="top")
        
        share_img=[]
        def callback(event):
            selection = event.widget.curselection()
            if share_img != []:
                share_img.clear()
            for i in selection:
                share_img.append(event.widget.get(i)) 
            
    
        mylist.bind('<<ListboxSelect>>',callback)
        
        def choose_user():
            return NULL
            # global receiver_user,re_N,re_E
            # # Allow user to select a directory and store it in global var
            # receiver_user=receiver.get()
            # isExist,re_N,re_E=backend.getKey(receiver_user)
            # if isExist:
            #     tk.messagebox.showinfo("Successfully", "Then you can share image for receiver "+receiver_user)
            # else:
                
            #     tk.messagebox.showerror("Error", "Recipient does not exist!!!")
            
            
        # tit = tk.Label(frame2,text="Choose the images you want to share",bg='blue',fg='white')
        # #tit.grid(row=2, column=1)
        # tit.pack("bottom")
        

        btn3 = tk.Button(frame1, text='Choose user', command= lambda: choose_user())
        btn3.pack(side="bottom")
        


        def shareimages():
            return NULL

            # USER_INP = tk.simpledialog.askstring(title="Test",prompt="Input your secret key (d):")
            # if USER_INP=='':
            #     tk.messagebox.showerror("Error", "Your private key filed are empty!! Pls input!!")
            # else:
            #     for img in share_img:
                    
            #         isDone=backend.shareImg(img,int(USER_INP),usname,receiver_user)
            #     if(isDone==False):
            #         tk.messagebox.showerror("Error", "Cannot share image to receiver!! ")
            #     else:
            #         tk.messagebox.showinfo("Successfully", "Oh yeah!")
        button3 = tk.Button(frame2,text="Share", command=shareimages)
        button3.pack(side="bottom",fill = tk.BOTH)        

        'functions to refresh list box. When user upload a photo from uploadPage '
        'They need to press Refresh button to update new photo to GUI'   
        
        def LoadList():
            return NULL
            # isOk,files=backend.retriveimages(usname)
            # if(isOk==False):
            #     tk.messagebox.showerror("Error", "Cannot connect to server.")
            # else:
            #     'create a list box with all file get above'
            #     for file in files: 
            #         mylist.insert(tk.END, file[0].split('.',1)[0]) 
        def Refresh_data():
            # Deletes the data in the current listbox and reinserts it.
            mylist.delete(0,tk.END)  
            LoadList()

        button1 = tk.Button(frame2, text="Refresh", command=lambda: Refresh_data())
        button1.pack(side="top")

        mylist.pack( side = tk.LEFT, fill = tk.BOTH )
        scrollbar.config( command = mylist.yview )



class storagePage(GUI):
    'Show list of images from firebase'
    def __init__(self, parent, controller):
        
        GUI.__init__(self, parent)
        
        frame1 = tk.LabelFrame(self, frame_styles, text="List my images")
        frame1.place(rely=0.05, relx=0.02, height=400, width=200)

        frame2 = tk.LabelFrame(self, frame_styles, text="Decrypt")
        frame2.place(rely=0.05, relx=0.25, height=400, width=650)

        scrollbar = tk.Scrollbar(frame1)
        scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

        mylist = tk.Listbox(frame1, yscrollcommand = scrollbar.set,width=40 )
        
        
        global folder_path
        folder_path = tk.StringVar()
        def browse_savebutton():
            # Allow user to select a directory and store it in global var
            filename = tk.filedialog.askdirectory()
            folder_path.set(filename)
            print(folder_path.get())
            print(type(folder_path.get()))
            print(filename)
        tit = tk.Label(frame2,text="Browse a path to save decrypted image:",bg='blue',fg='white')
        tit.grid(row=2, column=1)
        lbl1 = tk.Label(frame2,textvariable=folder_path)
        lbl1.grid(row=2, column=3)
        button3 = tk.Button(frame2,text="Browse", command=browse_savebutton)
        button3.grid(row=2, column=2)

        global decrypted_path
        decrypted_path = tk.StringVar()
        def browse_decryptbutton():
            # Allow user to select a directory and store it in global var
            filename = askopenfile(mode='r', filetypes=[('Numpy Files', '.npy')])
            decrypted_path.set(filename.name)
            print(filename)
        tit1 = tk.Label(frame2,text="Browse a decrypted image file to decrypt:",bg='blue',fg='white')
        tit1.grid(row=4, column=1)
        lbl2 = tk.Label(frame2,textvariable=decrypted_path)
        lbl2.grid(row=4, column=3)
        button2 = tk.Button(frame2,text="Browse", command=browse_decryptbutton)
        button2.grid(row=4, column=2)


        def decryptbutton():
            return NULL
            # if(folder_path.get() == '' or decrypted_path.get() =='' ):
            #     tk.messagebox.showerror("Error", "Your path is empty!! Pls browse!!")
            #     return
            # USER_INP = tk.simpledialog.askstring(title="Test",prompt="Input your secret key (d):")
            # if USER_INP=='':
            #     tk.messagebox.showerror("Error", "Your private key filed are empty!! Pls input!!")
            # else:
                
            #     isDone=backend.decrypt(decrypted_path.get(),folder_path.get(),int(USER_INP),usname)
            #     if(isDone==False):
            #         tk.messagebox.showerror("Error", "Cannot decrypt!! Maybe you input wrong pKey!!")
            #     else:
            #         tk.messagebox.showinfo("Successfully", "Oh yeah!")
                
            
        button2 = tk.Button(frame2,text="Decrypt", command=decryptbutton)
        button2.grid(row=5, column=2)
      
        def callback(event):
            selection = event.widget.curselection()
            index = selection[0]
            data = event.widget.get(index)
    
        mylist.bind('<<ListboxSelect>>',callback)

        'when users press button (btn2). A current image wil be move to a direct path which is selected by user'
        def downloadImage(isAll= False):
            return NULL
            # if isAll==False:
            #     value=str(mylist.get(mylist.curselection()))
            #     # print('s'+value)
            #     # filetype=[('Image Files', '.jpg .png .jpge')]

            #     try:
            #         f=askdirectory()
            #     except:
            #         tk.messagebox.showerror("Error", "Some thing wrong!")
            #         return
            #     if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            #         return
            #     backend.downloadAImage(value,f,usname)
            # else:
            #     f=askdirectory()
            #     backend.downloadAll(f,usname)
            
       
        btn2 = tk.Button(frame1, text='Download Image', command= lambda: downloadImage())
        btn2.pack(side="bottom")
        btn3 = tk.Button(frame1, text='Download All Image', command= lambda: downloadImage(isAll=True))
        btn3.pack(side="bottom")

        'functions to refresh list box. When user upload a photo from uploadPage '
        'They need to press Refresh button to update new photo to GUI'
        def LoadList():
            return NULL
            # isOk,files=backend.retriveimages(usname)
            # if(isOk==False):
            #     tk.messagebox.showerror("Error", "Cannot connect to server.")
            # else:
            #     'create a list box with all file get above'
            #     for file in files: 
            #         mylist.insert(tk.END, file[0].split('.',1)[0]) 
        def Refresh_data():
            # Deletes the data in the current listbox and reinserts it.
            mylist.delete(0,tk.END)  
            LoadList()

        button2 = ttk.Button(frame1, text="Refresh", command=lambda: Refresh_data())
        button2.pack(side="bottom")

        mylist.pack( side = tk.LEFT, fill = tk.BOTH )
        scrollbar.config( command = mylist.yview )


#main
root=MyApp()
root.title("Tkinter App Template")
root.withdraw()
root.mainloop()
