def definePalavra(palavra, letrasAcertadas):
    result = ''
    for i in range(0, (len(palavra))):
        if palavra[i] in (letrasAcertadas):
            result = result + palavra[i]
        else:
            result = result + '_'
            
    return result 

def defineAcertos(palavra):
    acertos = 0
    for i in range(0, len(palavra)):
        if palavra[i] != '_':
            acertos += 1
            
    return acertos        


def desenhaJogo(erros, palavra):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print(palavra)
        print()
    elif erros == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print(palavra)
        print()    
    elif erros == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /  ")
        print("|      ")
        print("|      ")
        print(palavra)
        print()    
    elif erros == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|      ")
        print("|      ")
        print(palavra)
        print() 
    elif erros == 4:
        print()
        print("|-----   ")
        print("|    |   ")
        print("|    O   ")
        print("|   /|\\ ")
        print("|        ")
        print("|        ")
        print(palavra)
        print()    
    elif erros == 5:
        print()
        print("|-----   ")
        print("|    |   ")
        print("|    O   ")
        print("|   /|\\ ")
        print("|    |   ")
        print("|        ")
        print(palavra)
        print()    
    elif erros == 6:
        print()
        print("|-----   ")
        print("|    |   ")
        print("|    O   ")
        print("|   /|\\ ")
        print("|    |   ")
        print("|   /    ")
        print(palavra)
        print()
    elif erros == 7:
        print()
        print("|-----   ")
        print("|    |   ")
        print("|    O   ")
        print("|   /|\\ ")
        print("|    |   ")
        print("|   / \\ ")
        print(palavra)
        print()    