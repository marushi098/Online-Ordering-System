from Tkinter import *
import tkMessageBox
import ttk
import random
import time
import datetime
import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        root.geometry("1920x1080")
        root.title("Ordering System")
        self.canvas = tk.Canvas(root, borderwidth=0, background="#00ffbf")
        self.frame = tk.Frame(self.canvas, background="#00ffbf")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.img=tk.PhotoImage(file="abhi.gif")
        tk.Button(self.frame,image=self.img,height=490).grid(row=0,column=0)
        self.t="Er. no.- 171B162 \n \n Name- Arushi Mishra \n\n Batch-B5(BY) \n \n Project on- Website Based \n Ordering System \n\n Contact No.-7869191834 \n\n Email Id- marushi098@gmail.com"
        tk.Label(self.frame,text=self.t,font='Arial 26 bold',fg="#000000",bg="#ff1a1a").grid(row=0,column=1)
        tk.Button(self.frame,text='Way To Project',height=3,width=90,bg="yellow",command=root.destroy).grid(row=1,column=1)
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
if __name__ == "__main__":
    root=tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

root=Tk()
root.geometry("1350x650+0+0")
root.title("Ordering System")
root.configure(background='black')

def Exit():
    ex=tkMessageBox.askyesno("Ordering System","Do you want to exit the system")
    if ex>0:
        root.destroy()
        return
def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
def OrderRef():
    Refpay=random.randint(10300,709467)
    Refpaid=("OS"+str(Refpay))
    CustomerRef.set(Refpaid)
def CostofOrder():
    Qty1=float(QtyWhiteWine.get())
    Qty2=float(QtyRedWine.get())
    Qty3=float(QtyOtherWine.get())
    
    UnitPrice1=float(UnitPriceWhiteWine.get())
    UnitPrice2=float(UnitPriceRedWine.get())
    UnitPrice3=float(UnitPriceOtherWine.get())

    CostofWine1="Rs.",str('%.2f'%(Qty1*UnitPrice1))
    CostofWine2="Rs.",str('%.2f'%(Qty2*UnitPrice2))
    CostofWine3="Rs.",str('%.2f'%(Qty3*UnitPrice3))

    CostofWhiteWine.set(CostofWine1)
    CostofRedWine.set(CostofWine2)
    CostofOtherWine.set(CostofWine3)

    CostWine1=(Qty1*UnitPrice1)
    CostWine2=(Qty2*UnitPrice2)
    CostWine3=(Qty3*UnitPrice3)
 
    AllCost=((Qty1*UnitPrice1)+(Qty2*UnitPrice2)+(Qty3*UnitPrice3))
    TaxALL="Rs.",str('%.2f'%((AllCost)*0.02))
    Tax.set(TaxALL)
    SubTotalp="Rs.",str('%.2f'%(AllCost))
    SubTotal.set(SubTotalp)
    TotalCostp="Rs.", str('%.2f'%(AllCost + ((AllCost) *0.02)))
    TotalCost.set(TotalCostp)
    return
#VARIABLES USED
CustomerRef=StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofWhiteWine=StringVar()
CostofRedWine=StringVar()
CostofOtherWine=StringVar()
CostofDelivery=StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
CustomerEmail=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
Discount=StringVar()
CostofOtherWine=StringVar()
CostofRedWine=StringVar()
CostofWhiteWine=StringVar()
UnitPriceOtherWine=StringVar()
UnitPriceRedWine=StringVar()
UnitPriceWhiteWine=StringVar()
QtyOtherWine=StringVar()
QtyRedWine=StringVar()
QtyWhiteWine=StringVar()

#init component are
CostofWhiteWine.set(0)
CostofRedWine.set(0)
CostofOtherWine.set(0)
UnitPriceOtherWine.set(0)
UnitPriceRedWine.set(0)
UnitPriceWhiteWine.set(0)
QtyOtherWine.set(0)
QtyRedWine.set(0)
Discount.set(0)
QtyWhiteWine.set(0)
TimeOfOrder.set(time.strftime("%H: %M: %S"))
DateOfOrder.set(time.strftime("%d/%m/%Y"))

#Frame...
Tops=Frame(root,width=1350,height=50,bd=16,relief="raise")
Tops.pack(side=TOP)
LF=Frame(root,width=700,height=650,bd=16,relief="raise")
LF.pack(side=LEFT)
RF=Frame(root,width=600,height=650,bd=16,relief="raise")
RF.pack(side=RIGHT)

Tops.configure(background='black')
LF.configure(background='black')
RF.configure(background='black')

LeftInsideLF=Frame(LF,width=700,height=100,bd=8,relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF,width=700,height=400,bd=8,relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame(RF,width=604,height=200,bd=8,relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF,width=306,height=400,bd=8,relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF,width=300,height=400,bd=8,relief="raise")
RightInsideRFRF.pack(side=RIGHT)
#TITLE
lblInfo=Label(Tops,font=('arial',50,'bold'),text="Ordering Systems",
              bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
#TopLeftFrame
lblCustomerName=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Name",
                      fg="black",bd=10,anchor='w')
lblCustomerName.grid(row=0,column=0)
txtCustomerName=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                      bg="white",justify='left',textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)
lblCustomerPhone=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Phone",
                       fg="black",bd=10,anchor='w')
