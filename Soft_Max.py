def my_softmax(z):
    ez = np.exp(z)
    sm = ex/np.sum(ez)
    return(sm)