import Avl
import time
from unidecode import unidecode

def ler_arquivo(nomeArqv):
    with open(nomeArqv, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    return texto

def remover_char_especial(string):
    char_especiais = '!@#$%¨&*()_=+[]}{/?:;.,><"'
    for i in char_especiais:
        string = string.replace(i, '')
    return string

def filtrar_texto(texto):
    texto = texto.split("\n")
    texto_formatado = []
    for frase in texto:
        frase = frase.split()
        for i in frase:
            if i not in texto_formatado:
                texto_formatado.append(i)
    
    palavras_excluidas = ['mas', 'é', 'e','em', 'se', 'ou', 'a','as','nas', 'o', 'os', 'nos', 'mais', 'com', 'uma', 'umas', 'da', 'das', 'dos', 'de', 'um', 'uns','do', 'por']
    for i, palavra in enumerate(texto_formatado):
        texto_formatado[i] = str(palavra).lower() 
        texto_formatado[i] = remover_char_especial(texto_formatado[i])
 
    texto_semi = [unidecode(palavra) for palavra in texto_formatado]
    for i, palavra in enumerate(texto_semi):
        if palavra in palavras_excluidas:
            texto_semi.remove(palavra)

    texto_retorno = []
    for palavra in texto_semi:
        if palavra not in texto_retorno:
            texto_retorno.append(palavra)

    return texto_retorno

def addTextOnAVL (self, text):
    for word in text:
      self.add(word)

def buscar_no_vetor(vetor, palavraChave):
    vetRetorno = []
    for palavra in vetor:
        if str(palavra).startswith(palavraChave):
            vetRetorno.append(str(palavra))
    return vetRetorno



avlTree = Avl.AVLTree()

texto = ler_arquivo("corpus.txt") 
texto = filtrar_texto(texto)
print(f'Quantidade de palavras da base de dados: {len(texto)}')
## Inserção em Avl
time_inicial = time.time()
addTextOnAVL(avlTree, texto)
time_final = time.time()
print(f'Executou a inserção na AVL em: {time_final - time_inicial:.0e}')

## Inserção em Vetor
vetorTexto = []
time_inicial = time.time()
for palavra in texto:
    vetorTexto.append(palavra)
time_final = time.time()
print(f'Executou a inserção no vetor em: {time_final - time_inicial:.0e}')

busca = input()

# Busca na AVL
time_inicial = time.time()
result = avlTree.autoCompletar(busca)
time_final = time.time()
print(f'Executou a busca na AVL em: {time_final - time_inicial:.0e}')
print(result)


# Busca no Vetor
time_inicial = time.time()
result = buscar_no_vetor(vetorTexto, busca)
time_final = time.time()
print(f'Executou a busca no vetor em: {time_final - time_inicial:.0e}')
print(result)





