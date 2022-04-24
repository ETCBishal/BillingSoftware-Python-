from tkinter import *
from tkinter import messagebox as msg
import random,os
from datetime import date
from datetime import datetime

root = Tk()

root.geometry("1366x768+0+0")
root.iconbitmap("BillIcon.ico")
root.attributes('-fullscreen', True)
root. bind('<Escape>',lambda e: root. destroy())  #<<-- To exit full screen

root.title("Billing Software -Bishal jaiswal")
root.configure(background="white")

# ----------------- Variable -----------------
# ----------------- Customer variables -------
c_name = StringVar()
c_number = StringVar()
RandomBillNo = random.randint(1000,9999)
c_bill_number = StringVar()
c_bill_number.set(str(RandomBillNo))

# ----------------- Cosmetic variable -----------------
#---> Quantity
soap_Qt = IntVar()
shampoo_Qt = IntVar()
face_wash_Qt = IntVar()
mahendi_Qt = IntVar()
makeup_kit_Qt = IntVar()
body_loshan_Qt = IntVar()
hair_spray_Qt = IntVar()
hair_gell_Qt = IntVar()

# print(soap_Qt.get()) #---> by default 0 because it is an integer value.

#----> Price
soap_price = IntVar()
shampoo_price = IntVar()
face_wash_price = IntVar()
mahendi_price = IntVar()
makeup_kit_price = IntVar()
body_loshan_price = IntVar()
hair_spray_price = IntVar()
hair_gell_price = IntVar()

cosmetic_price = IntVar()

# ----------------- Grocery variable -----------------
# Quantity variable

oil_qt = IntVar()
nun_qt = IntVar()
dal_qt = IntVar()
aata_qt = IntVar()
rice_qt = IntVar()
chini_qt = IntVar()
maida_qt = IntVar()

# Price variable
oil_price = IntVar()
nun_price = IntVar()
dal_price = IntVar()
aata_price = IntVar()
rice_price = IntVar()
chini_price = IntVar()
maida_price = IntVar()

grocery_price = IntVar()

# ------------- Others variable --------------
# Quantity variable
frooti_qt = IntVar()
chocolate_qt = IntVar()
chocoFun_qt = IntVar()
fenta_qt = IntVar()
bread_qt = IntVar()
puff_qt = IntVar()
biscuits_qt = IntVar()

# Price variable
frooti_price = IntVar()
chocolate_price = IntVar()
chocoFun_price = IntVar()
fenta_price = IntVar()
bread_price = IntVar()
puff_price = IntVar()
biscuits_price = IntVar()

others_price = IntVar()

#---------------------- Top section ----------------------

f1 = Frame(root, relief=GROOVE,borderwidth=10,background="#4D0039",pady=2)
la1 = Label(f1,text="Billing Software",padx=30,pady=6,font="Cambria 25 bold",background="#4D0039",fg="white")
la1.pack()
f1.pack(side=TOP,fill=BOTH)

#---------------------- Customer Details ----------------------
f2 = LabelFrame(text="Customer Details",font="Cambria 12 bold",fg="gold",background="#4D0039",relief=GROOVE,bd=6)
f2.place(x=1,y=80,relwidth=1)

cname_lbl = Label(f2,text="Customer Name :",font="Cambria 15 bold",background="#4D0039",fg="white").grid(row=0,column=0,pady=5,padx=20)
cname_text = Entry(f2,textvariable=c_name,width=20,font="Cambria 12 bold",bd=4,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5) 

cphone_lbl = Label(f2,text="Customer Number :",font="Cambria 15 bold",background="#4D0039",fg="white").grid(row=0,column=2,pady=5,padx=20)
cphone_text = Entry(f2,textvariable=c_number,width=20,font="Cambria 12 bold",bd=4,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5) 

past_bill_number = StringVar()

cbill_lbl = Label(f2,text="Bill No. :",font="Cambria 15 bold",background="#4D0039",fg="white").grid(row=0,column=4,pady=5,padx=20)
cbill_text = Entry(f2,textvariable=past_bill_number,width=20,font="Cambria 12 bold",bd=4,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5) 


#--------------------- Cosmetic Frame ------------------------

f3 = LabelFrame(text="Cosmetics",font="Cambria 12 bold",fg="gold",background="#4D0039",bd=6)
f3.place(x=1,y=148,width=345,height=380)

