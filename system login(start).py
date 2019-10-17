from tkinter import *
###################IMPORTING THE PASSDATA FILE FOR LOGIN & SIGNUP FUNCTIONS ######################################
import passdata as p
###################IMPORTING OPERATION_SDU FILE WHICH CONTAINS THE ORIGINAL PROGRAM######################
import operation_sdu as s

######################################################SIGNUP FUNCTION ###################################################################################
def signup():
    user = un_ent.get()
    passw = ps_ent.get()
    ms=ms_ent.get()
    if(p.signup(user,passw,ms)):
        l = Label(mainframe, text="You Have Successfully Created Account.", width=30)
        l.grid(column=2, row=4, columnspan=2)
    else:
        l = Label(mainframe, text="check the credentials you entered", width=30)
        l.grid(column=2, row=4, columnspan=2)


#######LOG FUNCTION HANLING THE LOGIN SECURITY BY IMPORTING DATA FROM PASSDATA FILE p AS OBJECT##################################################################################
def log():
    ########### GETTING DATA FROM USERNAME AND PASSWORD ENTRIES#########################################
    user=un_ent.get()
    passw=ps_ent.get()
    ############# CHECKING THE VALIDITY OF CREDENTIALS ################################################
    if(p.read(user,passw)):
        # DESTROYING THE LOGIN WINNDOW UPON VERIFICATION
        window.destroy()
        # OPENING THE OPERATIONS FILE
        s.operations()

    ############## IF VERIFICATION FAILS IT AGAIN ASKS FOR PASSWORD   #################################
    else:
        un_ent.delete('0', END)
        un_ent.insert(END, "invalid")

        ps_ent.delete('0', END)
        ps_ent.insert(END, "invalid")

        #A LABEL WILL APPEARS SHOWING ABOUT THE INVALIDITY
        l = Label(mainframe, text="check the credentials you entered", width=30)
        l.grid(column=2, row=4, columnspan=2)

############################INITIALIZING THE GUI INTERFACE WITH VARIABLE WINDOW###################################################################################################
window=Tk()
window.state('zoomed')
window.title("LOGIN TO BOOKSTORE")
window.config(bg="lightgreen")
window.colormapwindows()

############ H LABEL FOR HHEADING OF BOOKSTORE ########################################################
H=Label(window,text="BOOKSTORE",height=3,width=100,fg="white",bg="#000000",font=("Helvetica", 30, "bold italic"))
H.pack()
############### M LABEL FOR LOGIN HEADING #############################################################
M=Label(window,text="LOGIN",height=1,width=100,fg="#000000",font=("Helvetica", 30, "bold italic"))
M.pack()

############ DECLARING A FRAME WITH PLACE AND EMBEDDED GRID SYSTEM######################################################
mainframe=Frame(window,bg="lightgreen")
mainframe.place(relx=0.7,rely=0.4, anchor=NE)

####### LABELS: USERNAME AND PASSWORD
un = Label(mainframe, text="User Name",fg="black",font=('Copperplate Gothic Bold',16,"bold"),bg="lightgreen")
un.grid(column=0,row=0)

ps = Label(mainframe, text="Password",fg="black",font=('Copperplate Gothic Bold',16,"bold"),bg="lightgreen")
ps.grid(column=0,row=1)

ms = Label(mainframe, text="Master Code",fg="black",font=('Copperplate Gothic Bold',16,"bold"),bg="lightgreen")
ms.grid(column=0,row=2)
#USER STRINGVAR TO GET THE USERNAME FROM UN_ENT
user=StringVar()
un_ent=Entry(mainframe,width=40,bd=3,font=('Monotype Corsiva',12))
un_ent.grid(column=1,row=0,ipadx=5,ipady=5,padx=8,pady=8,columnspan=4,sticky=W)

#PASSWORD STRINGVAR TO GET THE PASSWORD FROM PASS_ENT
passw=StringVar()
ps_ent=Entry(mainframe,width=40,bd=3,font=('Monotype Corsiva',12))
ps_ent.grid(column=1,row=1,ipadx=5,ipady=5,padx=8,pady=8,columnspan=4,sticky=W)
#PASSWORD STRINGVAR TO GET THE PASSWORD FROM PASS_ENT
ms=StringVar()
ms_ent=Entry(mainframe,width=40,bd=3,font=('Monotype Corsiva',12))
ms_ent.grid(column=1,row=2,ipadx=5,ipady=5,padx=8,columnspan=4,sticky=W)

#DECLARING THE LOGIN BUTTON WHICH CONTAINS THE LOG() FUNCTION
but_login=Button(mainframe,text="LOGIN",width=8,height=1,font=('Copperplate Gothic Bold',16,"bold italic"),bd=4,bg="#000000",activebackground="grey",fg="white",
                 command=log,cursor="hand2")
but_login.grid(column=2,row=3,sticky=(E),pady=20)

but_sign=Button(mainframe,text="SIGNUP",width=8,height=1,font=('Copperplate Gothic Bold',16,"bold italic"),bd=4,bg="#000000",activebackground="grey",fg="white",
                 command=signup,cursor="hand2")
but_sign.grid(column=3,row=3,sticky=(E),pady=20)
######################LOOPING THE WINDOW#########################################################################################################################################
window.mainloop()
