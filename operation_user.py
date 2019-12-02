from tkinter import *
import tkinter.messagebox
################################IMPORTING THE MYSQL CONNECTION##################################################
import mysql.connector
import insert as check
#GLOBAL VARIABLE TIME TO SHOW RUNNING TIME ONSCREEN
time1=''
############################ENCLOSING THE WHOLE WINDOW AS FUNCTION TO PASS IT BY NAME TO OTHER INTERFACE###########################################################################
def operations():
    #IMPORTING TIME LIBRARY
    import time
    #ESTABLISHING CONNECTION WITH THE DATABASE NAME BOOKS
    db = mysql.connector.connect(host="localhost", user="admin", passwd="root", database="books")
    cursor = db.cursor()

    #GLOBAL VARAIBLE COUNT AND CODE TO COUNT THE NUMBER OF THE BOOKS IN THE SYSTEM IN REAL TIME
    count = 0
    cursor.execute("select COUNT(*) FROM newbook")
    for x in cursor:
        count = x[0]

#########################################################################  F  U  N  C  T  I  O  N  S     ##########################################################################

#RESETALL FUNCTION TO RESET ALL THE ENTRIES TO NULL IN THE INTERFACE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def reset_all():
        ent_title.delete(0, END)
        ent_auth.delete(0, END)
        ent_genre.delete(0, END)
        ent_publish.delete(0, END)



#FUNCTION TO SHOW ALL THE BOOKS STARTING FROM ID=1 ORDERED BY ID@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def showall():
        outputbox.delete(0, END)
        cursor.execute("SELECT Title,Author,Genre,Publisher FROM newbook")
        for x in cursor:
            outputbox.insert(END, x)





#FUNCTION SEARCH BY USING THE TITLE AS REFERENCE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def title_search():
        outputbox.delete(0, END)
        a = titl.get()
        #SEARCHING BY STRING IN TITLE NO NEED TO TYPE FULL TITLE
        b = "SELECT Title,Author,Genre,Publisher FROM newbook WHERE Title like '%" + str(a) + "%'"
        cursor.execute(b)
        rows = cursor.fetchall()
        #SHOWING RESULT TO LISTBOX
        for x in rows:
            outputbox.insert(END, x)

#FUNCTION SEARCH BY GENRE AS REFERENCE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def genre_search():
        outputbox.delete(0, END)
        d = genr.get()
        cursor.execute("SELECT Title,Author,Genre,Publisher FROM newbook WHERE Genre like '%" + str(d) + "%'")

        rows = cursor.fetchall()
        for x in rows:
            outputbox.insert(END, x)

#FUNCTION SEARCH BY PUBLISHER AS REFERNCE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def publisher_search():
        outputbox.delete(0, END)
        c = publ.get()
        cursor.execute("SELECT Title,Author,Genre,Publisher FROM newbook WHERE Publisher like '%" + str(c) + "%'")

        rows = cursor.fetchall()
        for x in rows:
            outputbox.insert(END, x)

#FUNCTION SEARCH BY AUTHOR AS REFERENCE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def author_search():
        outputbox.delete(0, END)
        b = author.get()
        cursor.execute("SELECT Title,Author,Genre,Publisher FROM newbook WHERE Author LIKE '%" + str(b) + "%'")

        rows = cursor.fetchall()
        for x in rows:
            outputbox.insert(END, x)

#FUNCTION TO GET THE DATA FROM LISTBOX AND PLACE IT INTO THE RESPECTIVE ENTRY BOXES@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def get_row(event):
        index = outputbox.curselection()[0]
        selected_tuple = outputbox.get(index)
        ent_title.delete(0, END)
        ent_title.insert(END, selected_tuple[0])
        ent_auth.delete(0, END)
        ent_auth.insert(END, selected_tuple[1])
        ent_genre.delete(0, END)
        ent_genre.insert(END, selected_tuple[2])
        ent_publish.delete(0, END)
        ent_publish.insert(END, selected_tuple[3])


##################################################   S T A R T I N G  O F  I N T E R F A C E   ####################################################################################

