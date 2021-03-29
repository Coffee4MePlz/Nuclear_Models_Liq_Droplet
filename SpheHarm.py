import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def gota_liquida(gamma,beta, R0):
    '''
	Generates a plot according to the liquid droplet model, with specific input values    
	gera um plot para a gota liquida, com os valores do input
    '''
    pi = np.pi
    cos = np.cos
    sin = np.sin

    def gota(theta, phi, gamma, beta, R0):

      R = R0*(1 + beta*np.sqrt(5/(16*pi)) * 
                (cos(gamma)*(3*(cos(theta)**2) -1 ) +
                 (np.sqrt(3)/2)*sin(gamma)*(sin(theta)**2)*cos(2*theta) ) )
      return R 

    theta = np.arange(0,pi,0.05)
    phi = np.arange(0,2*pi+0.1,0.1)
    Theta, Phi = np.meshgrid(theta,phi)
    R = gota(theta, phi, gamma, beta, R0)
    

    x = R*sin(Theta)*cos(Phi)
    y = R*sin(Theta)*sin(Phi)
    #X, Y = np.meshgrid(x,y)
    z = R*cos(Theta)
    
    fig = plt.figure()
    #ax = plt.axes(projection='3d')
    #ax.scatter(x,y,z, c=z, cmap='viridis', linewidth=0.5)
    ax = fig.add_subplot(111, projection='3d')
    plot = ax.plot_surface(x, y , z, rstride=1, cstride =1 , cmap=plt.get_cmap('jet'), linewidth=0, antialiased=False, alpha = 0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    #ax.scatter(x,y,z)
    plt.show()


    
