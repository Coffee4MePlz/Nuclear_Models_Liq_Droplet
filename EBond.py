import numpy as np
import scipy as spy
import matplotlib as plt
import pandas as pd 

# Def Function (B/A)
def B_1(Z=0,A=0, a_v=0, a_s=0, a_c=0, a_i=0, delta=0):
    N = A - Z
    return  a_v*A - a_s*pow(A,2/3) - a_c*Z*(Z-1)/pow(A,1/3) - a_i*pow(N-Z, 2)/A + delta

def B_true(Z=0,A=0, a_v=0, a_s=0, a_c=0, a_i=0, delta=0):
    av = 15.685; a_s = 18.566 ; ace2 = 0.727;  ai = 18.1
    return av*A - a_s*pow(A, 2/3) - a_c*Z*(Z-1)/pow(A,1/3) - a_i*pow(N-Z,2)/A +delta 
def SEMF(Z, N):
    aV, aS, aC, aA, delta = 15.75, 17.8, 0.711, 23.7, 11.18
    Z, N = np.atleast_1d(Z), np.atleast_1d(N)
    A = Z + N
    sgn = np.zeros(Z.shape)
    sgn[(Z%2) & (N%2)] = -1
    sgn[~(Z%2) & ~(N%2)] = +1
    E = (aV - aS / A**(1/3) - aC * Z**2 / A**(4/3) -
         aA * (A-2*Z)**2/A**2 + sgn * delta/A**(3/2))

    # Return E as a scalar or array as appropriate to the input Z.
    if Z.shape[0] == 1:
        return float(E) 
    return E
def Write_Data_to_CSV():
    data = pd.read_fwf('mass.mas03.txt', usecols=(2,3,4, 6, 11),
        names=('N', 'Z', 'A' , 'EL', 'avEbind'),
        widths=(1,3,5,5,5,1,3,4,1,13,11,11,9,1,2,11,9,1,3,1,12,11,1),
        header=39,
        index_col=False)
    data['avEbind'] = pd.to_numeric(data['avEbind'], errors='coerce')
    data = data.dropna()
    data['avEbind'] /= 1000
    grouped_data = data.groupby('A')
    #maxavEbind = grouped_data.apply(lambda t: t[t.avEbind==t.avEbind.max()])
    #maxavEbind['Eapprox'] = SEMF(maxavEbind['Z'], maxavEbind['N'])
    data.sort_values(["A","Z"])
    data.to_csv("Data.csv", index=None)
    return data


if __name__ == "__main__":
    #Para tratar os dados:
    # data = Write_Data_to_csv()
    #my_data = np.genfromtxt("Data.csv", delimiter = " , ", dtype=str )
    #data2 = my_data.split(',')
    data = pd.read_csv('Data.csv')
    Zn = data.get('Z')
    An = data.get('A')
    print(Zn[1:5])
    Eln = data.get('Eln')
    





    