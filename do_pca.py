from serializer.serializer import deserialize
import numpy as np
from sklearn.decomposition import PCA

def do_pca(data):
	pca = PCA(n_components=3)
	pca.fit(data)
	#print pca.components_
	#print pca.explained_variance_ratio_
	return pca.transform(data)
