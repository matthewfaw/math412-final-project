from serializer.serializer import deserialize
import numpy as np
from sklearn.decomposition import PCA

data = np.array(deserialize("entries"))
pca = PCA(n_components=2)
pca.fit(data)
print pca.components_
print pca.explained_variance_ratio_
