"""TaskTracker - Seu Gerenciador de Tarefas (Fase 2)

Aplicação CLI para cadastrar e visualizar tarefas.
Os dados ficam apenas em memória (somem ao fechar o programa).
"""

# Lista que guarda todas as tarefas em memória (cada tarefa é um dicionário)
tarefas = []

# Prioridades aceitas. A chave é o que o usuário pode digitar (em minúsculas)
# e o valor é o texto padronizado que será salvo na tarefa.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


# ---------- Validações ----------

def ler_titulo():
    """Pede o título até receber um valor que não seja vazio nem só espaços."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:  # string vazia é "falsa" no Python
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio.")


def ler_prioridade():
    """Pede a prioridade até receber Alta, Média (ou Media) ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


# ---------- Funcionalidades ----------

def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def cadastrar_tarefa():
    """Coleta os dados (com validação) e guarda a nova tarefa na lista."""
    print("\n--- Cadastro de nova tarefa ---")
    tarefa = {
        "titulo": ler_titulo(),
        "descricao": input("Descrição: ").strip(),
        "prioridade": ler_prioridade(),
        "data_limite": input("Data limite (ex: 25/12/2026): ").strip(),
        "status": "Pendente",  # sempre automático no cadastro
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas():
    """Mostra todas as tarefas cadastradas."""
    print("\n--- Tarefas cadastradas ---")
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada no momento.")
        return
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título     : {tarefa['titulo']}")
        print(f"  Descrição  : {tarefa['descricao']}")
        print(f"  Prioridade : {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status     : {tarefa['status']}")


def main():
    """Loop principal: repete o menu até o usuário escolher sair."""
    print("TaskTracker - Seu Gerenciador de Tarefas")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("Obrigado por usar o TaskTracker!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
