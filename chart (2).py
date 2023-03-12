import numpy as np
import pandas as pd
import plotly.express as px

ds = pd.read_excel('pkl2.xlsx')
teamName = list(ds.iloc[:,0])
matchesPlayes = list(ds.iloc[:,4])
matchesWon = list(ds.iloc[:,2])
teamPosition = list(ds.iloc[:,3])
df = px.data.tips()
fig = px.bar(df, x=teamName, y=matchesPlayes, orientation='v')
fig.show()