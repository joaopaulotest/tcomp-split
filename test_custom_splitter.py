"""
Testes para a implementação de split com fecho positivo
Equipe:
- Daniel Ferreira do Nascimento
- João Paulo Calixto da Silva
- Francisco Reginaldo
- Weller Uchoa Martins
Disciplina: Teoria da Computação - 2025.1
"""
import unittest
from custom_splitter import CustomSplitter

class TesteCustomSplitter(unittest.TestCase):
    
    def setUp(self):
        self.splitter = CustomSplitter()
    
    def test_fecho_positivo_caractere(self):
        resultado = self.splitter.split("aaaabbbb", "a+")
        self.assertEqual(resultado, ['', 'bbbb'])
    
    def test_digitos_com_fecho(self):
        resultado = self.splitter.split("123abc456def", r"\d+")
        self.assertEqual(resultado, ['', 'abc', 'def'])
    
    def test_conjunto_vogais_com_fecho(self):
        resultado = self.splitter.split("aeiobcdfgh", "[aeiou]+")
        self.assertEqual(resultado, ['', 'bcdfgh'])
    
    def test_conjunto_negado(self):
        resultado = self.splitter.split("hello^world", "[^^]+")
        self.assertEqual(resultado, ['', '^', ''])
    
    def test_sem_correspondencia(self):
        resultado = self.splitter.split("abcdef", "xyz")
        self.assertEqual(resultado, ["abcdef"])
    
    def test_exemplo_misto(self):
        resultado = self.splitter.split("a1b22c333d", r"\d+")
        self.assertEqual(resultado, ['a', 'b', 'c', 'd'])
    
    def test_erro_padrao_invalido(self):
        with self.assertRaises(ValueError):
            self.splitter.split("texto", "[abc")
    
    def test_erro_fecho_sem_token(self):
        with self.assertRaises(ValueError):
            self.splitter.split("texto", "+")

if __name__ == '__main__':
    unittest.main() 