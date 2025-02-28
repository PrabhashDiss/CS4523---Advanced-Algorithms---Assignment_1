from treap import Treap
import graphviz

# Replace with your UoM Registration number's last two digits
u = 76

data_priority_pairs = [
    (15, 35), (30, 40), (10, 20), (5, 60), (20, 50),
    (25, 30), (35, 10), (40, 25), (50, 70), (60, 45)
]

treap = Treap()

# Insert initial data
for data, priority in data_priority_pairs:
    key = data + u
    treap.insert_key(key, priority)

print("Treap after initial insertions:")
treap.print_treap()

def visualize_treap(treap):
    def add_edges(graph, node):
        if node.left:
            graph.edge(f"{node.key}\n{node.priority}", f"{node.left.key}\n{node.left.priority}")
            add_edges(graph, node.left)
        if node.right:
            graph.edge(f"{node.key}\n{node.priority}", f"{node.right.key}\n{node.right.priority}")
            add_edges(graph, node.right)

    dot = graphviz.Digraph()
    if treap.root:
        dot.node(f"{treap.root.key}\n{treap.root.priority}")
        add_edges(dot, treap.root)
    return dot

print("Treap visualization after initial insertions:")
visualize_treap(treap).render("treap_initial", format="png", view=True)

# Insert (data=45, priority=55)
key = 45 + u
treap.insert_key(key, 55)

print("\nTreap after inserting (data=45, priority=55):")
treap.print_treap()

print("\nTreap visualization after inserting (data=45, priority=55):")
visualize_treap(treap).render("treap_after_insert", format="png", view=True)

# Delete data=30
key = 30 + u
treap.delete_key(key)

print("\nTreap after deleting data=30:")
treap.print_treap()

print("\nTreap visualization after deleting data=30:")
visualize_treap(treap).render("treap_after_delete", format="png", view=True)
