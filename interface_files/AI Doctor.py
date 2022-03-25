import tkinter as tk
from tkinter import messagebox,PhotoImage
from PIL import Image, ImageTk

from Ecg_Analizer import ECG

name=0
phone=0
speed=0
age=0
sex=0
medicine=0







class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        topframe=tk.Frame(self,height=500,width=900,bg='white',bd=5)
        topframe.pack()
        image1 = Image.open(r'C:\Users\DIPRAJYOTI MAJUMDAR\Desktop\AI embedded doctor\interface_files\logo.jfif')
        image1 = image1.resize((300,300),Image.ANTIALIAS)

        test = ImageTk.PhotoImage(image1)
        label1=tk.Label(topframe,image=test)
        label1.image=test
        label1.place(x=258,y=56)



        L1 = tk.Label(topframe, text="DOCTOR  AI  IS  HERE  FOR  YOU", font=("Comic Sans MS",15,'bold'), fg='blue',bg='white')
        L1.place(x=220, y=20)


        self.photobtn = PhotoImage(file='Enterbutton.png')
        button = tk.Button(topframe, image=self.photobtn,bg='white',borderwidth=0, command=lambda: controller.show_frame(SecondPage))
        button.place(x=300, y=400)




class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.back = PhotoImage(file='back.png')



        Mainframe = tk.LabelFrame(self,text="Checkup & Predictions",font=("Raleway",10,'italic'),bg='light blue',bd=5)
        Mainframe.pack(side='top',fill='both',expand=True)
        load = Image.open(r'1689578.png')
        load= load.resize((774,500),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(Mainframe, image=photo)
        label.image=photo
        label.place(x=6,y=8)

        l2= tk.Label(Mainframe,text='LIVE ARRHYTHMIA DETECTOR :',font=('Times New Roman',15,'bold'),bg='light blue')
        l2.pack()



        B1 =  tk.Button(Mainframe,text='Patient Details',font=('Times New Roman',15,'bold'),bg='Indian Red1',command=lambda: controller.show_frame(ThirdPage))
        B1.place(x=150,y=250)
        def on_enter(e):
            B1.config(background='coral1',foreground='white')
        def on_leave(e):
            B1.config(background='Indian Red1',foreground='black')
        B1.bind('<Enter>' , on_enter)
        B1.bind('<Leave>', on_leave)

        B2 =  tk.Button(Mainframe,text='ECG TEST',font=('Times New Roman',15,'bold'),bg='floral white',command=lambda: controller.show_frame(FourthPage))
        B2.place(x=578,y=250)
        def on_enter1(e):
            B2.config(background='coral1',foreground='white')
        def on_leave1(e):
            B2.config(background='Indian Red1',foreground='black')
        B2.bind('<Enter>' , on_enter1)
        B2.bind('<Leave>', on_leave1)







        Button = tk.Button(self, image = self.back,borderwidth=0,bg='white',command=lambda: controller.show_frame(FirstPage))
        Button.place(x=389, y=440)





class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        userframe = tk.LabelFrame(self,text="Patient Details",font=("Raleway",10,'italic'),bg='light blue',bd=5)
        userframe.pack(side='top',fill='both',expand=True)

        name_var= tk.StringVar()
        phone_var=tk.IntVar()
        speed_var=tk.IntVar()
        age_var=tk.IntVar()
        sex_var=tk.IntVar()
        med_var=tk.IntVar()

        tk.Label(userframe,text="Enter Patient's Details :",font=('Times New Roman',20,'bold','italic'),bg='skyblue').place(x=260,y=10)

        Name= tk.Label(userframe,text=" Name : ",font=('Times New Roman',20,'bold'),bg='skyblue',borderwidth=4,relief='ridge').place(x=100,y= 100)
        Name_entry=tk.Entry(userframe,textvariable=name_var,font=('Times New Roman',20,'normal')).place(x=300,y=100)

        Phone= tk.Label(userframe,text=" Phone No. :",font=('Times New Roman',20,'bold'),bg='skyblue',borderwidth=4,relief='ridge').place(x=100,y= 150)
        phn_entry=tk.Entry(userframe,textvariable=phone_var,font=('Times New Roman',20,'normal')).place(x=300,y=150)
        Speed= tk.Label(userframe,text=" Pulse Rate :",font=('Times New Roman',20,'bold'),bg='skyblue',borderwidth=4,relief='ridge').place(x=100,y= 200)
        speed_entry=tk.Entry(userframe,textvariable=speed_var,font=('Times New Roman',20,'normal')).place(x=300,y=200)
        Age= tk.Label(userframe,text=" Age :",font=('Times New Roman',20,'bold'),bg='skyblue',borderwidth=4,relief='ridge').place(x=100,y= 250)
        age_entry=tk.Entry(userframe,textvariable=age_var,font=('Times New Roman',20,'normal')).place(x=300,y=250)
        Sex= tk.Label(userframe,text=" Sex :",font=('Times New Roman',20,'bold'),bg='skyblue',borderwidth=4,relief='ridge').place(x=100,y= 300)
        c= tk.Radiobutton(userframe,text='Male',variable=sex_var,value=1,font=('Times New Roman',20,'normal'),bg='lightblue').place(x=300,y=300)
        d=tk.Radiobutton(userframe,text='Female',variable=sex_var,value=0,font=('Times New Roman',20,'normal'),bg='lightblue').place(x=450,y=300)
        Med= tk.Label(userframe,text=" Takes Medicine :",font=('Times New Roman',15,'bold'),bg='skyblue',borderwidth=4,relief='ridge').place(x=100,y= 350)
        c= tk.Radiobutton(userframe,text='Yes',variable=med_var,value=1,font=('Times New Roman',20,'normal'),bg='lightblue').place(x=300,y=350)
        d=tk.Radiobutton(userframe,text='No',variable=med_var,value=0,font=('Times New Roman',20,'normal'),bg='lightblue').place(x=450,y=350)
        def submit():

            name= name_var.get()
            phone=phone_var.get()
            speed=speed_var.get()
            age=age_var.get()
            sex=sex_var.get()
            medicine=med_var.get()


            speed=speed/100

            print(name)
            print(phone)
            print(speed)
            print(age)
            print(sex)
            print(medicine)

            messagebox.showinfo("From Dr. AI"," Your details have been submitted. \nNow test your ECG.")

        self.submit = PhotoImage(file='submit.png')

        submit= tk.Button(userframe,image=self.submit, bg='light blue' ,borderwidth=0,command=submit)
        submit.place(x=400,y=400)
        self.back = PhotoImage(file='back.png')
        Button = tk.Button(self, image=self.back,bg='light blue',borderwidth=0, command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=430)
class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ecg=ECG(speed,age,sex,medicine,name)


        ecgframe = tk.LabelFrame(self,text="ECG TEST",font=("Raleway",10,'italic'),bg='light blue',bd=5)
        ecgframe.pack(side='top',fill='both',expand=True)

        ecgimg = Image.open(r'electrode.png')
        ecgimg = ecgimg.resize((300,300),Image.ANTIALIAS)

        test = ImageTk.PhotoImage(ecgimg)
        label1=tk.Label(ecgframe,image=test)
        label1.image=test
        label1.place(x=50,y=30)

        text=tk.Label(ecgframe,text="Place the 3 electrodes on body like any of these 2 images",font=('Times New Roman',15,'bold'),bg='lightblue')
        text.place(x=50,y=350)

        canvasframe= tk.Frame(ecgframe,width=400,height=302,bg='skyblue',bd=5)
        canvasframe.place(x=370,y=30)

        text2=tk.Label(canvasframe,text="Now rest your body and start capturing...",font=('Footlight MT light',15,'bold'),bg='skyblue')
        text2.place(x=10,y=35)

        self.capture=tk.PhotoImage(file='capture.png')
        capbtn=tk.Button(canvasframe,image=self.capture,bg='skyblue',borderwidth=0,command=ecg.ecgserial)
        capbtn.place(x=0,y=80)

        resultframe=tk.Frame(canvasframe,width=390,height=180,bg='white',bd=5)
        resultframe.place(x=0,y=122)


        def result():
            try:

                res=ecg.predict()

                ex=tk.Label(resultframe,text=f"'{ecg.Name}, you have {res}% chance of Arrhythmia."
                                                 "\n if your probability is above 50 %,=\n"
                                                 "1. Start excercises & yoga \n"
                                                 "2. Avoid street foods as well as spicy foods. \n"
                                                 "3. Manage healthy life style from morning to night.\n"
                                                 "4. If you feel any problem, consult with your phycisian.' ",bg='white',font=("Comic Sans MS",10,'roman','italic'), fg='black')
                ex.place(x=5,y=5)
                sign=tk.Label(resultframe,text=' - Dr. AI',font=("Comic Sans MS",13,'bold'), fg='blue',bg='white')
                sign.place(x=280,y=130)

            except:
                messagebox.showwarning("From Dr. AI","CAPTURE FIRST !!!")

        self.btn=tk.PhotoImage(file='predict.png')
        predict=tk.Button(canvasframe,image= self.btn,bg='skyblue',borderwidth=0,command=result)
        predict.place(x=290,y=77)



        self.home=tk.PhotoImage(file='home.png')
        Button = tk.Button(self, image=self.home,bg='lightblue' , borderwidth=0,command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=390)

        self.back=tk.PhotoImage(file='back.png')
        Buttonb = tk.Button(self, image=self.back,bg='lightblue' , borderwidth=0, command=lambda: controller.show_frame(SecondPage))
        Buttonb.place(x=100, y=425)
class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=450)
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage , FourthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("AI DOCTOR")
        icon = Image.open(r'1689578.png')
        icon = ImageTk.PhotoImage(icon)
        self.iconphoto(False,icon)

app = Application()
app.maxsize(800,500)
app.mainloop()





