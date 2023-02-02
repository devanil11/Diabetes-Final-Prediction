# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:47:13 2020

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:38:15 2019

@author: USER
"""

import pandas

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.datasets.samples_generator import make_blobs
import selection as slct
from tkinter import *


import matplotlib.pyplot as plt
import matplotlib as rc1
import pandas as pd
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk




master=Tk()
master.title("Diabetes Prediction")
master.geometry("640x640+0+0")
header = Label(master, text="Health Monitoring", font=("arial",30,"bold"), fg="black").pack()
#window.configure(background='blue')

l1=Label(master, text="Glucose",font=("arial", 18)).place(x=10,y=100)
#l1.grid(row=1,column=5)

l2=Label(master, text="BloodP",font=("arial", 18)).place(x=10,y=150)
#l2.grid(row=2,column=5)

l3=Label(master, text="Insulin",font=("arial", 18)).place(x=10,y=200)
#l3.grid(row=3,column=5)

l4=Label(master, text="mass",font=("arial", 18)).place(x=10,y=250)
#l4.grid(row=4,column=5)

l5=Label(master, text="skin",font=("arial", 18)).place(x=10,y=300)
#l5.grid(row=5,column=5)

l6=Label(master, text="Age",font=("arial", 18)).place(x=10,y=350)
#l6.grid(row=6,column=5)

Label(master, text = "Output",font=("arial", 18)).place(x=10,y=400)
#blank = Entry(window)
Output=StringVar()
blank = Entry(master, width=25,bg="white")
blank.place(x=110,y=400)
#blank.grid(row=8, column=5)



glucose=StringVar()
e1=Entry(master, width=25,bg="white",textvariable=l1)
e1.place(x=110,y=100)
#e1.grid(row=1,column=12)

blood_pressure=StringVar()
e2=Entry(master, width=25,bg="white")
e2.place(x=110,y=150)
#e2.grid(row=2,column=12)

skin_thickness=StringVar()
e3=Entry(master, width=25,bg="white")
e3.place(x=110,y=200)
#e3.grid(row=3,column=12)

insulin=StringVar()
e4=Entry(master, width=25,bg="white")
e4.place(x=110,y=250)
#e4.grid(row=4,column=12)

mass=StringVar()
e5=Entry(master, width=25,bg="white")
e5.place(x=110,y=300)
#e5.grid(row=5,column=12)

age=StringVar()                                     
e6=Entry(master, width=25,bg="white")
e6.place(x=110,y=350)
#e6.grid(row=6,column=12)

 
def process_data():
        
        
        glucose = e1.get()
        num_glu = int(float(glucose))

        blood_pressure = e2.get()
        num_pressure = int(float(blood_pressure))

        skin_thickness = e3.get()
        num_skin = int(float(skin_thickness))

        insulin = e4.get()
        num_insulin = int(float(insulin))

        mass = e5.get()
        num_mass = int(float(mass))

        age = e6.get()
        num_age = int(float(age))
	
      
        window=Tk()
        window.title("Diabetes Prediction")
        header = Label(window, text="Health Information", font=("arial",30,"bold"), fg="black").pack()

        canvas2=tk.Canvas(window,width=200,height=150)
        canvas2.pack()
        window.geometry("640x640+0+0")
        plt.rcdefaults()
        names = ['glucose', 'pres', 'skin', 'insulin', 'mass', 'age', 'outcome']
        dataframe = pandas.read_csv("Diabetes1.csv")
        array = dataframe.values
        X = array[:,0:6]
        Y = array[:,6]
        test_size = 0.33
        seed = 5
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
	# Fit the model on 33%
        model = LogisticRegression()
        model.fit(X_train, Y_train)
	# save the model to disk
        filename = 'finalized_model.sav'
        joblib.dump(model, filename)
	# load the model from disk
        loaded_model = joblib.load(filename)
        result = loaded_model.score(X_test, Y_test)
        print(result)
        X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)
        Xnew = [[num_glu, num_pressure, num_skin, num_insulin, num_mass, num_age]]
        ynew = model.predict(Xnew)
        labels=['glucose', 'pres', 'skin', 'insulin', 'mass', 'age']
        sizes=Xnew[0]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue','red']
    
        figure2=Figure(figsize=(5,4),dpi=100)
        subplot2=figure2.add_subplot(111)
    
        explode = (0.1, 0, 0, 0,0,0)
        subplot2.pie(sizes,explode=explode,labels=labels,colors=colors,shadow=True, startangle=140)
 
        #plt.axis('equal')
        pie2=FigureCanvasTkAgg(figure2,window)
        pie2.get_tk_widget().pack()
        #plt.show()
     


    
       # print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
        #print("Did patient found symptoms of diabetise?",result)
        #print("predicted diabetise",result)
        msg1="Did patient found symptoms of diabetise?",ynew[0]
        msg = tk.Message(window, text =msg1)
        msg.config(bg='lightgreen', font=('times', 12, 'italic'))
        msg.pack()
        
        msg2="predicted diabetise",result
        msg3 = tk.Message(window, text =msg2)
        msg3.config(bg='lightgreen', font=('times', 12, 'italic'))
        msg3.pack()
        ans = ("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
        Ans = ynew[0]
        blank.insert(0, Ans)
        window.mainloop()


        
def data():
    

#window =tk. Tk()
#window.title("Registration form")
#window.geometry('800x600+0+0')
#header = Label(window, text="graph", font=("arial",30,"bold"), fg="black").pack() 
    

    font={'family':'Arial','weight':'bold','size':13}   
    rc1.rc('font',**font)


    pf=pd.read_csv('data.csv')
#GUI
    options=list(pf['year'])
    master=tk.Tk()
    canvas1=tk.Canvas(master,width=250,height=150)
    canvas1.pack()

    plt.rcdefaults()
    master.geometry('500x400')
    text=Label(master, text='year wise diabetise patient ratio')
    selectoption=StringVar()
    selectoption.set(options[0])#default
    optionmenu=OptionMenu(master,selectoption,*options)
    text.pack()
    optionmenu.pack()
#crime graph

    def graph():
        op=selectoption.get()
        indx=slct.db(op)
        x_label=['Male','Female','CHILD','PREGNENT+','ppl<40','ppl>40']
        s=pf.iloc[indx,0:10]
        p=list(s)
        freq=p[1:]
        xs = np.arange(len(freq))
        figure2=Figure(figsize=(5,4),dpi=100)
        
        subplot2=figure2.add_subplot(111)
        subplot2.bar(xs,freq)
        
        #plt.ylabel('Count in lakhs')
        #plt.xlabel('people')
        
        subplot2.set_xticklabels(x_label,rotation=45)
        subplot2.set_xlabel('people')
        subplot2.set_ylabel('Count in lakhs')
        plt.title(op)
        pie2=FigureCanvasTkAgg(figure2,master)
        pie2.get_tk_widget().pack()
        #plt.show()
    button=Button(master,text='Search',command=graph)
    button.pack()
    mainloop()
'''
c=pf.iloc[0:45,1]
label=list(pf['year'])
data=list(c)
x=np.arange(len(data))
plt.bar(x,data)
plt.ylabel('RATE')
plt.xticks(x, label,rotation='vertical')
plt.title('Diabetise ratio increased\n ')
plt.show()
    '''
#for district graph
def data1():
    window = Tk()
    
    window.geometry('800x600+0+0')
    header = Label(window, text="Blood Available", font=("arial",30,"bold"), fg="black").pack() 
    

    plt.rcdefaults()
    f=open("blood.txt","r")
    str1=str(f.read())
    list1=str1.split()
    print(list1)

    y=[]
    dff=pd.read_csv('diabetes.csv')
    dff.columns
    sgpa=dff.iloc[:,-1]
    newlist=[]
    for word1 in sgpa:
        flag=0
        for word2 in list1:
            if word1==word2:
                #sgpa=sgpa.fillna(0)
                flag=1
        if flag==0:
            newlist.append(word1)
    #print("\n After removal of stopwords:")
    #print(len(newlist))

    #a11=len(newlist[newlist=='a+'])
#a11=newlist.count('ww')
    #print(a11)

    a=len(sgpa[sgpa=='a+'])
    y.append(a)

    a1=len(sgpa[sgpa=='a-'])
    y.append(a1)

    b=len(sgpa[sgpa=='b+'])
    y.append(a)

    b1=len(sgpa[sgpa=='b-'])
    y.append(b)

    c=len(sgpa[sgpa=='o+'])
    y.append(c)

    c1=len(sgpa[sgpa=='o-'])
    y.append(c1)

    d=len(sgpa[sgpa=='ab+'])
    y.append(d)

    d1=len(sgpa[sgpa=='ab-'])
    y.append(d1)

    labels=['a+','a-','b+','b-','o+','o-','ab+','ab-']
    sizes=y
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue','red','pink','yellow']
    figure2=Figure(figsize=(5,4),dpi=100)
    subplot2=figure2.add_subplot(111)

    explode = (0, 0, 0, 0,0,0,0,0.1)
    subplot2.pie(sizes, explode=explode, labels=labels, colors=colors,
                 autopct='%1.1f%%', shadow=True, startangle=140)
#plt.axis('equal')
    pie2=FigureCanvasTkAgg(figure2,window)
    pie2.get_tk_widget().pack()
#plt.show()
    
    msg2="Total Invald:...",len(newlist)
    msg = tk.Message(window, text =msg2)
    msg.config(bg='lightgreen', font=('times', 12, 'italic'))
    msg.pack()
    
    msg1="Invalid Blood Group..",newlist
    msg = tk.Message(window, text =msg1)
    msg.config(bg='lightgreen', font=('times', 12, 'italic'))
    msg.pack()
    window.mainloop()
    

    

#enter = Button(root, text="Enter Data", width=30, height=5, bg="lightblue", command=enter_data).place(x=250, y=300)
#process=Button(window, text="Process Data", width=30, height=5, bg="lightblue", command=process_data).place(x=500, y=300)
process=Button(master,text="Submit",width=12,command=process_data,font=("arial", 18)).place(x=10,y=500)
process1=Button(master,text="Graph",width=12,command=data,font=("arial", 18)).place(x=230,y=500)
process2=Button(master,text="BloodG",width=12,command=data1,font=("arial", 18)).place(x=450,y=500)
#process.grid(row=9,column=12)
master.mainloop()









