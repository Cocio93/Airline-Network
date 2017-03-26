import pandas as pd
import numpy as np
import networkx as nx

routes_headers = ['AIRLINE_CODE', 'SOURCE_CODE', 'DESTINATION_CODE', 'DISTANCE', 'TIME']
routes = pd.read_table('routes.txt', delimiter=';',decimal='.', dtype={'DISTANCE' : float}, header=None, names=routes_headers)

airports_headers = ['CODE', 'NAME', 'CITY' ,'COUNTRY', 'LATITUDE', 'LONGITUDE']
airports = pd.read_table('airports.txt', delimiter=';', decimal='.', header=None, names=airports_headers)
airport_dict = dict(zip(airports['CODE'],airports['NAME']))

G = nx.DiGraph()
G.add_nodes_from(airports)

for route in routes.iterrows():
    route = route[1]
    attributes = {'AIRLINE_CODE' : route['AIRLINE_CODE'], 'DISTANCE' : route['DISTANCE'], 'TIME' : route['TIME']}

    G.add_edge(route['SOURCE_CODE'], route['DESTINATION_CODE'], weight=attributes)


for u,v,a in G.edges(data=True):
    weight = a['weight']
    airline = weight['AIRLINE_CODE']
    distance = weight['DISTANCE']
    time = weight['TIME']
    s = 'From:', airport_dict.get(u), 'To:', airport_dict.get(v), 'Airline:', airline, 'Distance:', distance, 'Time:', time
    print(s)
