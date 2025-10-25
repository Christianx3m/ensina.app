# 🤖 AutoDev Bot

**AutoDev Bot** é uma plataforma experimental de aprendizado autônomo e criação assistida por IA, onde "professores" virtuais — Zeus, Gaia e Pulga — auxiliam desenvolvedores e criadores a aprender, programar e evoluir seus próprios projetos.

---

## 🌱 Visão do Projeto

A ideia central é criar um **ecossistema de aprendizado inteligente**, em que:
- **Zeus (Mentor)** ensina e orienta o aluno de forma didática;
- **Gaia (Executor)** executa tarefas, testa códigos e ajuda na prática;
- **Pulga (Avaliador)** analisa o código e sugere melhorias.

Essa estrutura permitirá:
1. Aprendizado personalizado e guiado por IA;
2. Criação de cursos e produtos digitais assistidos por agentes inteligentes;
3. Evolução contínua — o sistema aprende com as interações.

---

## 🧠 Estrutura de Pastas

autodev.bot/
├── backend/ # API principal em FastAPI
│ ├── main.py # Ponto de entrada da aplicação
│ ├── config.py # Configurações e variáveis de ambiente
│ ├── .env # (Privado) Variáveis locais
│ ├── .env.example # Modelo de variáveis públicas
│ └── requirements.txt # Dependências do backend
│
├── services/ # Agentes individuais
│ ├── zeus-mentor/
│ ├── gaia-executor/
│ └── pulga-evaluator/
│
├── vision.md # Documento de visão geral do projeto
└── README.md # Este arquivo


---

## ⚙️ Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI** — framework web moderno e performático
- **Uvicorn** — servidor ASGI para rodar a API
- **Pydantic** — validação de dados
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **OpenAI API** — motor de inteligência para os agentes

---

## 🚀 Como Rodar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Christianx3m/autodev.bot.git
