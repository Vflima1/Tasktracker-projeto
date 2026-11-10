# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastrar e visualizar tarefas.
Os dados ficam apenas em memória e são perdidos ao encerrar o programa.

**Autor:** Vitor Ferreira de Lima
**Projeto:** Desafio Final — Bootcamp II (Conteinerização, Orquestração e Deploy)

## Funcionalidades

- Cadastrar tarefa (título, descrição, prioridade e data limite)
- Visualizar tarefas cadastradas
- Validação de título obrigatório e de prioridade (Alta/Média/Baixa)

## Executando com Docker

Pré-requisito: [Docker](https://www.docker.com/) instalado e em execução.

Como construir a imagem:

```bash
docker build -t tasktracker .
```

Como rodar o container em modo isolado:

```bash
docker run -it tasktracker
```

Como rodar via orquestração (Recomendado):

```bash
docker compose run tasktracker
```

> O `-it` (e, no Compose, `stdin_open` + `tty`) é necessário porque a aplicação
> usa `input()` e precisa de um terminal interativo.

## Executando sem Docker

Requer Python 3.11 ou superior:

```bash
python src/main.py
```

## Estrutura do projeto

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento da Fase 1
├── src/
│   └── main.py                   # Código da Fase 2
├── Dockerfile                    # Fase 3: empacotamento
├── docker-compose.yml            # Fase 3: execução interativa
└── README.md
```

## Fases do projeto

1. **Fase 1:** planejamento lógico e pseudocódigo (`docs/`)
2. **Fase 2:** aplicação CLI em Python (`src/`)
3. **Fase 3:** conteinerização e orquestração com Docker
