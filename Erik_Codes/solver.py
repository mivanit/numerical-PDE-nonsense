## Code to solve the advection diffusion equation with the theta scheme

import numpy as np 
import pandas as pd 
import scipy.linalg as la
import matplotlib.pyplot as plt

class Solver():
    def __init__(self, a=1, eta=1, theta=0.8, N=64, T=1):
        self.a = 1
        self.eta = eta  
        self.theta = theta 
        self.N = N
        self.dx = 2*np.pi/(N+1) 
        if theta > 0.5:
            dt = self.dx
        else:
            dt = 0.1* self.dx**2 /abs(eta)
        self.T = T 
        self.nT = int(T/dt) + 1
        self.dt = T/self.nT
        self.cfl = eta * self.dt/self.dx**2

    def make_operators(self):
        N = self.N
        I = np.array(np.eye(N+1))
        D0 = np.zeros((N+1,N+1))
        Dpm = np.array(-2*np.eye(N+1)/(self.dx**2))
        for i in range(N + 1):
            for j in range(N + 1):
                if i==j+1:
                    D0[i,j] = -1/(2*self.dx)
                    Dpm[i,j] = 1/(self.dx**2)
                elif i==j-1:
                    D0[i,j] = 1/(2*self.dx)
                    Dpm[i,j] = 1/(self.dx**2)
        
        D0[-1,1] = 1/(2*self.dx)
        D0[0,-2] = -1/(2*self.dx)
        Dpm[-1,1] = 1/(self.dx**2)
        Dpm[0,-2] = 1/(self.dx**2)
        
        self.lhs = I - self.theta*self.dt*(-self.a*D0 + self.eta * Dpm)
        self.rhs = I + (1-self.theta)*self.dt*(-self.a*D0 + self.eta * Dpm)

        self.transition = la.inv(self.lhs) @ self.rhs

    def set_ic(self):
        self.x = np.linspace(0,2*np.pi,self.N + 1).reshape((self.N+1,1))
        self.v = np.sin(self.x)

    def solve_to_T(self):
        current = self.v 
        for i in range(self.nT):
            next = self.transition @ current 
            current = next 
        self.soln = next 
        return self.x, self.soln

    def get_analytic(self):
        x = np.linspace(0,2*np.pi,1000)
        self.u = np.sin(x - self.a*self.T)*np.exp(-self.eta*self.T)
        return x, self.u

    def get_errors(self):
        self.errors = self.soln - np.sin(self.x - self.a*self.T)*np.exp(-self.eta*self.T)
        return self.errors

    def run(self):
        self.make_operators()
        self.set_ic()
        return self.solve_to_T()

def main():
    a, eta, theta = 1, 1, 0.4
    T, N = 5, 32
    solver = Solver(a, eta, theta, N, T)
    x, v = solver.run()
    xx, uu = solver.get_analytic()
    #print(solver.get_errors())
    plt.figure()
    plt.plot(xx,uu)
    plt.scatter(x,v)
    plt.show()

if __name__=="__main__":
    main()


