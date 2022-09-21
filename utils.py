def plot_state(state):
    M,N = np.shape(state)[0],np.shape(state)[1]
    pixels=[]
    for i in range(0,N):
        for j in range(0,N):
            if state[i,j]==1:
                pixels.append((40,250,60))#verde
            if state[i,j]==-1:
                pixels.append((40,60,250))#azul
    im2 = Image.new("RGB", (N,N))
    im2.putdata(pixels)
    plt.imshow(im2)
    plt.show()
#plot_state(a)