qnt_lbl = Label(f3,text="Quantity",font="Cambria 12 bold",background="#4D0039",fg="gold").grid(row=0,column=1)
price_lbl = Label(f3,text="Price",font="Cambria 12 bold",background="#4D0039",fg="gold").grid(row=0,column=2)


bath_lbl = Label(f3,text="Bath Soap  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=1,column=0)
bath_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=soap_Qt).grid(row=1,column=1)
bath_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=soap_price).grid(row=1,column=2)

smp_lbl = Label(f3,text="Shampoo  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=2,column=0)
smp_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=shampoo_Qt).grid(row=2,column=1)
smp_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=shampoo_price).grid(row=2,column=2)

FW_lbl = Label(f3,text="Face Wash  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=3,column=0)
FW_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=face_wash_Qt).grid(row=3,column=1)
FW_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=face_wash_price).grid(row=3,column=2)

Hsp_lbl = Label(f3,text="Hair Spray  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=4,column=0)
Hsp_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=hair_spray_Qt).grid(row=4,column=1)
Hsp_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=hair_spray_price).grid(row=4,column=2)

Mhnd_lbl = Label(f3,text="Mahendi  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=5,column=0)
mhnd_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=mahendi_Qt).grid(row=5,column=1)
Mhnd_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=mahendi_price).grid(row=5,column=2)

Mkup_lbl = Label(f3,text="Makeup Kit  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=6,column=0)
Mkup_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=makeup_kit_Qt).grid(row=6,column=1)
Mkup_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=makeup_kit_price).grid(row=6,column=2)

Los_lbl = Label(f3,text="Body Loshan  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=7,column=0)
Los_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=body_loshan_Qt).grid(row=7,column=1)
Los_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=body_loshan_price).grid(row=7,column=2)

HG_lbl = Label(f3,text="Hair Gell  :", font="Cambria 12 bold",fg="light green",background="#4D0039").grid(pady=8,row=8,column=0)
HG_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=hair_gell_Qt).grid(row=8,column=1)
HG_lbl_entry = Entry(f3,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=hair_gell_price).grid(row=8,column=2,padx=10)


#---------------- Grocery ----------------

f4 = LabelFrame(text="Grocery",font="Cambria 12 bold",fg="gold",background="#4D0039",bd=6)
f4.place(x=346,y=148,width=330,height=380)

qnt_lbl = Label(f4,text="Quantity",font="Cambria 12 bold",background="#4D0039",fg="gold").grid(row=0,column=1)
price_lbl = Label(f4,text="Price",font="Cambria 12 bold",background="#4D0039",fg="gold").grid(row=0,column=2)

oil_lbl = Label(f4,text="Oil  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=1,column=0)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=oil_qt).grid(pady=10,padx=3,row=1,column=1)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=oil_price).grid(pady=10,padx=10,row=1,column=2)


nub_lbl = Label(f4,text="Nun  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=2,column=0)
nun_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=nun_qt).grid(pady=10,padx=3,row=2,column=1)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=nun_price).grid(pady=10,padx=3,row=2,column=2)


dal_lbl = Label(f4,text="Dal  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=3,column=0)
dal_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=dal_qt).grid(pady=10,padx=3,row=3,column=1)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=dal_price).grid(pady=10,padx=3,row=3,column=2)


rice_lbl = Label(f4,text="Rice  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=4,column=0)
rice_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=rice_qt).grid(pady=10,padx=3,row=4,column=1)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=rice_price).grid(pady=10,padx=3,row=4,column=2)


aata_lbl = Label(f4,text="Aata  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=5,column=0)
aata_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=aata_qt).grid(pady=10,padx=3,row=5,column=1)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=aata_price).grid(pady=10,padx=3,row=5,column=2)


maida_lbl = Label(f4,text="Maida  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=6,column=0)
maida_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=maida_qt).grid(pady=10,padx=3,row=6,column=1)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=maida_price).grid(pady=10,padx=3,row=6,column=2)


chini_lbl = Label(f4,text="Chini  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=7,column=0)
chini_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=chini_qt).grid(pady=10,padx=3,row=7,column=1)
oil_lbl_entry = Entry(f4,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=chini_price).grid(pady=10,padx=3,row=7,column=2)

#----------- Others ------------------

f5 = LabelFrame(text="Others",font="Cambria 12 bold",fg="gold",background="#4D0039",bd=6)
f5.place(x=676,y=148,width=345,height=380)

