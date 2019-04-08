from tkinter import *
from math import *

def number_button(num):
    text1.insert(END,str(num))

def clear():
    text1.delete(0,END)

root=Tk()
root.title('Калькулятор')
root.resizable(0,0)

frame1=Frame(root)
frame1.pack(side=TOP,pady=5)

frame2=Frame(root)
frame2.pack(side=LEFT,anchor=N,pady=5,padx=5)

text1=Entry(frame1,font='Arial 30',justify='right',bd=20,insertwidth=-1)
text1.pack(side=RIGHT,anchor=N)

#1 ryad
b_b=Button(frame2, text='n!',width=3, bd=8,fg='turquoise',font='Arial 30',command=factorial)
b_b.grid(row=1,column=1)
b_ce=Button(frame2,text='CE',width=3,bd=8,fg='turquoise',font='Arial 30',command=clear)
b_ce.grid(row=1,column=2)
b_c=Button(frame2,text='C',width=3,bd=8,fg='turquoise',font='Arial 30',command=clear)
b_c.grid(row=1,column=3)
b_p_m=Button(frame2,text='sqrt',width=3,bd=8,fg='turquoise',font='Arial 30',command=sqrt)
b_p_m.grid(row=1,column=4)
b_sqrt=Button(frame2,text='^',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button('**'))
b_sqrt.grid(row=1,column=5)

#2 ryad
b_7=Button(frame2,text='7',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(7))
b_7.grid(row=2,column=1)
b_8=Button(frame2,text='8',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(8))
b_8.grid(row=2,column=2)
b_9=Button(frame2,text='9',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(9))
b_9.grid(row=2,column=3)
b_sp=Button(frame2,text='/',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button('/'))
b_sp.grid(row=2,column=4)
b_sm1=Button(frame2,text='(',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button('('))
b_sm1.grid(row=2,column=5)

#3 ryad
b_4=Button(frame2,text='4',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(4))
b_4.grid(row=3,column=1)
b_5=Button(frame2,text='5',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(5))
b_5.grid(row=3,column=2)
b_6=Button(frame2,text='6',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(6))
b_6.grid(row=3,column=3)
b_x=Button(frame2,text='*',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button('*'))
b_x.grid(row=3,column=4)
b_sm2=Button(frame2,text=')',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(')'))
b_sm2.grid(row=3,column=5)

#4 ryad
b_1=Button(frame2,text='1',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(1))
b_1.grid(row=4,column=1)
b_2=Button(frame2,text='2',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(2))
b_2.grid(row=4,column=2)
b_3=Button(frame2,text='3',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(3))
b_3.grid(row=4,column=3)
b_mn=Button(frame2,text='-',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button('-'))
b_mn.grid(row=4,column=4)
b_eq = Button(frame2,text='=',width=3,height=3, bd=8, fg="turquoise",font='Arial 30',command=lambda:number_button('='))
b_eq.grid(row=4,column=5, rowspan=2)

#5 ryad
b_0=Button(frame2,text='0',width=8,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button(0))
b_0.grid(row=5,column=1,columnspan=2)
b_t=Button(frame2,text=',',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button('.'))
b_t.grid(row=5,column=3)
b_p=Button(frame2,text='+',width=3,bd=8,fg='turquoise',font='Arial 30',command=lambda:number_button('+'))
b_p.grid(row=5,column=4)

root.mainloop()


