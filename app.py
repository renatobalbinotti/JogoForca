from componentesTela.moduloInputs import inputCriaUsuario, inputDefinicaoPalavra, inputLetra
from componentesTela.moduloJanelas import definePalavra, defineAcertos, desenhaJogo
from jogo.moduloJogo import defineJogadorDesafiadoDesafiador, obtemJogadorDesafiado, obtemJogadorDesafiador

print('Bem vindo ao jogo da forca!\n')

while True:
    jogador1 = inputCriaUsuario()
    jogador2 = inputCriaUsuario()

    defineJogadorDesafiadoDesafiador(jogador1, jogador2)

    jogadorDesafiador = obtemJogadorDesafiador(jogador1, jogador2)
    jogadorDesafiado = obtemJogadorDesafiado(jogador1, jogador2)
    palavra = inputDefinicaoPalavra(jogadorDesafiador)

    bancoDeLetras = []
    letrasAcertadas = []
    acertos = 0
    erros = 0

    while True:
        hiddenPalavra = definePalavra(palavra, letrasAcertadas)
        acertos = defineAcertos(hiddenPalavra)
        desenhaJogo(erros, hiddenPalavra)
        
        if acertos == len(palavra):
            print(f"Parabéns {jogadorDesafiado.get('nome')}! Você venceu!") 
            break
        
        if erros == 7:
            print(f"Que pena {jogadorDesafiado.get('nome')}! Você perdeu!!")
            break
        
        letra = inputLetra(jogadorDesafiado)
        
        if letra.upper() not in (bancoDeLetras):
            bancoDeLetras.append(letra.upper())
        else:
            print(f"{jogadorDesafiado.get('nome')}, você já informou essa letra!") 
            print('Tente novamente!')
            
        if letra.upper() in (palavra.upper()):     
            letrasAcertadas.append(letra)
        else:
            erros += 1
    
    resp = input('\nGostariam de jogar novamente? S/N ')
    
    if resp in 'Nn':
        break
    
    print('\n'*20)