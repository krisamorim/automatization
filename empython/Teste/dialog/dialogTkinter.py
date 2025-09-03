import tkinter as tk

def solicitarDados():
    def mostrar_nome():
        nome = entrada_nome.get()
        label_nome.config(text="Olá, " + nome + "!")

    # Cria uma janela
    janela = tk.Tk()
    janela.title("Receber Nome")
    janela.configure(background='#4682B4')
    janela.geometry("200x200") #tamanho
    janela.resizable(True, True)
    janela.maxsize(width=500, height=500)

    # Cria um rótulo de instrução
    rotulo_instrucao = tk.Label(janela, text="Digite seu nome:")
    rotulo_instrucao.pack()

    # Cria um campo de entrada de texto
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()

    # Cria um botão para confirmar a entrada
    botao_confirmar = tk.Button(janela, text="Confirmar", command=mostrar_nome)
    botao_confirmar.pack()

    # Cria um rótulo para exibir o nome inserido
    label_nome = tk.Label(janela, text="")
    label_nome.pack()

    # Inicia o loop principal da interface gráfica
    janela.mainloop()


solicitarDados()