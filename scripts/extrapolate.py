import numpy as np

L = 140
S = 1.5
E = 0.7

def sigma_at(lumi):
    return S * np.sqrt(lumi/L)

def error_at(lumi):
    return E * np.sqrt(L/lumi)

def lumi_at_sigma(sigma):
    return L * (sigma/S)**2

def lumi_at_error(error):
    return L * (E/error)**2

for lumi in [140, 200, 300, 500, 1000, 3000]:
    print(lumi, sigma_at(lumi), error_at(lumi))
print()

for sigma in [1, 2, 3, 4, 5]:
    print(sigma, lumi_at_sigma(sigma))
print()

for error in [0.5, 0.3, 0.2]:
    print(error, lumi_at_error(error))

