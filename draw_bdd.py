from pyeda.inter import *
import graphviz

# Create variables
x1, x2, x3, x4 = map(bddvar, ['x1', 'x2', 'x3', 'x4'])

# Create the expression x1 + x2 + x3 + x4
bdd = x1 | x2 | x3 | x4

# Convert BDD to dot format
dot = bdd.to_dot()

# Create a Graphviz object from the dot string
graph = graphviz.Source(dot)

# Save the graph to a file (both dot and pdf formats)
graph.save('bdd.dot')
graph.render('bdd', format='pdf', cleanup=True)

print("BDD has been drawn and saved as 'bdd.pdf'")
