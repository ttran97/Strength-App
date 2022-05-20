#Tony Tran 5/20/2022
#Simple Strength Application Side Project GUI - Completed at 5/20/2022
from tkinter import * 
from tkinter import ttk
#Create a GUI myframe
class MyFrame(Frame):  
    def __init__(self, root):
        Frame.__init__(self, root)
        self.welcome()
#Clear out widget
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
#Exit application
    def exit_application(self):
        '''Exits the program'''
        root.destroy()
#User will see the options to calculate their 1RM or view 1RM chart
    def welcome(self):
        self.clear_frame()
        Label(self, text ="**Strength App**").pack() 
        self.btn_calculator = Button(self, text="1RM calculator", background= "Light Blue", command =self.strength_calculator).pack()
        self.btn_strengthchart = Button(self, text="Strength 1RM chart", background = "Light Green", command =self.show_strength_chart).pack()
        self.btn_exit=Button(self, text = "Exit Application", background = 'gray', command=self.exit_application).pack()
        
#1RM chart 
    def show_strength_chart(self): 
        self.clear_frame()
        strength_label1 = Label(self, text = "**Strength One Rep Max Chart**", foreground = "Blue")
        strength_label1.pack()
        set = ttk.Treeview(self) #Implement Treeview to see the chart in excel format
        set.pack()

        set['columns']= ('Reptitions', 'Percentage of 1RM','Multiply Weight Lifted By:')
        set.column("#0", width=0,  stretch=NO)
        set.column("Reptitions",anchor=CENTER, width=80)
        set.column("Percentage of 1RM",anchor=CENTER, width=200)
        set.column("Multiply Weight Lifted By:",anchor=CENTER, width=200)

        set.heading("#0",text="",anchor=CENTER)
        set.heading("Reptitions",text="Reptitions",anchor=CENTER)
        set.heading("Percentage of 1RM",text="Percentage of 1RM",anchor=CENTER)
        set.heading("Multiply Weight Lifted By:",text="Multiply Weight Lifted By:",anchor=CENTER)

        set.insert(parent='',index='end',iid=0,text='',
        values=('1','100%','1.00'))
        set.insert(parent='',index='end',iid=1,text='',
        values=('2','95%',"1.05"))
        set.insert(parent='',index='end',iid=2,text='',
        values=('3','93%','1.08'))
        set.insert(parent='',index='end',iid=3,text='',
        values=('4','90%','1.11'))
        set.insert(parent='',index='end',iid=4,text='',
        values=('5','87%',"1.15"))
        set.insert(parent='',index='end',iid=5,text='',
        values=('6','85%','1.18'))
        set.insert(parent='',index='end',iid=6,text='',
        values=('7','83%','1.20'))
        set.insert(parent='',index='end',iid=7,text='',
        values=('8','80%',"1.25"))
        set.insert(parent='',index='end',iid=8,text='',
        values=('9','77%','1.30'))
        set.insert(parent='',index='end',iid=9,text='',
        values=('10','75%','1.33'))
        set.insert(parent='',index='end',iid=10,text='',
        values=('11','70%',"1.43"))
        set.insert(parent='',index='end',iid=11,text='',
        values=('12','67%','1.49'))
        self.btn_exit=Button(self, text = "Go Back", background = 'green', command=self.welcome).pack() 
        self.btn_exit=Button(self, text = "Exit Application", background = 'gray', command=self.exit_application).pack() 
        

#1RM calculator to see their strength limit
    def strength_calculator(self):
        self.clear_frame()
        weight_label = Label(root,text="Enter training weight (ibs) here: ", padx=12, pady=10)
        weight_label.grid(row=2, column=0, sticky=W)

        weight_input = Entry(root)
        weight_input.grid(row=2, column=1)

        reps_input = Entry(root)
        reps_input.grid(row=3, column=1)
        reps_label = Label(root,text="Enter your repetitions here: ", padx=12)
        reps_label.grid(row=3, column=0, sticky=W)
        def calculate():
            weight = int(weight_input.get())
            reps = int(reps_input.get())
            one_rm = round(weight*(1+(reps/30))) #Implement 1RM equation to calculate users 1RM
            #Display the result of 1 Rep Max
            result_label = Label(root, text="1 Rep Max is: " + str(one_rm) + " ibs")
            result_label.grid(row=4)
            weight_input.delete(0,END)
            reps_input.delete(0,END)

        self.btn_exit=Button(self, text = "Exit Application", background = 'gray', command=self.exit_application)
        self.btn_exit.grid(row=15,column=6) 

        calculate_button = Button(root,text="Calculate",command=calculate, width=16 )
        calculate_button.grid(row=4,column=1,pady=10)
#Pyhton tkinter frame GUI
root = Tk() 
root.title("Strength App")
t1 = MyFrame(root) 
t1.grid()
root.mainloop()
