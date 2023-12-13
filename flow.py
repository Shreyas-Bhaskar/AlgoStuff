# Given data for the flow network with capacities and flows
edges = {
    ('s', 'v2'): {'flow': 8, 'capacity': 13},
    ('s', 'v1'): {'flow': 11, 'capacity': 16},
    ('v1', 'v3'): {'flow': 12, 'capacity': 12},
    ('v2', 'v1'): {'flow': 1, 'capacity': 4},
    ('v3', 'v2'): {'flow': 4, 'capacity': 9},
    ('v2', 'v4'): {'flow': 11, 'capacity': 14},
    ('v4', 'v3'): {'flow': 7, 'capacity': 7},
    ('v3', 't'): {'flow': 15, 'capacity': 20},
    ('v4', 't'): {'flow': 4, 'capacity': 4}
}


net_flow = 0
cut_capacity = 0

for (u, v), properties in edges.items():
    if u in {'s', 'v2', 'v4'} and v in {'v1', 'v3', 't'}:
        net_flow += properties['flow']
        cut_capacity += properties['capacity']
    elif u in {'v1', 'v3', 't'} and v in {'s', 'v2', 'v4'}:
        net_flow -= properties['flow']

print(net_flow, cut_capacity)
