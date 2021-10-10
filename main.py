import tkinter as tk
import pandas as pd

df = pd.read_csv('users.csv')
lf = pd.read_csv('attendance.csv')



def click():
    for j in range(0,len(df)):
        if(entryuser.get() == df.USERNAME[j]):
            if(entrypwd.get() == df.PASSWORD[j]):
                def secondcheck():
                    lf.loc[len(lf)] = [dateentry.get(), studententry.get(), comments.get()]
                    lf.to_csv("attendance.csv", index=False)

            
                
                #window=tk.Tk()
                #window.minsize(800,600)
                #window.configure(bg='#b5faa0')

                #attendance
                attend = tk.Label(window, text = "Attendance",width=25, bg='#b5faa0')
                attend.config(font=('Roboto' , 25))
                attend.grid(row=1,column=1,padx=15,pady=50)

                #studentname
                studentname = tk.Label(window, text='Student Name',fg="#000000", bg="#b5faa0")
                studententry = tk.Entry(window)
                studentname.config(font=('Roboto' , 25))
                studentname.grid(row=2,column=0, padx=50,pady=25)
                studententry.config(font=('Roboto' , 25))
                studententry.grid(row=2,column=1, columnspan = 1, pady=5)
                
                #date
                date = tk.Label(window, text='Date', width=15, fg="#000000", bg="#b5faa0")
                dateentry = tk.Entry(window, width=20)
                date.config(font=('Roboto' , 25))
                date.grid(row=3,column=0, padx=1, pady=30)
                dateentry.config(font=('Roboto' , 25))
                dateentry.grid(row=3,column=1, columnspan = 1, pady=5)

                #comment
                stdcomment = tk.Label(window, text='Comment',fg="#000000", bg="#b5faa0")
                comments = tk.Entry(window, width=20)
                stdcomment.config(font=('Roboto' , 25))
                stdcomment.grid(row=4,column=0, padx=1, pady=30)
                comments.config(font=('Roboto' , 25))
                comments.grid(row=4,column=1, columnspan = 1, pady=5)

                #save button
                savebtn = tk.Button(window, text = " Save ", bg='#FFFFFF', command=secondcheck)
                savebtn.grid(row=5,column=1, pady=30)
                savebtn.config(font=('Roboto' , 20))

                
def clickadd():
    df.loc[len(lf)] = [entryuser.get(), entrypwd.get()]
    df.to_csv("users.csv", index=False)
    #break         

        
window=tk.Tk()
window.minsize(800,600)
#window.maxsize(1000,600)
window.title("EduHelp")
window.configure(bg='#b5faa0')

#Label.config(font=('Roboto' , 25))

teacher = tk.Label(window, text = "Teacher Login", bg='#b5faa0')
teacher.config(font=('Roboto' , 25))
teacher.grid(row=1,column=1,padx=30,pady=60)



#username
Label1 = tk.Label(window, text='Username',fg="#000000", bg="#b5faa0")
entryuser = tk.Entry(window)
Label1.config(font=('Roboto' , 25))
Label1.grid(row=2,column=0, padx=70,pady=20)
entryuser.config(font=('Roboto' , 25))
entryuser.grid(row=2,column=1, columnspan = 1, pady=5)



#password
Label2 = tk.Label(window, text='Password',fg="#000000", bg="#b5faa0")
entrypwd = tk.Entry(window, width=20)
Label2.config(font=('Roboto' , 25))
Label2.grid(row=3,column=0, padx=70, pady=30)
entrypwd.config(font=('Roboto' , 25))
entrypwd.grid(row=3,column=1, columnspan = 1, pady=5)

#submit
button1 = tk.Button(window, text = "Submit", bg='#FFFFFF', command=click)
button1.grid(row=4,column=1, pady=30)
button1.config(font=('Roboto' , 16))

#create new user
createnewuser = tk.Button(window, text = "Add User", bg='#FFFFFF', command=clickadd)
createnewuser.grid(row=5,column=1, pady=30)
createnewuser.config(font=('Roboto' , 16))

window.mainloop()



