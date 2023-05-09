from tkinter import*
from tkinter import ttk

def valBarra(m):
    cont = 0
    etapas = m/10
    while cont < etapas:
        cont += 1
        i = 0
        while i < 100000:
            i = i + 1
            varBarra.set(cont)
            root.update


root =Tk()
root.title("pika")
root.geometry("300x300")

varBarra = DoubleVar()
varBarra.set(0)

progressbar = ttk.Progressbar(root, variable=varBarra, maximum=100)
progressbar.place(x = 0, y = 0, width=300, height=40)

btn = Button(root, text='definir barra', command=lambda:valBarra(1000))
btn.place(x=0, y=50, width=100, height=40)


root.mainloop()