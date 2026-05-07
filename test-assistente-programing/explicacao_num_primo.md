## Explicação linha a linha de num_primo.py

```python
from math import isqrt
```
- Importa a função `isqrt` do módulo `math`.
- `isqrt(number)` calcula a raiz quadrada inteira de `number` de forma segura e eficiente.

```python
def is_prime(number: int) -> bool:
```
- Declara a função `is_prime` com anotação de tipo.
- `number` é o valor a ser testado e a função retorna `True` ou `False`.

```python
    """Retorna True se o número for primo."""
```
- Docstring breve que descreve o propósito da função.
- Preferível manter as descrições objetivas em código simples.

```python
    if number <= 1:
        return False
```
- Verifica se o número é 1, 0 ou negativo.
- Esses valores não são primos, então a função retorna `False` imediatamente.

```python
    if number == 2:
        return True
```
- Trata o caso especial do número 2.
- 2 é o único primo par, então retorna `True` sem mais verificações.

```python
    if number % 2 == 0:
        return False
```
- Elimina todos os números pares maiores que 2.
- Esse teste simples reduz o trabalho do loop posterior.

```python
    max_divisor = isqrt(number)
```
- Calcula o maior divisor necessário para testar.
- Usar a raiz inteira evita conversões desnecessárias e mantém o código claro.

```python
    for divisor in range(3, max_divisor + 1, 2):
```
- Itera apenas por divisores ímpares a partir de 3.
- O passo `2` ignora pares, porque o caso par já foi tratado.
- Testa até `max_divisor` inclusive.

```python
        if number % divisor == 0:
            return False
```
- Verifica se o número é divisível por `divisor`.
- Se houver divisibilidade exata, o número é composto e não primo.
- Retorna `False` assim que encontra um divisor.

```python
    return True
```
- Se nenhum divisor foi encontrado, o número é primo.
- Essa linha é executada apenas após todas as tentativas de divisão.

```python
def run_tests() -> None:
```
- Declara função separada para executar os testes.
- Mantém `main` pequeno e melhora a organização do código.

```python
    try:
        number = int(input("Digite um número inteiro: "))
```
- Usa `input()` para solicitar um número ao usuário.
- `input()` lê a entrada como string e `int()` converte para inteiro.
- O `try-except` trata erros de conversão se o usuário digitar algo inválido.

```python
        result = is_prime(number)
        if result:
            print(f"O número {number} é primo!")
        else:
            print(f"O número {number} não é primo.")
```
- Chama a função `is_prime` com o número fornecido pelo usuário.
- Exibe mensagem clara indicando se o número é primo ou não.
- Usa `f-string` para formatar a saída com o número digitado.

```python
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
```
- Captura `ValueError` se o usuário digitar algo que não seja um número inteiro.
- Exibe mensagem de erro amigável orientando o usuário.

```python
if __name__ == "__main__":
    run_tests()
```
- Garante que os testes só serão executados ao rodar este arquivo diretamente.
- Quando o módulo for importado, a função `is_prime` fica disponível sem executar `run_tests()`.

---

## Resumo técnico

- O código agora usa `math.isqrt` para calcular a raiz quadrada inteira de forma explícita.
- A função `is_prime` possui anotações de tipo para maior clareza.
- `run_tests()` separa a lógica de verificação da lógica de execução de testes.
- O loop de verificação mantém apenas divisores ímpares depois de eliminar pares.
- A organização segue princípios de clean code: nomes claros, responsabilidades definidas e estrutura legível.
