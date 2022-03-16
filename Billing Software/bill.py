from tkinter import*
import math, random, os
from tkinter import messagebox
class bill_App:
        def __init__(self,root):
                self.root = root
        # self.root.geometry("1350x700+0+0")
                self.root.geometry("1400x800")
                self.root.title("Taukir's Billing Software")
                bg_color="#074463"
                title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white" ,font=("times new roman",30,"bold"),pady=2).pack(fill=X)
                #########################Variables########################################
                ##Cosmetics
                self.soap=IntVar()
                self.face_cream=IntVar()
                self.face_wash=IntVar()
                self.spray=IntVar()
                self.gell=IntVar()
                self.lotion=IntVar()
                ##Grocery
                self.rice=IntVar()
                self.foodoil=IntVar()
                self.daal=IntVar()
                self.wheat=IntVar()
                self.sugar=IntVar()
                self.tea=IntVar()
        ##Cold Drinks
                self.maza=IntVar()
                self.coke=IntVar()
                self.frooti=IntVar()
                self.thumbs_up=IntVar()
                self.limca=IntVar()
                self.sprite=IntVar()

        ##### Total Product price & variable #################
                self.cosmetic_price=StringVar()
                self.grocery_price=StringVar()
                self.cold_drink_price=StringVar()

                self.cosmetic_tax=StringVar()
                self.grocery_tax=StringVar()
                self.cold_drink_tax=StringVar()

        ######## Customer ##################
                self.c_name=StringVar()
                self.c_phone=StringVar()
                
                self.bill_no=StringVar()
                x=random.randint(1000, 9999)
                self.bill_no.set(str(x))
                self.search_bill=StringVar()



                ######################### Customer Detail Frame ####################################
                f1=LabelFrame(self.root,bd=10,relief=GROOVE ,text="Customer Details", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
                f1.place(x=0,y=80,relwidth=1)

                cname_lbl = Label(f1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
                cname_text=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
                cphone_lbl = Label(f1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
                cphone_text=Entry(f1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

                c_bill_lbl = Label(f1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
                c_bill_text=Entry(f1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

                bill_btn=Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)


                ########################### Cosmetic Frames #########################
                f2=LabelFrame(self.root,bd=10,relief=GROOVE ,text="Cosmetics", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
                f2.place(x=5,y=170,width=325,height=380)

                bath_label=Label(f2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
                bath_text=Entry(f2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

                facecream_label=Label(f2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
                facecream_txt=Entry(f2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
     
                face_w_label=Label(f2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
                face_w_text=Entry(f2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

                hair_s_label=Label(f2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
                hair_s_text=Entry(f2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

                hair_g_label=Label(f2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
                hair_g_text=Entry(f2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

                body_label=Label(f2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
                body_text=Entry(f2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


                ########################### Grocery Frames #########################
                f3=LabelFrame(self.root,bd=10,relief=GROOVE ,text="Groceries", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
                f3.place(x=340,y=170,width=325,height=380)

                g1_label=Label(f3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
                g1_text=Entry(f3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

                g2_label=Label(f3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
                g2_txt=Entry(f3,width=10,textvariable=self.foodoil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
     
                g3_label=Label(f3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
                g3_text=Entry(f3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

                g4_label=Label(f3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
                g4_text=Entry(f3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

                g5_label=Label(f3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
                g5_text=Entry(f3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

                g6_label=Label(f3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
                g6_text=Entry(f3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


                ########################### Cold Drink Frames #########################
                f4=LabelFrame(self.root,bd=10,relief=GROOVE ,text="Cold Drinks", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
                f4.place(x=670,y=170,width=325,height=380)

                cl_label=Label(f4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
                cl_text=Entry(f4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

                cl_label=Label(f4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
                cl_txt=Entry(f4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
     
                cl_label=Label(f4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
                cl_text=Entry(f4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

                cl_label=Label(f4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
                cl_text=Entry(f4,width=10,textvariable=self.thumbs_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

                cl_label=Label(f4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
                cl_text=Entry(f4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

                cl_label=Label(f4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
                cl_text=Entry(f4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

                ########################## Bill Area ##############################
                f5=Frame(self.root,bd=10,relief=GROOVE)
                f5.place(x=1010,y=170,width=350,height=380)

                bill_title=Label(f5,text="Bill Area",bd=7,relief=GROOVE,font=("Arial",15,"bold")).pack(fill=X)
                scrol_y=Scrollbar(f5,orient=VERTICAL)
                self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)

                ###################### Button Frame ########################
                f6=LabelFrame(self.root,bd=10,relief=GROOVE ,text="Bill Menu", font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
                f6.place(x=0,y=560,relwidth=1,height=200)

                m1_lbl=Label(f6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
                m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1,sticky="w")

                m2_lbl=Label(f6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
                m2_txt=Entry(f6,width=18,textvariable=self.grocery_price,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1,sticky="w")

                m3_lbl=Label(f6,text="Total ColdDrink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
                m3_txt=Entry(f6,width=18,textvariable=self.cold_drink_price,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1,sticky="w")
        
                c1_lbl=Label(f6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
                c1_txt=Entry(f6,width=18,textvariable=self.cosmetic_tax,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1,sticky="w")

                c2_lbl=Label(f6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
                c2_txt=Entry(f6,width=18,textvariable=self.grocery_tax,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1,sticky="w")

                c3_lbl=Label(f6,text="ColdDrink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
                c3_txt=Entry(f6,width=18,textvariable=self.cold_drink_tax,font="arial 18 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1,sticky="w")

                btn_F=Frame(f6,bd=7,relief=GROOVE)
                btn_F.place(x=950,width=550,height=140)

                total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=8,font="arial 15 bold",bd=5).grid(row=0,column=0,padx=5,pady=5)
                GBill_btn=Button(btn_F,text="Generate \nBill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=8,font="arial 15 bold",bd=5).grid(row=0,column=1,padx=5,pady=5)
                clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,width=8,font="arial 15 bold",bd=5).grid(row=0,column=2,padx=5,pady=5)
                exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",pady=15,width=8,font="arial 15 bold",bd=5).grid(row=0,column=3,padx=5,pady=5)
                self.welcome_bill()


        def total(self):
                self.c_s_p=self.soap.get()*40
                self.c_fc_p=self.face_cream.get()*120
                self.c_fw_P=self.face_wash.get()*60
                self.c_hs_p=self.spray.get()*180
                self.c_hg_p=self.gell.get()*140
                self.c_bl_p=self.lotion.get()*180
                self.total_cosmetic_price = float(
                                        self.c_s_p+
                                        self.c_fc_p+
                                        self.c_fw_P+
                                        self.c_hs_p+
                                        self.c_hg_p+
                                        self.c_bl_p
                                        )
                self.cosmetic_price.set(str(self.total_cosmetic_price))
                self.c_tax=round((self.total_cosmetic_price*0.05),2)
                self.cosmetic_tax.set(str(self.c_tax))

                self.g_r_p=self.rice.get()*80
                self.g_fo_p=self.foodoil.get()*180
                self.g_d_p=self.daal.get()*60
                self.g_w_p=self.wheat.get()*240
                self.g_s_p=self.sugar.get()*45
                self.g_t_p=self.tea.get()*150

                self.total_grocery_price = float(
                                        self.g_r_p+
                                        self.g_fo_p+
                                        self.g_d_p+
                                        self.g_w_p+
                                        self.g_s_p+
                                        self.g_t_p
                                        )
                self.grocery_price.set(str(self.total_grocery_price))
                self.g_tax=round((self.total_grocery_price*0.1),2)
                self.grocery_tax.set(str(self.g_tax))

                self.d_m_p=self.maza.get()*60
                self.d_c_p=self.coke.get()*60
                self.d_f_p=self.frooti.get()*50
                self.d_t_p=self.thumbs_up.get()*45
                self.d_l_p=self.limca.get()*40
                self.d_s_p=self.sprite.get()*60


                self.total_drinks_price = float(
                                        self.d_m_p+
                                        self.d_c_p+
                                        self.d_f_p+
                                        self.d_t_p+
                                        self.d_l_p+
                                        self.d_s_p
                                        )
                self.cold_drink_price.set(str(self.total_drinks_price))
                self.d_tax=round((self.total_drinks_price*0.05),2)
                self.cold_drink_tax.set(str(self.d_tax))

                self.total_bill=float(  self.total_cosmetic_price+
                                        self.total_grocery_price+
                                        self.total_drinks_price+
                                        self.c_tax+
                                        self.g_tax+
                                        self.d_tax)
        
        def welcome_bill(self):
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END, "\tWelcome to Retail\n")
                self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
                self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
                self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
                self.txtarea.insert(END, f"\n======================================")
                self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
                self.txtarea.insert(END, f"\n======================================")

        def bill_area(self):
                if self.c_name.get()=="" or self.c_phone.get()=="":
                        messagebox.showerror("Error","Customer Details are must")
                elif self.cosmetic_price.get()=="0.0" and self.grocery_price.get()=="0.0" and self.cold_drink_price.get()=="0.0":
                        messagebox.showerror("Error","No Product Purchased...!")
                else:
                        self.welcome_bill()
                        #cosmetics
                        if self.soap.get()!=0:
                                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
                        if self.face_cream.get()!=0:
                                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
                        if self.face_wash.get()!=0:
                                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_P}")
                        if self.spray.get()!=0:
                                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
                        if self.gell.get()!=0:
                                self.txtarea.insert(END, f"\n Hair Gel\t\t{self.gell.get()}\t\t{self.c_hg_p}")
                        if self.lotion.get()!=0:
                                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")
                        
                        ##Groceries
                        
                        if self.rice.get()!=0:
                                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
                        if self.foodoil.get()!=0:
                                self.txtarea.insert(END, f"\n Food Oil\t\t{self.foodoil.get()}\t\t{self.g_fo_p}")
                        if self.daal.get()!=0:
                                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
                        if self.wheat.get()!=0:
                                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
                        if self.sugar.get()!=0:
                                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
                        if self.tea.get()!=0:
                                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

                        ##ColdDrinks

                        if self.maza.get()!=0:
                                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
                        if self.coke.get()!=0:
                                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
                        if self.frooti.get()!=0:
                                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
                        if self.thumbs_up.get()!=0:
                                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.thumbs_up.get()}\t\t{self.d_t_p}")
                        if self.limca.get()!=0:
                                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
                        if self.sprite.get()!=0:
                                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

                        self.txtarea.insert(END, f"\n--------------------------------------")
                        if self.cosmetic_tax.get()!="0.0":
                                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t\t{self.cosmetic_tax.get()}")
                        
                        if self.grocery_tax.get()!="0.0":
                                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")
                        
                        if self.cold_drink_tax.get()!="0.0":
                                self.txtarea.insert(END, f"\n ColdDrink Tax\t\t\t\t{self.cold_drink_tax.get()}")
                        self.txtarea.insert(END, f"\n Total Bill\t\t\tRs. {self.total_bill}")                
                        self.txtarea.insert(END, f"\n--------------------------------------")
                        self.save_bill()

        def save_bill(self):
                op=messagebox.askyesno("Save Bill ?","Do you want to save the Bill?")
                if op>0:
                        self.bill_data=self.txtarea.get('1.0',END)
                        f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                        f1.write(self.bill_data)
                        f1.close()
                        messagebox.showinfo("Saved",f"Bill no : {self.bill_no.get()} Saved Successfully...!")
                else:
                        return
        
        def find_bill(self):
                present="no"
                for i in os.listdir("bills/"):
                       if i.split('.')[0]==self.search_bill.get():
                               f1=open(f"bills/{i}","r")
                               self.txtarea.delete('1.0',END)
                               for d in f1:
                                        self.txtarea.insert(END, d)
                               f1.close()
                               present="yes"
                if present=="no":
                        messagebox.showerror("Error","Invalid Bill No...!")


        def clear_data(self):
                        self.soap=set(0)
                        self.face_cream=set(0)
                        self.face_wash=set(0)
                        self.spray=set(0)
                        self.gell=set(0)
                        self.lotion=set(0)
                        self.rice=set(0)
                        self.foodoil=set(0)
                        self.daal=set(0)
                        self.wheat=set(0)
                        self.sugar=set(0)
                        self.tea=set(0)
                        self.maza=set(0)
                        self.coke=set(0)
                        self.frooti=set(0)
                        self.thumbs_up=set(0)
                        self.limca=set(0)
                        self.sprite=set(0)

                        self.cosmetic_price=set("")
                        self.grocery_price=set("")
                        self.cold_drink_price=set("")

                        self.cosmetic_tax=set("")
                        self.grocery_tax=set("")
                        self.cold_drink_tax=set("")

                        self.c_name=set("")
                        self.c_phone=set("")
                        
                        self.bill_no=set("")
                        x=random.randint(1000, 9999)
                        self.bill_no.set(str(x))
                        self.search_bill=set("")
                        self.welcome_bill()


        def exit_app(self):
                op=messagebox.askyesno("Exit","Do you really want to exit?")
                if op>0:
                        self.root.destroy()
                
                



        

root=Tk()
obj = bill_App(root)
root.mainloop()