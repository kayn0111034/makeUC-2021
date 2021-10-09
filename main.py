import tkinter as tk
import pandas as pd

window=tk.Tk()
window.minsize(1200,600)
window.title("hello world")
window.configure(bg='#b5faa0')

#Label.config(font=('Roboto' , 25))

teacher = tk.Label(window, text = "Teacher Login", width=40, height= 10, bg='#b5faa0')

teacher.grid(row=1,column=1,padx=200,pady=200)



#username
Label1 = tk.Label(window, text='Username' , height=3,fg="#FFFFFF", bg="#EA8B31")
entryuser = tk.Entry(window)
Label1.config(font=('Roboto' , 35))
Label1.grid(row=2,column=0, rowspan = 3, padx=175)
entryuser.config(font=('Roboto' , 25))
entryuser.grid(row=2,column=2, columnspan = 1, pady=5)



#password
Label2 = tk.Label(window, text='Username' , height=3,fg="#FFFFFF", bg="#EA8B31")
entrypwd = tk.Entry(window)
Label2.config(font=('Roboto' , 35))
Label2.grid(row=3,column=0, rowspan = 3, padx=175)
entrypwd.config(font=('Roboto' , 25))
entrypwd.grid(row=3,column=2, columnspan = 1, pady=5)

button1 = Button(window, text = "Submit", width=40, height= 10, bg='#FFFFFF')
button1.grid(row=4,column=1,padx=200,pady=200)
window.mainloop()