from pyeda.inter import *
import graphviz
import os

# Create results directory if it doesn't exist
os.makedirs('results', exist_ok=True)

# Create variables
x1, x2, x3, x4 = map(bddvar, ['x1', 'x2', 'x3', 'x4'])

# Create the expression f = x1 + x2 + x3 + x4
f = x1 | x2 | x3 | x4

# Create the expression g = x2 + x3 + x4 using a complement edge
g = ~x1 & f

# Convert BDDs to dot format
dot_f = f.to_dot()
dot_g = g.to_dot()

# Create Graphviz objects from the dot strings
graph_f = graphviz.Source(dot_f)
graph_g = graphviz.Source(dot_g)

# Save the graphs to files in the results folder
graph_f.save('results/bdd_f.dot')
graph_f.render('results/bdd_f', format='png', cleanup=True)

graph_g.save('results/bdd_g.dot')
graph_g.render('results/bdd_g', format='png', cleanup=True)

print("BDD for f has been drawn and saved as 'results/bdd_f.png'")
print("BDD for g has been drawn and saved as 'results/bdd_g.png'")
