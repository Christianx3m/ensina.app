# 🎵 RHYTHM — Fluxo de Trabalho do Ensina.app

## 🎯 Objetivo
Garantir um **ritmo de desenvolvimento consistente e colaborativo**,  
mantendo a harmonia entre o backend (IA), o frontend (plataforma) e o aprendizado do usuário.

---

## 🧩 Estrutura de Trabalho

1. **Planejamento**  
   - Revisão e atualização do `VISION.md` e `ARCHITECTURE.md`.  
   - Definição de metas e sprints semanais.  
   - Atualização do roadmap no GitHub e Notion.

2. **Desenvolvimento Modular**  
   - Cada agente (Zeus, Gaia, Pulga, Xavier e REPI) possui um módulo independente.  
   - Rotas, prompts e comportamentos isolados para facilitar manutenção e evolução.  
   - Uso de **microsserviços** e APIs dedicadas por agente.

3. **Testes e Feedback**
   - Testes locais via **Uvicorn** com logs estruturados.  
   - Revisões automáticas pela **Pulga**, com relatórios de consistência.  
   - Auditoria de comportamento e coerência pelo **Xavier**.  

4. **Deploy e Integração**
   - Deploy contínuo via **Vercel** e **AWS**.  
   - Integração automatizada após push na branch `main`.  
   - Ambiente de testes isolado (`staging`) antes da produção.


A documentação de cada agente está localizada em pastas individuais na raiz (ex.: /Gaia/README.md).
A documentação individual dos agentes está agrupada em `/agents-descriptions/`, facilitando manutenção e versionamento.
Exemplo: `/agents-descriptions/gaia-executor/README.md`

---

## 🧠 Comunicação entre Agentes

| Origem | Destino | Ação |
|--------|----------|------|
| Gaia | Zeus | Solicita execução de código ou exemplo prático |
| Pulga | Gaia | Revisa textos e exercícios, sugere correções |
| Xavier | Todos | Supervisiona o processo de ensino e aprendizado |
| REPI | Usuário | Interage via chat, voz ou WhatsApp |
| Xavier | REPI | Solicita relatórios e certificados de progresso |

A comunicação é **bidirecional** e ocorre por **eventos assíncronos (WebSocket)**, permitindo coordenação simultânea entre múltiplos alunos e agentes.

---

## 🪜 Metodologia de Desenvolvimento

- Desenvolvimento iterativo com **sprints curtas** (5–7 dias).  
- Cada sprint entrega um **módulo funcional ou melhoria incremental**.  
- Revisões documentadas em `/docs/internal/notes.md`.  
- A cada ciclo concluído, os agentes são reavaliados para alinhamento pedagógico e técnico.

---

## ⚙️ Ferramentas Principais

- **GitHub** — versionamento e controle de branches.  
- **Cursor IDE** — ambiente de desenvolvimento colaborativo com IA.  
- **FastAPI + Uvicorn** — backend e API principal.  
- **OpenAI GPT-5 / GPT-4o** — motores de linguagem.  
- **Supabase** — autenticação e banco de dados.  
- **Vercel / AWS** — deploy e infraestrutura.  

---

## 🧱 Estrutura do Backend

ensina.app/
├── backend/
│ ├── main.py
│ ├── routers/
│ │ ├── zeus_router.py
│ │ ├── gaia_router.py
│ │ ├── pulga_router.py
│ │ ├── xavier_router.py
│ │ └── repi_router.py
│ ├── prompts/
│ │ ├── zeus_prompt.py
│ │ ├── gaia_prompt.py
│ │ ├── pulga_prompt.py
│ │ ├── xavier_prompt.py
│ │ └── repi_prompt.py
│ ├── utils/
│ └── requirements.txt
└── docs/


---

## 🤖 Agentes Ativos

| Agente | Função | Status |
|--------|--------|--------|
| ⚡ **Zeus** | Professor executor e guia técnico | ✅ Ativo |
| 🌱 **Gaia** | Criadora de conteúdo e avaliadora | ✅ Ativo |
| 🪲 **Pulga** | Revisora crítica e aplicadora prática | ✅ Ativo |
| 👨‍🏫 **Xavier** | Diretor e coordenador de aprendizado | ✅ Ativo |
| 💬 **REPI** | Secretária e registradora de progresso | 🚧 Em desenvolvimento |

---

## 💾 Integrações

