# Análise Linha a Linha do Código Debug.py

Este documento apresenta uma explicação detalhada de cada parte do código [Debug.py](Debug.py), um programa para cálculo de compras com impostos e descontos.

---

## 1. Seção de Entrada de Dados

### Linha 1: Comentário
```python
# ENTRADA DE DADOS
```
Um comentário que indica o início da seção de coleta de dados do usuário. Comentários começam com `#` e são ignorados pelo Python.

---

### Linha 2: Coleta do nome do cliente
```python
cliente = input("Qual é seu nome? ")
```
- `input()`: Função nativa do Python que exibe uma mensagem ao usuário e aguarda entrada de texto
- `"Qual é seu nome? "`: A mensagem exibida (prompt) para orientar o usuário
- O resultado é armazenado na variável `cliente` como uma **string** (texto)

---

### Linha 3-4: Dados do Item 1
```python
qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))
```
- **Linha 3**: Coleta a quantidade do item 1
  - `input()`: Recebe o valor como texto
  - `int()`: Converte a string para número inteiro
  - Armazena em `qtd1`
  
- **Linha 4**: Coleta o preço do item 1
  - `input()`: Recebe o valor como texto
  - `float()`: Converte a string para número decimal (float)
  - Armazena em `item1`

> **Nota**: `int()` é usado para quantidades (números inteiros), enquanto `float()` é usado para preços (podem ter centavos).

---

### Linhas 5-8: Dados dos Itens 2 e 3

Seguem o mesmo padrão das linhas 3-4:
```python
qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))
```

---

## 2. Seção de Cálculos

### Linha 11: Comentário
```python
# CÁLCULOS DOS ITENS
```
Indica o início dos cálculos dos totais por item.

---

### Linhas 12-14: Cálculo do total de cada item
```python
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3
```
Multiplica a quantidade pelo preço de cada item:
- `total_item1 = qtd1 * item1` → Ex: 3 × R$ 50,00 = R$ 150,00
- O operador `*` realiza multiplicação aritmética

---

### Linha 16: Subtotal
```python
subtotal = total_item1 + total_item2 + total_item3
```
Soma os totais de todos os itens para obter o valor base antes dos impostos.

---

### Linha 17: Cálculo do imposto
```python
imposto = subtotal * 0.10
```
- Aplica 10% de imposto sobre o subtotal
- `0.10` representa 10% (10/100 = 0.10)
- Ex: R$ 300,00 × 0,10 = R$ 30,00

---

## 3. Seção de Desconto

### Linha 20: Comentário
```python
# DESCONTO
```
Indica o início do cálculo de desconto.

---

### Linha 21: Coleta do cupom de desconto
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```
- Exibe mensagem pedindo o percentual de desconto
- `float()` converte a entrada para número decimal
- Armazena o valor em `desconto_cupom` (ex: 15 para 15%)

---

### Linha 22: Cálculo do valor do desconto
```python
desconto = subtotal * (desconto_cupom / 100)
```
- `desconto_cupom / 100`: Converte percentual em decimal (15% → 0.15)
- Multiplica pelo subtotal para obter o valor monetário do desconto
- Ex: R$ 300,00 × 0,15 = R$ 45,00

---

## 4. Total Final

### Linha 25: Comentário
```python
# TOTAL FINAL
```
Indica o cálculo do valor total a pagar.

---

### Linha 26: Cálculo do total
```python
total = subtotal + imposto - desconto
```
- Soma o subtotal + imposto
- Subtrai o desconto
- Resultado é o valor final a ser pago

---

## 5. Seção de Exibição

### Linhas 29-30: Definição de formatadores
```python
linha = "=" * 31
separador = "-" * 31
```
- Cria strings de formatação visual para o recibo
- `"=" * 31`: Cria uma linha com 31 sinais de igual
- `"-" * 31`: Cria uma linha com 31 hífens

---

### Linhas 32-34: Cabeçalho do recibo
```python
print(linha)
print(f" Cliente: {cliente}")
print(linha)
```
- `print(linha)`: Imprime a linha superior
- `print(f" Cliente: {cliente}")`: Imprime o nome do cliente usando **f-string** (string formatada)
  - O `f` antes das aspas indica que há variáveis entre chaves `{}`
- `print(linha)`: Imprime a linha inferior do cabeçalho

---

### Linhas 35-37: Exibição dos itens
```python
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
```
- `: .2f`: Formato que limita a 2 casas decimais
- Exibe o total de cada item alinhado à direita do valor

---

### Linha 38: Separador
```python
print(separador)
```
Imprime a linha tracejada para separar itens dos valores totais.

---

### Linhas 39-40: Subtotal e Imposto
```python
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")
```
Exibe o subtotal e o valor do imposto com formatação de 2 casas decimais.

---

### Linhas 42-43: Desconto condicional
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
- **Condição**: `if desconto_cupom > 0:`
  - Verifica se o usuário inseriu um desconto maior que zero
  - Se não houver desconto (0), esta bloco é ignorado
  
- **Bloco indentado**: Apenas executa se a condição for verdadeira
  - `: .0f`: Formata o percentual sem casas decimais (15.0% → 15%)
  - O `-R$` indica que é um valor a ser subtraído

---

### Linhas 45-47: Total final
```python
print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```
- `print(linha)`: Linha superior do rodapé
- `print(f" TOTAL: ...")`: Exibe o valor total
  - `round(total, 2)`: Arredonda o total para 2 casas decimais (segurança extra)
  - `: .2f`: Formata com 2 casas decimais
- `print(linha)`: Linha inferior do rodapé

---

## Resumo do Fluxo do Programa

```
┌─────────────────────────────────────┐
│  1. ENTRADA DE DADOS                │
│     - Nome do cliente               │
│     - Quantidade e preço de 3 itens │
├─────────────────────────────────────┤
│  2. CÁLCULOS                         │
│     - Total por item                │
│     - Subtotal                      │
│     - Imposto (10%)                 │
│     - Desconto (se aplicável)       │
├─────────────────────────────────────┤
│  3. EXIBIÇÃO                        │
│     - Recibo formatado              │
│     - Total a pagar                 │
└─────────────────────────────────────┘
```

---

## Conceitos Python Utilizados

| Conceito | Exemplo no Código |
|----------|-------------------|
| Variáveis | `cliente`, `qtd1`, `item1` |
| Entrada de dados | `input()` |
| Conversão de tipos | `int()`, `float()` |
| Operadores aritméticos | `*`, `+`, `-`, `/` |
| F-strings | `f"Texto {variavel}"` |
| Formatação | `:.2f`, `:.0f` |
| Condicional | `if ... > 0:` |
| Comentários | `# texto` |