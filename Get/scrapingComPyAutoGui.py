import time
import pyautogui as pag
import pyperclip
import pandas as pd
import demoji

arquivo = 'OfficinaCervGORuaT64'
tolx, toly = 2, 2
N = 100

def getPosicao(n):
    time.sleep(0.2)
    print('\n', end = '')
    for i in range(n):
        print(n-i,end = '')
        for j in range(5):
            print('.', end = '')
            time.sleep(0.2)
    return pag.position()

def cStar1(xE, xD, yC, yB):
    # Delimita regiao da 1a estrela
    xmin, xmax = xD+tolx, xE-tolx
    ymin, ymax = yB+toly, yC-toly
    for x in range(xE-tolx, xD+tolx):
        for y in range(yC-toly, yB+toly):
            cor = pag.pixel(x, y)
            if cor == (251, 188, 4):
                xmin = x if x < xmin else xmin                    
                xmax = x if x > xmax else xmax                    
                ymin = y if y < ymin else ymin
                ymax = y if y > ymax else ymax                    
    return int((xmax+xmin)/2.0), int((ymax+ymin)/2.0), ymax - ymin

def cStar2(xE, xD, yC, yB):
    # Delimita regiao da 1a estrela c/ menos precisao
    ymin, ymax = yB+toly, yC-toly
    for x in range(xE, xD, 2):
        for y in range(yC-toly, yB+toly, 2):
            cor = pag.pixel(x, y)
            if cor == (251, 188, 4):
                ymin = y if y < ymin else ymin
                ymax = y if y > ymax else ymax
    return int((ymax+ymin)/2.0)

def boundaries():
    # Comentários para usuario
    # Delimita 6 pontos na tela
    print('Atenção, tempo correndo...')
    print('Você tem ***  4  segundos   ***  após pressionar Ok,')
    print('para posicionar o mouse.')

    textoa = 'Pressione ok e, então, POSICIONE o cursor do mouse\n'
    textob, textoc = 'da primeira estrela', 'do primeiro comentário'
    textod = 'do texto ' + textoc
    textox = ['do LADO ESQUERDO ', 'do LADO DIREITO ', 'ACIMA ', 'ABAIXO ', \
            'APÓS A ÚLTIMA ESTRELA ', 'ATÉ O LIMITE DIREITO ']
    textoy = [textob, textob, textob, textob, textoc, textod, textoc]

    # Com o mouse, delimitar 6 posicoes na tela
    horv = [0, 0, 1, 1, 0, 0] # 0 ou 1, horizontal ou vertical
    x = []
    for i in range(6):
        pag.alert(textoa + textox[i] + textoy[i] + '.')
        x.append(getPosicao(4)[horv[i]])
    pag.alert('Não mexa mais no mouse!')
    return x[0], x[1], x[2], x[3], x[4], x[5]

def salvar(dados, arquivo, acabou):
    if acabou:
        meio = time.strftime('%Y%m%d%H%M%S')
    else:
        meio = '_parciais'
    df = pd.DataFrame(dados)
    df.columns = ['review', 'date', 'rate']
    df.to_csv(arquivo + '_' + meio + '.csv', encoding = 'cp1252', errors = 'ignore', \
            index = True)
    df.to_excel(arquivo + '_' + meio + '.xlsx')
    return df


xE, xD, yC, yB, xLimM, xLimD = boundaries()
dados = []

cStarH, yM, lStar = cStar1(xE, xD, yC, yB)
print('\nAltura da estrela', lStar, 'pixels.')

pag.moveTo(xE, yM)

print("\n\nScraping.... Aguarde!\n")

for k in range(N):
    print(k+1, end = ' ')
    if (k+1)%10 == 0:
        print('\n', end='')

    # Achar o centro da estrela
    cStarV = cStar2(xE, xD, yC, yB)
    pag.moveTo(cStarH, cStarV)
    time.sleep(0.5)
    pag.moveTo(xE, yM)
    pag.scroll(yM - cStarV)

    nStar = 0
    corAlvo, trocaCor = 765, 443
    for posH in range(xE, xLimM):
        cor = pag.pixel(posH, yM)
        if sum(cor) == corAlvo:
            trocaCor, corAlvo = corAlvo, trocaCor
            if sum(cor) == 443:
                nStar += 1

    pag.moveTo(xLimM, yM)
    pag.dragTo(xLimD, yM, duration = 0.4)
    pag.hotkey('ctrl', 'c')
    pag.click()
    time.sleep(0.1)
    data = pyperclip.paste()
    data = data.replace('\r', '').replace('\n', '')
    data = data.removesuffix('NOVA')

    pag.moveTo(xLimM, yM)
    ds, s = 20, 0
    comment, y = False, yM+ds
    while y < pag.size()[1] - 11*lStar:
        pag.moveTo(xLimM, y)
        try:
            cor = pag.pixel(xLimM, y)
            if sum(cor) == 743:
                comment = True
                s = y - yM
                break
        except:
            continue
        y += ds

    comentario = ""
    if comment:
        pag.moveTo(xE, yM+4*lStar)
        dy = min(yM+s-5*lStar, yM+22*lStar)
        pag.dragTo(xLimD, dy, duration = 0.5)
        pag.hotkey('ctrl', 'c')
        time.sleep(0.2)
        comentario = pyperclip.paste()
        comentario = demoji.replace(comentario, '') # Remove emoji
        comentario = comentario.removesuffix('Mais').removesuffix('… ')
    pag.moveTo(cStarH, yM)
    pag.scroll(-s-15*lStar)

    item = [comentario, data, nStar]
    #print(item)
    dados.append(item)

    # Encontrar o próximo comentário
    x, y = cStarH, yM
    o = 0
    dy = int(0.9*lStar)
    while o < 100 and k < N-1:
        pag.scroll(-max(dy,2))
        try:
            cor = pag.pixel(x, y)
            if cor == (251, 188, 4):                
                x_, y_ = [x-1, x, x+1], [y-1, y, y+1]
                numerop = 0
                for i in x_:
                    for j in y_:
                        if pag.pixel(i, j) == (251, 188, 4):
                            numerop += 1
                if numerop > 5:
                    break
                dy -= 2
        except:
            continue
    else:
        print("Não há mais comentários!")

    posV = y

    pag.moveTo(cStarH, cStarV)
    pag.scroll(cStarV - posV)

    # Salvar a cada 10 'scraps' (resultados parciais)
    if (k+1)%10 == 0: #cp1252, latin_1
        salvar(dados, arquivo, False)


# Salvar os dados finais
df = salvar(dados, arquivo, True)
print(df)