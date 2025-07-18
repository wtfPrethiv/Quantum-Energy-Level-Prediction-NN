import random
import math
import numpy as np
import pandas as pd


class EnergyLevelDataGen:

    def data_gen(self, n, m, l):
        
        PLANKS_CONST = 6.62607015e-34 

        n = int(n)
        m = float(m)
        l = float(l)

        nth_energy = np.divide(np.multiply(n, np.square(PLANKS_CONST)), 
                               np.multiply(8*m , np.square(l))) #

        return nth_energy
    




data_gen = EnergyLevelDataGen()

def generate_n_2():
    n = random.randint(1, 100)
    return n, n ** 2
  

def generate_mass(min_mass=1e-30, max_mass=1e-26):
    log_min = math.log10(min_mass)
    log_max = math.log10(max_mass)
    rand_log = random.uniform(log_min, log_max)
    return 10 ** rand_log

def generate_length(min_length=1e-10, max_length=1e-8):
    return random.uniform(min_length, max_length)

data  = {
    'n' : [],
    'n_2' : [],
    'Mass' : [], 
    'Length' : [],
    'Energy' : []
}

for i in range(1, 50001):

    n, n_2 = generate_n_2()    
    data['n'].append(n)
    data['n_2'].append(n_2)

    m = generate_mass()
    data['Mass'].append(m)

    l = generate_length()
    data['Length'].append(l)

    energy = data_gen.data_gen(n, m, l)
    data['Energy'].append(energy)

df = pd.DataFrame(data)

df.to_csv('data/Energy-Level-data.csv', index=False)
