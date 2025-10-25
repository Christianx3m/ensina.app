# ⚙️ Ritmo de Desenvolvimento — Ensina.app

## 🚀 Fase 1 — Estrutura Base (Atual)
- [x] Criação do backend com FastAPI
- [x] Agentes Zeus, Gaia e Pulga operando em rotas independentes
- [x] Ambiente virtual e requirements configurados
- [x] Servidor local funcional (Uvicorn)

### Próximos passos:
- [ ] Integrar Xavier (Diretor) como orquestrador dos agentes
- [ ] Adicionar autenticação com login via Google
- [ ] Criar banco de dados inicial (SQLite → PostgreSQL)
- [ ] Criar dashboard administrativo para professores e alunos

---

## 🌱 Fase 2 — Plataforma Web
- [ ] Interface em React/Tailwind
- [ ] Painel de criação e gerenciamento de cursos
- [ ] Sistema de avaliação e badges (gamificação)
- [ ] Biblioteca pessoal do aluno

---

## 🔗 Fase 3 — Integrações e Expansão
- [ ] Integração com WhatsApp via API oficial
- [ ] Sistema de assinatura e monetização
- [ ] Deploy em nuvem (Railway, Render ou GCP)
- [ ] Documentação completa via Swagger e Markdown

---

## 🧭 Diretrizes gerais
- Cada agente deve operar em **microserviços independentes**.
- O backend servirá como **hub de orquestração**.
- Toda funcionalidade deve ser **testada modularmente** antes da integração.
