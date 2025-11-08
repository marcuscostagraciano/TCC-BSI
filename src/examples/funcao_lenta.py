def funcao_lenta(entrada: int) -> str:
    resultado: str = ''
    for _ in range(entrada):
        resultado += str(_)
    return resultado