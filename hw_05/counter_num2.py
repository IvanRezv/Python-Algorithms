from tkinter import *
tk=Tk()
tk.geometry("440x170")
tk.title("App")
tk.resizable(False,False)
tk["bg"] = "#FFF"

def count_simv():
    print("Введите текст -")
    string=input()
    f={}
    for i in string:
        f[i]=f.get(i,0)+1
    print(f)
    quit()


def count_world():
    s=input("Введите текст ")
    print(len(s.split()))
    quit()


import re
def count_sentences():
    text=input("Введите ваш текст - ")
    new_text = re.sub(r'[.!?]\s', r'|', text)
    sent_num = len(new_text.split('|'))
    print('В этом тексте {} предложения.'.format(sent_num))
    quit()



b1= Button(tk,text="Подсчет символов" , command=count_simv, font=("Times new Roman",12))
b1.place(x=10,y=100,width=120,height=50)

b2= Button(tk,text="Подсчет Слов" , command=count_world, font=("Times new Roman",12))
b2.place(x=155,y=100,width=120,height=50)

b3= Button(tk,text="Подсчет предложений" , command=count_sentences, font=("Times new Roman",12))
b3.place(x=300,y=100,width=120,height=50)

lbl1= Label(tk,text ="Выбери действие", bg="#FFF", font=("Times new Roman",15,"bold"))
lbl1.place(x=155,y=25,width=120,height=50)

tk.mainloop()