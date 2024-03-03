import numpy as np

# Parametros de entrada
x0 = float(input());  # condicao inicial
Nmax = int(input());  # número maximo de iteracoes
dr = float(input());  # o passo de r

# Criacao do vetor rvec
rvec = np.arange(0, 4, dr)

# Loop utilizado para calcular as iteracoes para cada valor de r em rvec
output = [] # lista que armazena os valores de r
for r in rvec:
    Xn = [x0]
    # Faz o calculo das ultimas 4 iteracoes do mapa logistico para o valor de r atual    
    for _ in range(Nmax):
        X = r * Xn[-1] * (1 - Xn[-1])
        Xn.append(X)
    output.append(Xn[-4:])
    
# Parametro de saida
Nr = len(output) # conta o tamanho da lista de valores de r
for ir in range(Nr):
    for ii in range(4):
        print("{:10.6f}".format(output[ir][ii]))
    print("\n")
                  
                  