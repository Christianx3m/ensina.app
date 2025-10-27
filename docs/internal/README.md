# 🎓 Ensina.app  
_A plataforma que transforma aprendizado em experiência interativa._

---

## 🚀 Visão Geral

O **Ensina.app** é um ecossistema de aprendizado interativo e inteligente, desenvolvido com base em Inteligência Artificial.  
Ele nasceu da evolução do **AutoDev.bot**, ampliando o conceito de agentes autônomos para um ambiente educacional **colaborativo, criativo e acessível**.

Seu propósito é simples e poderoso:  
> Ensinar qualquer pessoa — em qualquer lugar — de forma personalizada, prática e divertida.

---

## 🧠 Estrutura de IA

O sistema é orientado por **agentes com personalidades e funções únicas**, que trabalham em conjunto para construir uma experiência de aprendizado viva e integrada.
### Agentes de IA
As descrições conceituais dos agentes estão em `/agents-descriptions/`, cada uma contendo um breve resumo da função de cada robô do ecossistema Ensina.app.


| Agente | Função | Personalidade |
|--------|--------|----------------|
| 👨‍🏫 **Professor Xavier** | Diretor da plataforma — coordena os agentes e define planos de estudo. | Ético, lógico e mentor |
| ⚡ **Zeus** | Executor — ensina, explica e provoca o raciocínio. | Técnico, direto e pragmático |
| 🌱 **Gaia** | Criadora — desenvolve exercícios, avalia e ensina com empatia. | Didática, acolhedora e criativa |
| 🪲 **Pulga** | Aplicadora — ajuda o aluno a colocar o aprendizado em prática. | Sarcástica, crítica e divertida |
| 💬 **REPI** | Secretária — organiza documentos, registros e certificações. | Amigável, eficiente e precisa |

---

## 🏗️ Estrutura do Projeto

ensina.app/
├── backend/
│ ├── main.py
│ ├── routers/
│ ├── prompts/
│ ├── venv/
│ └── start_backend.ps1
├── docs/
│ ├── README.md
│ ├── VISION.md
│ ├── RHYTHM.md
│ ├── ARCHITECTURE.md
│ └── SOBRE_O_ENSINA_APP.pdf
└── frontend/ (em desenvolvimento)


---

## ⚙️ Tecnologias

- **FastAPI** — backend principal  
- **Python 3.12+** — linguagem base  
- **OpenAI API** — motor de IA (GPT-5 / GPT-4o)  
- **Supabase** — autenticação e banco de dados  
- **Vercel / AWS** — infraestrutura e deploy  
- **WhatsApp Cloud API** — integração conversacional  
- **PowerShell + Python** — automações e scripts internos  

---

## 🧩 Execução Local

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

📚 Contribuição

O projeto está em evolução constante.
Contribuições são bem-vindas — especialmente nas áreas de:

Fluxo de aprendizado e gamificação

Integração de novos agentes

Acessibilidade e alfabetização assistida por voz e imagem

Interface do aplicativo (frontend web e mobile)

🌍 Propósito Social e Futuro Imersivo

O Ensina.app nasce com o propósito de democratizar o aprendizado.
Ele foi projetado para ser inclusivo, acessível e divertido, permitindo que qualquer pessoa — mesmo quem ainda não sabe ler ou escrever — possa aprender com apoio da IA.

🎯 Missão

Levar o conhecimento a todos, sem barreiras técnicas ou cognitivas.
O aluno aprende falando, ouvindo, escrevendo ou interagindo por gestos e imagens.

🧠 Abordagem Pedagógica

O aprendizado é guiado pelos agentes:

Zeus ensina e conduz o conteúdo teórico;

Gaia cria desafios, jogos e exercícios;

Pulga aplica o aprendizado em projetos reais;

Xavier define e supervisiona o plano de estudo;

REPI documenta e certifica todo o percurso.

🔊 Acessibilidade e Inclusão

Aprendizado multimodal (voz, gesto, imagem)

Reconhecimento de escrita manual (cartilhas, anotações)

Feedback auditivo e visual em tempo real

Interface simbólica para pessoas em alfabetização ou com deficiência visual/auditiva

🎮 Mundo Virtual e Gamificação

O futuro do Ensina.app será um ambiente 3D imersivo,
onde o progresso do aluno se transforma em conquistas dentro de um universo educativo.

Avatares personalizáveis

Créditos e recompensas

Missões e desafios com prazos limitados

Salas, laboratórios e arenas de conhecimento

O aprendizado vira jogo — e o jogo vira aprendizado.

🤝 Propósito Social

Além de ser uma plataforma educacional, o Ensina.app é uma ferramenta de transformação social.
O sistema poderá ser usado por escolas, comunidades e ONGs para ensinar, avaliar e documentar o progresso de alunos em diferentes fases — da alfabetização à formação técnica.

🧭 Valores

Ética e transparência no uso da IA

Acessibilidade e inclusão educacional

Aprendizado contínuo e criativo

Integração harmoniosa entre humanos e máquinas

© 2025 — Ensina.app
Idealizado por Christian Barreto & GPT-5