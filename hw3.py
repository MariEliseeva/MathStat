import numpy as np
import math
import matplotlib.pyplot as plt

theta = 1
sampleSize = 100
max_k = 50
seriesNumber = 50

def getEstimatedUniform(k):
    m_k = 0
    for x in np.random.uniform(0, theta, sampleSize) :
        m_k = m_k + x ** k
    m_k = m_k / sampleSize
    return ((k + 1) * m_k) ** (1.0 / k) 

def getEstimatedExponential(k):
    m_k = 0
    for x in np.random.exponential(theta, sampleSize) :
        m_k = m_k + x ** k
    m_k = m_k / sampleSize
    return (m_k / math.factorial(k)) ** (1.0 / k) 

def generate():
    resultsExponential = []
    resultsUniform = []
    for k in range(1, max_k) :
        deviationExponential = 0
        deviationUniform = 0
        for _ in range(seriesNumber) :
            deviationExponential += (theta - getEstimatedExponential(k)) ** 2
            deviationUniform += (theta - getEstimatedUniform(k)) ** 2
        resultsExponential.append((deviationExponential / seriesNumber) ** (0.5))
        resultsUniform.append((deviationUniform / seriesNumber) ** 0.5)
    plt.plot(range(1, max_k), resultsUniform)
    plt.savefig("uniform.png")
    plt.clf()
    plt.plot(range(1, max_k), resultsExponential)
    plt.savefig("exponential.png")
    
if __name__ == '__main__':
    generate()
