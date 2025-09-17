# 🤖 Gerador Automático de Testes Pytest com Azure OpenAI

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-0078d4.svg)](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/)

Um agente inteligente que utiliza **LangChain** e **Azure OpenAI** para gerar automaticamente arquivos de teste pytest abrangentes e bem estruturados a partir de módulos Python. Esse projeto foi implementado como "desafio de projeto" do curso BairesDev - Machine Learning Training promovido pela Dio em parceria com a BairesDev. Esse projeto foi implementado como "desafio de projeto" do curso BairesDev - Machine Learning Training promovido pela Dio em parceria com a BairesDev.

----
## 🎯 **Funcionalidades**

- ✅ **Análise automática** de código Python para extrair funções
- ✅ **Geração inteligente** de casos de teste (sucesso, falha, edge cases)
- ✅ **Estruturação profissional** usando `@pytest.mark.parametrize`
- ✅ **Compatibilidade** com LangChain ≥0.2 e OpenAI ≥1.0.0
- ✅ **Validação de sintaxe** e tratamento de erros
- ✅ **Debug detalhado** e logging informativo
- ✅ **Documentação completa** em português

-----
## 📋 **Pré-requisitos**

### Software
- **Python 3.10+**
- **Conta Azure** com acesso ao Azure OpenAI Service

### Dependências Python
```bash
pip install langchain langchain-openai openai python-dotenv pytest
```

-----
## 🚀 **Configuração Rápida**

### 1. Clone e Configure o Ambiente
```bash
git clone https://github.com/thiagotims/ai-agents.git
cd unit-test-agent
pip install -r requirements.txt  
```

### 2. Configure o Azure OpenAI
1. **Acesse** [portal.azure.com](https://portal.azure.com)
2. **Crie** um recurso Azure OpenAI Service
3. **Crie** um deployment de modelo (recomendado: `gpt-35-turbo`)
4. **Copie** as credenciais (endpoint, API key, deployment name)

### 3. Configure o Arquivo `.env`
```env
# Copie suas credenciais do portal Azure
OPENAI_API_KEY=sua_api_key_aqui
AZURE_ENDPOINT=https://seu-recurso.openai.azure.com/
AZURE_DEPLOYMENT_NAME=nome_do_seu_deployment
OPENAI_API_VERSION=2023-05-15 #exemplo
```

-----
## 💻 **Como Usar**

### Uso Básico
```bash
# Gerar testes para o módulo de exemplo
python test_generator_agent.py

# Gerar testes para um módulo específico
python test_generator_agent.py meu_modulo.py
```

### Exemplo Prático
```python
# Exemplo de módulo Python (sample_module.py)
def extract_hashtags(text: str) -> List[str]:
    """Extrai hashtags (#palavras) de um texto."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return [tag[1:].lower() for tag in text.split() if tag.startswith("#")]
```

**Resultado:** Arquivo `test_sample_module.py` gerado automaticamente com testes abrangentes. Exemplo:
```python
import pytest
from sample_module import extract_hashtags

@pytest.mark.parametrize("text, expected", [
    ("Loving #Python and #AI today!", ["python", "ai"]),
    ("No hashtags here", []),
    ("#single", ["single"]),
])
def test_extract_hashtags_success_cases(text, expected):
    assert extract_hashtags(text) == expected

@pytest.mark.parametrize("invalid_input", [
    123, None, [], {}
])
def test_extract_hashtags_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        extract_hashtags(invalid_input)
```

-----
## 📁 **Estrutura do Projeto**

```
unit-test-agent/
├── 📜 test_generator_agent.py         # Agente principal
├── 📝 sample_module.py                # Módulo de exemplo
├── ⚙️  .env                           # Configurações (não versionado)
├── 📚 README.md                       # Esta documentação
```

-----
## 🧪 **Recursos de Teste Gerados**

O agente gera automaticamente:

### ✅ **Casos de Sucesso**
- Entradas válidas com saídas esperadas
- Casos típicos de uso
- Valores limítrofes válidos

### ❌ **Casos de Falha**
- Tipos incorretos de entrada
- Valores inválidos
- Exceções esperadas

### ⚡ **Edge Cases**
- Strings vazias, listas vazias
- Valores extremos (zero, negativos, muito grandes)
- Casos especiais específicos da função

### 📊 **Organização**
- `@pytest.mark.parametrize` para casos similares
- Nomes descritivos: `test_função_cenário`
- Documentação clara de cada teste

-----
## 🚨 **Solução de Problemas**

### Erro 404 "Resource not found"

**Soluções:**
- Verificar se `AZURE_DEPLOYMENT_NAME` está correto
- Confirmar se deployment foi criado no portal
- Aguardar alguns minutos após criação

### Erro 401 "Unauthorized"
**Soluções:**
- Verificar `OPENAI_API_KEY` no arquivo `.env`
- Regenerar chave no portal Azure se necessário
- Confirmar permissões do recurso

### Problemas de Região
**Soluções:**
- Criar recurso em `West US 2` ou `Central US` (comumente mais aceitas)
- Usar Azure AI Studio: [ai.azure.com](https://ai.azure.com)
- Verificar políticas da assinatura Azure

-----
## 📈 **Exemplos de Output**

### Input: `sample_module.py`
```python
def calculate_factorial(n: int) -> int:
    """Calcula fatorial de n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be non-negative integer")
    return 1 if n <= 1 else n * calculate_factorial(n-1)
```

### Output: `test_sample_module.py`
```python
import pytest
from sample_module import calculate_factorial

@pytest.mark.parametrize("n, expected", [
    (0, 1), (1, 1), (5, 120), (10, 3628800)
])
def test_calculate_factorial_success_cases(n, expected):
    assert calculate_factorial(n) == expected

@pytest.mark.parametrize("invalid_input", [
    -1, -5, "5", 5.5, None, []
])
def test_calculate_factorial_invalid_inputs(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        calculate_factorial(invalid_input)
```

-----
## 📝 **Licença**

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

-----
## 🧑‍💻 Autor / Contato
**Thiago Tim**  

Contribuições são bem-vindas!  Entre em contato:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devtim/) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:thiagotimdev@gmail.com)

---
