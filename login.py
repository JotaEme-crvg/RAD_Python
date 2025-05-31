import tkinter as tk
from tkinter import messagebox

# Dicionário de usuários (inicialmente com admin)
usuarios = {"admin": "1234"}

lista_alunos = []

menu_janela = None

# ----- Tela Login -----

def abrir_tela_login():
    global janela_login, entrada_usuario, entrada_senha

    janela_login = tk.Tk()
    janela_login.title("Login")
    janela_login.geometry("300x300")
    janela_login.configure(bg="#ffffff")

    fonte = ("Segoe UI", 11)

    tk.Label(janela_login, text="Usuário:", bg="#ffffff", font=fonte).pack(pady=10)
    entrada_usuario = tk.Entry(janela_login, width=30)
    entrada_usuario.pack()

    tk.Label(janela_login, text="Senha:", bg="#ffffff", font=fonte).pack(pady=10)
    entrada_senha = tk.Entry(janela_login, width=30, show="*")
    entrada_senha.pack()

    tk.Button(janela_login, text="Login", command=validar_login,
              bg="#006400", fg="white", width=20).pack(pady=10)

    tk.Button(janela_login, text="Registrar Novo Usuário", command=abrir_tela_registro,
              bg="#007acc", fg="white", width=20).pack()

    janela_login.mainloop()

def validar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        janela_login.destroy()
        criar_menu()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

# ----- Tela Registro -----

def abrir_tela_registro():
    janela_login.withdraw()
    global janela_registro, entrada_novo_usuario, entrada_nova_senha, entrada_confirma_senha

    janela_registro = tk.Toplevel()
    janela_registro.title("Registrar Novo Usuário")
    janela_registro.geometry("300x350")
    janela_registro.configure(bg="#ffffff")

    fonte = ("Segoe UI", 11)

    tk.Label(janela_registro, text="Novo Usuário:", bg="#ffffff", font=fonte).pack(pady=10)
    entrada_novo_usuario = tk.Entry(janela_registro, width=30)
    entrada_novo_usuario.pack()

    tk.Label(janela_registro, text="Senha:", bg="#ffffff", font=fonte).pack(pady=10)
    entrada_nova_senha = tk.Entry(janela_registro, width=30, show="*")
    entrada_nova_senha.pack()

    tk.Label(janela_registro, text="Confirmar Senha:", bg="#ffffff", font=fonte).pack(pady=10)
    entrada_confirma_senha = tk.Entry(janela_registro, width=30, show="*")
    entrada_confirma_senha.pack()

    tk.Button(janela_registro, text="Registrar", command=registrar_usuario,
              bg="#006400", fg="white", width=20).pack(pady=15)

    tk.Button(janela_registro, text="Voltar ao Login", command=voltar_ao_login,
              bg="#b22222", fg="white", width=20).pack()

    janela_registro.protocol("WM_DELETE_WINDOW", voltar_ao_login)

def registrar_usuario():
    novo_usuario = entrada_novo_usuario.get()
    senha = entrada_nova_senha.get()
    confirma = entrada_confirma_senha.get()

    if not novo_usuario or not senha or not confirma:
        messagebox.showwarning("Erro", "Preencha todos os campos.")
        return

    if senha != confirma:
        messagebox.showwarning("Erro", "As senhas não conferem.")
        return

    if novo_usuario in usuarios:
        messagebox.showwarning("Erro", "Usuário já existe.")
        return

    usuarios[novo_usuario] = senha
    messagebox.showinfo("Sucesso", f"Usuário '{novo_usuario}' registrado com sucesso!")
    janela_registro.destroy()
    janela_login.deiconify()

def voltar_ao_login():
    janela_registro.destroy()
    janela_login.deiconify()

# ----- Menu Principal -----

def criar_menu():
    global menu_janela
    menu_janela = tk.Tk()
    menu_janela.title("Menu Principal")
    menu_janela.geometry("300x350")
    menu_janela.configure(bg="#ffffff")

    fonte = ("Segoe UI", 11)
    tk.Label(menu_janela, text="Escolha uma opção:", bg="#ffffff", font=fonte).pack(pady=20)

    tk.Button(menu_janela, text="Adicionar Aluno", command=abrir_tela_adicionar,
              bg="#006400", fg="white", width=25).pack(pady=5)
    tk.Button(menu_janela, text="Alterar Aluno", command=abrir_tela_alterar,
              bg="#006400", fg="white", width=25).pack(pady=5)
    tk.Button(menu_janela, text="Remover Aluno", command=abrir_tela_remover,
              bg="#006400", fg="white", width=25).pack(pady=5)
    tk.Button(menu_janela, text="Gerar Relatório", command=gerar_relatorio,
              bg="#34a853", fg="white", width=25).pack(pady=5)

    menu_janela.mainloop()

