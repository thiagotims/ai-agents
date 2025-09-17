"""
test_generator_agent.py

🤖 GERADOR AUTOMÁTICO DE TESTES PYTEST COM AZURE OPENAI
=========================================================

Este agente utiliza LangChain + Azure OpenAI para gerar automaticamente
arquivos de teste pytest a partir de módulos Python.

FUNCIONALIDADES:
- ✅ Extrai funções automaticamente do código fonte
- ✅ Gera testes de sucesso e falha
- ✅ Usa @pytest.mark.parametrize para organizar casos
- ✅ Compatível com LangChain ≥0.2 e OpenAI ≥1.0.0
- ✅ Sistema de debugging e validação

DEPENDÊNCIAS:
pip install langchain langchain-openai openai python-dotenv pytest

"""

import ast
import os
import sys
from typing import List, Dict, Optional
from dotenv import load_dotenv

# -------------------------------
# Imports LangChain atualizados
# -------------------------------
try:
    from langchain_core.prompts import PromptTemplate
    from langchain_openai import AzureChatOpenAI
    print("✅ Dependências LangChain carregadas com sucesso")
except ImportError as e:
    print(f"❌ Erro ao importar LangChain: {e}")
    print("   Execute: pip install langchain langchain-openai")
    sys.exit(1)


# -------------------------------
# Utilitários de análise de código
# -------------------------------
def extract_functions_info(code: str) -> List[Dict]:
    """
    Extrai informações detalhadas de todas as funções top-level do código.
    
    Args:
        code (str): Código fonte Python
        
    Returns:
        List[Dict]: Lista com informações das funções (name, args, doc, source)
        
    Raises:
        SyntaxError: Se o código não for Python válido
    """
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        raise SyntaxError(f"Código Python inválido: {e}")
    
    functions = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            name = node.name
            args = [arg.arg for arg in node.args.args]
            doc = ast.get_docstring(node) or ""
            
            # Tentar extrair código fonte
            try:
                source = ast.get_source_segment(code, node) or ""
            except (AttributeError, Exception):
                # Fallback para versões antigas do Python
                lines = code.split('\n')
                start_line = node.lineno - 1
                end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 10
                source = '\n'.join(lines[start_line:end_line])
            
            functions.append({
                "name": name,
                "args": args, 
                "doc": doc,
                "source": source.strip(),
                "line_number": node.lineno
            })
    
    return functions


def validate_python_syntax(code: str) -> bool:
    """Valida se o código Python tem sintaxe correta."""
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


# -------------------------------
# Prompt otimizado para geração de testes
# -------------------------------
PROMPT_TEMPLATE = """Você é um especialista em testes Python que cria arquivos pytest profissionais e abrangentes.

🎯 OBJETIVO: Criar um arquivo de teste pytest completo e bem estruturado.

📋 REGRAS OBRIGATÓRIAS:
1. INÍCIO: O arquivo deve começar exatamente com 'import pytest'
2. IMPORTS: Importe as funções usando: from {module_name} import função1, função2, ...
3. TESTES: Para cada função, crie:
   - Testes de casos válidos (sucesso)
   - Testes de casos inválidos (exceções/erros)
   - Testes de casos extremos (edge cases)
4. ORGANIZAÇÃO: Use @pytest.mark.parametrize sempre que possível
5. NOMES: Use nomes descritivos: test_[função]_[cenário]
6. COBERTURA: Teste diferentes tipos de entrada e saída

🔧 ESTRUTURA DE CADA TESTE:
- test_[função]_success_cases: Casos que devem funcionar
- test_[função]_invalid_inputs: Entradas que devem gerar erro
- test_[função]_edge_cases: Casos extremos

⚡ INFORMAÇÕES DO MÓDULO:
Nome do módulo: {module_name}
Número de funções: {function_count}

📊 DETALHES DAS FUNÇÕES:
{functions_info}

🧪 CÓDIGO COMPLETO DO MÓDULO:
```python
{code}
```

💻 RESPOSTA: Gere APENAS o conteúdo do arquivo test_{module_name}.py (sem explicações):"""


