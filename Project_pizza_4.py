# CODE EFFICIENT USING VECTORIZATION 

import numpy as np
import math
import matplotlib.pyplot as plt


class short_Rate_Models(object):

    def __init__(self,r,K,theta,sigma,T,N,seed):
        self.r = r
        self.K = K
        self.theta = theta
        self.sigma = sigma
        self.T = int(T)
        self.N = int(N)
        self.seed = seed
        self.dt = self.T/float(self.N)
        
    def _vasicek_model_(self):
        np.random.seed(self.seed)
        self.interest_rates = []
        self.interest_rates.append(self.r)
        for i in range(1,self.N):
            self.dr = self.K * (self.theta - self.interest_rates[i-1]) * self.dt\
            + self.sigma *np.random.normal()
            self.interest_rates.append(self.interest_rates[i-1] + self.dr)
        f1 = plt.figure()
        ax1 = f1.add_subplot(111)
        ax1.plot(range(self.N), self.interest_rates,label = ("Vasicek","Seed = ",self.seed))
        plt.legend()
        plt.xlabel('N')
        plt.ylabel('Interest Rate')
        return range(self.N), self.interest_rates
        
    def _cox_ingersoll_ross_(self):
        np.random.seed(self.seed)
        self.interest_rates = []
        self.interest_rates.append(self.r)
        for i in range(1,self.N):
            self.dr = self.K * (self.theta - self.interest_rates[i-1]) * self.dt\
            + self.sigma * math.sqrt(self.interest_rates[i-1]) * np.random.normal()
            self.interest_rates.append(self.interest_rates[i-1] + self.dr)
        f2 = plt.figure()
        ax2 = f2.add_subplot(111)
        ax2.plot(range(self.N), self.interest_rates,label = ("CIR","Seed = ",self.seed))
        plt.legend()
        plt.xlabel('N')
        plt.ylabel('Interest Rate')
        return range(self.N), self.interest_rates
        
    def _rendleman_bartter_model_(self):
        np.random.seed(self.seed)
        self.interest_rates = []
        self.interest_rates.append(self.r)
        for i in range(1,self.N):
            self.dr = self.theta * self.interest_rates[i-1] * self.dt\
            + self.sigma * self.interest_rates[i-1]*np.random.normal()
            self.interest_rates.append(self.interest_rates[i-1] + self.dr)
        f3 = plt.figure()
        ax3 = f3.add_subplot(111)
        ax3.plot(range(self.N), self.interest_rates,label = ("RBM","Seed = ",self.seed))
        plt.legend()
        plt.xlabel('N')
        plt.ylabel('Interest Rate')
        return range(self.N), self.interest_rates
        
    def _brennan_schwartz_model_(self):
        np.random.seed(self.seed)
        self.interest_rates = []
        self.interest_rates.append(self.r)
        for i in range(1,self.N):
            self.dr = self.K * (self.theta - self.interest_rates[i-1]) * self.dt\
            + self.sigma * self.interest_rates[i-1] * np.random.normal()
            self.interest_rates.append(self.interest_rates[i-1] + self.dr)
        f4 = plt.figure()
        ax4 = f4.add_subplot(111)
        ax4.plot(range(self.N), self.interest_rates,label = ("BSM","Seed = ",self.seed))
        plt.legend()
        plt.xlabel('N')
        plt.ylabel('Interest Rate')
        return range(self.N), self.interest_rates
        
    def plot(self):
        self._vasicek_model_()
        self._cox_ingersoll_ross_()
        self._rendleman_bartter_model_()
        self._brennan_schwartz_model_()
        
if __name__ == '__main__':
    plot = short_Rate_Models(.025,0.23,0.023,0.01,10,200,547)
    plot.plot()