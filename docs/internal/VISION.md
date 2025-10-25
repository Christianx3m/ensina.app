cat > vision.md << 'EOF'
# 🌌 AutoDev.bot — Visão e Estrutura do Projeto

## 🧭 Propósito

O **AutoDev.bot** nasce com o propósito de ser uma plataforma de **aprendizado autônomo e construção de ferramentas com IA**, guiando desenvolvedores (ou iniciantes) na criação de seus próprios projetos e produtos digitais.

A ideia é simples e poderosa:
> “Aprender construindo, com mentores de IA que orientam, executam e avaliam o aluno em tempo real.”

---

## 🧩 Conceito dos Três Agentes

O ecossistema é formado por três entidades principais, cada uma representando uma camada do processo de aprendizado e criação.

### ⚡ Zeus (Mentor)
- Atua como o **professor e orientador**.
- Explica conceitos, cria desafios e propõe estudos personalizados.
- Interage com o aluno via chat, guiando o progresso conforme o desempenho.

### 🌍 Gaia (Executor)
- É a **mão na massa**.
- Executa códigos, valida tarefas, cria arquivos e interage com o ambiente.
- Simula o papel de um assistente técnico, ajudando a testar ideias e corrigir erros.

### 🐞 Pulga (Avaliador)
- O **crítico construtivo**.
- Analisa o código gerado, sugere melhorias e mede evolução do aluno.
- Pode gerar feedbacks, notas e relatórios de progresso.

---

## 🧱 Arquitetura Geral

\`\`\`
autodev.bot/
├── backend/
│   ├── main.py              # API principal FastAPI
│   ├── config.py            # Carrega variáveis de ambiente
│   ├── services/            # Comunicação entre os agentes
│   ├── .env.example         # Modelo de variáveis
│   └── requirements.txt     # Dependências do backend
│
├── services/
│   ├── zeus-mentor/         # Lógica do mentor
│   ├── gaia-executor/       # Lógica de execução
│   └── pulga-evaluator/     # Lógica de avaliação
│
├── vision.md                # Este arquivo
└── README.md                # Documentação técnica e instruções
\`\`\`

---

## 🧠 Fases de Desenvolvimento

### 🔹 **Fase 1 — Aprendizado Autônomo (modo pessoal)**
- Foco: Aprendizado do próprio criador (Chris)
- Estrutura base com FastAPI e integração OpenAI.
- Zeus, Gaia e Pulga interagem localmente via API.

### 🔹 **Fase 2 — Multiusuário (plataforma de aprendizado)**
- Autenticação com Google (OAuth2).
- Perfis de alunos e mentores IA.
- Armazenamento de progresso e histórico de aprendizado.

### 🔹 **Fase 3 — SaaS / Marketplace de Cursos IA**
- Professores humanos poderão criar cursos usando os robôs.
- Sistema de gamificação e reputação.
- Monetização dupla:
  - Assinaturas de aprendizado (para alunos)
  - Taxa de publicação (para criadores de conteúdo IA).

---

## ☁️ Infraestrutura e Tecnologias

- **Backend:** FastAPI + Python  
- **Frontend (futuro):** Next.js (Vercel)  
- **Banco de dados:** PostgreSQL (via Supabase)  
- **Autenticação:** Google OAuth2  
- **Deploy:** Vercel (frontend) + Render/AWS (backend)  
- **Integrações:** OpenAI API, GitHub, e futuras APIs educacionais.

---

## 🚀 Roadmap Técnico

| Fase | Meta Principal | Status |
|------|----------------|--------|
| 1 | Criar backend funcional e conectar com OpenAI | ✅ |
| 2 | Implementar comunicação entre Zeus, Gaia e Pulga | 🔄 |
| 3 | Criar interface interativa no browser (frontend) | ⏳ |
| 4 | Adicionar login e perfis | ⏳ |
| 5 | Evoluir para versão SaaS com cursos IA-assistidos | ⏳ |

---

## 💡 Filosofia

> “Ensinar máquinas a ensinar pessoas — e pessoas a ensinarem máquinas.”

O AutoDev.bot é mais do que um projeto técnico: é um **experimento vivo de aprendizado colaborativo entre humanos e inteligências artificiais**.  
Cada linha de código, cada teste e cada erro fazem parte de um ciclo de evolução contínua.

---

## 📜 Licença e Ética

Este projeto é experimental e segue princípios éticos de:
- Uso responsável de IA.
- Transparência no aprendizado.
- Privacidade de dados.
- Abertura ao conhecimento livre.

Licença: **MIT (a confirmar)**

---

© 2025 — **AutoDev.bot** by Christian Barreto & GPT-5  
*"Um ecossistema de aprendizado para humanos e IAs evoluírem juntos."*
EOF