- **GitHub:** [Christianx3m/ensina.app](https://github.com/Christianx3m/ensina.app)  
- **Controle de versão:** `git` (branch principal: `main`)  
- **Planejamento:** Notion (visualizações Kanban, Timeline e Tabela)  
- **Automação de Deploy:** CI/CD com GitHub Actions  

---

## 🧭 Status Atual — Fase 2

| Área | Situação | Observações |
|------|-----------|-------------|
| Estrutura de backend | ✅ Completa | FastAPI funcional |
| Rotas dos agentes | ✅ Testadas | Respostas coerentes |
| Prompts e personalidades | ⚙️ Revisando | Zeus e Gaia otimizados |
| Documentação | ⚙️ Atualizada | Estrutura coesa e limpa |
| Integração GitHub | ✅ Ativa | Fluxo contínuo |
| Infraestrutura (deploy) | 🚧 Planejamento | AWS + Vercel |
| Sistema de usuários | 🚧 Próxima etapa | Cadastro e convites |
| Agente REPI | 🚧 Em fase de design | Registro multimodal |

---

## 🧩 Inclusão e Acessibilidade

O Ensina.app está sendo projetado para **alunos de qualquer nível de alfabetização**,  
oferecendo aprendizado **multimodal** (voz, imagem e gesto).

### 🧠 Funcionalidades
- Aprendizado por **voz (STT/TTS)**.  
- Reconhecimento de escrita manual (OCR).  
- Interface visual com ícones e sons intuitivos.  
- Correção de tarefas com feedback auditivo e visual.  

Esses recursos permitem que pessoas com **dificuldades cognitivas, motoras ou auditivas** aprendam de forma natural e interativa.

---

## 🏆 Progressão e Ações do Usuário

A plataforma reconhece ações e marcos importantes do aluno, recompensando o esforço e a constância.

### 🎯 Ações que geram evolução
- Criar ou concluir projetos pessoais.  
- Participar de grupos colaborativos.  
- Ajudar outros alunos (feedback ou revisão).  
- Publicar cursos e compartilhar aprendizados.  
- Usar a plataforma de forma contínua e saudável.  

Cada ação gera **créditos e experiência (XP)**,  
que podem ser usados no **Shop** para adquirir itens cosméticos ou vantagens no ambiente virtual.

A **REPI** registra e valida todas as conquistas, emitindo certificados e relatórios automáticos.

---

## 🧩 Modo Colaborativo

Os alunos podem formar **grupos de estudo e desenvolvimento de projetos**.  
Cada grupo possui uma **sala virtual**, onde é possível:

- Conversar por **voz ou chat**.  
- Compartilhar arquivos e tarefas.  
- Receber suporte dos agentes.  
- Revisar entregas e trocar conhecimento.  

A **REPI** organiza todos os documentos e históricos de grupo.

---

## 🔊 Aprendizado por Voz e Imagem

O Ensina.app também pode ser operado **sem leitura** — apenas com voz, imagens e gestos.  
O sistema interpreta o que o aluno diz, escreve ou fotografa, permitindo:

- Enviar **fotos manuscritas** de exercícios.  
- Receber feedback falado e visual.  
- Aprender com **interações simbólicas** e não textuais.  

Isso torna o sistema ideal para **alfabetização e reabilitação cognitiva**.

---

## 🎮 Loop Gamificado de Aprendizado

🎯 Estudo → 🧠 Prática → 🧩 Avaliação → 🚀 Aplicação → 🪙 Recompensa → 🔁


Cada ciclo concluído gera:
- **Créditos (coins)** — usados no Shop e recompensas.  
- **XP (experiência)** — aumenta o nível do aluno.  
- **Títulos e emblemas** — exibidos no perfil.  
- **Itens cosméticos** — aplicáveis ao avatar no mundo virtual.  

O **Xavier** monitora o progresso e a **REPI** registra cada conquista, criando um histórico contínuo de aprendizado.

---

## 🌍 Futuro e Expansão

O objetivo é criar um **ambiente 3D interativo**, onde:
- Cada aluno tem um avatar com progressão própria.  
- A aprendizagem e o esforço refletem no mundo virtual.  
- Grupos cooperam para construir projetos e resolver desafios.  

As próximas fases incluem:
1. Integração com motores como **Unity / Roblox / Minecraft Education**.  
2. Ambientes híbridos (educação real + digital).  
3. Aulas e eventos em tempo real com IA e humanos.  

---

**© 2025 — Ensina.app**  
_Idealizado por Christian Barreto & GPT-5_
