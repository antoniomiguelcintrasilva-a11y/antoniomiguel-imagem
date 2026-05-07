## Explicação da Refatoração de refatoracao.py

### Código Original

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

### Código Refatorado

```python
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
```

---

## Melhorias Aplicadas

### 1. Nomenclatura de Função e Parâmetros
- **Antes**: `c(l)` — nome abreviado e confuso
- **Depois**: `calcular_estatisticas(numeros)` — nome descritivo que indica o propósito

### 2. Nomenclatura de Variáveis
- **Antes**: `t, m, mx, mn, a, b, c2, d` — nomes incompreensíveis
- **Depois**: `total, media, maior, menor, numeros` — nomes autoexplicativos

### 3. Uso de Funções Built-in
- **Antes**: Loop manual para somar (`for i in range(len(l))`)
- **Depois**: `sum(numeros)` — mais eficiente e idiomático

### 4. Cálculo de Máximo e Mínimo
- **Antes**: Loop manual para encontrar maior e menor
- **Depois**: `max(numeros)` e `min(numeros)` — funções built-in do Python

### 5. Tipagem de Dados
- **Antes**: Sem nenhum tipo definido
- **Depois**: `list[int]` e `tuple[int, float, int, int]` — annotations de tipo para clareza

### 6. Docstring
- **Antes**: Sem documentação
- **Depois**: Docstring explicativa com Args e Returns

### 7. Proteção if __name__ == "__main__"
- **Antes**: Código executado automaticamente ao importar
- **Depois**: Código só executa quando o arquivo é rodado diretamente

### 8. Formatação de Saída
- **Antes**: `print("total:",a)` — formato antigo
- **Depois**: `f"Total: {total}"` — f-strings mais legíveis

---

## Resumo

A refatoração transformou um código obscuro e difícil de manter em um código limpo, legível e que segue as boas práticas do Python. As principais melhorias foram:
- Nomes descritivos para funções e variáveis
- Uso de funções built-in do Python
- Adição de tipagem e documentação
- Estrutura modular com proteção de execução