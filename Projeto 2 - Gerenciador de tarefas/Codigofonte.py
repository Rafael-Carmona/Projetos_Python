import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

# Cores
verde_mar = "#0f3b39"
verde_mar2 = "#155c59"
azul_agua = "#8bafb3"
cinza = "#505859"

# Criar a janela
class TaskManager:
    def __init__(self, root):
        self.tasks = []  
        self.root = root
        self.root.title("Gerenciador de Tarefas - Rafael")
        self.root.configure(bg=verde_mar)
        
        # Configurar a interface
        self.frame = tk.Frame(self.root, bg=verde_mar2)
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        # Adicionar um Label e uma Entrada de texto
        self.task_label = tk.Label(self.frame, text="Tarefa:", bg=verde_mar2, fg="white")
        self.task_label.grid(row=0, column=0, padx=5, pady=5)
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Adicionar um Botão pras tarefas
        self.add_button = tk.Button(self.frame, text="Adicionar uma Tarefa", command=self.add_task, bg=cinza, fg="white")
        self.add_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Adicionar uma listbox com scroll pra mostrar as tarefas
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.task_listbox = tk.Listbox(self.task_list_frame, width=50, bg=azul_agua, bd=2, relief="solid")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_listbox.bind('<Double-1>', self.toggle_task_done)

        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        # Adicionar Botão pra remover as tarefas
        self.remove_button = tk.Button(self.root, text="Remover tarefa selecionada", command=self.remove_task, bg=cinza, fg="white")
        self.remove_button.grid(row=2, column=0, padx=5, sticky="ew")
        
        # Configurar redimensionamento
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.frame.grid_columnconfigure(1, weight=1)
        self.root.bind("<Configure>", self.update_font_size)
        
        self.font = tkFont.Font(size=10)
        self.task_listbox.config(font=self.font)

    # Criar as funções da janela
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, False))  # Adicionar a tarefa como não feita
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Escreva uma tarefa")
    
    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover")
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task, done in self.tasks:
            display_text = task
            if done:
                display_text = f"✔ {task}"
            self.task_listbox.insert(tk.END, display_text)
            if done:
                self.task_listbox.itemconfig(tk.END, {'fg': 'grey'})
            else:
                self.task_listbox.itemconfig(tk.END, {'fg': 'black'})

    def toggle_task_done(self, event):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task, done = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = (task, not done)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para marcar como feita ou não feita")

    def update_font_size(self, event):
        new_size = max(10, int(self.root.winfo_width() / 50))
        self.font.configure(size=new_size)

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()

