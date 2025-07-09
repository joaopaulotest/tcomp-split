class CustomSplitter:
    """
    Implementação manual de função split com suporte a metacaracteres
    Desenvolvido por: 
    Daniel Ferreira do Nascimento, 
    João Paulo Calixto da Silva, 
    Francisco Reginaldo, 
    Weller Uchoa Martins
    Disciplina: Teoria da Computação - 2025.1
    """
    
    def tokenizar(self, padrao):
        """
        Converte o padrão em uma lista de tokens
        Cada token pode ser: caractere, digito ou conjunto
        """
        tokens = []
        i = 0
        n = len(padrao)
        
        while i < n:
            # Trata metacaractere \d (dígitos)
            if padrao[i] == '\\':
                if i + 1 < n and padrao[i+1] == 'd':
                    tokens.append({'tipo': 'digito', 'plus': False})
                    i += 2
                else:
                    raise ValueError("Erro: Escape incompleto")
            
            # Trata conjunto de caracteres [ ]
            elif padrao[i] == '[':
                j = i + 1
                negado = False
                caracteres = set()
                
                # Verifica negação [^ ]
                if j < n and padrao[j] == '^':
                    negado = True
                    j += 1
                
                # Coleta caracteres do conjunto
                while j < n and padrao[j] != ']':
                    if j + 2 < n and padrao[j+1] == '-':
                        inicio = padrao[j]
                        fim = padrao[j+2]
                        # Adiciona intervalo de caracteres
                        for codigo in range(ord(inicio), ord(fim) + 1):
                            caracteres.add(chr(codigo))
                        j += 3
                    else:
                        caracteres.add(padrao[j])
                        j += 1
                
                if j >= n:
                    raise ValueError("Erro: Conjunto não fechado")
                
                tokens.append({
                    'tipo': 'conjunto',
                    'caracteres': caracteres,
                    'negado': negado,
                    'plus': False
                })
                i = j + 1  # Pula o ']'
            
            # Trata fecho positivo +
            elif padrao[i] == '+':
                if not tokens:
                    raise ValueError("Erro: Nada para aplicar o +")
                # Aplica o plus ao último token
                tokens[-1]['plus'] = True
                i += 1
            
            # Trata caracteres normais
            else:
                tokens.append({
                    'tipo': 'caractere',
                    'valor': padrao[i],
                    'plus': False
                })
                i += 1
                
        return tokens

    def verificar_token(self, token, texto, posicao):
        """
        Verifica se o token casa na posição do texto
        Retorna número de caracteres casados (0 se não casar)
        """
        if posicao >= len(texto):
            return 0
            
        char = texto[posicao]
        
        # Verificação para caractere normal
        if token['tipo'] == 'caractere':
            return 1 if char == token['valor'] else 0
                
        # Verificação para dígitos
        elif token['tipo'] == 'digito':
            return 1 if char.isdigit() else 0
                
        # Verificação para conjuntos
        elif token['tipo'] == 'conjunto':
            no_conjunto = char in token['caracteres']
            if token['negado']:
                return 1 if not no_conjunto else 0
            else:
                return 1 if no_conjunto else 0
        
        return 0

    def verificar_padrao(self, tokens, texto, inicio):
        """
        Verifica o padrão completo a partir da posição inicial
        Retorna o total de caracteres casados
        """
        total_casados = 0
        pos_atual = inicio
        
        for token in tokens:
            casados = 0
            
            # Caso sem plus: verificação única
            if not token['plus']:
                if pos_atual >= len(texto):
                    return 0
                casados = self.verificar_token(token, texto, pos_atual)
                if casados == 0:
                    return 0
                pos_atual += casados
            
            # Caso com fecho positivo: múltiplas verificações
            else:
                # Enquanto houver correspondência
                while pos_atual + casados < len(texto):
                    c = self.verificar_token(token, texto, pos_atual + casados)
                    if c == 0:
                        break
                    casados += c
                    
                # Pelo menos uma ocorrência é obrigatória
                if casados == 0:
                    return 0
                pos_atual += casados
                
            total_casados += casados
            
        return total_casados

    def split(self, texto, padrao):
        """
        Divide o texto usando o padrão como delimitador
        Suporta metacaracteres: \\d, [ ], +
        """
        if not texto or not padrao:
            return [texto]
            
        try:
            tokens = self.tokenizar(padrao)
        except ValueError as e:
            raise ValueError(f"Erro no padrão: {str(e)}")
        
        partes = []
        inicio_parte = 0
        pos = 0
        
        while pos < len(texto):
            # Tenta casar o padrão a partir da posição atual
            casados = self.verificar_padrao(tokens, texto, pos)
            
            if casados > 0:
                # Adiciona a parte anterior ao delimitador
                partes.append(texto[inicio_parte:pos])
                # Atualiza posição para após o delimitador
                inicio_parte = pos + casados
                pos = inicio_parte
            else:
                pos += 1
                
        # Adiciona o restante do texto
        partes.append(texto[inicio_parte:])
        return partes 
        