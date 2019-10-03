
#?===================Importing Required Libraries==========================

from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pytz import all_timezones, country_timezones, timezone

#?===================Creating and configuring the Root Window==============
root = Tk()
root.title('Dual Clock')
root.resizable(0, 0) #* To restrict resizing the window
root.config(bg='#075E54')
#?=========================================================================

#?====Function to display the window at the center of the screen===========
def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#?=========================================================================

#* To Display System Time, uncomment this
#*  time():
#*  string_01 = strftime('%I:%M:%S %p \n %d-%b-%Y')
#*  lbl.config(text=string_01, bg='#25D366',
#*             fg='#075E54')
#*  lbl.after(1000, time)
#* Use this to display all the TimeZones
#* print(all_timezones)

#?================Function to display German Time==========================
def germantime():
    germany = timezone('Europe/Berlin')
    de_time = datetime.now(germany)
    string_01 = de_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl1.config(text=string_01, bg='#25D366',
                fg='black', borderwidth=2, relief='raised')
    lbl1.after(1000, germantime)
#?=========================================================================

#?================Function to display Indian Time==========================
def indiantime():
    india = timezone('Asia/Kolkata')
    in_time = datetime.now(india)
    string_03 = in_time.strftime('%I:%M:%S %p \n %d-%b-%Y')
    lbl2.config(text=string_03, bg='#075E54',
                fg='white', borderwidth=2, relief='raised')
    lbl2.after(1000, indiantime)
#?==========================================================================

lbl1 = Label(root, font=('calibri', 20, 'bold'))
lbl2 = Label(root, font=('calibri', 20, 'bold'))

#?============================Function Calls================================
center_window(260, 150)
germantime()
indiantime()
#?==========================================================================

#?===============================Windows Size===============================
widthValue = 100
heightValue = 65
#?==========================================================================

#?===============German Flag Source and Configuration=======================
img1 = Image.open('./Images/GermanFlag.png')
img1 = img1.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg1 = ImageTk.PhotoImage(img1)
panel1 = Label(root, image=photoImg1)
panel1.config(borderwidth=2, relief='raised')

#?================Indian Flag Source and Configuration======================
img2 = Image.open('./Images/IndianFlag.png')
img2 = img2.resize((widthValue, heightValue), Image.ANTIALIAS)
photoImg2 = ImageTk.PhotoImage(img2)
panel2 = Label(root, image=photoImg2)
panel2.config(borderwidth=2, relief='raised')
#?==========================================================================

#?==============Aligning the TKinter widgets in a Grid======================
panel1.grid(row=0, column=0, sticky=W, pady=2)
panel2.grid(row=1, column=0, sticky=W, pady=2)
lbl1.grid(row=0, column=1, sticky=W, pady=2)
lbl2.grid(row=1, column=1, sticky=W, pady=2)
#?==========================================================================
root.mainloop()
#216DFF