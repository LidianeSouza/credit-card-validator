# 🔐 Identificador de Bandeiras de Cartões de Crédito 💳

Olá! 👋
Seja bem-vindo(a) ao meu projeto de detecção de bandeiras de cartões de crédito! 

Esse é um projeto simples, com o objetivo de desenvolver uma aplicação em **Python** capaz de identificar a bandeira de um cartão de crédito com base em seu número.

Além disso, o uso do **GitHub Copilot**, como assistente de codificação, pode acelerar o desenvolvimento, sugerir trechos de código e melhorar a produtividade.

---

## 🧠 O que você vai encontrar aqui

- Um script que identifica a bandeira de um cartão a partir dos primeiros dígitos do número
- Um conjunto de testes para garantir que tudo esteja funcionando corretamente
- Um código simples, limpo e fácil de entender

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
- Sugerir condições `if` com base nos prefixos
- Gerar funções auxiliares para análise de prefixos e dígitos
- Criar estrutura inicial de testes
- Criar código para exportar os resultados para arquivo

---

## 📁 Estrutura do Projeto

card-flag-detector/
- src/ # Código-fonte da aplicação
  - main.py # Função principal que identifica a bandeira
- tests/ # Testes automatizados
  - test_main.py # Casos de teste com unittest
- data/ # Resultados de execução
  - test_results.txt # Arquivo de saída com resultados dos testes
- docs/ # Documentações adicionais
  - notas_importantes.md# Observações e anotações relevantes
- README.md # Documentação principal do projeto

---
