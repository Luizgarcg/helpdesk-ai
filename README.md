# HelpDesk AI 🤖

Sistema inteligente de triagem de chamados que usa IA para classificar automaticamente a urgência de cada solicitação de suporte (Baixa, Média ou Alta).

## 💡 Sobre o projeto

Muitas equipes de suporte recebem dezenas de chamados por dia sem nenhuma priorização automática — alguém precisa ler tudo manualmente pra saber o que é urgente. O HelpDesk AI resolve isso: ao cadastrar um chamado, a IA analisa a descrição e classifica a urgência automaticamente, ajudando a equipe a priorizar o que realmente importa.

## 🚀 Funcionalidades

- Cadastro de chamados via formulário web
- Classificação automática de urgência usando IA (Google Gemini)
- Listagem dos chamados cadastrados
- CRUD completo em Python (criar, listar, editar, deletar)
- Interface web com Flask

## 🛠️ Tecnologias

- **Python** — lógica de negócio e CRUD
- **Flask** — servidor web e rotas
- **HTML5 semântico** — estrutura da página
- **CSS3** — estilização
- **Google Gemini API** — classificação de urgência via IA
- **python-dotenv** — gerenciamento seguro de variáveis de ambiente

## 📁 Estrutura do projeto

```
helpdesk-ai/
├── main.py              # classe Chamado e funções de CRUD
├── servidor.py           # servidor Flask e rotas
├── templates/
│   └── index.html        # página principal
├── static/
│   └── style.css          # estilização
├── .env                   # chave da API (não versionado)
└── .gitignore
```

## ▶️ Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/Luizgarcg/helpdesk-ai.git
cd helpdesk-ai
```

2. Instale as dependências:
```bash
pip install flask python-dotenv google-genai
```

3. Crie um arquivo `.env` na raiz do projeto com sua chave da API do Gemini (gratuita em [aistudio.google.com](https://aistudio.google.com)):
```
GEMINI_API_KEY=sua_chave_aqui
```

4. Rode o servidor:
```bash
python servidor.py
```

5. Acesse no navegador:
```
http://127.0.0.1:5000
```

## 🧠 O que aprendi

Esse projeto foi minha primeira integração real entre lógica de programação (POO e CRUD em Python), uma API de IA externa, e uma interface web completa usando Flask — conectando formulário HTML, backend Python e um modelo de linguagem para automatizar a triagem de chamados de suporte.

## 🤝 Sobre o processo de desenvolvimento

Esse projeto foi desenvolvido por mim com apoio do **Claude (Anthropic)** atuando como mentor de programação — me guiando conceito por conceito, revisando meu código e explicando erros, sem escrever as soluções por mim. Toda a lógica (classe `Chamado`, funções de CRUD, rotas Flask, integração com a API do Gemini) foi escrita e debugada por mim, linha por linha, com o Claude no papel de tutor Socrático.

Acho importante deixar isso registrado: uso de IA como ferramenta de aprendizado é uma habilidade real do mercado (e tema de uma das minhas disciplinas, Engenharia de Prompt), e prefiro ser transparente sobre como o projeto foi construído.

## 👤 Autor

**Luis Eduardo Henrique Gabriel**
Estudante de Análise e Desenvolvimento de Sistemas (ADS) — UNIPE
[GitHub](https://github.com/Luizgarcg)