def voltar_para_menu(janela_atual):
    janela_atual.destroy()
    if menu_janela:
        menu_janela.deiconify()

# ----- Adicionar Aluno -----

def abrir_tela_adicionar():
    global janela_adicionar, campo_nome, campo_cpf, campo_email, campo_curso
    menu_janela.withdraw()

    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Aluno")
    janela_adicionar.geometry("400x350")
    janela_adicionar.configure(bg="#FFFFFF")

    botao_voltar = tk.Button(janela_adicionar, text="← Voltar", command=lambda: voltar_para_menu(janela_adicionar))
    botao_voltar.pack(anchor='nw', padx=5, pady=5)

    fonte = ("Segoe UI", 10)
    tk.Label(janela_adicionar, text="Nome:", bg="#ffffff", font=fonte).pack(pady=5)
    campo_nome = tk.Entry(janela_adicionar, width=40)
    campo_nome.pack()
    tk.Label(janela_adicionar, text="CPF:", bg="#ffffff", font=fonte).pack(pady=5)
    campo_cpf = tk.Entry(janela_adicionar, width=40)
    campo_cpf.pack()
    tk.Label(janela_adicionar, text="Email:", bg="#ffffff", font=fonte).pack(pady=5)
    campo_email = tk.Entry(janela_adicionar, width=40)
    campo_email.pack()
    tk.Label(janela_adicionar, text="Curso:", bg="#ffffff", font=fonte).pack(pady=5)
    campo_curso = tk.Entry(janela_adicionar, width=40)
    campo_curso.pack()
    tk.Button(janela_adicionar, text="Concluir", command=concluir_adicao, bg="#006400", fg="white", width=20).pack(pady=20)

    janela_adicionar.protocol("WM_DELETE_WINDOW", lambda: voltar_para_menu(janela_adicionar))

def concluir_adicao():
    nome = campo_nome.get()
    cpf = campo_cpf.get()
    email = campo_email.get()
    curso = campo_curso.get()

    if nome and cpf and email and curso:
        lista_alunos.append({"nome": nome, "cpf": cpf, "email": email, "curso": curso})
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
        janela_adicionar.destroy()
        menu_janela.deiconify()
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos.")

# ----- Alterar Aluno -----

def abrir_tela_alterar():
    global janela_alterar, lista_box_alterar
    menu_janela.withdraw()

    janela_alterar = tk.Toplevel()
    janela_alterar.title("Alterar Aluno")
    janela_alterar.geometry("400x300")
    janela_alterar.configure(bg="#FFFFFF")

    botao_voltar = tk.Button(janela_alterar, text="← Voltar", command=lambda: voltar_para_menu(janela_alterar))
    botao_voltar.pack(anchor='nw', padx=5, pady=5)

    tk.Label(janela_alterar, text="Selecione um aluno para alterar:", bg="#ffffff").pack(pady=10)
    lista_box_alterar = tk.Listbox(janela_alterar, width=50)
    lista_box_alterar.pack(padx=10, pady=10)

    for aluno in lista_alunos:
        lista_box_alterar.insert(tk.END, f"{aluno['nome']} | {aluno['cpf']} | {aluno['curso']}")

    tk.Button(janela_alterar, text="Alterar Selecionado", command=editar_aluno, bg="#006400", fg="white").pack(pady=5)
    janela_alterar.protocol("WM_DELETE_WINDOW", lambda: voltar_para_menu(janela_alterar))

