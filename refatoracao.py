def calcular_estatisticas(numeros: list[int]) -> tuple[int, float, int, int]:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros: Lista de números inteiros.
    
    Returns:
        Tupla com (total, média, maior, menor).
    """
    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    
    return total, media, maior, menor


if __name__ == "__main__":
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    total, media, maior, menor = calcular_estatisticas(numeros)
    
    print(f"Total: {total}")
    print(f"Média: {media}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")