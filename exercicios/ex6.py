## Exercícios

#Vamos revisar funções adicionando type hints e Pydantic

#6. **Encontrar Valores Ausentes em uma Sequência**


def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))