#DECLARING THE WINDOW WITH A WINDO AS OBJECT$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    windo = Tk()
    windo.config(bg="#dfffc9")
    windo.attributes('-fullscreen', True)
    windo.title("search box")

#DECLARING T AS TOP LABEL AND PACKING IT TO ACQUIRE WHOLE WIDTH$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    T = Label(windo, text="WELCOME TO THE BOOKSTORE", bg="black", fg="red", width=100,
              font=("Helvetica", 30, "bold italic"),
              height=2)
    T.pack()

#DECLARING M_FRAME AS A FRAME ENCLOSING ELEMENT AS GRID WITHIN PLACE ARRANGEMENT$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    m_frame = Frame(windo,bg="#dfffc9")
    m_frame.place(anchor=(W), rely=0.55, relx=0.03)

    #ENTRY AND LABEL OF THE TITLE ATTRIBUTE OF THE BOOK AND TEXT VARIABLE AS TITL
    label_titl = Label(m_frame, text="TITLE", font=('ARIAL', 10, "bold italic"),bg="#dfffc9")
    label_titl.grid(row=0, column=0, sticky=(W), padx=5, pady=3)

    titl = StringVar()
    ent_title = Entry(m_frame, font=('ARIAL', 10, "bold italic"), textvariable=titl, bd=5, width=50,bg="#d2f7c8")
    ent_title.grid(row=1, column=0, padx=5, pady=3, sticky=(W))

    #ENTRY AN LABEL FOR GENRE ATTRIBUTE OF BOOK AND TEXT VARIABLE AS GENR
    genre_titl = Label(m_frame, text="GENRE", font=('ARIAL', 10, "bold italic"),bg="#dfffc9")
    genre_titl.grid(row=2, column=0, sticky=(W), padx=5, pady=3)

    genr = StringVar()
    ent_genre = Entry(m_frame, textvariable=genr, font=('ARIAL', 10, "bold italic"), bd=5, width=50,bg="#d2f7c8")
    ent_genre.grid(row=3, column=0, sticky=(W), padx=5, pady=3)

    #ENTRY AND LABEL FOR PUBLISHER OF BOOK AND TEXT VARIABLE AS PUBL
    publish_titl = Label(m_frame, text="PUBLISHER", font=('ARIAL', 10, "bold italic"),bg="#dfffc9")
    publish_titl.grid(row=4, column=0, sticky=(W), padx=5, pady=3)

    publ = StringVar()
    ent_publish = Entry(m_frame, font=('ARIAL', 10, "bold italic"), textvariable=publ, bd=5, width=50,bg="#d2f7c8")
    ent_publish.grid(row=5, column=0, padx=5, pady=3, sticky=(W))

    #ENTRY AND LABEL FOR AUTHOR OF BOOK AND TEXT VARIABLE AS AUTHOR
    auth_titl = Label(m_frame, text="AUTHOR", font=('ARIAL', 10, "bold italic"),bg="#dfffc9")
    auth_titl.grid(row=6, column=0, sticky=(W), padx=5, pady=3)

    author = StringVar()
    ent_auth = Entry(m_frame, font=('ARIAL', 10, "bold italic"), textvariable=author, bd=5, width=50,bg="#d2f7c8")
    ent_auth.grid(row=7, column=0, sticky=(W), padx=5, pady=3)

    #BUTTON FOR SEARCH BY TITLE
    but1 = Button(m_frame, text="SEARCH BY TITLE", height=1, width=20, font=('ARIAL', 10, "bold italic"), bd=5,
                  command=title_search,cursor="hand2",bg="black",fg="white",activebackground="#d2f7c8")
    but1.grid(row=1, column=1, padx=1, sticky=(W))

    #BUTTON FOR SEARCH BY GENRE
    but1 = Button(m_frame, text="SEARCH BY GENRE", height=1, width=20, font=('ARIAL', 10, "bold italic"), bd=5,
                  command=genre_search,cursor="hand2",bg="black",fg="white",activebackground="#d2f7c8")
    but1.grid(row=3, column=1, padx=1, sticky=(W))

    #BUTTON FOR SEARCH BY PUBLISHER
    but1 = Button(m_frame, text="SEARCH BY PUBLISHER", height=1, width=20, font=('ARIAL', 10, "bold italic"), bd=5,
                  command=publisher_search,cursor="hand2",bg="black",fg="white",activebackground="#d2f7c8")
    but1.grid(row=5, column=1, padx=1, sticky=(W))

    #BUTTON FOR SEARCH BY AUTHOR
    but1 = Button(m_frame, text="SEARCH BY AUTHOR", height=1, width=20, font=('ARIAL', 10, "bold italic"), bd=5,
                  command=author_search,cursor="hand2",bg="black",fg="white",activebackground="#d2f7c8")
    but1.grid(row=7, column=1, padx=1, sticky=(W))

