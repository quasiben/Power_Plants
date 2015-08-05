from collections import OrderedDict

import pandas as pd

from bokeh.charts import Bar, output_file, show
from bokeh.models import HoverTool
from bokeh.sampledata.olympics2014 import data

df = pd.read_csv("bystate.csv", header=0)

df = df.sort("pctcoal", ascending=False)

# get the states and we group the data by pctcoal
states = df.postal.values.tolist()
coal = df.pctcoal.astype(float).values
natural_gas = df.pctnatural_gas.astype(float).values
nuclear = df.pctnuclear.astype(float).values
hydro = df.pcthydro.astype(float).values
wind = df.pctwind.astype(float).values
solar = df.pctsolar.astype(float).values
oil = df.pctpetroleum.astype(float).values
other = df.pctother.astype(float).values

# build a dict containing the grouped data
power = OrderedDict(coal=coal, natural_gas=natural_gas, nuclear=nuclear, hydro=hydro, wind=wind, solar=solar, oil=oil, other=other)

output_file("stacked_bar.html")


coal = "#58595b"
gas = "#F68B28"
nuclear = "#CF4A9A"
hydro = "#0081C5"
wind = "#0DB14B"
solar = "#D7C944"
oil = "#ED1C24"
other = "#F6e0C0"

palette = [oil, nuclear, coal, gas, other, solar, wind, hydro]
bar = Bar(power, states, title="Stacked bars", stacked=True, width=1024, height=500, palette=palette, tools='hover')

hover = bar.select(dict(type=HoverTool))

hover.tooltips = [
    ("index", "$index"),
    ("Coal", "@coal"),
    ("Natural Gas", "@gas"),
    ("Nuclear", "@nuclear"),
]
show(bar)
