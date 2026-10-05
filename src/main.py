"""TaskTracker - Seu Gerenciador de Tarefas (Fase 2)
Versão do COMMIT 3: estrutura principal (menu e loop), ainda sem validações.
"""

# Lista que guarda todas as tarefas em memória (cada tarefa é um dicionário)
tarefas = []


def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def cadastrar_tarefa():
    """Pede os dados ao usuário e guarda a nova tarefa na lista."""
    print("\n--- Cadastro de nova tarefa ---")
    tarefa = {
        "titulo": input("Título: "),
        "descricao": input("Descrição: "),
        "prioridade": input("Prioridade (Alta/Média/Baixa): "),
        "data_limite": input("Data limite (ex: 25/12/2026): "),
        "status": "Pendente",
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
