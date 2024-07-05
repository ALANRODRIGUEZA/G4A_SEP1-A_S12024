Alan Rodríguez Ayala\
Sergio Camilo Rojas

Este análisis se enfoca en el estudio de sistemas eléctricos de potencia utilizando pandapower, una biblioteca de Python diseñada para el análisis de redes eléctricas. Se llevó a cabo una modelación de una red eléctrica específica, la ejecución de un flujo de carga y el análisis de la matriz de admitancia nodal (Y-bus). Aquí se presentan los puntos más destacados:


Configuración Inicial:

Importación de bibliotecas necesarias como pandapower, numpy, y pandas.\
Creación de una red vacía y definición de las barras del sistema.


Adición de Componentes:

Transformadores, generadores y líneas se añadieron a la red para completar el modelo.\
Se definieron y ubicaron las cargas en las diferentes barras del sistema.


Ejecución del Flujo de Carga con pandapower:

El flujo de carga se ejecutó utilizando pandapower y se obtuvo la matriz de admitancia nodal (Y-bus).


Implementación del Método de Newton-Raphson:

Se implementó el método de Newton-Raphson para resolver el sistema de ecuaciones no lineales.\
Se calcularon las potencias activas y reactivas inyectadas en cada barra.\
Se construyó y resolvió la matriz jacobiana para encontrar las correcciones necesarias en las tensiones y ángulos de fase.


Resultados:

Se mostró la matriz Y-bus redondeada y los resultados del flujo de carga, incluyendo las tensiones y ángulos de fase en cada barra.
Los resultados indicaron una no convergencia del método de Newton-Raphson implementado y valores de tensiones y ángulos de fase distintos en aproximandamente un 56% respecto a la libreria pandapower.