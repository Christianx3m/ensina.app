# 🧱 Arquitetura — Ensina.app

## 🧭 Visão Geral
O **Ensina.app** foi projetado como uma plataforma de aprendizado modular e extensível,  
onde **agentes inteligentes** colaboram com usuários em um ecossistema dinâmico de ensino, prática e documentação.

A arquitetura é baseada em **microsserviços**, com foco em **escalabilidade, acessibilidade e automação pedagógica**.

---

## ⚙️ Estrutura Técnica

| Camada | Responsabilidade | Tecnologias |
|--------|------------------|--------------|
| **Backend** | Coordenação entre agentes, APIs e controle de fluxo | FastAPI, Python 3.12+ |
| **IA / Agentes** | Processamento de linguagem e comportamento dos personagens | OpenAI API (GPT-5 / GPT-4o) |
| **Banco de Dados** | Armazenamento de usuários, cursos e progressos | Supabase (PostgreSQL) |
| **Frontend (em planejamento)** | Interface web e mobile | Next.js / React / Vercel |
| **Infraestrutura** | Hospedagem e automação | AWS, PowerShell, CI/CD |
| **Integrações** | Comunicação externa e voz | WhatsApp Cloud API, OCR, TTS/STT |

---

## 🧩 Arquitetura de Agentes

Os **agentes do Ensina.app** são módulos independentes que se comunicam entre si via API interna e eventos assíncronos.  
Cada agente possui um papel e uma personalidade que moldam a experiência educacional.

| Agente | Função | Descrição |
|--------|---------|-----------|
| ⚡ **Zeus** | Professor executor | Encarregado da explicação prática e didática, conduz os conteúdos teóricos e práticos. |
| 🌱 **Gaia** | Criadora de desafios | Gera exercícios, quizzes e jogos educativos personalizados. |
| 🪲 **Pulga** | Aplicadora prática | Transforma teoria em prática, orientando o aluno em seu projeto principal. |
| 👨‍🏫 **Professor Xavier** | Diretor e mentor | Coordena a jornada de aprendizado e supervisiona a interação entre os agentes. |
| 💬 **REPI** | Secretária e gestora de registros | Administra arquivos, certificados, comunicações e documentos de alunos e grupos. |

Cada agente possui uma pasta independente na raiz (Zeus, Gaia, Pulga, Xavier, etc.), com seu respectivo README.md.
Cada agente possui uma pasta descritiva dentro de `/agents-descriptions/`, onde estão seus respectivos README.md resumidos:

/agents-descriptions/
├── xavier-director/
├── zeus-mentor/
├── gaia-executor/
├── pulga-analyst/
└── repi-archivist/

Essas pastas contêm apenas documentação explicativa sobre o papel e a função de cada agente.


---

## 🧠 Fluxo de Aprendizado

Aluno → Xavier → Zeus → Gaia → Pulga → REPI → Xavier


1. **Aluno** define o que deseja aprender (ex.: “criar um site”, “aprender violão”).  
2. **Xavier** interpreta o objetivo e cria um plano de estudo dinâmico.  
3. **Zeus** ensina e provoca o raciocínio do aluno.  
4. **Gaia** aplica exercícios, desafios e mini-jogos para fixação.  
5. **Pulga** auxilia na aplicação prática no projeto do aluno.  
6. **REPI** documenta e registra o aprendizado, gerando relatórios e certificados.  
7. **Xavier** avalia o progresso e reinicia o ciclo com base na evolução do aluno.

Esse fluxo permite que o aprendizado seja **cíclico, interativo e evolutivo**, sem dependência de tutoria humana constante.

---

## 💬 REPI — Registro e Processamento de Informações

A **REPI** é o coração administrativo do Ensina.app.  
Ela atua como secretária inteligente e assistente documental, garantindo que toda a jornada de aprendizado seja registrada, certificada e sincronizada.

### 🧩 Funções principais
- Armazena apostilas, relatórios, certificados e histórico de aprendizado.  
- Gera **certificados automáticos** com base no desempenho e conclusão.  
- Faz a ponte de comunicação entre **aluno, agentes e backend**.  
- Controla **permissões, visibilidade e compartilhamentos** (público, privado, colaborativo).  
- Armazena **imagens, áudios e manuscritos** dos alunos (OCR + TTS/STT).  
- Realiza backup automático e sincronização segura com a nuvem.  

