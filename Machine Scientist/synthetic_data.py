import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sys as s
th1 = -1.19;th2 = 0.29
x1 = np.linspace(-6,6,40)
x2 = np.linspace(-6,6,40)

x1, x2 = np.meshgrid(x1,x2)
#print(np.shape(x1))
#print(x1[1])
#print('-'*100)
#print(x1[10])
#print(np.shape(x2))
#plt.plot(x1,x2)
#plt.show()

#s.exit()

def F(x1,x2,th1,th2):
    return (x1*(th1+x2)*np.cos(x1))/(th2*np.log(th2)) + np.random.normal(0,1)
for i in range(0,10):
    y = F(x1,x2,th1,th2)
    
    fig = plt.figure(figsize =(20, 20))
    ax = plt.axes(projection ='3d')
    ax.plot_surface(x1, x2, y)
    plt.show()
#fig = go.Figure(data=[go.Surface(y)])

#fig.update_layout(title='Mt Bruno Elevation', autosize=False,
#                  width=500, height=500,
#                  margin=dict(l=65, r=50, b=65, t=90))

#fig.show()
