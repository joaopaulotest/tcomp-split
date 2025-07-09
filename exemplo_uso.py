"""
Exemplos de uso da implementação de split
Equipe:
- Daniel Ferreira do Nascimento
- João Paulo Calixto da Silva
- Francisco Reginaldo
- Weller Uchoa Martins
Disciplina: Teoria da Computação - 2025.1
"""
from custom_splitter import CustomSplitter

def main():
    splitter = CustomSplitter()
    
    print("Exemplo 1: Divisão por dígitos")
    texto = "123abc456def"
    print(f"Texto: {texto}")
    print(f"Padrão: \\d+")
    print(f"Resultado: {splitter.split(texto, r'\d+')}")
    print()
    
    print("Exemplo 2: Divisão por vogais repetidas")
    texto = "aeiobcdfgh"
    print(f"Texto: {texto}")
    print(f"Padrão: [aeiou]+")
    print(f"Resultado: {splitter.split(texto, '[aeiou]+')}")
    print()
    
    print("Exemplo 3: Divisão por 'o's repetidos")
    texto = "hellooooooworld"
    print(f"Texto: {texto}")
    print(f"Padrão: o+")
    print(f"Resultado: {splitter.split(texto, 'o+')}")
    print()
    
    print("Exemplo 4: Caso complexo")
    texto = "a1b22c333d4444e"
    print(f"Texto: {texto}")
    print(f"Padrão: \\d+")
    print(f"Resultado: {splitter.split(texto, r'\d+')}")

if __name__ == "__main__":
    main() 