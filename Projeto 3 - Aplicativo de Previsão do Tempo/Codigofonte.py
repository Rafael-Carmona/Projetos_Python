import requests as rq
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Cores
azul_escuro = "#161042"
azul_claro = "#265685"
dourado = "#d48a1c"
cinza = "#60615c"
cinza_claro = "#abafb3"
branco = "white"

# Criando a janela
janela = tk.Tk()
janela.title('Previsão do tempo - Rafael')
janela.geometry("400x500")
janela.config(bg=azul_escuro, bd=2)

# Função para limpar entrada e resultados
def limpar():
    entrada_cidade.delete(0, tk.END)
    resultado_label.config(text="")
    cidade_label.config(text="")
    descricao_label.config(text="")
    temperatura_label.config(text="")
    temp_max_label.config(text="")
    temp_min_label.config(text="")
    umidade_label.config(text="")
    visibilidade_label.config(text="")
    vento_label.config(text="")
    sunrise_label.config(text="")
    sunset_label.config(text="")
    feels_like_label.config(text="")

# Adicionando os widgets iniciais
tk.Label(janela, text="Localização: ", bg=azul_escuro, fg=dourado, font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_cidade = tk.Entry(janela, bd=2, highlightbackground=cinza, highlightcolor=dourado, highlightthickness=2, bg=cinza, font=("Tahoma", 12, "bold"), fg="white")
entrada_cidade.grid(row=0, column=1, padx=10, pady=5, sticky="we")
botao_buscar = tk.Button(janela, text="Buscar", command=lambda: buscar_previsao(), relief=tk.RAISED, bg=azul_claro, fg=dourado, font=("Roboto", 12, "bold"), borderwidth=2)
botao_buscar.grid(row=0, column=2, padx=10, pady=5, sticky="e")
resultado_label = tk.Label(janela, text="", justify="left", bg=azul_escuro, fg="white")
resultado_label.grid(row=1, columnspan=3, padx=10, pady=5, sticky="ew")
botao_limpar = tk.Button(janela, text="Limpar", relief=tk.RAISED, bg=cinza_claro, font=("Helvetica", 12, "bold"), command=limpar)
botao_limpar.grid(row=12, column=2, padx=10, pady=10, sticky="se")

# Criando Labels para exibir os resultados separados
cidade_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco, font=("Helvetica", 12, "bold"))
cidade_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

descricao_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
descricao_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

temperatura_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
temperatura_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

temp_max_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
temp_max_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

temp_min_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
temp_min_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

umidade_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
umidade_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

visibilidade_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
visibilidade_label.grid(row=7, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

vento_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
vento_label.grid(row=8, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

sunrise_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
sunrise_label.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

sunset_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
sunset_label.grid(row=10, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

feels_like_label = tk.Label(janela, text="", bg=azul_escuro, fg=branco)
feels_like_label.grid(row=11, column=0, columnspan=3, padx=10, pady=5, sticky="nw")


# Definindo a Função de buscar previsão
def buscar_previsao():
    cidade = entrada_cidade.get()
    if not cidade:
        messagebox.showerror("Erro", "Por favor, insira o nome da cidade")
        return
    key = "6fbf541c4eef0b44d3bf1a40f8177046"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&lang=pt_br&units=metric"
    
    # Tratamento de erros aprimorado
    try:
        requisicao = rq.get(url)
        requisicao.raise_for_status()
    except rq.exceptions.HTTPError as errh:
        messagebox.showerror("Erro HTTP", f"Erro HTTP: {errh}")
    except rq.exceptions.ConnectionError as errc:
        messagebox.showerror("Erro de Conexão", f"Erro de Conexão: {errc}")
    except rq.exceptions.Timeout as errt:
        messagebox.showerror("Erro de Timeout", f"Timeout: {errt}")
    except rq.exceptions.RequestException as err:
        messagebox.showerror("Erro", f"Ocorreu um erro: {err}")
    else:
        dados_clima = requisicao.json()
        exibir_previsao(dados_clima)

# Definindo a função de exibir previsão
def exibir_previsao(dados_clima):
    cidade = dados_clima["name"]
    descricao = dados_clima["weather"][0]["description"]
    temperatura = dados_clima["main"]["temp"]
    temp_max = dados_clima["main"]["temp_max"]
    temp_min = dados_clima["main"]["temp_min"]
    umidade = dados_clima["main"]["humidity"]
    visibilidade = dados_clima.get("visibility", "Não disponível") / 1000  # Convertendo para km
    wind = dados_clima["wind"]["speed"]
    sunrise = converter_timestamp(dados_clima["sys"]["sunrise"])
    sunset = converter_timestamp(dados_clima["sys"]["sunset"])
    feels_like = dados_clima["main"]["feels_like"]
    horario_previsao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cidade_label.config(text=f"Cidade: {cidade} ({horario_previsao})")
    descricao_label.config(text=f"Descrição: {descricao}")
    temperatura_label.config(text=f"Temperatura: {temperatura}°C (Sensação: {feels_like}°C)")
    temp_max_label.config(text=f"Temp. Máx: {temp_max}°C")
    temp_min_label.config(text=f"Temp. Mín: {temp_min}°C")
    umidade_label.config(text=f"Umidade: {umidade}%")
    visibilidade_label.config(text=f"Visibilidade: {visibilidade} km")
    vento_label.config(text=f"Vento: {wind} m/s")
    sunrise_label.config(text=f"Nascer do sol: {sunrise}")
    sunset_label.config(text=f"Pôr do sol: {sunset}")
    feels_like_label.config(text=f"Sensação Térmica: {feels_like}°C")

# Converter timestamps para um formato legível
def converter_timestamp(timestamp):
    horario = datetime.fromtimestamp(timestamp)
    return horario.strftime("%H:%M:%S")

# Configurando o redimensionamento proporcional da janela
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)
janela.grid_rowconfigure(4, weight=1)
janela.grid_rowconfigure(5, weight=1)
janela.grid_rowconfigure(6, weight=1)
janela.grid_rowconfigure(7, weight=1)
janela.grid_rowconfigure(8, weight=1)
janela.grid_rowconfigure(9, weight=1)
janela.grid_rowconfigure(10, weight=1)
janela.grid_rowconfigure(11, weight=1)
janela.grid_rowconfigure(12, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

# Iniciando o loop da aplicação
janela.mainloop()
