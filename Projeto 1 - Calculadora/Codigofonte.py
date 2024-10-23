from tkinter import *

# Criando a janela
Janela = Tk()
Janela.title("Calculadora - Rafael")
Janela.geometry('300x320')

# Cores
cor1 = "#292929"
cor2 = "#a6a3a2"
cor3 = "#de7812"

# Frame para o display
frame_display = Frame(Janela, bd=2, relief=SUNKEN, bg=cor1)
frame_display.grid(row=0, column=0, sticky="nsew")

# Frame para os botões
frame_corpo = Frame(Janela, bg="blue")
frame_corpo.grid(row=1, column=0, sticky="nsew")

# Permitir que as linhas e colunas da janela principal se expandam
Janela.grid_rowconfigure(0, weight=1)
Janela.grid_rowconfigure(1, weight=9)
Janela.grid_columnconfigure(0, weight=1) 


# Permitir que as colunas e linhas dentro dos frames se expandam
frame_corpo.grid_rowconfigure(0, weight=1)
frame_corpo.grid_rowconfigure(1, weight=1)
frame_corpo.grid_rowconfigure(2, weight=1)
frame_corpo.grid_rowconfigure(3, weight=1)
frame_corpo.grid_rowconfigure(4, weight=1)
frame_corpo.grid_columnconfigure(0, weight=1)
frame_corpo.grid_columnconfigure(1, weight=1)
frame_corpo.grid_columnconfigure(2, weight=1)
frame_corpo.grid_columnconfigure(3, weight=1)

# Armazenar o texto exibido
display_text = StringVar()
display_text.set("")

# Função pra inserir texto no display
def inserir_texto(texto):
    if texto == ",":
        texto = "."
    display_text.set(display_text.get()+ texto)

# Função pra calcular e exibir os resultados
def calcular():
    expressao = display_text.get()
    
    if "%" in expressao:
        partes = expressao.split("%")
        if len(partes) == 2:
            try:
                numero = float(partes[0])
                percentual = float(partes[1]) / 100.0
                resultado = numero * percentual
                display_text.set(str(resultado))
                return
            except:
                display_text.set("Erro")
                return
    try:
        resultado = eval(expressao) 
        display_text.set(str(resultado))  
    except Exception as e:
        display_text.set("Erro")  
# Display da calculadora
display = Entry(frame_display, font=("Georgia", 17), relief=FLAT, justify='left', bg=cor1, fg="white", textvariable=display_text)
display.pack(fill=X, padx=5, pady=5, ipady=10)


# Lista de Botões
b_1 = Button(frame_corpo, text="APAGAR", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: display_text.set(""))
b_1.grid(row=0, column=0, columnspan=2, sticky="nsew")

b_2 = Button(frame_corpo, text="%", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("%"))
b_2.grid(row=0, column=2, sticky="nsew")

b_3 = Button(frame_corpo, text="/", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("/"))
b_3.grid(row=0, column=3, sticky="nsew")

b_4 = Button(frame_corpo, text="1", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("1"))
b_4.grid(row=1, column=0, sticky="nsew")

b_5 = Button(frame_corpo, text="2", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("2"))
b_5.grid(row=1, column=1, sticky="nsew")

b_6 = Button(frame_corpo, text="3", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("3"))
b_6.grid(row=1, column=2, sticky="nsew")

b_7 = Button(frame_corpo, text="4", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("4"))
b_7.grid(row=2, column=0, sticky="nsew")

b_8 = Button(frame_corpo, text="5", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("5"))
b_8.grid(row=2, column=1, sticky="nsew")

b_9 = Button(frame_corpo, text="6", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("6"))
b_9.grid(row=2, column=2, sticky="nsew")

b_10 = Button(frame_corpo, text="7", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("7"))
b_10.grid(row=3, column=0, sticky="nsew")

b_11 = Button(frame_corpo, text="8", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("8"))
b_11.grid(row=3, column=1, sticky="nsew")

b_12 = Button(frame_corpo, text="9", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("9"))
b_12.grid(row=3, column=2, sticky="nsew")

b_13 = Button(frame_corpo, text="0", font=("Ivy 12 bold"), bg=cor2, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("0"))
b_13.grid(row=4, column=0, columnspan=2, sticky="nsew")

b_14 = Button(frame_corpo, text="V.", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto(","))
b_14.grid(row=4, column=2, sticky="nsew")

b_15 = Button(frame_corpo, text="=", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=calcular)
b_15.grid(row=4, column=3, sticky="nsew")

b_16 = Button(frame_corpo, text="x", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("*"))
b_16.grid(row=1, column=3, sticky="nsew")

b_17 = Button(frame_corpo, text="Soma", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("+"))
b_17.grid(row=2, column=3, sticky="nsew")

b_18 = Button(frame_corpo, text="Subt.", font=("Ivy 12 bold"), bg=cor3, fg="black", relief=RAISED, overrelief=RIDGE, command=lambda: inserir_texto("-"))
b_18.grid(row=3, column=3, sticky="nsew")



Janela.mainloop()