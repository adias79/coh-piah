import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    grau_de_similaridade = ((as_a[0]-as_b[0])+(as_a[1]-as_b[1])+(as_a[2]-as_b[2])+(as_a[3]-as_b[3])+(as_a[4]-as_b[4]))/6
    
    return grau_de_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    sentencas = separa_sentencas(texto)
    
    frases = []
    for i in sentencas:
        frases_separadas = separa_frases(i)
        frases = frases + frases_separadas
    
    palavras = []
    for i in frases:
        palavras_separadas = separa_palavras(i)
        palavras = palavras + palavras_separadas

    total_de_sentencas = 0
    for i in sentencas:
        total_de_sentencas = total_de_sentencas + 1
    
    total_de_frases = 0
    for i in frases:
        total_de_frases = total_de_frases + 1

    total_de_palavras = 0
    for i in palavras:
        total_de_palavras = total_de_palavras + 1

    total_de_caracteres = 0
    for i in palavras:
        total_de_caracteres = total_de_caracteres + len(i)

    total_de_palavras_diferentes = n_palavras_diferentes(palavras)

    total_de_palavras_unicas = n_palavras_unicas(palavras)

    tam_medio_de_palavra = total_de_caracteres / total_de_palavras
    type_token = total_de_palavras_diferentes / total_de_palavras
    hapax_legomana = total_de_palavras_unicas / total_de_palavras
    tam_medio_de_sentenca = total_de_caracteres / total_de_sentencas
    complexidade_de_sentenca = total_de_frases / total_de_sentencas
    tam_medio_de_frase = total_de_caracteres / total_de_frases

    assinatura = [tam_medio_de_palavra,type_token,hapax_legomana,tam_medio_de_sentenca,complexidade_de_sentenca,tam_medio_de_frase]
    
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    graus_de_similaridade = []
    for i in textos:
        grau_de_similaridade = compara_assinatura(calcula_assinatura(i),ass_cp)
        graus_de_similaridade.append(grau_de_similaridade)

    return print(min(graus_de_similaridade))