from tkinter import*
import random
from time import strftime
root= Tk()
root.geometry('1600x800+0+0')
root.title('Dream Bean Cafe')
root.iconbitmap(r'coffee_cup.ico')
#create three frames
f1= Frame(root ,width= 1600, height= 50 , bg= "lightgreen",relief= RAISED)
f1.pack(side= TOP)
f2= Frame(root ,width=800 , height= 700 ,relief= RAISED)
f2.pack(side=LEFT )
f3 = Frame(root ,width= 300, height= 700, bg= 'black' ,relief= RAISED)
f3.pack(side= RIGHT)
#label
top_label= Label(f1, font=('Lucida console' , 50 , 'bold'), text="DREAM BEAN CAFE", fg='purple' ,bd=10 , anchor='w')
top_label.grid(row=0 , column=0 )
#timefunction
def time():
     string = strftime('%H:%M:%S %p')
     lbl.config(text = string)
     lbl.after(1000, time)
lbl= Label(f1, font=('Cuckoo' , 10 )  ,fg='purple' ,bd=10 , anchor='w')
lbl.grid(row=1 , column=0 )
time()
#calculator
e= Entry(f3 , font=('arial' , 20  ) , bd=10 , bg="white" , insertwidth=4 , justify ='left')
e.grid(columnspan=4)
def button_click(number):
    current= e.get()
    e.delete(0 , END)
    e.insert(0 , str(current) + str(number))
def button_add():
    f_num=e.get()
    global f_number
    global math
    math ="addition"
    f_number=int(f_num)
    e.delete(0, END)
def button_sub():
    f_num= e.get()
    global f_number
    global math
    math = "subtraction"
    f_number= int(f_num)
    e.delete(0, END)
def button_mul():
    f_num=e.get()
    global f_number
    global math
    math = "multiplication"
    f_number = int(f_num)
    e.delete(0 , END)
def button_div():
    f_num = e.get()
    global f_number
    global math
    math = "division"
    f_number = int(f_num)
    e.delete(0 , END)
def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if math== "addition":
       e.insert(0 ,  f_number + int(second_number))
    elif math== "subtraction":
         e.insert(0,  f_number  - int(second_number))
    elif math=="multiplication":
         e.insert(0 , f_number * int(second_number))
    elif math== "division":
         e.insert(0,  f_number / int(second_number))
def button_clear():
    e.delete(0 , END)
