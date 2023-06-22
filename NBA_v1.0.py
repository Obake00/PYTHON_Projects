from time import sleep

frase_feitos = ('Insira o placar de pontos feitos do')
frase_sofridos = ('Insira o placar de pontos sofridos do')


print('!! Calculo OVER/UNDER para NBA !!\n')
sleep(3)
print('Para este calculo, preciso que voce tenha os 4 ultimos jogos dos 2 times a serem avaliados!!\n')
sleep(3)
print('com os placares em mãos, insira os 4 placares de pontos feitos primeiramente, e depois os 4 placares sofridos pelo time em questão\n')
sleep(3)
print('Voce fara isso para ambos os times, Por favor insira a baixo os valores para o primeiro time!\n')
sleep(2)

tAf1 = int(input('{} primeiro jogo: '.format(frase_feitos)))
tAf2 = int(input('{} segundo jogo: '.format(frase_feitos)))
tAf3 = int(input('{} terceiro jogo: '.format(frase_feitos)))
tAf4 = int(input('{} quarto jogo: '.format(frase_feitos)))

media_feitos_timeA = (tAf1 + tAf2 + tAf3 + tAf4)/4

print('\n')
print('PROCESSANDO...\n')
sleep(1)
print('Agora insira os valores de pontos SOFRIDOS nos mesmos jogos pela Equipe!\n')
sleep(1)

tAs1 = int(input('{} primeiro jogo: '.format(frase_sofridos)))
tAs2 = int(input('{} segundo jogo: '.format(frase_sofridos)))
tAs3 = int(input('{} terceiro jogo: '.format(frase_sofridos)))
tAs4 = int(input('{} quarto jogo: '.format(frase_sofridos)))

media_sofridos_timeA = (tAs1 + tAs2 + tAs3 + tAs4)/4

print('\n')
print('PROCESSANDO...\n')
sleep(1)
print('Agora repita o mesmo para o outro time!\n')

tBf1 = int(input('{} primeiro jogo: '.format(frase_feitos)))
tBf2 = int(input('{} segundo jogo: '.format(frase_feitos)))
tBf3 = int(input('{} terceiro jogo: '.format(frase_feitos)))
tBf4 = int(input('{} quarto jogo: '.format(frase_feitos)))

media_feitos_timeB = (tBf1 + tBf2 + tBf3 + tBf4)/4

print('\n')
print('PROCESSANDO...\n')
sleep(1)
print('Agora insira os valores de pontos SOFRIDOS nos mesmos jogos pela Equipe!\n')
sleep(1)

tBs1 = int(input('{} primeiro jogo: '.format(frase_sofridos)))
tBs2 = int(input('{} segundo jogo: '.format(frase_sofridos)))
tBs3 = int(input('{} terceiro jogo: '.format(frase_sofridos)))
tBs4 = int(input('{} quarto jogo: '.format(frase_sofridos)))

media_sofridos_timeB = (tBs1 + tBs2 + tBs3 + tBs4)/4

print('\n')
print('PROCESSANDO...\n')
sleep(1)
print('PROCESSANDO...\n')
sleep(3)

print('A média de pontos feitos pelo time A é de {}, e sofridos são {}\n'.format(media_feitos_timeA, media_sofridos_timeA))
print('A média de pontos feitos pelo time B é de {}, e a media de sofridos foram {}'.format(media_feitos_timeB, media_sofridos_timeB))
sleep(4)
print('\n'*2)
calculo_final = (media_feitos_timeA + media_sofridos_timeA + media_feitos_timeB + media_sofridos_timeB)/2
print('Com base nos calculos, o numero base para a entrada é {} pontos!\n'.format(calculo_final))
print('Lembre-se, se o valor de pontos estiver em torno de {}, ideal que entre como OVER!'.format(calculo_final + 10))
print('Agora para uma entrada em UNDER, ideal que esteja em torno de {} pontos\n'.format(calculo_final - 10))
sleep(2)
print('ESTA PROGRAMA SE AUTO DESTRUIRA EM 30 SEGUNDOS...')
sleep(30)