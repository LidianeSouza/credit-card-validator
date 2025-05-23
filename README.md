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

- Python 3.13 
- Visual Studio Code  
- GitHub Copilot (IA para desenvolvimento)
- Testes automatizados
- Estrutura de diretórios clara
- Muita vontade de aprender 😄
  
---

## 🎯 Funcionalidades

- **Entrada flexível**: aceita números de cartão como string, com ou sem espaços
- **Identificação automática da bandeira**: Visa, MasterCard, e outras com base nos primeiros dígitos
- **Validação básica**: verifica se o número inserido tem formato válido
- **Função reutilizável**: `identificar_bandeira` pode ser usada em outros contextos
- **Testes automatizados**: garantem o correto funcionamento do sistema
- **Exportação de resultados**: os testes são registrados em `results/test_results.txt` para rastreabilidade
- **Organização por pastas**: código, testes e resultados separados para facilitar a manutenção

---

## 🤖 Uso do GitHub Copilot

Durante o desenvolvimento, o GitHub Copilot foi utilizado para:
- Sugerir a estrutura inicial da função de identificação
- Criar estrutura inicial de testes
- Criar código para exportar os resultados para arquivo

Essa experiência me mostrou como a IA pode ser uma excelente parceira para quem está aprendendo, sem deixar de lado o raciocínio lógico e o aprendizado ativo.

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
