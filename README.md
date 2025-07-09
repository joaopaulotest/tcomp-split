# Implementação de Split com Fecho Positivo

Trabalho da disciplina Teoria da Computação - 2025.1

## Nossa equipe
- Daniel Ferreira do Nascimento  
- João Paulo Calixto da Silva (representante)  
- Francisco Reginaldo  
- Weller Uchoa Martins  

## Como usar na prática
```python
from custom_splitter import CustomSplitter

# Cria uma instância do splitter personalizado
splitter = CustomSplitter()

# Exemplo simples de divisão por dígitos
texto = "123abc456"
partes = splitter.split(texto, r"\d+")
print(partes)  # Resultado: ['', 'abc', '']
```

Recursos implementados
- \d para reconhecer números de 0 a 9
- [ ] para criar grupos de caracteres
- + para indicar uma ou mais ocorrências

Testando nossa implementação
Execute os testes para verificar se tudo está funcionando:

```bash
python test_custom_splitter.py
```
Os testes devem mostrar que tudo passou com sucesso.

Exemplos reais
Veja exemplos práticos executando:

```bash
python exemplo_uso.py
```

Limitações conhecidas
Algumas limitações que encontramos durante o desenvolvimento:
- Não trabalhamos com grupos complexos ( )
- Não implementamos outros metacaracteres (*, ?, etc)
- Em textos muito grandes, o desempenho pode ser afetado

Referência teórica
Usamos como base o livro:
SIPSER, Michael. Introdução à Teoria da Computação. 2ª edição. São Paulo: Cengage Learning, 2007. 