qnt_lbl = Label(f5,text="Quantity",font="Cambria 12 bold",background="#4D0039",fg="gold").grid(row=0,column=1)
qnt_lbl = Label(f5,text="Price",font="Cambria 12 bold",background="#4D0039",fg="gold").grid(row=0,column=2)


bath_lbl = Label(f5,text="Frooti  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=1,column=0)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=frooti_qt).grid(pady=10,padx=3,row=1,column=1)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=frooti_price).grid(pady=10,padx=3,row=1,column=2)


smp_lbl = Label(f5,text="Chocolate  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=2,column=0)
smp_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=chocolate_qt).grid(pady=10,padx=3,row=2,column=1)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=chocolate_price).grid(pady=10,padx=3,row=2,column=2)


FW_lbl = Label(f5,text="ChocoFun  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=3,column=0)
FW_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=chocoFun_qt).grid(pady=10,padx=3,row=3,column=1)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=chocoFun_price).grid(pady=10,padx=3,row=3,column=2)


Hsp_lbl = Label(f5,text="Fenta  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=4,column=0)
Hsp_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=fenta_qt).grid(pady=10,padx=3,row=4,column=1)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=fenta_price).grid(pady=10,padx=3,row=4,column=2)


Mhnd_lbl = Label(f5,text="Biscuits  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=5,column=0)
mhnd_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=biscuits_qt).grid(pady=10,padx=3,row=5,column=1)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=biscuits_price).grid(pady=10,padx=3,row=5,column=2)


Mkup_lbl = Label(f5,text="Bread  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=6,column=0)
Mkup_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=bread_qt).grid(pady=10,padx=3,row=6,column=1)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=bread_price).grid(pady=10,padx=3,row=6,column=2)


Los_lbl = Label(f5,text="Puff  :", font="Cambria 15 bold",fg="light green",background="#4D0039").grid(pady=5,row=7,column=0)
Los_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=puff_qt).grid(pady=10,padx=3,row=7,column=1)
bath_lbl_entry = Entry(f5,relief=SUNKEN, bd=3,font="Cambria 12 bold",width=10,textvariable=puff_price).grid(pady=10,padx=10,row=7,column=2)


# ------------------ Bill Area ----------------

f6 = LabelFrame(root,font="Cambria 12 bold",fg="black",background="white",bd=7)
f6.place(x=1022,y=148,width=345,height=385)
Bill_Area = Label(f6, text="Bill Area",font="Cambria 16 bold",relief=GROOVE,bd=6).pack(fill=X)

y_scroll = Scrollbar(f6,orient=VERTICAL)
text_area = Text(f6,yscrollcommand=y_scroll.set)
y_scroll.pack(side=RIGHT, fill= Y)
y_scroll.config(command=text_area.yview)
text_area.pack()

#--------- Bill Menu Frame ---------
f7 = LabelFrame(relief=GROOVE,text="Bill Menu",font="Cambria 12 bold", fg="gold",background="#4D0039",bd=6)
f7.place(x=1,y=527,width=505,height=240)

cosmt_total_lbl = Label(f7, text="Total cosmetics  :",fg="white", font="cambria 15 bold",background="#4D0039").grid(row=0,column=0,pady=15)
cosmt_total_entry = Entry(f7,textvariable = cosmetic_price,relief=SUNKEN,bd=3,font="Cambria 10 bold",width=10,state="readonly").grid(row=0,column=1)

grocery_total_lbl = Label(f7, text="Total Grocery  :",fg="white", font="cambria 15 bold",background="#4D0039").grid(row=1,column=0,pady=15)
grocery_total_entry = Entry(f7,textvariable =grocery_price,relief=SUNKEN,bd=3,font="Cambria 10 bold",width=10,state="readonly").grid(row=1,column=1)

others_total_lbl = Label(f7, text="Others Total  :",fg="white", font="cambria 15 bold",background="#4D0039").grid(row=2,column=0,pady=15)

others_total_entry = Entry(f7,textvariable =others_price,relief=SUNKEN,bd=3,font="Cambria 10 bold",width=10,state="readonly").grid(row=2,column=1)

#---------- File -> Save,Exit ------
f8 = LabelFrame(relief=GROOVE,text="Customer -DataBase",font="Cambria 12 bold", fg="gold",background="#4D0039",bd=6)
f8.place(x=505,y=527,width=860,height=240)

Test_Area = Text(f8,relief=GROOVE,bd=8)
Test_Area.pack(side=LEFT,padx=5,anchor=N)

