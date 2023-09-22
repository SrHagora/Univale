import tkinter as tk


def mostrar_mensagem():
    # nome da mensagem
    nome = nome_entry.get()
    mensagem = mensagem_entry.get()
    root.withdraw()

    #exibir a mensagem
    janela_mensagem = tk.Toplevel(root)
    janela_mensagem.title("Mensagem Enviada")

    # mostrar mensagme
    mensagem_label = tk.Label(janela_mensagem, text=f"Nome: {nome} diz: {mensagem}")
    mensagem_label.pack()


# Configura a janela principal.
root = tk.Tk()
root.title("Enviar Mensagem")
root.geometry("400x150")

# Cria um rótulo para o nome
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()


# canpo nome e mensagem
nome_entry = tk.Entry(root)
nome_entry.pack()
mensagem_label = tk.Label(root, text="Mensagem:")
mensagem_label.pack()
mensagem_entry = tk.Entry(root)
mensagem_entry.pack()


#mostrar
enviar_button = tk.Button(root, text="Enviar", command=mostrar_mensagem)
enviar_button.pack()
#credito
criado_por_label = tk.Label(root, text="Criado por Maicon Dametto", foreground='red')
criado_por_label.pack()


root.mainloop()
