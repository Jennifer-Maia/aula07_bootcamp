## Exercícios

#Vamos revisar funções adicionando type hints e Pydantic

#1. **Calcular Média de Valores em uma Lista**


from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

