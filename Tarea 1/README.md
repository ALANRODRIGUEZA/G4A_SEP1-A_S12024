# Tarea-1 G4A SEP1\A S12024
 Sergio Camilo Rojas\
 Alan Rodríguez Ayala\

Respecto a las tareas relacionadas con el estudio de ingeniería y el contexto del problema:\
2.a) Basándonos en la Norma Técnica de Seguridad y Calidad de Servicio 9, definir los límites admisibles de operación para este estudio\
Para tensiones:\
Estado normal.\
    a. 0.97 y 1.03 pu para instalaciones de tensión nominal igual o superior a 500 [kv] (Sistema 1).\
    b. 0.95 y 1.05 pu para instalaciones de tensión nominal igual o superior a 200 [kv] e inferior a 500 [kv] (Sistema 2).\
    c. 0.93 y 1.07 pu para instalaciones de tensión nominal inferior a 200 [kv].\
Estado Alerta.\
    a. 0.95 y 1.05 pu para instalaciones de tensión nominal igual o superior a 500 [kv] (Sistema 1).\
    b. 0.93 y 1.07 pu para instalaciones de tensión nominal igual o superior a 200 [kv] e inferior a 500 [kv] (Sistema 2).\
    c. 0.90 y 1.10 pu para instalaciones de tensión nominal inferior a 200 [kv].\
Para potencia se tendrá que no se podrá superar el 80% del límite nominal de transmisión de potencia\ 

2.b) Defina el modelamiento con parámetros concentrado de una línea de transmisión e indique las diferencias que tiene con un modelo de parámetros distribuidos. Además, identifique con cuál de los dos tipos de modelamiento trabaja la librería escogida.\

Respecto al modelo de la Figura 1(a):\
3.a) Simule y grafique en solo una Figura el comportamiento de la tensión para una carga que cambie en el rango ±50 % de la potencia indicada en la Figura. Justifique teóricamente el resultado.\

En simulación Tarea 1.pynb\

3.b) Para el mismo rango de operación, calcule la compensación shunt necesaria para que la tensión esté dentro de los
valores indicados por la normativa. Muestre los resultados a través de solo una Figura que contenga gráficos de tensión
en por unidad versus potencia demandada en por unidad\

En simulación Tarea 1.pynb\

3.c) Grafique en solo una Figura las pérdidas en la línea para todo el rango de potencia demandada y todo el rango de compensación que escogió. En la misma Figura deberá indicar una curva de las pérdidas sin compensación. Justifique teóricamente los resultados y comente.

En simulación Tarea 1.pynb\
Comentarios:\
Se entrega la potencia total de las dos lineas en paralelo, por eso que el codigo llega en algunas partes una multiplicación por 2. De la gráfica se puede concluir que la línea tiene menores pérdidas cuando es compensada, esto se vuelve más relevante cuanto mayor es la variación de la carga original, tanto cuando se disminuye como cuando se aumenta.\

Respecto al modelo de la Figura 1(b):\
4.a) Identifique las líneas que se encuentran saturadas o fuera de norma en las condiciones iniciales del problema. Haga un gráfico que indique el estado de cada línea y proponga un método para resolver este problema.\
En simulación Tarea 1.pynb\
Comentarios:\
Para el sistema analizado se tiene que todas las líneas están por debajo del limite del 80% de potencia transmitida, por lo cual se encuentran dentro de la norma. De todas manera se describirá a continuación un método para abordar dicho problema planteado.\

Método para solucionar la saturación y/o valor fuera de norma:\
Reconfiguración de la Red.\
Descripción:\
    La reconfiguración de la red implica cambiar la topología de la red eléctrica mediante la operación de interruptores y seccionadores. Esto permite alterar el flujo de potencia de manera que se alivie la carga en las líneas saturadas y se distribuya mejor la carga en la red.
    Implementación.\
Monitoreo y Análisis de la Red:\ 
    Utilizar sistemas SCADA y herramientas de análisis de flujo de potencia para entender cómo está fluyendo la potencia en la red y dónde se encuentran las sobrecargas.\
Identificación de Puntos de Operación:\ 
    Determinar qué interruptores y seccionadores pueden ser operados para cambiar la topología de la red.\ 
Simulación de Configuraciones:\ 
    Ejecutar simulaciones de diferentes configuraciones de red para identificar la configuración que mejor alivie las sobrecargas sin comprometer la estabilidad y seguridad del sistema.\
Operación de Interruptores:\ 
    Realizar las operaciones necesarias en los interruptores y seccionadores para implementar la nueva configuración de red.\

4.b) Indique si las tensiones en las barras se encuentran fuera de norma considerando dos escenarios:\
• Escenario 1: Estado normal\
• Escenario 2: Estado de alerta\

En simulación Tarea 1.pynb\
Escenarios tensiones en las barras.\
Las tesniones en las barras en todos los casos se encuentran dentro de la norma con una fluctación dentro del rango de 0.95 a 1.05 pu para tensiones comprendidas entre los 200 a 500 [kv].\

4.c) Proponga medidas para llevar a su sistema a puntos de operación dentro de norma en ambos escenarios. Haga su justificación acompañada de una Figura que muestre resultados relevantes.\

