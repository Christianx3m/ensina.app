import os
from openai import OpenAI

# Cria o cliente com a chave do .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Memória temporária para manter o contexto da conversa
sessions = {}

SYSTEM_PROMPT = """
Você é o Professor Xavier, diretor do Ensina.app.
Seu papel é ajudar o aluno a estruturar um projeto de aprendizado.
Você deve:
- Interpretar o que o aluno deseja criar ou aprender;
- Avaliar o nível de dificuldade e sugerir possíveis caminhos;
- Fazer perguntas para entender melhor o aluno e montar o plano de estudo;
- Sempre falar de forma didática e gentil, como um professor experiente.
"""

def start_session(student_id: str, project_description: str):
    """
    Cria uma nova sessão de aprendizado para o aluno.
    """
    sessions[student_id] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"O aluno disse que quer aprender ou criar: {project_description}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=sessions[student_id],
        temperature=0.7
    )

    message = response.choices[0].message.content.strip()

    # Armazena resposta na sessão
    sessions[student_id].append({"role": "assistant", "content": message})

    return {
        "resposta_do_xavier": message,
        "session_id": student_id
    }

def continue_session(student_id: str, answer: str):
    """
    Continua uma sessão existente, respondendo às perguntas do Xavier.
    """
    if student_id not in sessions:
        return {"erro": "Sessão não encontrada. Inicie uma nova com /xavier/analyze_project"}

    sessions[student_id].append({"role": "user", "content": answer})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=sessions[student_id],
        temperature=0.7
    )

    message = response.choices[0].message.content.strip()
    sessions[student_id].append({"role": "assistant", "content": message})

    return {"resposta_do_xavier": message}
