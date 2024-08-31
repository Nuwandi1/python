from tkinter import*

def add():
    a=int(txt1.get("1.0","end-1c"))
    b=int(txt2.get("1.0","end-1c"))
    print(a+b)
def sub():
    a=int(txt1.get("1.0","end-1c"))
    b=int(txt2.get("1.0","end-1c"))
    print(a-b)
def multi():
    a=int(txt1.get("1.0","end-1c"))
    b=int(txt2.get("1.0","end-1c"))
    print(a*b)
def div():
    a=int(txt1.get("1.0","end-1c"))
    b=int(txt2.get("1.0","end-1c"))
    print(a/b)

calculator=Tk()
calculator.title("GUL Calculator")
calculator.geometry("400x600")

lbl1 =Label(calculator,text="First Number:")
lbl2 =Label(calculator,text="Second Number:")

btn1= Button(calculator,text="Add",command=add,height=2,width=20)
btn2= Button(calculator,text="Sub",command=sub,height=2,width=20)
btn3= Button(calculator,text="Multiply",command=multi,height=2,width=20)
btn4= Button(calculator,text="Divide",command=div,height=2,width=20)

txt1=Text(calculator,height=2,width=20)
txt2=Text(calculator,height=2,width=20)

lbl1.pack()
txt1.pack()
lbl2.pack()
txt2.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()