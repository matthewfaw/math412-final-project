from TDA import *
import matplotlib.pyplot as plt

#Given delay reconstruction data, return TDA analysis of data
#@param int specifies which dimension of persistence to compute
#@param np.array 2D
#@returns np.array of tuples birth death pairs of only dimension specified
def one_tda(dr_data, dimension):
    persistence_data = doRipsFiltration(dr_data, dimension)
    return persistence_data[dimension]


#Given delay reconstruction data, return TDA analysis of data
#@param int specifies which dimension of persistence to compute
#@param np.array 2D
#@returns np.array 2D of tuples birth death pairs for dimension 0-dim
def batch_tda(dr_data, dimension):
    return doRipsFiltration(dr_data, dimension)
