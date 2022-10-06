curso  =  ' pyThon  '

print(curso.upper()) #deixa tudo maisculo

print(curso.lstrip()) #remove espaço da esquerda

print(curso.rstrip()) ## remomve espaço da direira

curso = "python"

print(curso.center(10,"#")) #centraliza o texto e acrescenta a # como  caracteres concatenados

print('.'.join(curso)) #vai colocar o caracte em cada letra que passar


nome = 'pAulo'

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = '  ola mundo  '

print(texto)
print(texto.strip() + ".")
print(texto.rstrip()  + ".")
print(texto.lstrip() +  '.')

menu = 'pyhton'

print(menu.center(14,"."))
print('-'.join(menu))




pi = 3.14159

print(f'valor de pi: {pi:.2f}')