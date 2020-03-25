import pandas as pd
import numpy as np
import datetime

import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('data-240320.csv',sep=';')

df['Fecha de diagnóstico'] = pd.to_datetime(df['Fecha de diagnóstico'])
df = df.rename(columns={'Fecha de diagnóstico': 'fecha'})
df = df.rename(columns={'ID de caso':'conteo'})


grouped_df = df.groupby(('fecha')).size().reset_index(name='conteo')
traces = [go.Scatter(
    x = grouped_df['fecha'],
    y = grouped_df['conteo'].cumsum(),
    mode = 'markers+lines',
    name = 'Colombia'
)]

layout = go.Layout(
    title = 'Casos Coronavirus Nivel Nacional',
    xaxis = {'title':'Fechas de diagnostico'},
    yaxis = {'title':'Población Afectada'},
    hovermode = 'closest'
)

fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig, filename='Tendencia Nacional.html')
