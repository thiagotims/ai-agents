# Stride Agent: Agente para Detecção de Vulnerabilidades em Arquiteturas 

Este projeto foi implementado como parte de um desafio de **cibersegurança aplicada a arquiteturas modernas**, utilizando:

- **Python + FastAPI** para a API backend
- **Azure OpenAI** para geração de modelos de ameaças via _prompt engineering_
- **Cytoscape.js** para visualização do grafo de ameaças
    
O objetivo é demonstrar como a metodologia **STRIDE** pode ser aplicada automaticamente para apoiar a **análise de riscos em arquiteturas de software**.  Esse projeto foi implementado como "_desafio de projeto_" do curso _BairesDev - Machine Learning Training_ promovido pela Dio em parceria com a BairesDev.

---
## 🚀 Funcionalidades
- Upload de **imagem da arquitetura** e preenchimento de informações do sistema.
- Geração automática de **modelo de ameaças STRIDE** usando **Azure OpenAI**.
- Exibição do modelo em **grafo interativo** com Cytoscape.js.
- Sugestões de melhoria para o modelo de ameaças.
- Botão para **imprimir/exportar o grafo** gerado.

---
## 📌 Metodologia STRIDE

A aplicação segue a metodologia **STRIDE**, contemplando as seguintes categorias de ameaças:
- **S**poofing (Falsificação de Identidade)
- **T**ampering (Violação de Integridade)
- **R**epudiation (Repúdio)
- **I**nformation Disclosure (Divulgação de Informações)
- **D**enial of Service (Negação de Serviço)
- **E**levation of Privilege (Elevação de Privilégio)

---
## 📂 Estrutura do projeto

```
stride-threat-analyzer/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env (criado pelo usuário)
│
├── frontend/
│   └── index.html
│
└── README.md
```

---
## 🛠️ Como executar o projeto

### 1. Pré-requisitos
- **Python 3.10+**
- **Conta no Azure OpenAI** com um deployment configurado
- (Opcional) **Node.js** caso queira servir o front-end com um servidor local

---
### 2. Clonando o repositório
```bash
git clone https://github.com/thiagotims/ai-agents.git
cd ai-agents/stride-agent
```

---
### 3. Configurando o backend (FastAPI)

Acesse a pasta do backend:
```bash
cd backend
```

Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Crie um arquivo **`.env`** com as variáveis de ambiente do Azure OpenAI:
```ini
AZURE_OPENAI_API_KEY=xxxxxx
AZURE_OPENAI_ENDPOINT=https://<seu-endpoint>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-09-11
AZURE_OPENAI_DEPLOYMENT_NAME=<nome-do-deployment>
```

Execute o backend:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```
O backend estará disponível em:  
👉 **[http://localhost:8001](http://localhost:8001/)**

---
### 4. Configurando o front-end

Acesse a pasta do front-end:
```bash
cd ../frontend
```

Abra o arquivo **`index.html`** diretamente no navegador.

Se preferir servir com um servidor local:
```bash
npx serve .
# ou
python -m http.server 8080
```

> ⚠️ O front-end espera que o backend esteja rodando em **[http://localhost:8001](http://localhost:8001/)**

---
## ⚡ Cuidados e dicas
- **Azure OpenAI**: certifique-se de que seu deployment está ativo e as variáveis do `.env` estão corretas.
- **CORS**: o backend já está configurado para aceitar requisições de qualquer origem (ajuste em produção).
- **Limite de tokens**: ajuste `max_tokens` no backend se a resposta vier cortada.
- **Impressão do grafo**: o botão **"Imprimir Grafo"** exporta a visualização como imagem para PDF ou impressão.
- **Formato JSON**: o front-end espera o retorno do backend no formato configurado.
- **Portas**: use **8001** para o backend e **8080** (ou outra) para o front-end.

---
## 📃 Licença
Este projeto está sob a licença [MIT](LICENSE).

---
## 📮Contato
**Thiago Tim**  

Contribuições são bem-vindas!  Entre em contato:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devtim/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:thiagotimdev@gmail.com)