def editar_aluno():
    sel = lista_box_alterar.curselection()
    if not sel:
        messagebox.showwarning("Erro", "Selecione um aluno.")
        return

    idx = sel[0]
    aluno = lista_alunos[idx]

    for widget in janela_alterar.winfo_children():
        widget.destroy()

    botao_voltar = tk.Button(janela_alterar, text="← Voltar", command=lambda: voltar_para_menu(janela_alterar))
    botao_voltar.pack(anchor='nw', padx=5, pady=5)

    campo_ed_nome = tk.Entry(janela_alterar, width=40)
    campo_ed_cpf = tk.Entry(janela_alterar, width=40)
    campo_ed_email = tk.Entry(janela_alterar, width=40)
    campo_ed_curso = tk.Entry(janela_alterar, width=40)

    def salvar_alteracao():
        novo = {
            "nome": campo_ed_nome.get(),
            "cpf": campo_ed_cpf.get(),
            "email": campo_ed_email.get(),
            "curso": campo_ed_curso.get()
        }
        if all(novo.values()):
            lista_alunos[idx] = novo
            messagebox.showinfo("Sucesso", "Aluno alterado com sucesso!")
            janela_alterar.destroy()
            menu_janela.deiconify()
        else:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios.")

    tk.Label(janela_alterar, text="Editar Nome:", bg="#ffffff").pack()
    campo_ed_nome.pack()
    campo_ed_nome.insert(0, aluno['nome'])

    tk.Label(janela_alterar, text="Editar CPF:", bg="#ffffff").pack()
    campo_ed_cpf.pack()
    campo_ed_cpf.insert(0, aluno['cpf'])

    tk.Label(janela_alterar, text="Editar Email:", bg="#ffffff").pack()
    campo_ed_email.pack()
    campo_ed_email.insert(0, aluno['email'])

    tk.Label(janela_alterar, text="Editar Curso:", bg="#ffffff").pack()
    campo_ed_curso.pack()
    campo_ed_curso.insert(0, aluno['curso'])

    tk.Button(janela_alterar, text="Salvar", command=salvar_alteracao, bg="#006400", fg="white").pack(pady=10)

# ----- Remover Aluno -----

def abrir_tela_remover():
    global janela_remover, lista_box_remover
    menu_janela.withdraw()

    janela_remover = tk.Toplevel()
    janela_remover.title("Remover Aluno")
    janela_remover.geometry("400x300")
    janela_remover.configure(bg="#FFFFFF")

    botao_voltar = tk.Button(janela_remover, text="← Voltar", command=lambda: voltar_para_menu(janela_remover))
    botao_voltar.pack(anchor='nw', padx=5, pady=5)

    tk.Label(janela_remover, text="Selecione um aluno para remover:", bg="#ffffff").pack(pady=10)
    lista_box_remover = tk.Listbox(janela_remover, width=50)
    lista_box_remover.pack(padx=10, pady=10)

    for aluno in lista_alunos:
        lista_box_remover.insert(tk.END, f"{aluno['nome']} | {aluno['cpf']} | {aluno['curso']}")

    tk.Button(janela_remover, text="Remover Selecionado", command=remover_aluno, bg="#b22222", fg="white").pack(pady=5)
    janela_remover.protocol("WM_DELETE_WINDOW", lambda: voltar_para_menu(janela_remover))

def remover_aluno():
    sel = lista_box_remover.curselection()
    if not sel:
        messagebox.showwarning("Erro", "Selecione um aluno.")
        return

    idx = sel[0]
    nome = lista_alunos[idx]['nome']
    del lista_alunos[idx]
    messagebox.showinfo("Removido", f"Aluno '{nome}' removido.")
    janela_remover.destroy()
    menu_janela.deiconify()

# ----- Gerar Relatório -----

def gerar_relatorio():
    if not lista_alunos:
        messagebox.showinfo("Relatório", "Nenhum aluno cadastrado.")
        return

    relatorio = tk.Toplevel()
    relatorio.title("Relatório de Alunos")
    relatorio.geometry("500x400")
    relatorio.configure(bg="#ffffff")

    botao_voltar = tk.Button(relatorio, text="← Voltar", command=relatorio.destroy)
    botao_voltar.pack(anchor='nw', padx=5, pady=5)

    texto = tk.Text(relatorio, width=60, height=25)
    texto.pack(padx=10, pady=10)

    for aluno in lista_alunos:
        texto.insert(tk.END, f"Nome: {aluno['nome']}\nCPF: {aluno['cpf']}\nEmail: {aluno['email']}\nCurso: {aluno['curso']}\n\n")

    texto.config(state=tk.DISABLED)

# ----- Iniciar programa -----

if __name__ == "__main__":
    abrir_tela_login()