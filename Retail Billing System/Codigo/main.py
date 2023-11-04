from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#functionality Part
billnumberRadom = random.randint(500,3000)

listEntrys = {"bathsoapEntry":['Bath Soap',20],'facecreamEntry':["Face Cream",50],'facewashEntry':["Face Wash",100],'hairsprayEntry':['Hair Spray',150],
              'hairgelEntry':['Hair Gel',80],'bodylotionEntry':['Body Lotion',60],'riceEntry':['Rice',200],'oilEntry':['Oil',200],'daalEntry':['Daal',200],
              'wheatEntry':['Wheat',200],'sugarEntry':['Sugar',200],'teaEntry':['Tea',200],'maazaEntry':['Maaza',50],'pespiEntry':['Pespi',20],
              'dewEntry':['Dew',30],'spriteEntry':['Sprite',20],'frootiEntry':['Frooti',40],'cocacolaEntry':['Coca Cola',50]}  
if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumberRadom
    result= messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0,END)
        file = open(f'bills/{billnumberRadom}.txt','w')
        file.write(bill_content)
        file.close
        messagebox.showinfo('Succes',f'{billnumberRadom} is saved successfully')
        billnumberRadom = random.randint(500,3000)


def bill_area():
    textarea.delete('1.0',END)
    if nameEntry.get() == '' or phoneEntry.get() =='':
        messagebox.showerror('Error','Customer Details are Required!')
    elif comesticPriceEntry.get() == '' and groceryPriceEntry.get() == '' and coldDrinksPriceEntry.get()=='':
        messagebox.showerror('Error','Products details are Required!')
    elif comesticPriceEntry.get() == '$ 0' and groceryPriceEntry.get() == '$ 0' and coldDrinksPriceEntry.get()=='$ 0':
        messagebox.showerror('Error','No products are selected!')
    else:
        textarea.insert(END,'\t\t\t***** Welcome *****')
        textarea.insert(END,f'\n Bill Number: {billnumberRadom}')
        textarea.insert(END,f'\n Custome Name: {nameEntry.get()}')
        textarea.insert(END,f'\n Phone Number: {phoneEntry.get()}')   
        textarea.insert(END,'\n' +'='*51)
        textarea.insert(END,'\n Products \t\t\t QTY \t\t\t  Price')
        textarea.insert(END,'\n' +'='*51+'\n')
        #textarea.insert(END,oilLabel.cget("text").replace(' ','').lower())

        for entry_name,(display_name,price) in listEntrys.items():
            entry = globals().get(entry_name)
            if entry is not None and entry.get() != "0":
                qty =int(entry.get())
                item_total = qty*price
                textarea.insert(END, f"{display_name} \t\t\t  {entry.get()} \t\t\t $ {item_total} \n")
        textarea.insert(END,'\n' +'-'*94+'\n')  
    
        TaxsList = {'comestictTaxLEntry':['Comestic Tax',comesticTax],'groceryTaxLEntry':['Grocery Tax',groecryTaxPrice],
                'coldDrinkTaxEntry':['Cold Drink Tax',coldrinksTaxPrice]}
        for tax_entry, (display_NameTax,Taxs) in TaxsList.items():
            entrytax = globals().get(tax_entry)
            if entrytax is not None and Taxs != 0:
                textarea.insert(END,f"{display_NameTax}: $ {Taxs} \n")
        textarea.insert(END,f"\n Total Bill: $ {TotalBill}")
        save_bill()
        

