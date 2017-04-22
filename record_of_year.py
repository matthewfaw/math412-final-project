from data_collection.grammys.csv_helper import deserialize
import numpy as np
import rips
import matplotlib.pyplot as plt

entries = deserialize("RECORD_OF_THE_YEAR.csv")
vector_list = []
for entry in entries:
    vector_list.append(entry.feature_vector)

vector_array = np.array(vector_list)

bd_pairs = rips.one_tda(vector_array, 0)

rips.plotDGM(bd_pairs)
plt.show()




