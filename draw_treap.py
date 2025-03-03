from treap import Treap
import graphviz

u = 44

data_priority_pairs = [
    (15, 35), (30, 40), (10, 20), (5, 60), (20, 50),
    (25, 30), (35, 10), (40, 25), (50, 70), (60, 45)
]

treap = Treap()
treap_insert = Treap()
treap_delete = Treap()

# Insert initial data into treap, treap_insert, and treap_delete
for data, priority in data_priority_pairs:
    key = data + u
    treap.insert_key(key, priority)
    treap_insert.insert_key(key, priority)
    treap_delete.insert_key(key, priority)

print("Treap after initial insertions:")
treap.print_treap()

def visualize_treap(treap):
    # Set node defaults to a light fill colour.
    dot = graphviz.Digraph()
    dot.attr('node', style='filled', fillcolor='lightblue')
    
    def add_edges(graph, node):
        # Process left child: add dummy "None" node if missing.
        if node.left:
            graph.edge(f"{node.key}\n{node.priority}", f"{node.left.key}\n{node.left.priority}", label="L")
            add_edges(graph, node.left)
        else:
            none_id = f"None_{node.key}_L"
            # Override default so that None nodes are not lightblue.
            graph.node(none_id, label="None", style='filled', fillcolor='white')
            graph.edge(f"{node.key}\n{node.priority}", none_id, label="L")
        
        # Process right child: add dummy "None" node if missing.
        if node.right:
            graph.edge(f"{node.key}\n{node.priority}", f"{node.right.key}\n{node.right.priority}", label="R")
            add_edges(graph, node.right)
        else:
            none_id = f"None_{node.key}_R"
            # Override default so that None nodes are not lightblue.
            graph.node(none_id, label="None", style='filled', fillcolor='white')
            graph.edge(f"{node.key}\n{node.priority}", none_id, label="R")
    
    if treap.root:
        dot.node(f"{treap.root.key}\n{treap.root.priority}")
        add_edges(dot, treap.root)
    return dot

visualize_treap(treap).render("results/treap_initial", format="png")

# Insert (data=45, priority=55)
key = 45 + u
treap_insert.insert_key(key, 55)

print("\nTreap after inserting (data=45, priority=55):")
treap_insert.print_treap()

visualize_treap(treap_insert).render("results/treap_after_insert", format="png")

# Delete data=30
key = 30 + u
treap_delete.delete_key(key)

print("\nTreap after deleting data=30:")
treap_delete.print_treap()

visualize_treap(treap_delete).render("results/treap_after_delete", format="png")
