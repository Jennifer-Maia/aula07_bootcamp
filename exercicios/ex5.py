## Exercícios

#Vamos revisar funções adicionando type hints e Pydantic

#5. **Calcular Desvio Padrão de uma Lista**


def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5