button_1= Button(f3, text= "1" ,padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') ,command=  lambda : button_click(1))
button_2= Button(f3 , text ="2",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  , command = lambda :button_click(2))
button_3= Button(f3 , text ="3",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') , command = lambda :button_click(3))
button_4= Button(f3 , text ="4",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  , command = lambda :button_click(4))
button_5= Button(f3 , text ="5",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  , command = lambda :button_click(5))
button_6= Button(f3 , text ="6",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') , command = lambda:button_click(6))
button_7= Button(f3 , text ="7",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  , command = lambda:button_click(7))
button_8= Button(f3 , text ="8",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  , command =lambda: button_click(8))
button_9= Button(f3 , text ="9",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  , command = lambda:button_click(9))
button_0= Button(f3, text ="0",padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') , command = lambda:button_click(0))
button_add= Button(f3 , text ="+" , padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') , command= button_add)
button_equal= Button(f3 , text= "=" , padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') , command = button_equal)
button_clear= Button(f3, text ="C" ,padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  , command = button_clear)
button_sub = Button(f3 , text="-" , padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') ,command= button_sub)
button_mul = Button(f3 , text="*" ,padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold')  ,command= button_mul)
button_div = Button(f3 , text="/" , padx =16 ,pady=16,bd=8,fg='black',font=('arial' , 20 , 'bold') ,command= button_div)
button_1.grid(row=4 ,column=0)
button_2.grid(row=4, column =1)
button_3.grid(row=4, column =2)
button_4.grid(row=3, column =0)
button_5.grid(row=3, column =1)
button_6.grid(row=3, column =2)
button_7.grid(row=2, column =0)
button_8.grid(row=2, column =1)
button_9.grid(row=2, column =2)
button_0.grid(row=5, column =0)
button_add.grid(row=2 , column= 3)
button_equal.grid(row=5 ,column=2 )
button_clear.grid(row=5 ,column =1 )
button_sub.grid(row=3 ,column=3)
button_mul.grid(row=4 ,column=3)
button_div.grid(row=5 ,column=3)
#frame2
rand= StringVar()
coffee_decaf= StringVar()
espresso=StringVar()
cappuccino= StringVar()
mocha_madness= StringVar()
raspberry_mocha=StringVar()
sandwich = StringVar()
pasta= StringVar()
pizza= StringVar()
brownie= StringVar()
burger_meal = StringVar()
icecream=StringVar()
cost_of_meal= StringVar()
service_charge= StringVar()
state_tax= StringVar()
sub_total= StringVar()
total_cost= StringVar()
label_reference= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Reference:" , bd=10 , anchor='w')
label_reference.grid(row=0 , column=0)
text_reference=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=rand , insertwidth=4 , bg='lightgreen', justify='right')
text_reference.grid(row=0 , column=1)

label_coffee_decaf= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Coffee/Decaf:" , bd=10 , anchor='w')
label_coffee_decaf.grid(row=1 , column=0)
text_coffee_decaf=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=coffee_decaf , insertwidth=4 , bg='lightgreen', justify='right')
text_coffee_decaf.grid(row=1 , column=1)

label_espresso= Label(f2 , font= ('Lucida Sans' , 15, 'bold') , text= "Espresso:" , bd=10 , anchor='w')
label_espresso.grid(row=2 , column=0)
text_espresso=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=espresso , insertwidth=4 , bg='lightgreen', justify='right')
text_espresso.grid(row=2 , column=1)

label_cappuccino= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Cappuccino:" , bd=10 , anchor='w')
label_cappuccino.grid(row=3 , column=0)
text_cappuccino=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=cappuccino , insertwidth=4 , bg='lightgreen', justify='right')
text_cappuccino.grid(row=3 , column=1)

label_mocha_madness= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Mocha Madness:" , bd=10 , anchor='w')
label_mocha_madness.grid(row=4 , column=0)
text_mocha_madness=Entry(f2 , font=('Lucida Sans', 15, 'bold') , textvariable=mocha_madness, insertwidth=4 , bg='lightgreen', justify='right')
text_mocha_madness.grid(row=4 , column=1)

label_raspberry_mocha = Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Raspberry Mocha:" , bd=10 , anchor='w')
label_raspberry_mocha .grid(row=5, column=0)
text_raspberry_mocha =Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=raspberry_mocha , insertwidth=4 , bg='lightgreen', justify='right')
text_raspberry_mocha .grid(row=5 , column=1)

label_sandwich= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Sandwich:" , bd=10 , anchor='w')
label_sandwich.grid(row=6 , column=0)
text_sandwich=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=sandwich , insertwidth=4 , bg='lightgreen', justify='right')
text_sandwich.grid(row=6 , column=1)

label_pasta= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Pasta:" , bd=10 , anchor='w')
label_pasta.grid(row=7, column=0)
text_pasta=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=pasta , insertwidth=4 , bg='lightgreen', justify='right')
text_pasta.grid(row=7, column=1)

label_pizza= Label(f2 , font= ('Lucida Sans' , 15, 'bold') , text= "Pizza:" , bd=10 , anchor='w')
label_pizza.grid(row=8, column=0)
text_pizza=Entry(f2 , font=('Lucida Sans', 15, 'bold') , textvariable=pizza , insertwidth=4 , bg='lightgreen', justify='right')
text_pizza.grid(row=8, column=1)

label_brownie= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Brownie:" , bd=10 , anchor='w')
label_brownie.grid(row=9, column=0)
text_brownie=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=brownie , insertwidth=4 , bg='lightgreen', justify='right')
text_brownie.grid(row=9, column=1)

label_burger_meal= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Burger Meal:" , bd=10 , anchor='w')
label_burger_meal.grid(row=0, column=2)
text_burger_meal=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=burger_meal , insertwidth=4 , bg='lightgreen', justify='right')
text_burger_meal.grid(row=0, column=3)

label_icecream= Label(f2 , font= ('Lucida Sans' , 15, 'bold') , text= "Icecream:" , bd=10 , anchor='w')
label_icecream.grid(row=1, column=2)
text_icecream=Entry(f2 , font=('Lucida Sans', 15, 'bold') , textvariable=icecream, insertwidth=4 , bg='lightgreen', justify='right')
text_icecream.grid(row=1, column=3)

label_cost_of_meal= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Cost Of Meal:" , bd=10 , anchor='w')
label_cost_of_meal.grid(row=2, column=2)
text_cost_of_meal=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=cost_of_meal , insertwidth=4 , bg='lightgreen', justify='right')
text_cost_of_meal.grid(row=2, column=3)

label_service_charge= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Service Charge:" , bd=10 , anchor='w')
label_service_charge.grid(row=3, column=2)
text_service_charge=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=service_charge , insertwidth=4 , bg='lightgreen', justify='right')
text_service_charge.grid(row=3, column=3)

label_state_tax= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "State Tax:" , bd=10 , anchor='w')
label_state_tax.grid(row=4, column=2)
text_state_tax=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=state_tax, insertwidth=4 , bg='lightgreen', justify='right')
text_state_tax.grid(row=4, column=3)

