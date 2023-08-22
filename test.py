# from graph_tiger.measures import run_measure
# from graph_tiger.graphs import graph_loader

# graph = graph_loader(graph_type='BA', n=1000, seed=1)
# print(1)

# spectral_radius = run_measure(graph, measure='spectral_radius')
# print("Spectral radius:", spectral_radius)

# effective_resistance = run_measure(graph, measure='effective_resistance')
# print("Effective resistance:", effective_resistance)


from graph_tiger.measures import run_measure
from graph_tiger.graphs import graph_loader

graph = graph_loader(graph_type='BA', n=1000, seed=1)

effective_resistance = run_measure(graph, measure='effective_resistance', k=30)
print("Effective resistance (k=30):", effective_resistance)