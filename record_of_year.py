from data_collection.grammys.csv_helper import deserialize
import numpy as np
import rips
import matplotlib.pyplot as plt
import data_analysis.do_pca as pca
from mpl_toolkits.mplot3d import Axes3D

entries = deserialize("RECORD_OF_THE_YEAR.csv")
vector_list = []
for entry in entries:
    vector_list.append(entry.feature_vector)

vector_array = np.array(vector_list)

pca_vectors = pca.do_pca(vector_array)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pca_vectors[:, 0], pca_vectors[:, 1], pca_vectors[:, 2])
plt.show()

#bd_pairs = rips.one_tda(vector_array, 0)

#rips.plotDGM(bd_pairs)
#plt.show()




