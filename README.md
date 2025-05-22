# 🔐 Identificador de Bandeiras de Cartões de Crédito

Este projeto tem como objetivo desenvolver uma aplicação simples em **Python** capaz de identificar a bandeira de um cartão de crédito com base em seu número.

Além disso, exploramos como o **GitHub Copilot**, como assistente de codificação, pode acelerar o desenvolvimento, sugerir trechos de código e melhorar a produtividade.

---

## 🚀 Tecnologias Utilizadas

- Python 3.13.3  
- Visual Studio Code  
- GitHub Copilot  

---

## 🎯 Funcionalidades

- Entrada: número do cartão (como string, com ou sem espaços)
- Saída: nome da bandeira (Visa, MasterCard, etc.)
- Validação básica do número informado
- Função principal reutilizável (`identificar_bandeira`)
- Registro de resultados em arquivo (`test_results.txt`)
- Testes simples de verificação

---

## 🤖 Uso do GitHub Copilot

Durante o desenvolvimento, o GitHub Copilot foi utilizado para:

- Sugerir condições `if` com base nos prefixos (BIN/IIN)
- Gerar funções auxiliares para análise de prefixos e dígitos
- Criar estrutura inicial de testes
- Criar código para exportar os resultados para arquivo

> ⚠️ **Importante:** Nem todo código gerado pela IA está correto. Por exemplo, o Copilot sugeriu que a bandeira **Voyager** usava 16 dígitos, mas a base correta indica **15 dígitos**, o que levou a falha na identificação. Sempre revise o código gerado!

---

## ✅ Exemplos de Uso

```python
identificar_bandeira("4111 1111 1111 1111")  # Visa
identificar_bandeira("5500 0000 0000 0004")  # MasterCard
identificar_bandeira("3714 4963 5398 431")   # American Express


