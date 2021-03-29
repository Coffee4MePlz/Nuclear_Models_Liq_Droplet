import numpy as np
import scipy as spy
import matplotlib.pyplot as plt
from SpheHarm import gota_liquida

def Bond(Z, A, lev=4):
    ''' Function for bonding energy. 
	The values of lev define how many parameters are zero
	from right to left (from av to delta)
	Funcao de calculo da energia de ligacao,
	    os valores para lev, definem quantos dos parametros sao zerados
    	comecando da direita para esquerda (de av para delta)
    '''
    aV, aS, aC, aI, delta, sgn = 15.68, 18.56, 0.72, 18.1, 34*A**(-3/4), 0
    if lev==0: aS,aC,aI,delta = 0,0,0,0
    if lev==1: aC,aI,delta = 0,0,0
    if lev==2: aI,delta = 0,0
    if lev==3: delta = 0
    N = A - Z
    if (Z%2 + N%2) == 1:
        sgn = 1
    if (Z%2 + N%2) == 2:
        sgn = -1
    if Z==1: sgn=0
    E = aV*A - aS*A**(2/3) - aC*Z*(Z-1)/(A**(1/3)) - aI*(N-Z)**2/(A) + sgn*delta
    B = E/A
    #print(B)
    return float(B)

def Plot_Bond():
    '''
	generates plot for each value in Bond() with lev=0 to 4    
	gera o plot para cada valor de Bond() com lev = 0 a 4
    '''
    Data = np.loadtxt('tabela_isotopos_round.txt')
    An, Zn, B_Plot = [],[],([],[],[],[])
    for i in range(0,108):
        An.append(Data[i,0])
        Zn.append(Data[i,1])
    fig, ax = plt.subplots()
    for i in range(0,4):
        for r in range(0,len(An)):
            B_Plot[i].append(Bond(Zn[r],An[r],lev=i))
        plt.plot(An,B_Plot[i], label = f'B/A com {i+1} param')
    plt.xlabel("A")
    plt.ylabel("B/A in MeV")
    plt.title("Binding energy by expansion of parameters")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    gota_liquida(30,4,1)
    #Plot_Bond()
    
    