frame = Frame(f8,bg="white",relief=GROOVE,bd=3)
frame.pack()

currentTime = datetime.now().strftime("%I:%M:%S")


def DataBase():
    Test_Area.delete(1.0,END)
    Test_Area.insert(END,"\t\t----- Welcome To The Billing Software DataBase -----\n\n")
    Test_Area.insert(END,f"\nCustomer Name   : {c_name.get()}")
    Test_Area.insert(END,f"\nCustomer Number : {c_number.get()}")
    Test_Area.insert(END,f"\nBill Number     : {c_bill_number.get()}")
    Test_Area.insert(END,f"\nPurchased Date  : {date.today()}")
    Test_Area.insert(END,f"\nPurchased Time  : {currentTime}")

def TOTAL():
    
    ask_for_total= msg.askyesno("Total -calculation","Are you sure to Total?")


    if ask_for_total>0:
        cosmetic_total = (
                        (soap_Qt.get()*soap_price.get())+
                        (shampoo_Qt.get()*shampoo_price.get())+
                        (face_wash_Qt.get()*face_wash_price.get())+
                        (hair_gell_Qt.get()*hair_gell_price.get())+
                        (hair_spray_Qt.get()*hair_spray_price.get())+
                        (mahendi_Qt.get()*mahendi_price.get())+
                        (makeup_kit_Qt.get()*makeup_kit_price.get())
                        )          
        
        cosmetic_price.set(cosmetic_total)

    
        grocery_total = (
                        (oil_qt.get()*oil_price.get())+
                        (nun_qt.get()*nun_price.get())+
                        (dal_qt.get()*dal_price.get())+
                        (maida_qt.get()*maida_price.get())+
                        (rice_qt.get()*rice_price.get())+
                        (chini_qt.get()*chini_price.get())+
                        (aata_qt.get()*aata_price.get())
                        )

        grocery_price.set(grocery_total)

        others_total = (
                        (frooti_qt.get()*frooti_price.get())+
                        (chocolate_qt.get()*chocolate_price.get())+
                        (fenta_qt.get()*fenta_price.get())+
                        (bread_qt.get()*bread_price.get())+
                        (puff_qt.get()*puff_price.get())+
                        (chocoFun_qt.get()*chocoFun_price.get())+
                        (biscuits_qt.get()*biscuits_price.get())
                        )
        
            
        
        others_price.set(others_total)
        ItemsToShow()
        DataBase()

def welcomeBill():
    text_area.delete(1.0,END)
    text_area.insert(END,"\tWelcome To The Shop\t")
    text_area.insert(END,"\n\t+-----------------+\n")
    text_area.insert(END,f"\nCustomer Name   : {c_name.get()}")
    text_area.insert(END,f"\nCustomer Number : {c_number.get()}")
    text_area.insert(END,f"\nBill Number     : {c_bill_number.get()}")
    text_area.insert(END,f"\nPurchased Date  : {date.today()}")
    text_area.insert(END,f"\nPurchased Time  : {currentTime}")
    text_area.insert(END,"\n======================================")
    text_area.insert(END,"\n Item\t\tQnt\t\tPrice")
    text_area.insert(END,"\n======================================\n") 
    DataBase()
welcomeBill()

