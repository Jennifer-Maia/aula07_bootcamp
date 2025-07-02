## Exercícios

#Vamos revisar funções adicionando type hints e Pydantic

#2. **Filtrar Dados Acima de um Limite**


def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado