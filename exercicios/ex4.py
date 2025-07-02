## Exercícios

#Vamos revisar funções adicionando type hints e Pydantic

#4. **Converter Celsius para Fahrenheit em uma Lista**


def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]