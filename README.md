# TaskTracker

Aplicação de linha de comando (CLI) em Python para organizar tarefas do dia a dia.
Projeto do **Bootcamp II – Fase 2 (Entrega Intermediária)**.

## Funcionalidades

- Cadastrar nova tarefa (título, descrição, prioridade e data limite)
- Visualizar todas as tarefas cadastradas
- Sair da aplicação

## Regras de negócio

- **Título**: obrigatório; entradas vazias ou só com espaços são rejeitadas.
- **Prioridade**: aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`.
- **Status**: definido automaticamente como `Pendente` no cadastro.
- **Data limite**: texto livre (sugestão: `DD/MM/AAAA`).

## Tecnologias

- Python 3 (somente biblioteca padrão, sem dependências externas)
- Git e GitHub

## Como executar

1. Instale o [Python 3](https://www.python.org/downloads/).
2. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
   cd tasktracker-projeto
   ```

3. Execute a aplicação:

   ```bash
   python src/main.py
   ```

   (Em alguns sistemas o comando é `python3 src/main.py`.)

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## Autor

Vitor Ferreira de Lima
