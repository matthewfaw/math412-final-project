def single_window(x, M, n):
    window = []
    for i in range(M):
        window += x[n+i]
    return window

def window_embedding(x, M):
    embedding = []
    for i in range(len(x) - M + 1):
        embedding += [single_window(x, M, i)]
    return embedding
