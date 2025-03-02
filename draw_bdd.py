from pyeda.inter import *
import graphviz
import os

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Create variables
x1, x2, x3, x4 = map(bddvar, ['x1', 'x2', 'x3', 'x4'])

# Create the expression x1 + x2 + x3 + x4
bdd = x1 | x2 | x3 | x4

# Convert BDD to dot format
dot = bdd.to_dot()

# Create a Graphviz object from the dot string
graph = graphviz.Source(dot)

# Save the graph to a file in the results folder
graph.save('results/bdd.dot')
graph.render('results/bdd', format='png', cleanup=True)

print("BDD has been drawn and saved as 'results/bdd.png'")
