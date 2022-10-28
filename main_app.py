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

frameMeio= Frame(janela, width=300, height=90, bg=co10, relief="flat")
frameMeio.grid(row=1, column=0)

frameBixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
frameBixo.grid(row=2, column=0)

# Logo

app_ = Label(frameCima, text='Orçamento', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Arial 20'), bg=co1, fg=co4)
app_.place(x=0, y=0)

# imagem
app_img = Image.open('imagen/pig.png')
app_img = app_img.resize((80, 60))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Arial 20'), bg=co1, fg=co4)
app_logo.place(x=160, y=0)









janela.mainloop()