# -------------------------------
# Funções principais de geração
# -------------------------------
def generate_pytest_for_code(code: str, module_name: str, llm) -> str:
    """
    Gera o conteúdo do arquivo de testes pytest usando o modelo LLM.
    
    Args:
        code (str): Código fonte do módulo
        module_name (str): Nome do módulo (sem extensão)
        llm: Instância do modelo LangChain
        
    Returns:
        str: Conteúdo do arquivo de teste gerado
        
    Raises:
        ValueError: Se nenhuma função for encontrada
        Exception: Se houver erro na geração
    """
    print(f"🔍 Analisando código do módulo '{module_name}'...")
    
    # Validar sintaxe do código
    if not validate_python_syntax(code):
        raise ValueError("Código fonte contém erros de sintaxe")
    
    # Extrair informações das funções
    functions = extract_functions_info(code)
    if not functions:
        raise ValueError("Nenhuma função top-level encontrada no código fornecido.")
    
    print(f"📊 Encontradas {len(functions)} função(s): {[f['name'] for f in functions]}")
    
    # Formatar informações das funções para o prompt
    function_details = []
    for func in functions:
        detail = f"""
FUNÇÃO: {func['name']}
├── Assinatura: {func['name']}({', '.join(func['args'])})
├── Linha: {func['line_number']}
├── Docstring: {func['doc'] or 'Não documentada'}
└── Código:
{func['source']}
"""
        function_details.append(detail.strip())
    
    functions_info = "\n" + "="*50 + "\n".join(function_details)
    
    # Criar prompt
    prompt = PromptTemplate(
        input_variables=["module_name", "function_count", "functions_info", "code"],
        template=PROMPT_TEMPLATE,
    )
    
    print("🤖 Gerando testes com Azure OpenAI...")
    
    # Usar a sintaxe moderna do LangChain
    chain = prompt | llm
    
    try:
        result = chain.invoke({
            "module_name": module_name,
            "function_count": len(functions),
            "functions_info": functions_info,
            "code": code
        })
        
        # Extrair conteúdo da resposta
        if hasattr(result, 'content'):
            content = result.content
        else:
            content = str(result)
            
        print("✅ Testes gerados com sucesso!")
        return content
        
    except Exception as e:
        print(f"❌ Erro na geração: {e}")
        raise Exception(f"Falha ao gerar testes: {e}")


def generate_pytest_from_file(file_path: str, llm, output_path: Optional[str] = None) -> str:
    """
    Lê um arquivo Python e gera arquivo de testes correspondente.
    
    Args:
        file_path (str): Caminho para o arquivo Python
        llm: Instância do modelo LangChain
        output_path (str, optional): Caminho de saída personalizado
        
    Returns:
        str: Conteúdo do arquivo de teste gerado
        
    Raises:
        FileNotFoundError: Se o arquivo não existir
        Exception: Se houver erro na geração
    """
    print(f"📂 Processando arquivo: {file_path}")
    
    # Verificar se arquivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    # Ler código fonte
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        print(f"✅ Arquivo lido: {len(code)} caracteres")
    except Exception as e:
        raise Exception(f"Erro ao ler arquivo: {e}")
    
    # Extrair nome do módulo
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Gerar conteúdo dos testes
    test_content = generate_pytest_for_code(code, module_name, llm)
    
    # Definir caminho de saída
    if output_path is None:
        output_path = f"test_{module_name}.py"
    
    # Salvar arquivo de teste
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(test_content)
        print(f"💾 Arquivo de teste salvo: {output_path}")
    except Exception as e:
        print(f"⚠️  Erro ao salvar arquivo: {e}")
        print("🔍 Conteúdo gerado:")
        print("-" * 50)
        print(test_content)
        print("-" * 50)
        raise
    
    return test_content


def test_azure_connection() -> bool:
    """
    Testa a conexão com Azure OpenAI com informações detalhadas de debug.
    
    Returns:
        bool: True se conexão bem-sucedida, False caso contrário
    """
    load_dotenv()
    
    azure_endpoint = os.getenv("AZURE_ENDPOINT")
    api_key = os.getenv("OPENAI_API_KEY")
    deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")
    api_version = os.getenv("OPENAI_API_VERSION", "2023-05-15")
    temperature = float(os.getenv("TEMPERATURE", "0.1"))
    
    print("🔍 Debug - Configurações carregadas:")
    print(f"   AZURE_ENDPOINT: {azure_endpoint}")
    print(f"   AZURE_DEPLOYMENT_NAME: {deployment_name}")
    print(f"   API_KEY: {'*' * 20 + api_key[-10:] if api_key else 'Não encontrada'}")
    print(f"   API_VERSION: {api_version}")
    print(f"   TEMPERATURE: {temperature}")
    
    # Validações básicas
    if not all([azure_endpoint, api_key, deployment_name]):
        print("❌ Erro: Variáveis obrigatórias não encontradas no .env")
        print("   Verifique se AZURE_ENDPOINT, OPENAI_API_KEY e AZURE_DEPLOYMENT_NAME estão definidas")
        return False
    
    if not azure_endpoint.startswith("https://"):
        print("❌ Erro: AZURE_ENDPOINT deve começar com https://")
        return False
    
    if not azure_endpoint.endswith("/"):
        print("⚠️  Aviso: AZURE_ENDPOINT deve terminar com '/' - corrigindo automaticamente")
        azure_endpoint = azure_endpoint + "/"
    
    try:
        print("\n🚀 Testando conexão com Azure OpenAI...")
        llm = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            azure_deployment=deployment_name,
            api_key=api_key,
            api_version=api_version,
            temperature=temperature,
            max_tokens=50
        )
        
        # Teste simples
        print("📡 Enviando mensagem de teste...")
        response = llm.invoke("Responda apenas: Conexão OK!")
        
        if hasattr(response, 'content'):
            response_text = response.content
        else:
            response_text = str(response)
            
        print(f"✅ Sucesso! Resposta do modelo: '{response_text.strip()}'")
        return True
        
    except Exception as e:
        print(f"❌ Erro na conexão: {type(e).__name__}: {e}")
        
        # Sugestões específicas baseadas no tipo de erro
        error_str = str(e).lower()
        if "404" in error_str:
            print("💡 Sugestão: Verifique se o deployment foi criado e o nome está correto")
        elif "401" in error_str or "unauthorized" in error_str:
            print("💡 Sugestão: Verifique se a API key está correta e válida")
        elif "timeout" in error_str:
            print("💡 Sugestão: Problema de conectividade - tente novamente")
        else:
            print("💡 Sugestão: Execute 'python diagnose_azure_openai.py' para mais detalhes")
        
        return False


