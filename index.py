from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import csv
import datetime

class Library:

    def __init__(self,root):
        self.root = root
        self.root.title("LIBRARY MANAGER")
        self.width = self.root.winfo_screenwidth() // 2 - ( 1280 // 2 )  # SET UP WIDTH SCREEN MIDDLE 
        self.height = self.root.winfo_screenheight() // 2 - ( 720 // 2 )  # SET UP HEIGHT SCREEN MIDDLE
        self.root.geometry("{}x{}+{}+{}".format(1280,720,self.width,self.height))

        MemberType   = StringVar()
        BookID       = StringVar()
        getID        = StringVar()
        BookTitle    = StringVar()
        Title        = StringVar()
        FirstName    = StringVar()
        LastName     = StringVar()
        Address      = StringVar()
        PostCode     = StringVar()
        Moblie       = StringVar()
        Author       = StringVar()
        Cagetory     = StringVar()
        DateDue      = StringVar()
        PriceOverDue =StringVar()
        DateBorrow   = StringVar()
        Price        = StringVar()

        def Reset():
            MemberType.set("")
            BookID.set("")
            getID.set("")
            BookTitle.set("")
            Title.set("")
            FirstName.set("")
            LastName.set("")
            Address.set("")
            PostCode.set("")
            Moblie.set("")
            Author.set("")
            Cagetory.set("")
            DateDue.set("")
            PriceOverDue.set("")
            DateBorrow.set("")
            Price.set("")
            self.txtDisplayR.delete("1.0",END)
        def Delete():
            self.txtDisplayR.delete("1.0",END)
        
        def Exit():
        	Exit = tkinter.messagebox.askyesno("Library Management System", "Confirm Do You Want To Exit")
        	if Exit>0:
        		root.destroy()
        		return

        def Receipt():
            self.txtDisplayR.insert(END,'Member Type:    \t\t' + MemberType.get()   + "\n")
            self.txtDisplayR.insert(END,'Book ID:        \t\t' + BookID.get()       + "\n")
            self.txtDisplayR.insert(END,'ID:             \t\t' + getID.get()        + "\n")
            self.txtDisplayR.insert(END,'FirstName:      \t\t' + FirstName.get()    + "\n")
            self.txtDisplayR.insert(END,'Book Title:     \t\t' + BookTitle.get()    + "\n")
            self.txtDisplayR.insert(END,'Moblie:         \t\t' + Moblie.get()       + "\n")
            self.txtDisplayR.insert(END,'Author:         \t\t' + Author.get()       + "\n")
            self.txtDisplayR.insert(END,'Cagetory:       \t\t' + Cagetory.get()     + "\n")
            self.txtDisplayR.insert(END,'DateDue:        \t\t' + DateDue.get()      + "\n")
            self.txtDisplayR.insert(END,'Price Over Due: \t\t' + PriceOverDue.get() + "\n")
            self.txtDisplayR.insert(END,'Price:          \t\t' + Price.get()        + "\n") 
            self.txtDisplayR.insert(END, "\n" , '\n') 

        

        #!------------------------------------------------Frames--------------------------------------------------------#
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame =Frame(MainFrame,width=1450,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle =Label(TitleFrame,width=34,font=('Times New Roman',40,'bold'),text="\tLibrary Management System\t",bg="brown",fg='white',padx=12)
        self.lblTitle.pack()
        
        ButtonFrame =Frame(MainFrame,bd=20,width=1250,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM, fill='y')

        DataFrame =Frame(MainFrame,bd=20,width=1300,height=400,padx=20, pady=50 ,relief=RIDGE)
        DataFrame.pack()

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=900, height=300, relief=RIDGE, font=('Times New Roman',12,'bold'), text="MEMBERSHIP INFORMATION", fg="brown")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('Times New Roman',12,'bold'),text="BOOK DETAILS",fg="Crimson")
        DataFrameRIGHT.pack(side=RIGHT)

        #!------------------------------------------------WIDGET------------------------------------------------
        self.lblMemberType = Label(DataFrameLEFT, font=('Times New Roman',12),text="MemberType",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)
        
        self.cboMemberType = ttk.Combobox(DataFrameLEFT, state='readonly',textvariable = MemberType, font=('Times New Roman',12), width=23)
        self.cboMemberType['value']=('--select--','Student','Lecturer','AdminStaff','MembershipNo')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1)

        self.lblBookID = Label(DataFrameLEFT, font=('Times New Roman',12),text="BookID",padx=2,pady=2)
        self.lblBookID.grid(row=0,column=2,sticky=W)
        self.lblBookID=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=BookID,width=25)
        self.lblBookID.grid(row=0,column=3)

        self.lblgetID = Label(DataFrameLEFT, font=('Times New Roman',12),text="ID",padx=2,pady=2)
        self.lblgetID.grid(row=1,column=0,sticky=W)
        self.lblgetID=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=getID,width=25)
        self.lblgetID.grid(row=1,column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=('Times New Roman',12),text="Book Title",padx=2,pady=2)
        self.lblBookTitle.grid(row=1,column=2,sticky=W)
        self.lblBookTitle=Entry(DataFrameLEFT, font=('Times New Roman',12), textvariable=BookTitle, width=25)
        self.lblBookTitle.grid(row=1,column=3)

        self.lblTitle = Label(DataFrameLEFT, font=('Times New Roman',12),text="Title",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)
        self.cboTitle = ttk.Combobox(DataFrameLEFT, state='readonly',textvariable = Title, font=('Times New Roman',12), width=23)
        self.cboTitle['value']=('--select--','Mr.','Mrs.','Ms')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=1)


        self.lblFirstName = Label(DataFrameLEFT,font=('Times New Roman',12),text="First Name",padx=2,pady=2)
        self.lblFirstName.grid(row=3,column=0,sticky=W)
        self.lblFirstName=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=FirstName,width=25)
        self.lblFirstName.grid(row=3,column=1)
        
        self.lblLastName = Label(DataFrameLEFT,font=('Times New Roman',12),text="LastName",padx=2,pady=2)
        self.lblLastName.grid(row=4,column=0,sticky=W)
        self.lblLastName=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=LastName,width=25)
        self.lblLastName.grid(row=4,column=1)

        self.lblAddress = Label(DataFrameLEFT,font=('Times New Roman',12),text="Address",padx=2,pady=2)
        self.lblAddress.grid(row=5,column=0,sticky=W)
        self.lblAddress=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=Address,width=25)
        self.lblAddress.grid(row=5,column=1)
        
        self.lblPostCode = Label(DataFrameLEFT,font=('Times New Roman',12),text="PostCode",padx=2,pady=2)
        self.lblPostCode.grid(row=6,column=0,sticky=W)
        self.lblPostCode=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=PostCode,width=25)
        self.lblPostCode.grid(row=6,column=1)
        
        self.lblMoblie = Label(DataFrameLEFT,font=('Times New Roman',12),text="Moblie",padx=2,pady=2)
        self.lblMoblie.grid(row=7,column=0,sticky=W)
        self.lblMoblie=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=Moblie,width=25)
        self.lblMoblie.grid(row=7,column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=('Times New Roman',12),text="Author",padx=2,pady=2)
        self.lblAuthor.grid(row=2,column=2,sticky=W)
        self.lblAuthor=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=Author,width=25)
        self.lblAuthor.grid(row=2,column=3)

        self.lblCagetory = Label(DataFrameLEFT, font=('Times New Roman',12),text="Cagetory",padx=2,pady=2)
        self.lblCagetory.grid(row=3,column=2,sticky=W)
        self.lblCagetory=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=Cagetory,width=25)
        self.lblCagetory.grid(row=3,column=3)
        
        self.lblDueDate = Label(DataFrameLEFT, font=('Times New Roman',12),text="Date Due",padx=2,pady=2)
        self.lblDueDate.grid(row=4,column=2,sticky=W)
        self.lblDueDate=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=DateDue,width=25)
        self.lblDueDate.grid(row=4,column=3)

        self.lblPriceOverDue = Label(DataFrameLEFT, font=('Times New Roman',12),text="Price Over Due",padx=2,pady=2)
        self.lblPriceOverDue.grid(row=5,column=2,sticky=W)
        self.lblPriceOverDue=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=PriceOverDue,width=25)
        self.lblPriceOverDue.grid(row=5,column=3)

        self.lblDateBorrow  = Label(DataFrameLEFT, font=('Times New Roman',12),text="Date Borrow",padx=2,pady=2)
        self.lblDateBorrow.grid(row=6,column=2,sticky=W)
        self.lblDateBorrow=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=DateBorrow,width=25)
        self.lblDateBorrow.grid(row=6,column=3)

        self.lblPrice = Label(DataFrameLEFT, font=('Times New Roman',12),text="Price",padx=2,pady=2)
        self.lblPrice.grid(row=7,column=2,sticky=W)
        self.lblPrice=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=Price,width=25)
        self.lblPrice.grid(row=7,column=3)
        #=======================================Widget=================================================================
        self.txtDisplayR=Text(DataFrameRIGHT,font=('Times New Roman',12,'bold'),width=40,height=13,padx=8,pady=20)
        self.txtDisplayR.grid(row=0,column=2)
        #======================================ListBox==================================================================
        
        listBooks = []
        path = "C:\\Users\\ASUS\\Desktop\\CODEGYM\\Managent Library\\Book.txt"
        with open(path, 'r') as f:
                listBooks = csv.reader(f, delimiter=",")
                listBooks = list(listBooks)[0]
                f.close()
        
        
        def SelectedBook(evt):
            value =str(booklist.get(booklist.curselection()))
            print(value) # check infor book
            w=value

            if (w == "Learn Python The Hard Way"):
                BookID.set("ITBL 1001")
                BookTitle.set("Learn Python The Hard Way")
                Author.set("Paul Parker")
                PriceOverDue.set("20$")
                Price.set("133$")            
                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateBorrow.set(d1)
                DateDue.set(d3)
                Cagetory.set("Computing & Internet")
                Receipt()

            elif(w == "Think Python"):
                 BookID.set("ITBL 1002")
                 BookTitle.set("Language Programming")
                 Author.set("Yuval Noah Harari")
                 PriceOverDue.set("32$")
                 Price.set("100$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("Computing & Internet")   
                 Receipt()

            elif(w == "Mathematics"):
                 BookID.set("EMB 10010")
                 BookTitle.set("Mathematics")
                 Author.set("Robison")
                 PriceOverDue.set("29$")
                 Price.set("120$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set('Education')  
                 Receipt()      

            elif(w == "Sat Math WordBook"):
                 BookID.set("EMB 10020")
                 BookTitle.set("Sat Math WordBook")
                 Author.set("Vector")
                 PriceOverDue.set("9$")
                 Price.set("80$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set('Education')  
                 Receipt() 
            	 
            elif(w == "The History Book"):
            	 BookID.set("THB 100")
            	 BookTitle.set("The History Book")
            	 Author.set("Chinua Achebe")
            	 PriceOverDue.set("12$")
            	 Price.set("213$")
            	 d1=datetime.date.today()
            	 d2=datetime.timedelta(days=10)
            	 d3=(d1+d2)
            	 DateBorrow.set(d1)
            	 DateDue.set(d3)
            	 Cagetory.set("History")
                #  Receipt()

            elif(w == "World History"):
                 BookID.set("THB 200")
                 BookTitle.set("World History")
                 Author.set("Babasaheb")
                 PriceOverDue.set("24$")
                 Price.set("320$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("History")
                 Receipt()

            elif(w == "New Way Food"):
                 BookID.set("FDB 001")
                 BookTitle.set("New Way Food")
                 Author.set("Vector Raken")
                 PriceOverDue.set("23$")
                 Price.set("350$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("Drink & Food")
                 Receipt()

            elif(w == "My Very First Book of Food"):
                 BookID.set("FDB 002")
                 BookTitle.set("My Very First Book of Food")
                 Author.set("Dinesh Trum")
                 PriceOverDue.set("11$")
                 Price.set("200$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("Drink & Food")
                 Receipt()

            elif(w == "The Work of Art"):
                 BookID.set("TWA 120")
                 BookTitle.set("The Work of Art")
                 Author.set("Guido van")
                 PriceOverDue.set("224$")
                 Price.set("1200$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("Arts & Photographer")              	 
                 Receipt()

            elif(w == "Zero to One"):
                 BookID.set("TWA 130")
                 BookTitle.set("Zero to One")
                 Author.set("Bekkam")
                 PriceOverDue.set("14$")
                 Price.set("100$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("Arts & Photographer")              	 
                 Receipt()

            elif(w == "Think and Grow Rich"):
                 BookID.set("TBB 010")
                 BookTitle.set("Think and Grow Rich")
                 Author.set("Helor")
                 PriceOverDue.set("4$")
                 Price.set("110$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("Business")              	 
                 Receipt()

            elif(w == "Secret DotCom"):
                 BookID.set("TBB 020")
                 BookTitle.set("Secret DotCom")
                 Author.set("Benlor Jusyma")
                 PriceOverDue.set("17$")
                 Price.set("234$")
                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 DateBorrow.set(d1)
                 DateDue.set(d3)
                 Cagetory.set("Business")              	 
                 Receipt()
           
        booklist = Listbox(DataFrameRIGHT,width=20,height=12,font=('Times New Roman',12,'bold'))
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)

        for items in listBooks:
        	booklist.insert(END,items)
            	
        #=======================================Button=========================================================================

        self.btnDelete=Button(ButtonFrame,text="DELETE",fg="white",bg="brown",font=('Times New Roman',12,'bold'),width=30,bd=4,command=Delete)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame,text="RESET",fg="white",bg="brown",font=('Times New Roman',12,'bold'),width=30,bd=4,command=Reset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame,text="EXIT",fg="white",bg="brown",font=('Times New Roman',12,'bold'),width=30,bd=4,command=Exit)
        self.btnExit.grid(row=0,column=3)





if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