lblCustomerPhone.grid(row=1,column=0)
txtCustomerPhone=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                       bg="white",justify='left',textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1,column=1)

lblCustomerEmail=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Email",
                       fg="black",bd=10,anchor='w')
lblCustomerEmail.grid(row=2,column=0)
txtCustomerEmail=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                       bg="white",justify='left',textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)
#Top Right Frame

lblDateOfOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Date Of Order",
                     fg="black",bd=10,anchor='w')
lblDateOfOrder.grid(row=0,column=0)
txtDateOfOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,
                     bg="white",justify='left',textvariable=DateOfOrder)
txtDateOfOrder.grid(row=0,column=1)
lblTimeOfOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Time of Order",
                     fg="black",bd=10,anchor='w')
lblTimeOfOrder.grid(row=1,column=0)
txtTimeOfOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,
                     bg="white",justify='left',textvariable=TimeOfOrder)
txtTimeOfOrder.grid(row=1,column=1)

lblCustomerRef=Label(RightInsideLF,font=('arial',12,'bold'),text="Customer Ref",
                     fg="black",bd=10,anchor='w')
lblCustomerRef.grid(row=2,column=0)
txtCustomerRef=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,
                     bg="white",justify='left',textvariable=CustomerRef)
txtCustomerRef.grid(row=2,column=1)

#Bottom Right Frame

lblMethodOfPayment=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Method of Payment",
                         fg="black",bd=16,anchor="w")
lblMethodOfPayment.grid(row=0,column=0)
cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF,font=('arial',10,'bold'))
cmdMethodOfPayment['value']=(' ','CASH','DEBIT CARD','VISA CARD','MASTER CARD')
cmdMethodOfPayment.grid(row=0,column=1)
lblDiscount=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Discount",
                  fg="black",bd=16,anchor='w')
lblDiscount.grid(row=1,column=0)
txtDiscount=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                  bg="white",justify='left',textvariable=Discount)
txtDiscount.grid(row=1,column=1)

lblTax=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Tax",
             fg="black",bd=16,anchor='w')
lblTax.grid(row=2,column=0)
txtTax=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
             bg="white",justify='left',textvariable=Tax)
txtTax.grid(row=2,column=1)

lblSubTotal=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Sub Total",
                  fg="black",bd=16,anchor='w')
lblSubTotal.grid(row=3,column=0)
txtSubTotal=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                  bg="white",justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)
lblTotalCost=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Total Cost",
                   fg="black",bd=16,anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                   bg="white",justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1)
#Bottom Left Frame
lblItemOrder=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Item Order',fg="black",bd=20)
lblItemOrder.grid(row=0,column=0)
lblQty=Label(LeftInsideLFLF,font=('arial',14,'bold'),text="Qty",fg="black",bd=10)
lblQty.grid(row=0,column=1)
lblUnitPrice=Label(LeftInsideLFLF,font=('arial',14,'bold'),text="Unit Price",fg="black",bd=20)
lblUnitPrice.grid(row=0,column=2)
lblCostofItem=Label(LeftInsideLFLF,font=('arial',14,'bold'),text="Cost Of Item",fg="black",bd=20)
lblCostofItem.grid(row=0,column=3)
###
lblWhiteWine=Label(LeftInsideLFLF,font=('arial',14,'bold'),text="White Wine",fg="black",bd=20)
lblWhiteWine.grid(row=1,column=0)
lblRedWine=Label(LeftInsideLFLF,font=('arial',14,'bold'),text="Red Wine",fg="black",bd=20)
lblRedWine.grid(row=2,column=0)
lblOtherWine=Label(LeftInsideLFLF,font=('arial',14,'bold'),text="Other Wine",fg="black",bd=20)
lblOtherWine.grid(row=3,column=0)
###
txtQtyWhiteWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=QtyWhiteWine)
txtQtyWhiteWine.grid(row=1,column=1)
txtQtyRedWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=QtyRedWine)
txtQtyRedWine.grid(row=2,column=1)
txtQtyOtherWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=QtyOtherWine)
txtQtyOtherWine.grid(row=3,column=1)
###
txtUnitPriceWhiteWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=UnitPriceWhiteWine)
txtUnitPriceWhiteWine.grid(row=1,column=2)
txtUnitPriceRedWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=UnitPriceRedWine)
txtUnitPriceRedWine.grid(row=2,column=2)
txtUnitPriceOtherWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=UnitPriceOtherWine)
txtUnitPriceOtherWine.grid(row=3,column=2)
###
txtCostofWhiteWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=CostofWhiteWine)
txtCostofWhiteWine.grid(row=1,column=3)
txtCostofRedWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=CostofRedWine)
txtCostofRedWine.grid(row=2,column=3)
txtCostofOtherWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                      bg="white",justify='left',textvariable=CostofOtherWine)
txtCostofOtherWine.grid(row=3,column=3)
#Buttons Right Frame
btnTotalCost=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'),width=11,
                    text="Total Cost",bg="white",command=CostofOrder).grid(row=0,column=0)
btnReset=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'),width=11,
                    text="Reset",bg="white",command=Reset).grid(row=1,column=0)
btnOrderRef=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'),width=11,
                    text="Order Ref",bg="white",command=OrderRef).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'),width=11,
                    text="Exit",bg="white",command=Exit).grid(row=3,column=0)
root.mainloop()
