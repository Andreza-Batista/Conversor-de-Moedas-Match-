#________Importando Tkinter________
from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk

#_________Importando bibliotecas_________
import requests
import json

#________Cores_______
cor0 = "#ffffff" #branco
cor1 = "#000000" #preto
cor2 = "#236e1d" #verde

#_______Janela_______

janela = Tk()
janela.title("Conversor de moedas")
janela.geometry('300x320')
janela.configure(bg= cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
#Use LANCZOS

#________Frames_________

frameCima = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor2, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2)

frameBaixo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief="flat")
frameBaixo.grid(row=1, column=0, sticky=NSEW)

#________função converter________

def converter():

    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrado = valor.get()

    response = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
    dados = json.loads(response.text)
    cambio = dados['rates'][moeda_para]

    resultado = float(valor_entrado) * float(cambio)

    if moeda_para == 'USD':
        simbolo = '$'
    elif moeda_para == 'EUR':
        simbolo = '€'
    elif moeda_para == 'KRW':
        simbolo = '₩'
    elif moeda_para == 'JPY':
        simbolo = '¥'
    elif moeda_para == 'GBP':
        simbolo = '£'
    elif moeda_para == 'CNY':
        simbolo = '¥'
    elif moeda_para == 'BRL':
        simbolo = 'R$'
    else:
        simbolo = '$'

    moeda_equivalente = simbolo + "{:,.2f}".format(resultado)

    app_resultado['text'] = moeda_equivalente

                


#________Configurando frames_________

icon = Image.open('icon.png')
icon = icon.resize((40,40), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)

#Frame de cima
app_nome = Label(frameCima, image=icon, compound=LEFT, text=("Conversor de moedas  "), height=5,padx=13, pady=30, relief='raised', anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_nome.place(x=0,y=0)

#Frame de baixo
app_resultado = Label(frameBaixo, text='', width=16, height=2, relief='solid', anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
app_resultado.place(x=50,y=10)

moeda = ['ARS','AUD','BRL','CAD','CNY','EUR','GBP','JPY','KRW','USD']

app_de = Label(frameBaixo, text='De', width=8, height=1, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_de.place(x=48,y=90)
combo_de = ttk.Combobox(frameBaixo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_de.place(x=50,y=115)
combo_de['values'] = (moeda)

app_para = Label(frameBaixo, text='Para', width=8, height=1, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_para.place(x=158,y=90)
combo_para = ttk.Combobox(frameBaixo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_para.place(x=160,y=115)
combo_para['values'] = (moeda)

valor = Entry(frameBaixo, width=22, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50,y=155)

#Botão Converter
botao = Button(frameBaixo, command=converter, text='Converter', width=19, padx=5, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief='raised', overrelief=RIDGE)
botao.place(x=50,y=200)


janela.mainloop()