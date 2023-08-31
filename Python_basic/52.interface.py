from tkinter import* #é com esse Tkinter que se cria a interface
import pyautogui as pg
import time

def pegar_texto():  #def serve para definir uma função
    a = Entrada.get()
    z = Entrada2.get()
    x = 0

    time.sleep(.2)
    while a<z:
        pg.write(f'{a}, #{x}\n')
        x+=1#esse while serve para 'enquanto a for menor que z\
        #adiciona mais\
        #e ainda tem o 'pg' que substitui o print o qual\
        #serve para escrever os argumentos

root = Tk()#raiz
root.geometry('300x300')#formato do display
root.config(bg='lightblue')#cor de fundo do display gráfico
root.title('Myapp')#esse é o título

Entrada = Entry(root,)
Entrada.place(relx=.3, rely=0.30)
Entrada2 = Entry(root,)
Entrada2.place(relx=.3, rely=0.20)#onde o usuário usa escreve

btn = Button(root, text = 'enviar',
foreground='white',
bg='darkgreen', command=pegar_texto
)
btn.place(relx=0.4,rely=0.40)#botão de enviar

root.mainloop()#o main loop tem que ficar no final
#ele serve para rodar o programa rodar sem parar