Para el caso que las tensiones en las barras estén en estado de alerta o energencia se deberá realizar las siguientes operaciones con tal de llegar la tensión dentro de los margenes del Estado normal:\
    a) Conexión o desconexión de bancos de condensadores shunt.\
    b) Conexión o desconexión de condensadores síncronos.\
    c) Conexión o desconexión de reactores shunt.\
    d) Operación de compensadores estáticos de potencia reactiva.\
    e) Operación de cambiadores de taps bajo carga de transformadores.\
    f) Operación de centrales generadoras con capacidad de inyectar o absorber potencia reactiva.\
    g) Modificación de consigna de equipos de compensación reactiva activos (STATCOM).\
    h) Modificación de la potencia de referencia de los convertidores HVDC.\
No se presenta una justificación en figura ya que el sistema se encuentra dentro de el rango de operación normal para todas las barras del sistema analizado.\

4.d) Investigue al menos tres métodos que se utilicen para llevar a un estado normal el sistema.\

1. Método de reserva de potencia reactiva.\
    Mantener reservas adecuadas de potencia reactiva es esencial para el soporte de la tensión, especialmente en condiciones de carga variable o eventos contingentes. Esto incluye:\
    Reservas en Generadores:\
        Generadores que operan con capacidad adicional para proporcionar o absorber potencia reactiva según sea necesario.
        Operación dentro de un diagrama P-Q que define la capacidad del generador para manejar diferentes combinaciones de potencia activa y reactiva.\
    Parques Eólicos y Fotovoltaicos:\
        Estos parques también deben mantener una capacidad de inyección o absorción de potencia reactiva para apoyar el control de la tensión en redes con alta penetración de energías renovables.\

2. Compensación de Potencia Reactiva.\
    La compensación de potencia reactiva es crucial para el control de la tensión y la mejora de la eficiencia del sistema. Los métodos incluyen:\
    Compensadores Estáticos y Síncronos:\
        Compensadores Síncronos: Máquinas eléctricas que pueden generar o absorber potencia reactiva, proporcionando un ajuste dinámico de la tensión.\
        Compensadores Estáticos (SVCs): Dispositivos basados en electrónica de potencia que regulan la potencia reactiva inyectada o absorbida en el sistema. Incluyen capacitores y reactores controlados por tiristores (TCR, TSC).\
    Bancos de Condensadores Shunt:\
        Se conectan o desconectan automáticamente para proporcionar o absorber potencia reactiva, ajustando así la tensión del sistema.\
    Reactores Shunt:\
        Similar a los bancos de condensadores, pero utilizados para absorber potencia reactiva y reducir la tensión en el sistema.\
    Transformadores con Cambiadores de Tap bajo Carga:\
        Permiten ajustar la relación de transformación bajo carga, cambiando así la tensión en el lado secundario del transformador sin interrumpir el servicio.\
    Operación de Centrales Generadoras:\
        Las centrales pueden ajustar la cantidad de potencia reactiva que generan o absorben, operando dentro de su capacidad especificada por el diagrama P-Q (potencia activa vs. potencia reactiva).

3. Manejo de Contingencias.\
    El manejo de contingencias implica prever y gestionar eventos que puedan perturbar el sistema, como la falla de una línea de transmisión o un generador. Las estrategias incluyen:\
    Simulación de Contingencias:\
        Realización de estudios de flujo de carga y análisis de estabilidad para diferentes escenarios de fallas. Ajuste de las configuraciones del sistema y los recursos disponibles para asegurar que el sistema pueda soportar estas contingencias sin violar los límites de tensión o estabilidad.\
    Ajustes de Operación:\
        Modificación de la operación del sistema basado en los resultados de las simulaciones para asegurar que se mantengan las tensiones dentro de los límites aceptables durante y después de una contingencia.\

4.e) Implemente una medida en un escenario de estado normal de operación y desconecte la línea 3A-2B (a través de los switches indicados) indicada en la Figura. Comente con respecto al comportamiento de las variables en el sistema ante el cambio en la topología.\

En simulación Tarea 1.pynb\
Cambios de la tensión al desconectar línea 3A-2B.\
De la barra 1 de referencia (0), barra 2 (1), barra 1A (2) y barra 2A (3) no se aprecian variaciones significativa ante la contingencia. \
En cuanto las barras 3A y 2B (4 y 6) se ve un aumento en sus tensiones al momento de la contingencia pero manteniendose dentro de los márgenes de operación normal.\
De la barra 1B (5) se aprecia una disminución de su tensión, pero al igual que las barras 3A Y 2B se mantiene dentro de los márgenes de operación normal.\

4.f) Vuelva a conectar la línea e inyecte un 20% más de reactivos desde el generador y analice el comportamiento de las variables del sistema. Comente y muestre resultados en una Figura.\

En simulación Tarea 1.pynb\

4.g) Cree tantos escenarios como cargas tenga y evalúe en cada uno de los escenarios la variación de las variables del sistema al cambiar un ±15% la potencia consumida en una de las cargas.\

En simulación Tarea 1.pynb\
