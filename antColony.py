import numpy as np
import matplotlib.pyplot as plt

def antColony(distancias, qtdCidades, qtdFormigas, qtditeracoes, taxaEvaporacao, alfa, beta, Q, feromonioInicial):
    # inicialmente todas as rotas tem feromonio igual 1
    feromonios = np.ones((qtdCidades, qtdCidades)) * feromonioInicial

    # salvar a mlehor rota e a melhor distancia
    melhorRota = None
    melhorDistancia = np.inf

    # a cada iteração armazena a melhor distancia
    distanciasIteracoes = []

    for iteracao in range(qtditeracoes):
        distanciasFormigas = np.zeros(qtdFormigas)
        rotasFormigas = []

        for formiga in range(qtdFormigas):
            # constroi as solucoes
            visitadas = np.zeros(qtdCidades, dtype=bool)
            rota = []
            cidadeAtual = np.random.randint(qtdCidades)
            rota.append(cidadeAtual)
            visitadas[cidadeAtual] = True

            # calcula tabela de probabilidade
            for x in range(qtdCidades - 1):
                with np.errstate(divide='ignore'): #isso é para ignorar o aviso de possível divisao por 0
                    probabilidades = pow(feromonios[cidadeAtual], alfa) * (1.0 / pow(distancias[cidadeAtual], beta))
                probabilidades[visitadas] = 0
                probabilidades = probabilidades / np.sum(probabilidades)
                
                # aqui é como a roleta, seleciona de acordo com a probabilidade
                cidadeAtual = np.random.choice(range(qtdCidades), p = probabilidades)
                rota.append(cidadeAtual)
                visitadas[cidadeAtual] = True

            rotasFormigas.append(rota)
            
            # calcula a distancia percorrida nessa rota
            distanciaFormiga = 0
            for i in range(len(rota) - 1):
                cidadeAtual = rota[i]
                proximaCidade = rota[i + 1]
                distanciaFormiga += distancias[cidadeAtual, proximaCidade]

            distanciaFormiga += distancias[rota[-1], rota[0]]
            distanciasFormigas[formiga] = distanciaFormiga

        # atualização dos feromônios
        feromonios *= taxaEvaporacao
        for formiga in range(qtdFormigas):
            rota = rotasFormigas[formiga]
            variacaoFerormonio = Q / distanciasFormigas[formiga]
            
            for i in range(len(rota) - 1):
                cidadeAtual = rota[i]
                proximaCidade = rota[i + 1]
                feromonios[cidadeAtual, proximaCidade] += variacaoFerormonio
                feromonios[proximaCidade, cidadeAtual] += variacaoFerormonio

        # verificada melhor solução encontrada
        melhorFormiga = np.argmin(distanciasFormigas)
        if distanciasFormigas[melhorFormiga] < melhorDistancia:
            melhorRota = rotasFormigas[melhorFormiga]
            melhorDistancia = distanciasFormigas[melhorFormiga]

            if iteracao == 0:
                melhorRI = rota

        #salva a melhor distancia da iteracao
        distanciasIteracoes.append(melhorDistancia)

    plt.plot(range(qtditeracoes), distanciasIteracoes)
    plt.xlabel('Iteração')
    plt.ylabel('Distância')
    plt.title('Melhor Distância por Iteração')
    plt.show()

    print('Rota Inicial:', melhorRI)
    print('Distancia Inicial:', distanciasIteracoes[0])

    print('Rota Final:', melhorRota)
    print('Distancia Final:', melhorDistancia)