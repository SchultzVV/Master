import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

import plotly.graph_objects as go
import pandas as pd
import sys as s
# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
print(type(z_data.values))
print(np.shape(z_data.values))
s.exit()
fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