########################################   B U T T O N S    ############################################################
    logo = PhotoImage(file="hop.png")
    imgl = Label(m_frame, image=logo)
    imgl.grid(row=0, column=2,rowspan=7)

    #SHOW ALL BOOKS BUTTON
    show = Button(m_frame, text="SHOW ALL BOOKS", height=1, width=25, font=('ARIAL', 10, "bold italic"), bd=5,
                  command=showall,cursor="hand2",bg="#03012e",fg="white",activebackground="#d2f7c8")
    show.grid(row=7, column=2, padx=120, sticky=(E))


    #RESET ALL ENTRIES BUTTON
    reset = Button(m_frame, text="RESET ALL ENTRIES", height=1, width=25, font=('ARIAL', 10, "bold italic"), bd=5,
                         command=reset_all, cursor="hand2",bg="#5d6b02",fg="white",activebackground="#d2f7c8")
    reset.grid(row=1, column=3, sticky=(W))

    #QUIT THE WINDOW BUTTON
    quit = Button(m_frame, text="EXIT (X)", height=1, width=25, font=('ARIAL', 10, "bold italic"), bd=5,
                   command=windo.destroy, cursor="hand2",bg="#730909",fg="white",activebackground="#d2f7c8")
    quit.grid(row=3, column=3, sticky=(W))

############################################### COUNT AND TIME LABLES  #################################################

    #DHOW THE COUNT OF THE NUMBER OF BOOK
    no_books = Label(m_frame, text="TOTAL BOOKS\t"+str(count), height=1, font=('ARIAL', 10, "bold italic"),bg="#dfffc9")
    no_books.grid(row=5, column=3, sticky=(W))

    #SHOW THE REAL TIME USING THE FUNCTION TICK()
    clock = Label(m_frame, height=1, font=('ARIAL', 10, "bold italic"),bg="#dfffc9")
    clock.grid(row=7, column=3, sticky=(W))
    time1 = ''
#FUNCTION TO ENALBES THE RUNNING CLOCK IN  THE INTERFACE@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def tick():
        global time1
        time2 = time.strftime('%H:%M:%S')

        if time2 != time1:
            #UPDATING THE GLOBAL VARIABLE TIME1
            time1 = time2
            #SETTING THE RUUNING CLOCK TO CLOCK LABEL
            clock.config(text="CLOCK:\t"+time2+"\tIST")

        #REFERSHING CLOCK AFTER EVERY 200 MS
        clock.after(200, tick)
    #CALLING THE TICK
    tick()
############################################# L    I    S    T    B    O    X   #################################################################

    outputbox = Listbox(m_frame, height=15, width=200, bd=9,cursor="hand2",bg="#d2f7c8")
    outputbox.grid(row=8, column=0, columnspan=30, sticky=(W), pady=30)

    #BINDING THE LISTBOX WITH GETROW FUNCTION AND <<LISYTBOX>> ATTRIBUTE TO SLECT DATA FROM IT
    outputbox.bind('<<ListboxSelect>>', get_row)
###LOOPING THE WINDOW
    windo.mainloop()
############################################# E N D   O F    P R O G R A M ##########################################################################################################



