with open('br-sem-acentos.txt', 'r') as arquivo:
    lista_palavras = arquivo.read().split('\n')

palavra_mais_longa = ''

for palavra in lista_palavras:

    if len(palavra) <= len(palavra_mais_longa):
        continue                            # Caso a palavra atual seja menor que que a mais longa

    if any(caractere in palavra for caractere in ['g', 'k', 'm', 'q', 't', 'v', 'w', 'x', 'z']):
        continue                      # Caso a palavra atual possua algum dos caracteres proibidos

    palavra_mais_longa = palavra   # Palavra não possui nenhum caractere proibido e é a mais longa!

print(palavra_mais_longa)
