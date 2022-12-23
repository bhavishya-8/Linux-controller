import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import file1
import subprocess
from tkinter.messagebox import showwarning



# Main Window Commands
window = tk.Tk()
window.title('Linux controller')
# width, height = window.winfo_screenwidth()/1.6, window.winfo_screenheight()/1.5
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
window.configure(background='light steel blue')



# folder_path = StringVar()

message = tk.Label(window,  text = "Linux controller", bg="slate blue", fg="black", height=2, width=int(window.winfo_screenwidth()/2), font=('times', 30, 'italic bold ')).pack()

#frames left and right
# terminal_result = tk.Label(window, text="Terminal Result: ", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
# terminal_result.place(x=650, y=130)

# dataFrameRight = Frame(window, bd=10, padx=20, relief=RIDGE)
# dataFrameRight.place(x=650, y=170, width=590, height=400)

# termf = Frame(window)
# dataFrameRight.pack(side=BOTTOM, fill=X)
# id=dataFrameRight.winfo_id()
# try:
#     p = subprocess.Popen(
#         ["xterm", "-into", str(id), "-geometry", "80x20"],
#         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# except FileNotFoundError:
#    showwarning("Error", "xterm is not installed")
#    raise SystemExit 


this = tk.Label(window, text="Choose the name of the command", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this.place(x=50, y=100)
this.pack(padx=20 ,pady=40 ,anchor="w")

this_1 = tk.Label(window, text="1 --> Date", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_1.place(x=50, y=120)
this_1.pack(padx=50 ,pady=5 ,anchor="w")

this_2 = tk.Label(window, text="2 --> Calender", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_2.place(x=50, y=140)
this_2.pack(padx=50 ,pady=5 ,anchor="w")

this_3 = tk.Label(window, text="3 --> SSH", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_3.place(x=50, y=160)
this_3.pack(padx=50 ,pady=5 ,anchor="w")

this_4 = tk.Label(window, text="4 --> Configure httpd server", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_4.place(x=50, y=180)
this_4.pack(padx=50 ,pady=5 ,anchor="w")

this_5 = tk.Label(window, text="5 --> Exit", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_5.place(x=50, y=200)
this_5.pack(padx=50 ,pady=5 ,anchor="w")

#invoking the IP address input

# def ip_window():
#    ip_input_window = tk.Label(window, text="Enter choice:", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
#    ip_input_window.place(x=20, y=460)

#    ip_varible = tk.Entry(window, width=40, bg="linen", fg="gray9",font=('times', 15, ' bold '))
#    ip_varible.place(x=150, y=480)

# URL Message

def prt():
#    print(url.get())
   file1.opt(url.get())


lbl_url = tk.Label(window, text="Enter choice:", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
lbl_url.place(x=20, y=440)

url = tk.Entry(window, width=40, bg="linen", fg="gray9",font=('times', 15, ' bold '))
url.place(x=150, y=450)


# # Path Message
# lbl_path = tk.Label(window, text="Enter Path :", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
# lbl_path.place(x=20, y=490)

# path = tk.Entry(window, width=40, bg="linen", fg="gray9", font=('times', 15, ' bold '))
# path.place(x=150, y=500)

#button
# clearButton = tk.Button(window, text="Clear",fg="black" ,bg="dark turquoise" ,width=10 ,height=2 , activebackground = "Red" ,font=('times', 15, ' bold '))
# clearButton.place(x=180, y=570)

#Partition Line



# Add a line in canvas widget
# canvas.create_line(25,40,25,40, fill="green", width=5)


down = tk.Button(window, text="Enter", fg="black" ,bg="yellow green" ,width=10 ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '), command=prt)
down.place(x=250, y=500)


# message = tk.Label(window,  text = "", bg="slate blue",
#             fg="black", height=1, width=int(window.winfo_screenwidth()/2), font=('times', 30, 'italic bold ')).pack(side = BOTTOM)
# sep = ttk.Separator(window, orient='vertical')
# sep.pack(padx=5, pady=5, fill= tk.Y, expand= True)





window.mainloop()
