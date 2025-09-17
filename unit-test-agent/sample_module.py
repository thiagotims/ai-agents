"""
sample_module.py

🧪 MÓDULO DE EXEMPLO PARA GERAÇÃO AUTOMÁTICA DE TESTES
======================================================

Este módulo contém funções de exemplo bem documentadas para demonstrar
as capacidades do gerador automático de testes pytest.

Funcionalidades incluídas:
- ✅ Processamento de texto (hashtags, encurtamento)
- ✅ Operações matemáticas (fatorial, números primos)
- ✅ Manipulação de listas (filtros, transformações)
- ✅ Validação de dados (emails, CPF)

"""

import re
from typing import List, Union


def extract_hashtags(text: str) -> List[str]:
    """
    Extrai hashtags (#palavras) de um texto e retorna lista em minúsculas.
    
    Args:
        text (str): Texto para extrair hashtags
        
    Returns:
        List[str]: Lista de hashtags sem o símbolo #, em minúsculas
        
    Raises:
        TypeError: Se text não for string
        
    Examples:
        >>> extract_hashtags("Loving #Python and #AI today!")
        ['python', 'ai']
        >>> extract_hashtags("No hashtags here")
        []
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Usar regex para encontrar hashtags (# seguido de letras/números)
    hashtags = re.findall(r'#(\w+)', text)
    return [tag.lower() for tag in hashtags]


def shorten_text(text: str, max_len: int) -> str:
    """
    Encurta o texto para no máximo max_len caracteres, adicionando '...' se necessário.
    
    Args:
        text (str): Texto a ser encurtado
        max_len (int): Comprimento máximo permitido
        
    Returns:
        str: Texto encurtado ou original se não exceder max_len
        
    Raises:
        TypeError: Se text não for string ou max_len não for int
        ValueError: Se max_len for menor que 3 (impossível adicionar '...')
        
    Examples:
        >>> shorten_text("Este é um texto longo", 10)
        'Este é...'
        >>> shorten_text("Curto", 10)
        'Curto'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(max_len, int):
        raise TypeError("max_len must be int")
    if max_len < 3:
        raise ValueError("max_len must be at least 3 to accommodate '...'")
    
    if len(text) <= max_len:
        return text
    else:
        return text[:max_len-3] + "..."


def calculate_factorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro não negativo.
    
    Args:
        n (int): Número para calcular fatorial (n >= 0)
        
    Returns:
        int: Fatorial de n
        
    Raises:
        TypeError: Se n não for inteiro
        ValueError: Se n for negativo
        
    Examples:
        >>> calculate_factorial(5)
        120
        >>> calculate_factorial(0)
        1
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        n (int): Número a ser verificado
        
    Returns:
        bool: True se n for primo, False caso contrário
        
    Raises:
        TypeError: Se n não for inteiro
        
    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    
    if n < 2:
        return False
    
    # Verificar divisibilidade até a raiz quadrada
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filtra apenas os números pares de uma lista.
    
    Args:
        numbers (List[int]): Lista de números inteiros
        
    Returns:
        List[int]: Lista contendo apenas números pares
        
    Raises:
        TypeError: Se numbers não for lista ou contiver não-inteiros
        
    Examples:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> filter_even_numbers([1, 3, 5])
        []
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("all elements must be integers")
    
    return [num for num in numbers if num % 2 == 0]


def validate_email(email: str) -> bool:
    """
    Valida se uma string é um email válido usando regex simples.
    
    Args:
        email (str): String a ser validada como email
        
    Returns:
        bool: True se email for válido, False caso contrário
        
    Raises:
        TypeError: Se email não for string
        
    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    if not isinstance(email, str):
        raise TypeError("email must be a string")
    
    # Regex simples para validação de email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def convert_temperature(temp: Union[int, float], from_unit: str, to_unit: str) -> float:
    """
    Converte temperatura entre Celsius, Fahrenheit e Kelvin.
    
    Args:
        temp (Union[int, float]): Temperatura a ser convertida
        from_unit (str): Unidade de origem ('C', 'F', 'K')
        to_unit (str): Unidade de destino ('C', 'F', 'K')
        
    Returns:
        float: Temperatura convertida
        
    Raises:
        TypeError: Se temp não for número ou units não forem strings
        ValueError: Se unidades forem inválidas ou conversão resultar em temperatura impossível
        
    Examples:
        >>> convert_temperature(0, 'C', 'F')
        32.0
        >>> convert_temperature(273.15, 'K', 'C')
        0.0
    """
    if not isinstance(temp, (int, float)):
        raise TypeError("temp must be a number")
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("units must be strings")
    
    valid_units = ['C', 'F', 'K']
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("units must be 'C', 'F', or 'K'")
    
    # Converter tudo para Celsius primeiro
    if from_unit == 'F':
        celsius = (temp - 32) * 5/9
    elif from_unit == 'K':
        celsius = temp - 273.15
        if celsius < -273.15:
            raise ValueError("temperature below absolute zero")
    else:  # já é Celsius
        celsius = temp
        if celsius < -273.15:
            raise ValueError("temperature below absolute zero")
    
    # Converter de Celsius para unidade desejada
    if to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:  # manter Celsius
        return celsius

