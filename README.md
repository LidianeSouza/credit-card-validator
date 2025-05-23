# 🔐 Identificador de Bandeiras de Cartões de Crédito 💳

Olá! 👋  
Seja bem-vindo(a) ao meu projeto de detecção de bandeiras de cartões de crédito!

Este é um projeto simples, desenvolvido com o objetivo de criar uma aplicação em **Python** capaz de identificar a bandeira de um cartão de crédito com base em seu número.

Além disso, explorei o uso do **GitHub Copilot** como assistente de codificação — uma ferramenta que pode acelerar o desenvolvimento, sugerir trechos de código e aumentar a produtividade.

---

## 🧠 O que você vai encontrar aqui

- Um script que identifica a bandeira de um cartão a partir dos primeiros dígitos
- Um conjunto de testes automatizados para validar a aplicação
- Um código simples, limpo e fácil de entender

---

## 🚀 Tecnologias Utilizadas

- Python 3.13  
- Visual Studio Code  
- GitHub Copilot (IA para desenvolvimento)  
- Testes automatizados  
- Estrutura de diretórios clara  
- Muita vontade de aprender 😄

---

## 🎯 Funcionalidades

- **Entrada flexível**: aceita números de cartão como string, com ou sem espaços
- **Identificação automática da bandeira**: Visa, MasterCard e outras, com base nos prefixos
- **Validação básica**: verifica se o número inserido segue um padrão válido
- **Função reutilizável**: `identificar_bandeira` pode ser aplicada em outros projetos
- **Testes automatizados**: garantem o correto funcionamento da lógica
- **Exportação de resultados**: os resultados dos testes são registrados em `results/test_results.txt` para rastreabilidade
- **Organização clara**: código, testes, resultados e documentação separados em pastas específicas

---

## 🤖 Uso do GitHub Copilot

Durante o desenvolvimento, o GitHub Copilot foi utilizado para:

- Sugerir a estrutura inicial da função de identificação
- Gerar rapidamente os primeiros casos de teste
- Criar trechos de código para exportar os resultados de testes

Essa experiência mostrou como a IA pode ser uma excelente aliada no aprendizado, sem substituir o raciocínio lógico e a prática ativa.

---

## 📁 Estrutura do Projeto

card-flag-detector/
- notes/ # Documentações adicionais
  - base.png
  - notas_importantes.md# Observações e anotações relevantes
- results/ # Resultados de execução
  - test_results.txt # Arquivo de saída com resultados dos testes
- src/ # Código-fonte da aplicação
  - main.py # Função principal que identifica a bandeira
- tests/ # Testes automatizados
  - test_main.py # Casos de teste
- README.md # Documentação principal do projeto

---
