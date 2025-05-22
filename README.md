# 🔐 Identificador de Bandeiras de Cartões de Crédito

Este projeto tem como objetivo desenvolver uma aplicação simples em Python capaz de identificar a bandeira de um cartão de crédito com base em seu número.

## 🚀 Tecnologias
- Python 3.10+
- GitHub Copilot (como assistente de codificação)

## 🎯 Funcionalidades
- Entrada: número do cartão (string)
- Saída: bandeira correspondente (Visa, MasterCard, etc.)
- Validação básica de entrada
- Testes simples

## 📦 Como usar

```bash
python main.py


## Ou use a função `identificar_bandeira(numero_cartao)` diretamente.

---

### 🤖 Uso do GitHub Copilot

Durante o desenvolvimento, o GitHub Copilot foi utilizado para:

- Sugerir condições `if` baseadas em padrões de prefixo
- Gerar funções auxiliares
- Criar mensagens de erro
- Gerar estrutura de testes

---

### ✅ Exemplos

```python
identificar_bandeira("4111 1111 1111 1111")  # Visa
identificar_bandeira("5500 0000 0000 0004")  # MasterCard