def ItemsToShow():
    welcomeBill()
    
    # ------ Cosmetic --------
    if soap_price.get() != 0 or soap_Qt.get() != 0:
        text_area.insert(END, f" Soap\t\t{soap_Qt.get()}\t\t{soap_Qt.get()*soap_price.get()}\n")
    
    if face_wash_Qt.get() != 0 or face_wash_price.get() != 0:
        text_area.insert(END, f" Face Wash\t\t{face_wash_Qt.get()}\t\t{face_wash_Qt.get()*face_wash_price.get()}\n")

    if mahendi_Qt.get() != 0 or mahendi_price.get() != 0:
        text_area.insert(END, f" Mahendi\t\t{mahendi_Qt.get()}\t\t{mahendi_Qt.get()*mahendi_price.get()}\n")

    if makeup_kit_Qt.get() != 0 or makeup_kit_price.get() != 0:
        text_area.insert(END, f" MakeUp Kir\t\t{makeup_kit_Qt.get()}\t\t{makeup_kit_Qt.get()*makeup_kit_price.get()}\n")
    
    if hair_spray_Qt.get() != 0 or hair_spray_price.get() != 0:
        text_area.insert(END, f" Hair Spray\t\t{hair_spray_Qt.get()}\t\t{hair_spray_Qt.get()*hair_gell_price.get()}\n")

    if hair_gell_Qt.get() != 0 or hair_gell_price.get() != 0:
        text_area.insert(END, f" Hair Gell\t\t{hair_gell_Qt.get()}\t\t{hair_gell_Qt.get()*hair_gell_price.get()}\n")

    if body_loshan_Qt.get() != 0 or body_loshan_price.get() != 0:
        text_area.insert(END, f" Body Loshan\t\t{body_loshan_Qt.get()}\t\t{body_loshan_Qt.get()*body_loshan_price.get()}\n")
    
    # ------ Grocery --------    
    if oil_qt.get() != 0 or oil_price.get() != 0:
        text_area.insert(END, f" Oil\t\t{oil_qt.get()}\t\t{oil_qt.get()*oil_price.get()}\n")
    
    if nun_qt.get() != 0 or nun_price.get() != 0:
        text_area.insert(END, f" Nun\t\t{nun_qt.get()}\t\t{nun_qt.get()*nun_price.get()}\n")

    if dal_qt.get() != 0 or dal_price.get() != 0:
        text_area.insert(END, f" Dal\t\t{dal_qt.get()}\t\t{dal_qt.get()*dal_price.get()}\n")

    if chini_qt.get() != 0 or chini_price.get() != 0:
        text_area.insert(END, f" Chini\t\t{chini_qt.get()}\t\t{chini_qt.get()*chini_price.get()}\n")
    
    if maida_qt.get() != 0 or maida_price.get() != 0:
        text_area.insert(END, f" Maida\t\t{maida_qt.get()}\t\t{maida_qt.get()*maida_price.get()}\n")

    if aata_qt.get() != 0 or aata_price.get() != 0:
        text_area.insert(END, f" Aata\t\t{aata_qt.get()}\t\t{aata_qt.get()*aata_price.get()}\n")

    if rice_qt.get() != 0 or rice_price.get() != 0:
        text_area.insert(END, f" Rice\t\t{rice_qt.get()}\t\t{rice_qt.get()*rice_price.get()}\n")   
    
    # ------ Others --------    
    if frooti_qt.get() != 0 or frooti_price.get() != 0:
        text_area.insert(END, f" Frooti\t\t{frooti_qt.get()}\t\t{frooti_qt.get()*frooti_price.get()}\n")
    
    if fenta_qt.get() != 0 or fenta_price.get() != 0:
        text_area.insert(END, f" Fenta\t\t{fenta_qt.get()}\t\t{fenta_qt.get()*fenta_price.get()}\n")

    if biscuits_qt.get() != 0 or biscuits_price.get() != 0:
        text_area.insert(END, f" Biscuit\t\t{biscuits_qt.get()}\t\t{biscuits_qt.get()*biscuits_price.get()}\n")

    if bread_qt.get() != 0 or bread_price.get() != 0:
        text_area.insert(END, f" Bread\t\t{bread_qt.get()}\t\t{bread_qt.get()*bread_price.get()}\n")
    
    if puff_qt.get() != 0 or puff_price.get() != 0:
        text_area.insert(END, f" Puff\t\t{puff_qt.get()}\t\t{puff_qt.get()*puff_price.get()}\n")

    if chocoFun_qt.get() != 0 or chocoFun_price.get() != 0:
        text_area.insert(END, f" Choco Fun\t\t{chocoFun_qt.get()}\t\t{chocoFun_qt.get()*chocoFun_price.get()}\n")

    if chocolate_price.get() != 0 or chocolate_qt.get() != 0:
        text_area.insert(END, f" Chocolate\t\t{chocolate_qt.get()}\t\t{chocolate_qt.get()*chocolate_price.get()}\n")
    text_area.insert(END,"\n--------------------------------------\n")
    a = text_area.insert(END,f"  Total\t\t\tRs.{cosmetic_price.get()+grocery_price.get()+others_price.get()}")
    text_area.insert(END,"\n--------------------------------------")
    
