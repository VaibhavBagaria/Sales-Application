# Basic tkinter template
from tkinter import *
root=Tk()
root.title("Sales Application")
root.geometry("800x250")

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") 
profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

label_Month=Label(root,text='Month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")')
label_Profit=Label(root,text='Profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)')
label1=Label(root)
label2=Label(root)

def work():
    maxprofit=max(profits)
    minprofit=min(profits)

    maxprofitindex=profits.index(maxprofit)
    minprofitindex=profits.index(minprofit)

    maxprofitmonth=month[maxprofitindex]
    minprofitmonth=month[minprofitindex]

    label1["text"]="The max profit of "+str(maxprofit)+" has been recorded in the month of "+str(maxprofitmonth)
    label2["text"]="The min profit of "+str(minprofit)+" has been recorded in the month of "+str(minprofitmonth)

button1=Button(root,text="Show Max and Min Profit of Month",command=work)

label_Month.place(relx=0.5,rely=0.2,anchor=CENTER)
label_Profit.place(relx=0.5,rely=0.3,anchor=CENTER)
label1.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()