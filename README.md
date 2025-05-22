# 🔐 Identificador de Bandeiras de Cartões de Crédito

Este projeto tem como objetivo desenvolver uma aplicação simples em Python capaz de identificar a bandeira de um cartão de crédito com base em seu número.

## 🚀 Tecnologias
- Python 3.13.3
- VS Studio Code
- GitHub Copilot (como assistente de codificação)
  
## 🎯 Funcionalidades
- Entrada: número do cartão
- Saída: bandeira correspondente (Visa, MasterCard, etc.)
- Validação básica de entrada
- Testes simples

### 🤖 Uso do GitHub Copilot

Durante o desenvolvimento, o GitHub Copilot foi utilizado para:

- Sugerir condições `if` baseadas em padrões de prefixo
- Gerar funções auxiliares
- Gerar estrutura de testes

Anotações importantes:
- Sempre conferir o codigo gerado pela IA> No caso, o Copilot escreveu uma parte do código incorretamente na bandeira Voyager ele tinha inserido 16 dígitos, sendo que no print "base" consta 15, então o resultado gerado vinha como "desconhecido".
- Pedi para o Copilot criar um código python que envie os resultados obtidos no terminal para o arquivo test_results.txt e ficar mais organizado a visualização dos resultados aqui no repositório.

## 📦 Como usar

```bash
python main.py


## Ou use a função `identificar_bandeira(numero_cartao)` diretamente.

---

