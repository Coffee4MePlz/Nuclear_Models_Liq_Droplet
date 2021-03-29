from fractions import  Fraction
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from Bond import Bond

class NuclearModels:

  def __init__(self): # Get data we treated and stores in an objetct

    try:
      self.isotopos = pd.read_csv('isotopos.csv', index_col='nome')
    except:
      url = 'https://gist.githubusercontent.com/AnthonyAposta/3a4457b2e23ffce13c133ba8a97d3149/raw/ae38df1e49607b76cbc263bc914bb112429eb737/isotopos.csv'
      wget.download(url, ' ') #put your directory here
      self.isotopos = pd.read_csv('isotopos.csv', index_col='nome')
    
    self.camadas = None
  
  def paridade(self, N,Z): #Finds parity
    
    if ((N%2)==0) & ((Z%2)==0):
      p = 1
    elif ((N%2)!=0) & ((Z%2)!=0):
      p = -1
    else:
      p = 0

    return p

  def criar_camadas(self, n_max=3): #Defines all possible shells
    
    n_max = 3
    idx = ['s', 'p', 'd', 'f', 'g', 'h', 'i']
    niveis = []

    for n_ in range(1, n_max+1):
      for l_ in range(len(idx)):

        J = [l_ - 1/2, l_+1/2]

        for j_ in J:
          if j_ > 0:
            N = 2*(n_-1) + l_
            N2 = 2*j_ + 1
            niveis.append([n_, l_, j_, N, N2, f'{n_}{idx[l_]}_{str(Fraction(j_))}'])

    niveis = pd.DataFrame( niveis, columns=['n','l', 'j', 'N', 'N2', 'estado'])
    niveis.sort_values( ['N','j'], ascending= [True, False], inplace=True)
    niveis = niveis[['n','l', 'N', 'j', 'N2', 'estado']]

    #fixing lines
    b, c = niveis.iloc[4], niveis.iloc[5]
    niveis.iloc[4], niveis.iloc[5] = c,b 
    b, c = niveis.iloc[7], niveis.iloc[8]
    niveis.iloc[7], niveis.iloc[8] = c,b  
 
    niveis['max_ocupacao'] = pd.Series.cumsum( niveis.N2)
    self.camadas = niveis

    return niveis
    
  def estado_fundamental(self, Z=None, N=None, nome=None): #Computes fundamental state

    if nome is not None:
      Z = self.isotopos.loc[nome].Z
      N = self.isotopos.loc[nome].N

    if self.camadas is None:
      self.criar_camadas()

    # Checks if nucleus is even-even
    
    if self.paridade(N, Z) == 1:
      estado_fund = 'O+'
      estado_valencia = ' '
      Spin_parid = 0

    else:
      # Defines U as the nuclideus with higher number (either Z or N)
      U = max(N, Z)
      V = N+Z -U

      # Finds Valence band and spins

      valencia_U = self.camadas[ self.camadas.max_ocupacao >= U ].iloc[0]
      max_1U = self.camadas[self.camadas.max_ocupacao >= U].iloc[0][6]
      N2_1U = self.camadas[self.camadas.max_ocupacao >= U].iloc[0][4]
      Spin_U = (U - (max_1U - N2_1U))
      if Spin_U <= (N2_1U)/2:
          Spin_U = Spin_U/2
      else: Spin_U = -((N2_1U)/2 - Spin_U)/2


      valencia_V = self.camadas[ self.camadas.max_ocupacao >= V ].iloc[0]
      max_1V = self.camadas[self.camadas.max_ocupacao >= V].iloc[0][6]
      N2_1V = self.camadas[self.camadas.max_ocupacao >= V].iloc[0][4]
      Spin_V = (V - (max_1V - N2_1V))
      if Spin_V <= (N2_1V)/2:
          Spin_V = Spin_V/2
      else: Spin_V = -((N2_1V) - Spin_V)/2

      paridade = '+' if (valencia_U.l + valencia_V.l)%2==0 else '-'
      if (2*Spin_V)%2 == 0 :
          estado_valencia = valencia_U.estado
          estado_fund = f'({str(Fraction(valencia_U.j))}){paridade}'
      else: 
          estado_valencia = valencia_V.estado
          estado_fund = f'({str(Fraction(valencia_V.j))}){paridade}'

      Spin = Spin_U + Spin_V
      Spin_parid = f'({str(Fraction(Spin))}){paridade}'  
    return estado_fund, estado_valencia, Spin_parid

  def descrever(self, Z=None, N=None, nome=None): #Prints a quick description of the Isotope

    if nome is not None:
      Z = self.isotopos.loc[nome].Z
      N = self.isotopos.loc[nome].N

    energia = Bond(Z, N+Z, lev=4) #This functions is in another archive

    estado_fundamental, camada_valencia, Spin_parid = self.estado_fundamental(Z,N, nome)

    print(f"Description of Isotope {nome}, with N={N}, Z={Z}\n\n Nucleon bonding energy: {energia} Mev\n valence band: {camada_valencia}\n Fundamental state: {estado_fundamental}")

    return [nome, N, Z, energia, camada_valencia, estado_fundamental]

def Write_Table_txt(Tabela=[]): #This function generates a Latex Table for many results
    File = open("Tabela.txt", "w")
    for i in range(0, len(Tabela)):
        L = Tabela[i]
        for i in range(0,len(L)-2):
            File.write(f" ${L[i]}$ & ")
        File.write(f" ${abs(L[1]-L[2])+1}$ & ")
        File.write(f"{L[len(L)-1]} \\\ \n")
    File.close()

if __name__ == "__main__":
    c = NuclearModels()
    N_Isotop, Tabela = [], []
    c.descrever(nome="u236")

    ''' #Generates a Latex Table
    for i in range(54,59):
        N_Isotop.append(f'fe{i}')
        Tabela.append(c.descrever(nome=f'fe{i}'))
    Write_Table_txt(Tabela)
    ''' 
   