label_sub_total= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Sub Total:" , bd=10 , anchor='w')
label_sub_total.grid(row=5, column=2)
text_sub_total=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=sub_total , insertwidth=4 , bg='lightgreen', justify='right')
text_sub_total.grid(row=5, column=3)

label_total_cost= Label(f2 , font= ('Lucida Sans' , 15 , 'bold') , text= "Total Cost:" , bd=10 , anchor='w')
label_total_cost.grid(row=6, column=2)
text_total_cost=Entry(f2 , font=('Lucida Sans', 15 , 'bold') , textvariable=total_cost, insertwidth=4 , bg='lightgreen', justify='right')
text_total_cost.grid(row=6, column=3)
#buttons
def Ref():
    x=random.randint(12900 , 687373)
    randomRef=str(x)
    rand.set(randomRef)
    Cocoffee = float( coffee_decaf.get())
    Coespresso=float(espresso.get())
    Cocappuccino=float(cappuccino.get())
    Comocha=float(mocha_madness.get())
    Corasp=float(raspberry_mocha.get())
    Cosandwich=float(sandwich.get())
    Copasta=float(pasta.get())
    Copizza=float(pizza.get())
    Cobrownie=float(brownie.get())
    Coburger=float( burger_meal.get())
    Coicecream=float(icecream.get())

    Costofcoffee =  Cocoffee * 150
    Costofespresso= Coespresso* 200
    Costofcappuccino=Cocappuccino*350
    Costofmocha_madness= Comocha *400
    Costofraspberry_mocha=Corasp *300
    Costofsandwich= Cosandwich* 100
    Costofpasta=Copasta *370
    Costofpizza= Copizza*280
    Costofbrownie=Cobrownie*485
    Costofburgermeal=Coburger*250
    Costoficecream= Coicecream*199

    CostofMeal= "Rs" , str ('%.2f' % (Costofcoffee+Costofespresso+Costofcappuccino+ Costofmocha_madness
                            +Costofraspberry_mocha+Costofsandwich+ Costofpasta+Costofpizza+ Costofbrownie+
                            Costofburgermeal+ Costoficecream))
    Paytax=     ((Costofcoffee+Costofespresso+Costofcappuccino+ Costofmocha_madness
                            +Costofraspberry_mocha+Costofsandwich+ Costofpasta+Costofpizza+ Costofbrownie+
                            Costofburgermeal+ Costoficecream)* 0.2)
    Totalcost=  (Costofcoffee+Costofespresso+Costofcappuccino+ Costofmocha_madness
                            +Costofraspberry_mocha+Costofsandwich+ Costofpasta+Costofpizza+ Costofbrownie+
                            Costofburgermeal+ Costoficecream)
    Ser_charge=  ((Costofcoffee+Costofespresso+Costofcappuccino+ Costofmocha_madness
                            +Costofraspberry_mocha+Costofsandwich+ Costofpasta+Costofpizza+ Costofbrownie+
                            Costofburgermeal+ Costoficecream)/99)
    Service="Rs" , str('%.2f' % Ser_charge)

    Overallcost= "Rs" , str('%.2f' % (Paytax+Totalcost+Ser_charge))
    Paidtax="Rs" , str('%.2f' % Paytax)
    service_charge.set(Service)
    cost_of_meal.set(CostofMeal)
    state_tax.set(Paidtax)
    sub_total.set(CostofMeal)
    total_cost.set(Overallcost)
def Exit():
    root.destroy()
def Reset():
    rand.set(" ")
    coffee_decaf.set(" ")
    espresso.set(" ")
    cappuccino.set(" ")
    mocha_madness.set(" ")
    raspberry_mocha.set(" ")
    sandwich.set(" ")
    pasta.set(" ")
    pizza.set(" ")
    brownie.set(" ")
    burger_meal.set(" ")
    icecream.set(" ")
    cost_of_meal.set(" ")
    service_charge.set(" ")
    state_tax.set(" ")
    sub_total.set(" ")
    total_cost.set(" ")
btn_total= Button(f2 , padx=10 , pady=10 , bd=10 , fg="black" , text= "Total" ,font=('Lucida Sans', 15 , 'bold'), bg="white" , command=Ref)
btn_total.grid(row=8 , column =2)
btn_reset = Button(f2 , padx=10 , pady=10 , bd=10 , fg="black" , text= "Reset" ,font=('Lucida Sans', 15 , 'bold'), bg="white" , command=Reset)
btn_reset.grid(row =8 , column=3)
btn_exit = Button(f2 , padx=10 , pady=10 , bd=10 , fg="black" , text= "Exit" ,font=('Lucida Sans', 15 , 'bold'), bg="white" , command=Exit)
btn_exit.grid(row =8 , column=4)
root.mainloop()
