#figura 1a

import numpy as np
import pandas as pd 
import pandapower as pp 
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update(
    {'font.size':10, "text.usetex":False, "font.family": "serif",
     "font.sans-serif":['Computer Modern']})

# Red vacia
net = pp.create_empty_network()

# Barras
bus1 = pp.create_bus(net, vn_kv=1.0, name="bus 1")
bus2 = pp.create_bus(net, vn_kv=1.0, name="bus 2")

# Generador 
pp.create_ext_grid(net, bus1, vs_pu=1.0, name="Slack bus" )

# Lineas entre Barras
pp.create_line_from_parameters(net, from_bus=bus1, to_bus=bus2, length_km=500, r_ohm_per_km=0.02, x_ohm_per_km=0.115, c_nf_per_km=19.1, max_i_ka=1, name="Line 12A")
pp.create_line_from_parameters(net, from_bus=bus1, to_bus=bus2, length_km=500, r_ohm_per_km=0.02, x_ohm_per_km=0.115, c_nf_per_km=19.1, max_i_ka=1, name="Line 12B")

#Carga Barra 2 
pp.create_load(net, bus2, p_mw=1080, q_mvar=523.07, name="Load 1")

pp.runpp(net, algorithm='nr', numba=False,max_iteration=100)

# Mostrar los resultados de las barras
net.res_line.index = net.line.name
net.res_bus.index = net.bus.name

