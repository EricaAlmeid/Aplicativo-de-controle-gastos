from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk


# cores
co0 = "#2e2d2b"  # Preto
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  #
co11 = "#f2f4f2"
co12 = "#E0FFFF" #LightCyan
co13 = "#6A5ACD" #SlateBlue
co14 = "#836FFF" #SlateBlue1

## Janela ##

janela = Tk()
janela.title("")
janela.geometry('250x400')
janela.configure(background=co12)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

### Frames ###

frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio= Frame(janela, width=300, height=90, bg=co14, relief="flat")
frameMeio.grid(row=1, column=0)

frameBixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
frameBixo.grid(row=2, column=0)

# Logo

app_ = Label(frameCima, text='Orçamento', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Arial 20'), bg=co1, fg=co4)
app_.place(x=0, y=0)

# imagem
app_img = Image.open('imagen/pig2.png')
app_img = app_img.resize((100, 60))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Arial 20'), bg=co1, fg=co4)
app_logo.place(x=150, y=0)

app_linha = Label(frameCima, width=295,  relief=FLAT, anchor=NW, font=('Arial 1'), bg=co13, fg=co1)
app_linha.place(x=0, y=47)


# Função calcular

def calcular():
    ## Obtendo as porcentagens ##

    # Obtendo renda mensal #

    renda_mensal = float(e_valor.get())

    ## Obtendo as porcentagens ##
    obter_50_porcento = (50 / 100) * renda_mensal
    obter_30_porcento = (30 / 100) * renda_mensal
    obter_20_porcento = (20 / 100) * renda_mensal


    l_necessidades['text'] = ('R$: %f' % obter_50_porcento)
    l_gastos['text'] = ('R$: %f' % obter_30_porcento)
    l_poupanca['text'] = ('R$: %f' % obter_20_porcento)



# Frame Meio
app_ = Label(frameMeio, text='Renda mensal',  relief=FLAT, anchor=NW, font=('Arial 12'), bg=co14, fg=co0)
app_.place(x=7, y=15)

e_valor = Entry(frameMeio, width=10, font=('Ivy 14'), justify='center', relief='solid')
e_valor.place(x=10, y=40)

b_calculado = Button(frameMeio, command=calcular,  text='Calcular'.upper(),  overrelief=RIDGE, anchor=NW, font=('Arial 10'), bg=co1, fg=co0)
b_calculado.place(x=150, y=40)

#frame baixo
app_ = Label(frameBixo, text='Seus numeros de 50% 30% 20%',  relief=FLAT, width=35, anchor=NW, font=('Arial 11'), bg=co3, fg=co9)
app_.place(x=0, y=0)

#Total necessidades

l_total_necessidades = Label(frameBixo, text='Necessidades',  relief=FLAT, width=35, anchor=NW, font=('Arial 11'), bg=co9, fg=co0)
l_total_necessidades.place(x=8, y=30)

l_necessidades = Label(frameBixo,   relief=FLAT, width=22, anchor=NW, font=('Arial 11'), bg=co1, fg=co4)
l_necessidades.place(x=8, y=65)

# Gastos

l_total_gastos= Label(frameBixo, text='Gastos',  relief=FLAT, width=35, anchor=NW, font=('Arial 11'), bg=co9, fg=co0)
l_total_gastos.place(x=8, y=105)

l_gastos = Label(frameBixo,   relief=FLAT, width=22, anchor=NW, font=('Arial 11'), bg=co1, fg=co4)
l_gastos.place(x=8, y=145)

# Poupança

l_total_poupanca= Label(frameBixo, text='Poupanças',  relief=FLAT, width=35, anchor=NW, font=('Arial 11'), bg=co9, fg=co0)
l_total_poupanca.place(x=8, y=185)

l_poupanca = Label(frameBixo,   relief=FLAT, width=22, anchor=NW, font=('Arial 11'), bg=co1, fg=co4)
l_poupanca.place(x=8, y=225)









janela.mainloop()