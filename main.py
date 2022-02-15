from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import requests

# cores - preta, branca e azul respectivamente

co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"

fundo = "#484f60"

# criando janela
janela = Tk()
janela.title('Bitcoin Now')
janela.geometry('400x400')
janela.configure(bg=fundo)

# dividindo janela
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=200)

frame_cima = Frame(janela, width=400, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)

# função para pegar dados
def info():
    api_link ='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL'

    # HTTP resquests
    response = requests.get(api_link)

    # convertendo os dados em dicionário
    dados = response.json()

    # valor em dolar
    valor_dolar = float(dados['USD'])
    valor_formatado_dolar = "$ {:,.2f}".format(valor_dolar)
    l_dolar['text'] = valor_formatado_dolar

    # valor em euro
    valor_euro = float(dados['EUR'])
    valor_formatado_euro = "€ {:,.2f}".format(valor_euro)
    l_euro['text'] = valor_formatado_euro

    # valor em real
    valor_real = float(dados['BRL'])
    valor_formatado_real = "R$ {:,.2f}".format(valor_real)
    l_real['text'] = valor_formatado_real

    # valor em kz (moeda da angola)
    valor_kz = float(dados['AOA'])
    valor_formatado_kz = "Kz {:,.2f}".format(valor_kz)
    l_kz['text'] = valor_formatado_kz

    frame_baixo.after(1000, info)






# configurando o frame acima
imagem = Image.open('image/bitcoin_2.webp')
imagem = imagem.resize((100,47), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=fundo, relief=FLAT)
l_icon.place(x=0, y=0)

l_nome = Label(frame_cima, text='Bitcoin Price Tracker', bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Aril 20'))
l_nome.place(x=115, y=5)

# configurando o frame baixo
l_dolar = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Aril 20'))
l_dolar.place(x=50, y=50)

l_euro = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Aril 20'))
l_euro.place(x=10, y=150)

l_real = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Aril 20'))
l_real.place(x=10, y=200)

l_kz = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Aril 20'))
l_kz.place(x=10, y=250)

info()

# dividindo janela
janela.mainloop()