### 🔊 Camada de Voz e Imagem
A REPI integra recursos multimodais para tornar o aprendizado acessível:
- **Reconhecimento de fala (STT)** — converte a voz do aluno em texto compreensível.  
- **Síntese de voz (TTS)** — permite que a plataforma "fale" com o aluno.  
- **Reconhecimento de escrita manual (OCR)** — interpreta fotos de cartilhas e anotações.  
- **Feedback multimodal** — respostas por som, imagem e movimento.  

Essas funções permitem que pessoas com **baixa alfabetização ou limitações físicas** aprendam de forma intuitiva e divertida.

---

## 🧭 Acessibilidade e Inclusão

A arquitetura do Ensina.app foi pensada para **abranger diferentes perfis de alunos**,  
desde iniciantes até pessoas com necessidades educacionais especiais.

### 🌐 Mecanismos de Inclusão
- Interação por **voz, gesto e imagem**.  
- Interface adaptativa para diferentes dispositivos (PC, celular, tablets).  
- Sistema de narração automática e tradução instantânea.  
- Aprendizado auditivo e visual — ideal para fases iniciais de alfabetização.  

Essas funcionalidades estão sendo implementadas em camadas paralelas para garantir compatibilidade com o backend atual.

---

## 🌍 Integração com Mundo Virtual

O Ensina.app foi projetado com uma visão de longo prazo:  
um **ambiente educacional 3D**, onde o aprendizado real se reflete em conquistas virtuais.

### 🎮 Estrutura Imersiva
- Avatares personalizáveis que evoluem com o aprendizado.  
- Missões e recompensas vinculadas a cursos concluídos.  
- Salas temáticas, laboratórios e arenas de conhecimento.  
- Interação social entre alunos e professores em tempo real.

### 💡 Stack sugerida
- **Unity** ou **Unreal Engine** para ambiente 3D.  
- **API de integração** entre o backend (FastAPI) e o motor de jogo.  
- Sincronização de dados de conquistas via **Supabase**.  

---

## 🧩 Comunicação entre Agentes

Os agentes se comunicam por eventos REST e WebSocket, coordenados pelo **Xavier** e gerenciados pela **REPI**.  
Essa estrutura mantém o sistema modular e permite escalar novas IAs ou modos de ensino sem quebrar o fluxo existente.

[Aluno] ⇄ [Xavier] ⇄ [Zeus] ⇄ [Gaia] ⇄ [Pulga] ⇄ [REPI]


Cada mensagem entre agentes é tratada como um **bloco contextual**, contendo:
- Identificação do aluno e progresso.  
- Histórico de aprendizado e tarefas pendentes.  
- Feedback automatizado e sugestão de próxima etapa.  

---

## 🧠 Foco em Escalabilidade

O backend foi projetado para escalar horizontalmente.  
Cada agente pode ser executado como um serviço independente, conectado por eventos assíncronos (via Redis ou WebSocket).  
Isso permite a execução simultânea de **milhares de jornadas de aprendizado** sem sobrecarga.

---

## 🧩 Segurança e Privacidade

- Dados criptografados em repouso e em trânsito.  
- Tokens de acesso (JWT) para autenticação e controle de sessão.  
- Logs de interação armazenados pela REPI com pseudonimização.  
- Conformidade com **LGPD** e **GDPR**.

---

## 🧭 Futuro da Arquitetura

1. **Front-end interativo** — integração com React / Next.js.  
2. **App mobile** — experiência multimodal e offline.  
3. **Ambiente virtual 3D** — integração com Unity/Roblox.  
4. **IA adaptativa** — agentes que evoluem com base no comportamento dos alunos.  
5. **Infra escalável** — arquitetura multi-tenant com SaaS completo.

Cada agente possui uma pasta independente na raiz (Zeus, Gaia, Pulga, Xavier, etc.), com seu respectivo README.md.



---

**© 2025 — Ensina.app**  
_Idealizado por Christian Barreto & GPT-5_