def reset_data():
    want_to_reset = msg.askyesno("Reset -Data","Do you want to reset?")
    if want_to_reset>0:
        # ----------------- Customer variables -------
        c_name.set("")
        c_number.set("")
        RandomBillNo = random.randint(1000,9999)
        c_bill_number.set("")
        c_bill_number.set(str(RandomBillNo))

        # ----------------- Cosmetic variable -----------------
        #---> Quantity
        soap_Qt.set(0)
        shampoo_Qt.set(0)
        face_wash_Qt.set(0)
        mahendi_Qt.set(0)
        makeup_kit_Qt.set(0)
        body_loshan_Qt.set(0)
        hair_spray_Qt.set(0)
        hair_gell_Qt.set(0)

        #----> Price
        soap_price.set(0)
        shampoo_price.set(0)
        face_wash_price.set(0)
        mahendi_price.set(0)
        makeup_kit_price.set(0)
        body_loshan_price.set(0)
        hair_spray_price.set(0)
        hair_gell_price.set(0)

        cosmetic_price.set(0)

        # ----------------- Grocery variable -----------------
        # Quantity variable

        oil_qt.set(0)
        nun_qt.set(0)
        dal_qt.set(0)
        aata_qt.set(0)
        rice_qt.set(0)
        chini_qt.set(0)
        maida_qt.set(0)

        # Price variable
        oil_price .set(0)
        nun_price .set(0)
        dal_price .set(0)
        aata_price .set(0)
        rice_price .set(0)
        chini_price .set(0)
        maida_price.set(0)

        grocery_price.set(0)

        # ------------- Others variable --------------
        # Quantity variable
        frooti_qt.set(0)
        chocolate_qt.set(0)
        chocoFun_qt.set(0)
        fenta_qt.set(0)
        bread_qt.set(0)
        puff_qt.set(0)
        biscuits_qt.set(0)

        # Price variable
        frooti_price.set(0)
        chocolate_price.set(0)
        chocoFun_price.set(0)
        fenta_price.set(0)
        bread_price.set(0)    #9845241472
        puff_price.set(0)
        biscuits_price.set(0)

        others_price.set(0)
        welcomeBill()
        msg.showinfo("Reset -Data","Reseted successfully :D")
    else:
        return

def exit_app():
    ask_to_exit = msg.askyesno("Exit -Billing Software","Do you want to Exit?")
    if ask_to_exit>0:
        root.destroy()
    else:
        return

def save_File():
    ask_to_save = msg.askyesno("Save -Data","Are you sure to save the file?")
    if ask_to_save>0:
        bill_number = c_bill_number.get()
        file = open(f"BillingSoftwareFiles/{bill_number}.txt","w")
        file.write(text_area.get(1.0,END))
        file.close()
        msg.showinfo("Save",f"Bill no {c_bill_number.get()}: is Saved Successfully")
    else:
        return

def search_data():
    text_area.delete(1.0,END)
    present = 'no'
    for files in os.listdir("BillingSoftwareFiles/"):
        if files.split(".")[0] == past_bill_number.get():
            openFile = open(f"BillingSoftwareFiles/{files}","r")            
            text_area.delete(1.0,END)
            for content in openFile:
                text_area.insert(END,f"{content}")
            openFile.close()
            present='yes'    
    if present == "no":
        msg.showerror("Not Found","Sorry File Not Found")

    DataBase()


# --------------------- Buttons ------------------
Total_button = Button(root, text="Total",font="lucida 9 bold",command=TOTAL,width=12,height=2,bg="#4D0039",fg="white",bd=4)
Total_button.pack(side=BOTTOM,anchor=W,padx=350,pady=15)

generate_bill_button = Button(root,command=ItemsToShow, text="Generate Bill",font="lucida 9 bold",width=12,height=2,bg="#4D0039",fg="white",bd=4)
generate_bill_button.pack(side=BOTTOM,anchor=W,padx=350,pady=15)

reset_bill_button = Button(root, text="Reset",command=reset_data,font="lucida 9 bold",width=12,height=2,bg="#4D0039",fg="white",bd=4)
reset_bill_button.pack(side=BOTTOM,anchor=W,padx=350,pady=15)

Save_btn = Button(frame,text="Save",command=save_File,font="lucida 9 bold",width=9,height=2,bg="pink",fg="Black",relief=GROOVE,bd=4).pack(side=LEFT,padx=5,pady=5)
Exit_btn = Button(frame,text="Exit",command=exit_app,font="lucida 9 bold",width=9,height=2,bg="pink",fg="Black",relief=GROOVE,bd=4).pack(side=LEFT,padx=5,pady=5)

bill_btn = Button(f2, text="Search",command=search_data,width=10,bd=3,font="Cambria 12 bold",anchor="n",bg="Green",fg="white").grid(row=0,column=6,padx=51,ipadx=2)




root.mainloop()