def total():
    #Calculation Comestics
    global comesticTax,groecryTaxPrice,coldrinksTaxPrice, TotalBill
    soapPriceValue = int(bathsoapEntry.get())*20
    faceCreamValue=int(facecreamEntry.get())*50
    faceWashValue=int(facewashEntry.get())*100
    hairSprayValue=int(hairsprayEntry.get())*150
    hairGelValue=int(hairgelEntry.get())*80
    bodyLotionValue=int(bodylotionEntry.get())*60
    totalComesticPrice = soapPriceValue+faceCreamValue+faceWashValue+hairSprayValue+hairGelValue+bodyLotionValue  
   
    comesticPriceEntry.delete(0,END)
    comesticPriceEntry.insert(0,"$ " + str(totalComesticPrice))
    comesticTax = round(totalComesticPrice*0.12,2)
    comestictTaxLEntry.delete(0,END)
    comestictTaxLEntry.insert(0,f'$ {comesticTax}')
    
    #Calculation Grocery
    
    ricePrice = int(riceEntry.get())*200
    oilPrice = int(oilEntry.get())*200
    daalPrice = int(daalEntry.get())*200
    wheatPrice = int(wheatEntry.get())*200
    sugarPrice = int(sugarEntry.get())*200
    teaPrice = int(teaEntry.get())*200
    totalGroceryPrice = ricePrice+oilPrice+daalPrice+wheatPrice+sugarPrice+teaPrice
    groceryPriceEntry.delete(0,END)
    groceryPriceEntry.insert(0,f'$ {totalGroceryPrice}')

    groecryTaxPrice = round(totalGroceryPrice*0.12,2)
    groceryTaxLEntry.delete(0,END)
    groceryTaxLEntry.insert(0,f'$ {groecryTaxPrice}')

    #Cold drinks
    maazaPrice=int(maazaEntry.get())*50
    pepsiPrice=int(pespiEntry.get())*20
    dewPrice=int(dewEntry.get())*30
    spritePrice=int(spriteEntry.get())*20
    frootiPrice=int(frootiEntry.get())*40
    cocaPrice=int(cocacolaEntry.get())*50

    coldrinksTotal = maazaPrice+pepsiPrice+dewPrice+spritePrice+frootiPrice+cocaPrice
    coldDrinksPriceEntry.delete(0,END)
    coldDrinksPriceEntry.insert(0,f'$ {coldrinksTotal}')
    
    coldrinksTaxPrice = round(coldrinksTotal*0.12,2) 
    coldDrinkTaxEntry.delete(0,END)
    coldDrinkTaxEntry.insert(0,f'$ {coldrinksTaxPrice}')

    TotalBill = round(totalComesticPrice + comesticTax + totalGroceryPrice + groecryTaxPrice+coldrinksTotal+coldrinksTaxPrice,2)

def searchBill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billNumberEntry.get():
            text = open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for j in text:
                textarea.insert(END,j)
            text.close()
            break
    else:
        messagebox.showerror('Error','Invalid bill Number')
           
def print_bill():
    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file1 = tempfile.mktemp('.txt')
        open(file1,'w').write(textarea.get(1.0,END))
        os.startfile(file1,'print')

