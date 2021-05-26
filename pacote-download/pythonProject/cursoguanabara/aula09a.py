frase = 'Curso em vídeo Python'
print(frase)
#Fatiamento
print(frase[3]) #mostra a 4ª letra
print(frase[3:13]) #mostra as letras das posições 4ª até 12ª
print(frase[:13]) #mostra as letras do início até a 12ª
print(frase[15:22])
print(frase[2:19:2])
print(frase[3::2])
print(frase[::2])

#Análise
print(frase.count('O')) #conta o número de ocorrências da letra "O" e imprime na tela
print(frase.upper().count('O')) #É possível combinar métodos. Aqui estamos fazendo a contagem de "O" depois de
#deixar toda a frase com letras maísculas
print(len(frase.strip())) #conta o número de caracteres na cadeia após a mesma ter tido suprimido os espaços a
#no inicio e fim da string
print(frase.replace('Python', 'Android')) #Substitui Python por Android e imprime na tela, porém a string 'Curso
#em vídeo Python' não é efetivamente modificada. Para confirmar a alteração, é preciso fazer a atribuição:
#frase = frase.replace('Python', 'Android')
print('Curso' in frase) #verifica se existe a palavra 'Curso' na string frase
print(frase.find('Vídeo')) #Se encontra a palavra, retorna a posição do primeiro caractere; Se não encontra, retorna
#-1
print(frase.split()) #Divide uma string em uma lista formada por cada palavra separada. O ponto de separação
#por padrão é o espaço, porém pode-se definir outro separador com o parâmetro 'sep'