# 🧠 AI Multi-Agent Writer

## ✍️ Geração Colaborativa de Conteúdo com Agentes de IA

Este projeto demonstra a criação de um sistema colaborativo composto por **três agentes de inteligência artificial** — planejador, redator e editor — que trabalham juntos para produzir automaticamente artigos otimizados e coesos com base em um tema central. O sistema é alimentado pelo modelo **LLaMA 3** via **Ollama** e orquestrado pela biblioteca **CrewAI**.

---

## 🛠️ Ficha Técnica

| 🔍 **Item**             | 📄 **Descrição**                                           |
| ----------------------- | ---------------------------------------------------------- |
| **🛠️ Tecnologias**     | Python, LangChain, CrewAI, Ollama                          |
| **📦 Dependências**     | crewai, langchain, ollama                                  |
| **⚙️ Funcionalidade**   | Produção automática de artigos por múltiplos agentes de IA |
| **📌 Modelo Utilizado** | LLaMA 3 (via Ollama)                                       |
| **🤖 Arquitetura**      | 3 agentes (Planner, Writer, Editor) trabalhando em fluxo   |
| **📥 Entrada**          | Um tópico de interesse (ex: *social anthropology*)         |
| **📤 Saída**            | Artigo em formato Markdown, pronto para publicação         |

---

## 🧠 Agentes de IA no Projeto

1. **🗂️ Content Planner**
   Planeja o conteúdo com base em tendências, público-alvo e SEO.

2. **✍️ Content Writer**
   Redige o artigo com base no plano fornecido, com linguagem envolvente e bem estruturada.

3. **🧾 Editor**
   Revisa o texto para garantir qualidade editorial, clareza e adequação à voz da marca.

---

## 🚀 Como Usar

1. Certifique-se de que o **Ollama** esteja instalado e que o modelo `llama3` esteja disponível.
2. Instale as dependências com:

   ```bash
   pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
   ```
3. Execute o script Python e defina o tópico desejado (ex: `"social anthropology"`).
4. O resultado será exibido em formato Markdown, pronto para publicação.

---

## 🧑‍💻 Autor

**Thiago Tim**  
[🔗 LinkedIn](https://www.linkedin.com/in/devtim/) • [📂 Portfólio](https://github.com/thiagotims/) • [📫 Contato](mailto:thiagotimdev@gmail.com)

---

## 📃 Licença

Este projeto está sob a licença [MIT](LICENSE).
