from tkinter import *
import operation_sdu as s
def frontpage():
    front = Tk()
    front.title("BOOKSTORE PORTAL")
    front.geometry("1200x1200")
    front.colormapwindows()

    def searchit():
        s.search()

    Tu = Label(front, text="BOOKSTORE PORTAL", font=('ARIAL', 30, "bold italic"), width=100, height=3, bg="lightblue")
    Tu.pack()

    mainframe = Frame(front)
    mainframe.place(anchor=(W), rely=0.58, relx=0.03)

    but_search=Button(mainframe,text="SEARCH\nDELETE\nUPDATE",width=10,bd=10,bg="black",fg="white", font=('ARIAL', 30, "bold italic"),command=searchit)
    but_search.grid(column=0,row=0,sticky=(W))
    front.mainloop()
