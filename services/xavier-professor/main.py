def orient(message: str):
    """Professor Xavier orienta e coordena os agentes do Ensina.app."""
    response = (
        f"Professor Xavier diz: '{message}'\n"
        "Lembre-se: o aprendizado não está na resposta, mas no caminho até ela."
    )
    return {"xavier": response}
