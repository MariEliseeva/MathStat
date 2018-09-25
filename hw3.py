import numpy as np
import math as m
import matplotlib.pyplot as plt

theta = 1
n = 100
max_k = 50
series = 50

def getEstimateUniform(k):
    m_k = 0
    for x in np.random.uniform(0, theta, n) :
        m_k = m_k + x ** k
    m_k = m_k / n
    return ((k + 1) * m_k) ** (1.0 / k) 

def getEstimateExponential(k):
    m_k = 0
    for x in np.random.exponential(theta, n) :
        m_k = m_k + x ** k
    m_k = m_k / n
    return (m_k / m.factorial(k)) ** (1.0 / k) 

def generate():
    resultsExponential = []
    resultsUniform = []
    for k in range(1, max_k) :
        deviationExponential = 0
        deviationUniform = 0
        for s in range(series) :
            deviationExponential += (theta - getEstimateExponential(k)) ** 2
            deviationUniform += (theta - getEstimateUniform(k)) ** 2
        resultsExponential.append((deviationExponential / series) ** (0.5))
        resultsUniform.append((deviationUniform / series) ** 0.5)
    plt.plot(range(1, max_k), resultsUniform)
    plt.savefig("uniform.png")
    plt.clf()
    plt.plot(range(1, max_k), resultsExponential)
    plt.savefig("exponential.png")
    
if __name__ == '__main__':
    generate()