def send_email():
    def send_gmail():
        ob =smtplib.SMTP("smtp.mail.yahoo.com")
        ob.set_debuglevel(1)
        ob.starttls()
        
        useEmail= "Your Email Adress"
       
        ob.login(useEmail,'Your PassWord')
        messague = messageArea.get(1.0,END)
       
        ob.sendmail(useEmail, emailAdressrentryEntry.get(),messague)
       
        ob.quit()
        messagebox.showinfo('Sucess','Bill is succesfully send!')
    #  if textarea.get(1.0,END) == '\n':
    #     messagebox.showerror('Error','Bill is Empty')
    #  else:
    root1 = Toplevel()
    root1.config(bg='chartreuse3')
    root1.title('Send Email')
    root1.resizable(0,0)

    senderFrame = LabelFrame(root1,text='SENDER',font=("Segoe UI",15,'bold'),bg='chartreuse3',bd=5, relief= GROOVE)
    senderFrame.grid(row = 0, column=0,padx=40, pady=20)

    senderLabel = Label(senderFrame, text="Sender's Email:",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
    senderLabel.grid(row=0,column=0, padx= 10, pady= 8)

    senderentry = Entry(senderFrame,bd=2, width= 23,font=("Segoe UI",14), relief= GROOVE)
    senderentry.grid(row=0, column=1, padx= 10, pady= 8)

    passwordLabel = Label(senderFrame, text="Password",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
    passwordLabel.grid(row=1,column=0, padx= 10, pady= 8)

    passwordentry = Entry(senderFrame,bd=2, width= 23,font=("Segoe UI",14), relief= GROOVE)
    passwordentry.grid(row=1, column=1, padx= 10, pady= 8)

    recipientFrame = LabelFrame(root1,text='RECIPIENT',font=("Segoe UI",15,'bold'),bg='chartreuse3',bd=5, relief= GROOVE)
    recipientFrame.grid(row = 1, column=0,padx=40, pady=20)

    emailAdressLabel = Label(recipientFrame, text="Email Address:",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
    emailAdressLabel.grid(row=0,column=0, padx= 10, pady= 8)

    emailAdressrentryEntry = Entry(recipientFrame,bd=2, width= 23,font=("Segoe UI",14), relief= GROOVE)
    emailAdressrentryEntry.grid(row=0, column=1, padx= 10, pady= 8)

    messagueLabel =  Label(recipientFrame, text="Message:",font=("Segoe UI",12,'bold'),bg= 'chartreuse3')
    messagueLabel.grid(row=1, column=0, padx= 10, pady= 8)

    messageArea = Text(recipientFrame,font=("Segoe UI",12,'bold'), bd =2 , relief=SUNKEN,width=42,height=11)
    messageArea.grid(row=2, column=0, columnspan=2)
    messageArea.insert(END,'\t\t***** Welcome *****')
    messageArea.insert(END,f'\n Bill Number: {billnumberRadom}')
    messageArea.insert(END,f'\n Custome Name: {nameEntry.get()}')
    messageArea.insert(END,f'\n Phone Number: {phoneEntry.get()}')   
    messageArea.insert(END,'\n' +'='*34)
    messageArea.insert(END,'\n Products \t\t QTY \t  Price')
    messageArea.insert(END,'\n'+ '='*34 +'\n')
    
    for entry_name,(display_name,price) in listEntrys.items():
        entry = globals().get(entry_name)
        if entry is not None and entry.get() != "0":
            qty =int(entry.get())
            item_total = qty*price
            messageArea.insert(END, f"{display_name} \t\t {entry.get()} \t\t $ {item_total} \n")
    messageArea.insert(END,'\n' +'-'*63+'\n')  

    TaxsList = {'comestictTaxLEntry':['Comestic Tax',comesticTax],'groceryTaxLEntry':['Grocery Tax',groecryTaxPrice],
            'coldDrinkTaxEntry':['Cold Drink Tax',coldrinksTaxPrice]}
    for tax_entry, (display_NameTax,Taxs) in TaxsList.items():
        entrytax = globals().get(tax_entry)
        if entrytax is not None and Taxs != 0:
            messageArea.insert(END,f"{display_NameTax}: $ {Taxs} \n")
    messageArea.insert(END,f"\n Total Bill: $ {TotalBill}")
    
    sendButton = Button(recipientFrame, text= 'SEND', font=('Segoe UI',15,'bold'),bd=5,relief=GROOVE,command= send_gmail)
    sendButton.grid(row=3,column=0, columnspan= 2, padx=5)

    root1.mainloop()



    
#Gui part
#Criando a Janela Principal
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap("D:/OneDrive - uema.br/Scripts/Python/Retail Billing System/Imagens/icon_billing.ico")
#Criando Labels(widgets)
headingLabel =  Label(root,text='Retail Billing System',font=("Segoe UI",30,'bold')
                      ,bg= 'chartreuse3',bd=12, relief=RIDGE)
headingLabel.pack(fill= X,pady=10)

#Criando um Frame

customer_details_frame = LabelFrame(root,text = "Customer Details",font= ("Segoe UI",15,'bold')
                                    ,bg='chartreuse3',bd=12,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name',font= ("Segoe UI",13,'bold'),bg='chartreuse3')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry = Entry(customer_details_frame,font=('Segoe UI',12),bd=7,width=20)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel = Label(customer_details_frame,text='Phone Number',font=("Segoe UI",13,'bold'),bg='chartreuse3')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry= Entry(customer_details_frame,font=('Segoe UI',12),bd=7,width=20)
phoneEntry.grid(row=0,column=3,padx=8)

billNumberLabel = Label(customer_details_frame,text='Bill Number',font=("Segoe UI",13,'bold'),
                        bg='chartreuse3')
billNumberLabel.grid(row=0,column=4,padx=20,pady=2)
billNumberEntry= Entry(customer_details_frame,font=('Segoe UI',12),bd=7,width=20)
billNumberEntry.grid(row=0,column=5,padx=8)

#Criando Botão
searchButton = Button(customer_details_frame,text= 'SEARCH',font=('Segoe UI',12),bd=7,command=searchBill)
searchButton.grid(row=0,column=6,padx=10,pady=8)

#Adicionando Frame
productsFrames = Frame(root)
productsFrames.pack(pady=10)

#Frame de Produto
cosmeticLabelFrame = LabelFrame(productsFrames,text='Cometics',font= ('Segoe UI',15,'bold'),
                                bg='chartreuse3',bd= 12,relief=GROOVE)
cosmeticLabelFrame.grid(row=0, column=0)

bathsoapLabel = Label(cosmeticLabelFrame,text='Bath Soap',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
bathsoapLabel.grid(row=1,column=0)

bathsoapEntry = Entry(cosmeticLabelFrame,font=('Segoe UI',12),bd=7, width=10)
bathsoapEntry.grid(row=1,column=1,padx=8,pady=4)
bathsoapEntry.insert(0,0)

facecreamLabel = Label(cosmeticLabelFrame,text='Face Cream',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
facecreamLabel.grid(row=2,column=0)

facecreamEntry = Entry(cosmeticLabelFrame,font=('Segoe UI',12),bd=7, width=10)
facecreamEntry.grid(row=2,column=1,padx=8,pady=4)
facecreamEntry.insert(0,0)

facewashLabel = Label(cosmeticLabelFrame,text='Face Wash',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
facewashLabel.grid(row=3,column=0)

facewashEntry = Entry(cosmeticLabelFrame,font=('Segoe UI',12),bd=7, width=10)
facewashEntry.grid(row=3,column=1,padx=8,pady=4)
facewashEntry.insert(0,0)

hairsprayLabel = Label(cosmeticLabelFrame,text='Hair Spray',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
hairsprayLabel.grid(row=4,column=0)

hairsprayEntry = Entry(cosmeticLabelFrame,font=('Segoe UI',12),bd=7, width=10)
hairsprayEntry.grid(row=4,column=1,padx=8,pady=4)
hairsprayEntry.insert(0,0)

hairgelLabel = Label(cosmeticLabelFrame,text='Hair Gel',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
hairgelLabel.grid(row=5,column=0)

hairgelEntry = Entry(cosmeticLabelFrame,font=('Segoe UI',12),bd=7, width=10)
hairgelEntry.grid(row=5,column=1,padx=8,pady=4)
hairgelEntry.insert(0,0)

bodylotionLabel = Label(cosmeticLabelFrame,text='Body Lotion',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
bodylotionLabel.grid(row=6,column=0)

bodylotionEntry = Entry(cosmeticLabelFrame,font=('Segoe UI',12),bd=7, width=10)
bodylotionEntry.grid(row=6,column=1,padx=8,pady=4)
bodylotionEntry.insert(0,0)
#Frame Doces

groceryLabelFrame = LabelFrame(productsFrames,text='Grocery',font= ('Segoe UI',15,'bold'),
                                bg='chartreuse3',bd= 12,relief=GROOVE)
groceryLabelFrame.grid(row=0, column=1)
 

riceLabel = Label(groceryLabelFrame,text='Rice',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
riceLabel.grid(row=0,column=0)

riceEntry = Entry(groceryLabelFrame,font=('Segoe UI',12),bd=7, width=10)
riceEntry.grid(row=0,column=1,padx=8,pady=4)
riceEntry.insert(0,0)

oilLabel = Label(groceryLabelFrame,text='Oil',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
oilLabel.grid(row=1,column=0)

oilEntry = Entry(groceryLabelFrame,font=('Segoe UI',12),bd=7, width=10)
oilEntry.grid(row=1,column=1,padx=8,pady=4)
oilEntry.insert(0,0)

daalLabel = Label(groceryLabelFrame,text='Daal',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
daalLabel.grid(row=2,column=0)

daalEntry = Entry(groceryLabelFrame,font=('Segoe UI',12),bd=7, width=10)
daalEntry.grid(row=2,column=1,padx=8,pady=4)
daalEntry.insert(0,0)

wheatLabel = Label(groceryLabelFrame,text='Wheat',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
wheatLabel.grid(row=3,column=0)

wheatEntry = Entry(groceryLabelFrame,font=('Segoe UI',12),bd=7, width=10)
wheatEntry.grid(row=3,column=1,padx=8,pady=4)
wheatEntry.insert(0,0)

sugarLabel = Label(groceryLabelFrame,text='Sugar',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
sugarLabel.grid(row=4,column=0)

sugarEntry = Entry(groceryLabelFrame,font=('Segoe UI',12),bd=7, width=10)
sugarEntry.grid(row=4,column=1,padx=8,pady=4)
sugarEntry.insert(0,0)

teaLabel = Label(groceryLabelFrame,text='Tea',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
teaLabel.grid(row=5,column=0)

teaEntry = Entry(groceryLabelFrame,font=('Segoe UI',12),bd=7, width=10)
teaEntry.grid(row=5,column=1,padx=8,pady=4)
teaEntry.insert(0,0)

#Cold Drinks Label Frame
coldDriknsLabelFrame = LabelFrame(productsFrames,text='Cold Drinks',font= ('Segoe UI',15,'bold'),
                                bg='chartreuse3',bd= 12,relief=GROOVE)
coldDriknsLabelFrame.grid(row=0, column=2)

maazaLabel = Label(coldDriknsLabelFrame,text='Maaza',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
maazaLabel.grid(row=0,column=0)

maazaEntry = Entry(coldDriknsLabelFrame,font=('Segoe UI',12),bd=7, width=10)
maazaEntry.grid(row=0,column=1,padx=8,pady=4)
maazaEntry.insert(0,0)

pepsiLabel = Label(coldDriknsLabelFrame,text='Pepsi',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
pepsiLabel.grid(row=1,column=0)

pespiEntry = Entry(coldDriknsLabelFrame,font=('Segoe UI',12),bd=7, width=10)
pespiEntry.grid(row=1,column=1,padx=8,pady=4)
pespiEntry.insert(0,0)

dewLabel = Label(coldDriknsLabelFrame,text='Dew',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
dewLabel.grid(row=2,column=0)

dewEntry = Entry(coldDriknsLabelFrame,font=('Segoe UI',12),bd=7, width=10)
dewEntry.grid(row=2,column=1,padx=8,pady=4)
dewEntry.insert(0,0)

spriteLabel = Label(coldDriknsLabelFrame,text='Sprite',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
spriteLabel.grid(row=3,column=0)

spriteEntry = Entry(coldDriknsLabelFrame,font=('Segoe UI',12),bd=7, width=10)
spriteEntry.grid(row=3,column=1,padx=8,pady=4)
spriteEntry.insert(0,0)

frootiLabel = Label(coldDriknsLabelFrame,text='Frooti',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
frootiLabel.grid(row=4,column=0)

frootiEntry = Entry(coldDriknsLabelFrame,font=('Segoe UI',12),bd=7, width=10)
frootiEntry.grid(row=4,column=1,padx=8,pady=4)
frootiEntry.insert(0,0)

cocacolaLabel = Label(coldDriknsLabelFrame,text='Coca Cola',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
cocacolaLabel.grid(row=5,column=0)

cocacolaEntry = Entry(coldDriknsLabelFrame,font=('Segoe UI',12),bd=7, width=10)
cocacolaEntry.grid(row=5,column=1,padx=8,pady=4)
cocacolaEntry.insert(0,0)
#Bill Area Label Frame
billFrame = Frame(productsFrames,bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3,padx=10)

headinglabelBillArea = Label(billFrame,text='Bill Area',font= ('Segoe UI',15,'bold')
                             ,bd=7,relief= GROOVE)
headinglabelBillArea.pack(fill= X)

scrollbar = Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea = Text(billFrame, font=('Segoe UI',12), height=12.2, width =63,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#Bill Menu Frame

billMenuFrame =  Frame(root)
billMenuFrame.pack(fill=X,padx=2)

billMenuLabelFrame = LabelFrame(billMenuFrame,text='Bill Menu',font= ('Segoe UI',15,'bold'),
                                bg='chartreuse3',bd= 12,relief=GROOVE)
billMenuLabelFrame.grid(row=0, column=0)

comesticPriceLabel = Label(billMenuLabelFrame,text='Comestic Price',font= ('Segoe UI',12,'bold')
                           ,bg='chartreuse3')
comesticPriceLabel.grid(row=0,column=0)

comesticPriceEntry = Entry(billMenuLabelFrame,font=('Segoe UI',12),bd=7, width=20)
comesticPriceEntry.grid(row=0,column=1,padx=8,pady=4)

groceryPriceLabel = Label(billMenuLabelFrame,text='Grocery Price',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
groceryPriceLabel.grid(row=1,column=0)

groceryPriceEntry = Entry(billMenuLabelFrame,font=('Segoe UI',12),bd=7, width=20)
groceryPriceEntry.grid(row=1,column=1,padx=8,pady=4)

coldDrinksPriceLabel = Label(billMenuLabelFrame,text='Cold Drinks Price',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
coldDrinksPriceLabel.grid(row=2,column=0)

coldDrinksPriceEntry = Entry(billMenuLabelFrame,font=('Segoe UI',12),bd=7, width=20)
coldDrinksPriceEntry.grid(row=2,column=1,padx=8,pady=4)

comestictTaxLabel = Label(billMenuLabelFrame,text='Comestic Tax',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
comestictTaxLabel.grid(row=0,column=3)

comestictTaxLEntry = Entry(billMenuLabelFrame,font=('Segoe UI',12),bd=7, width=20)
comestictTaxLEntry.grid(row=0,column=4,padx=8,pady=4)

groceryTaxLabel = Label(billMenuLabelFrame,text='Grocery Tax',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
groceryTaxLabel.grid(row=1,column=3)

groceryTaxLEntry = Entry(billMenuLabelFrame,font=('Segoe UI',12),bd=7, width=20)
groceryTaxLEntry.grid(row=1,column=4,padx=8,pady=4)

coldDrinkTaxLabel = Label(billMenuLabelFrame,text='Cold Drink',font= ('Segoe UI',12,'bold'),bg='chartreuse3')
coldDrinkTaxLabel.grid(row=2,column=3)

coldDrinkTaxEntry = Entry(billMenuLabelFrame,font=('Segoe UI',12),bd=7, width=20)
coldDrinkTaxEntry.grid(row=2,column=4,padx=8,pady=4)

# ... (Código anterior)

buttonFrame = Frame(billMenuLabelFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=5, rowspan=3, padx=10, pady=10)

totalButton = Button(buttonFrame, text='Total', font=('Segoe UI', 12, 'bold'), bd=8, width=8,pady=10, command= total)
totalButton.grid(row=0, column=0, padx=5,pady=20 )

billButton = Button(buttonFrame, text='Bill', font=('Segoe UI', 12, 'bold'), bd=8, width=8,pady=10
                    ,command=bill_area)
billButton.grid(row=0, column=1, padx=5, pady=20)

emailButton = Button(buttonFrame, text='Email', font=('Segoe UI', 12, 'bold'), bd=8, width=8,pady=10, command= send_email)
emailButton.grid(row=0, column=2, padx=5, pady=20)

printButton = Button(buttonFrame, text='Print', font=('Segoe UI', 12, 'bold'), bd=8, width=8,pady=10,command=print_bill)
printButton.grid(row=0, column=3, padx=5, pady=20)

clearButton = Button(buttonFrame, text='Clear', font=('Segoe UI', 12, 'bold'), bd=8, width=8,pady=10)
clearButton.grid(row=0, column=4, padx=5, pady=20)

# ... (Código posterior)

root.mainloop()