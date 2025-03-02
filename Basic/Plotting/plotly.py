#!/usr/bin/env python3

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

py.sign_in(username='voorbeeld', api_key='L0McCrDpID71OLCEgRtK')

mx = [1, 2, 3, 4]
my = [1, 2, 3, 4]

trace = go.Scatter(
    x = mx,
        y = my
	)

data = [trace]
py.plot(data)


import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4])],
        "layout": go.Layout(title="line chart")
	}, auto_open=True)

import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

plotly.offline.iplot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
        "layout": go.Layout(title="hello world")
	})