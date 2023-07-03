import antColony
import numpy as np

def main():
    print("Ant colony applied to the traveling salesman problem.\n")

    distancias = np.loadtxt("lau15.txt")
    qtdCidades = distancias.shape[0]
    qtdFormigas = qtdCidades
    qtditeracoes = 10
    taxaEvaporacao = 0.5
    alfa = 1
    beta = 2
    Q = 50
    feromonioInicial = 1

    antColony.antColony(distancias, 
                        qtdCidades, 
                        qtdFormigas, 
                        qtditeracoes, 
                        taxaEvaporacao, 
                        alfa, 
                        beta, 
                        Q, 
                        feromonioInicial)
    
main()