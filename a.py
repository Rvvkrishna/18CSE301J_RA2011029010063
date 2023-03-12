import pandas as pd
import plotly.express as px

df=pd.read_excel('pkl(2).xlsx')


name=list(df.iloc[:,0]),
owner=list(df.iloc[:,1]),
coach=list(df.iloc[:,2]),
captain=list(df.iloc[:,3]),
noofplayers=list(df.iloc[:,4]),
homeground=list(df.iloc[:,5]),



fig=px.treemap(df,path=[list(df.iloc[:,4]),list(df.iloc[:,0])],values=list(df.iloc[:,4]))
fig.update_traces(hovertemplate='TeamName=%{label}<br>No of Player=%{value}<br>')


fig.show()