# -------------------------------
# Execução principal
# -------------------------------
def main():
    """Função principal que coordena a execução do gerador de testes."""
    print("🤖 GERADOR AUTOMÁTICO DE TESTES PYTEST")
    print("=" * 45)
    print("📅 Versão: 1.0 | Data: 2025-09-16")
    print("🔗 Powered by: LangChain + Azure OpenAI")
    print()
    
    # Primeiro testa a conexão
    print("🔧 ETAPA 1: Verificação da configuração")
    print("-" * 30)
    if not test_azure_connection():
        print("\n🛑 Parando execução devido ao erro de conexão.")
        print("\n📋 PRÓXIMOS PASSOS:")
        print("1. Verifique o arquivo .env")
        print("2. Execute: python diagnose_azure_openai.py")
        print("3. Confirme se o deployment foi criado no portal Azure")
        sys.exit(1)
    
    print("\n🧠 ETAPA 2: Inicialização do modelo")
    print("-" * 30)
    
    # Carregar configurações
    load_dotenv()
    azure_endpoint = os.getenv("AZURE_ENDPOINT")
    api_key = os.getenv("OPENAI_API_KEY")
    deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")
    api_version = os.getenv("OPENAI_API_VERSION", "2023-05-15")
    temperature = float(os.getenv("TEMPERATURE", "0.1"))
    max_tokens = int(os.getenv("MAX_TOKENS", "2000"))
    
    # Criar instância do LLM
    try:
        llm = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            azure_deployment=deployment_name,
            api_key=api_key,
            api_version=api_version,
            temperature=temperature,
            max_tokens=max_tokens
        )
        print(f"✅ Modelo configurado: {deployment_name}")
        print(f"   Temperature: {temperature} | Max tokens: {max_tokens}")
    except Exception as e:
        print(f"❌ Erro ao configurar modelo: {e}")
        sys.exit(1)
    
    print("\n📂 ETAPA 3: Processamento do arquivo")
    print("-" * 30)
    
    # Determinar arquivo de entrada
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "sample_module.py"
    
    print(f"📄 Arquivo de entrada: {input_file}")
    
    # Verificar se arquivo existe
    if not os.path.exists(input_file):
        print(f"❌ Arquivo não encontrado: {input_file}")
        print("\n📋 ARQUIVOS PYTHON DISPONÍVEIS:")
        python_files = [f for f in os.listdir('.') if f.endswith('.py') and not f.startswith('test_')]
        for file in python_files:
            print(f"   • {file}")
        sys.exit(1)
    
    # Gerar arquivo de testes
    try:
        print(f"\n🚀 Gerando testes para {input_file}...")
        test_content = generate_pytest_from_file(input_file, llm)
        
        # Estatísticas
        lines = len(test_content.split('\n'))
        test_functions = test_content.count('def test_')
        
        print(f"\n📊 ESTATÍSTICAS DO ARQUIVO GERADO:")
        print(f"   📏 Linhas de código: {lines}")
        print(f"   🧪 Funções de teste: {test_functions}")
        print(f"   📁 Arquivo salvo: test_{os.path.splitext(os.path.basename(input_file))[0]}.py")
        
        print(f"\n✅ PROCESSO CONCLUÍDO COM SUCESSO!")
        print(f"\n🧪 Para executar os testes:")
        print(f"   pytest test_{os.path.splitext(os.path.basename(input_file))[0]}.py -v")
        
    except FileNotFoundError as e:
        print(f"❌ Arquivo não encontrado: {e}")
    except ValueError as e:
        print(f"❌ Erro de validação: {e}")
    except Exception as e:
        print(f"❌ Erro durante geração: {e}")
        print("\n🔍 Para diagnóstico detalhado, execute:")
        print("   python diagnose_azure_openai.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
