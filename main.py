import tkinter as tk
import pandas as pd

df = pd.read_csv('users.csv')
lf = pd.read_csv('attendencecount.csv')




def click():
    for j in range(0,len(df)):
        if(entryuser.get() == df.USERNAME[j]):
            if(entrypwd.get() == df.PASSWORD[j]):
                secondwindow=tk.Tk()
                secondwindow.minsize(800,600)
                secondwindow.configure(bg='#b5faa0')
                #studentname
                studentname = tk.Label(secondwindow, text='Student Name',fg="#000000", bg="#b5faa0")
                studententry = tk.Entry(secondwindow)
                studentname.config(font=('Roboto' , 25))
                studentname.grid(row=2,column=0, padx=1)
                studententry.config(font=('Roboto' , 25))
                studententry.grid(row=2,column=2, columnspan = 1, pady=5)
                
                #date
                date = tk.Label(secondwindow, text='Date',fg="#000000", bg="#b5faa0")
                dateentry = tk.Entry(secondwindow, width=20)
                date.config(font=('Roboto' , 25))
                date.grid(row=3,column=0, padx=1, pady=5)
                dateentry.config(font=('Roboto' , 25))
                dateentry.grid(row=3,column=2, columnspan = 1, pady=5)


                

        
window=tk.Tk()
window.minsize(800,600)
#window.maxsize(1000,600)
window.title("hello world")
window.configure(bg='#b5faa0')

#Label.config(font=('Roboto' , 25))

teacher = tk.Label(window, text = "Teacher Login", bg='#b5faa0')
teacher.config(font=('Roboto' , 25))
teacher.grid(row=1,column=0,padx=15,pady=15)



#username
Label1 = tk.Label(window, text='Username',fg="#000000", bg="#b5faa0")
entryuser = tk.Entry(window)
Label1.config(font=('Roboto' , 25))
Label1.grid(row=2,column=0, padx=1)
entryuser.config(font=('Roboto' , 25))
entryuser.grid(row=2,column=2, columnspan = 1, pady=5)



#password
Label2 = tk.Label(window, text='Password',fg="#000000", bg="#b5faa0")
entrypwd = tk.Entry(window, width=20)
Label2.config(font=('Roboto' , 25))
Label2.grid(row=3,column=0, padx=1, pady=5)
entrypwd.config(font=('Roboto' , 25))
entrypwd.grid(row=3,column=2, columnspan = 1, pady=5)

button1 = tk.Button(window, text = "Submit", bg='#FFFFFF', command=click)
button1.grid(row=4,column=2, pady=30)
button1.config(font=('Roboto' , 20))

window.mainloop()



