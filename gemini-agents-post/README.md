# 🤖 Sistema Multiagente com Google Gemini – Criador de Post para Instagram

Este projeto é uma aplicação prática de Inteligência Artificial aplicada ao marketing digital, desenvolvida durante a Imersão IA promovida por Alura + Google. O sistema utiliza **agentes autônomos baseados em IA generativa** para criar conteúdos completos para redes sociais (Instagram), com foco em **lançamentos e tendências atuais**. Foram feitas pequenas adaptações e modificações no código original.

---
## 📌 Visão Geral

Este sistema é composto por **quatro agentes de IA** interconectados que executam de forma sequencial:

1. **Agente Pesquisador** – Realiza buscas em tempo real no Google para identificar os lançamentos mais relevantes de um tema.
2. **Agente Planejador** – Avalia os resultados do pesquisador e escolhe o melhor conteúdo a ser desenvolvido em um post.
3. **Agente Redator** – Cria um rascunho do post com linguagem adequada, hashtags e foco em engajamento.
4. **Agente Revisor** – Analisa o texto gerado, sugere melhorias ou valida sua qualidade final para publicação.

---

## 📋 Ficha Técnica

| Item                      | Detalhes                                                                 |
|---------------------------|--------------------------------------------------------------------------|
| 📦 Framework de Agentes   | [Google ADK](https://github.com/google/adk)                              |
| 🧠 Modelo de IA           | `gemini-2.0-flash` (via SDK oficial do Google)                           |
| 🔍 Ferramentas            | `google_search` via ADK Tools                                            |
| 📅 Execução               | Ambiente Google Colab                                                    |
| 📁 Organização            | Código modular com funções por agente e interface via `input()`          |
| 🔐 Segurança              | Uso de `userdata.get()` para acessar a chave de API de forma segura      |

---

## 🚀 Como Funciona

1. O usuário informa um tópico de interesse (ex: "inteligência artificial na saúde").
2. O agente pesquisador busca as últimas notícias sobre o tema.
3. O agente planejador define o melhor assunto e esboça o plano do post.
4. O agente redator escreve o post com linguagem adequada para o Instagram.
5. O agente revisor revisa, aprova ou sugere melhorias no conteúdo.

---

## 🧪 Exemplo de Saída

Dado o input:

```bash
Digite o tópico: artistas que se destacam na cena de jazz contemporâneo
```
## O sistema gera:
- Uma análise crítica dos artistas mais relevantes no último mês
- Um plano de conteúdo para post
- Um texto engajador para Instagram
- Uma revisão final com resumo da qualidade do post

## ✅ Requisitos
- Google Colab
- Conta Google com acesso à API Gemini
- Chave de API Gemini armazenada via userdata.get('GOOGLE_API_KEY')

## 💡 Aprendizados e Aplicações
Este projeto demonstra o poder dos sistemas multiagentes com LLMs aplicados em tarefas reais de conteúdo e marketing. Ele também mostra como usar a ferramenta google_search integrada a agentes autônomos com o Gemini para automatizar fluxos criativos com alta qualidade.

## 💡 Próximos Passos
-  Encapsular o fluxo principal em uma função (main()), para utilizar fora do ambiente Colab.
- Adicionar tratamento de exceções para requisições ou chamadas de API.
- Tornar os prompts de instrução parametrizáveis para maior flexibilidade.

## 📬 Contato
Para dúvidas, sugestões ou colaboração, sinta-se à vontade para abrir uma *issue* ou me enviar uma mensagem!



