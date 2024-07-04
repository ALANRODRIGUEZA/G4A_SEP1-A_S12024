#Figura 1b

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

#Crear las barras 
bus1 = pp.create_bus(net, vn_kv=220, name="bus 1")
bus2 = pp.create_bus(net, vn_kv=110, name="bus 2")
bus1A = pp.create_bus(net, vn_kv=110, name="bus 1A")
bus1B = pp.create_bus(net, vn_kv=110, name="bus 1B")
bus2A = pp.create_bus(net, vn_kv=110, name="bus 2A")
bus2B = pp.create_bus(net, vn_kv=110, name="bus 2B")
bus3A = pp.create_bus(net, vn_kv=110, name="bus 3A")

#Crear Transformador entre bus1 y bus 2 
pp.create_transformer(net, bus1, bus2, std_type="100 MVA 220/110 kV")

# Crear el Generador en bus1 y definirlo como barra la slack
pp.create_ext_grid(net, bus1, vs_pu=1.0, name="Slack bus" )

# Crear cargas en bus1A, bus1B, bus2A, bus2B, bus3A  
pp.create_load(net, bus1A, p_mw=30, q_mvar=20, name="Load1A")
pp.create_load(net, bus1B, p_mw=15, q_mvar=10, name="Load1B" )
pp.create_load(net, bus1A, p_mw=52.5, q_mvar=35, name="Load2A")
pp.create_load(net, bus1B, p_mw=90, q_mvar=60, name="Load2B" )
pp.create_load(net, bus1A, p_mw=22.5, q_mvar=15, name="Load3A")

std_type_line = "N2XS(FL)2Y 1x300 RM/35 64/110 kV" 

# Crear una linea entre bus2 y bus1A
pp.create_line(net, bus2, bus1A, length_km=10, std_type=std_type_line,name='L2-1A')
# bus1A y bus2A
pp.create_line(net, bus1A, bus2A, length_km=15, std_type=std_type_line,name='L1A-2A')
# bus2A y bus3A
pp.create_line(net, bus2A, bus3A, length_km=20, std_type=std_type_line,name='L2A-3A')
# bus3A y bus2B
pp.create_line(net, bus3A, bus2B, length_km=15, std_type=std_type_line,name='L3A-2B')
# bus2B y bus1B
pp.create_line(net, bus2B, bus1B, length_km=30, std_type=std_type_line,name='L2B-1B')
# bus2 y bus1B
pp.create_line(net, bus2, bus1B, length_km=10, std_type=std_type_line,name='L2-1B')


# Ejecutar el flujo de carga
pp.runpp(net)

# Actualizar los índices para los resultados
net.res_line.index = net.line.name
net.res_bus.index = net.bus.name

# Mostrar los resultados de las barras
print(net.res_bus)