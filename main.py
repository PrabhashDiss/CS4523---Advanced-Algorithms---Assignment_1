from treap import Treap

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

# Insert (data=45, priority=55)
key = 45 + u
treap.insert_key(key, 55)

print("\nTreap after inserting (data=45, priority=55):")
treap.print_treap()

# Delete data=30
key = 30 + u
treap.delete_key(key)

print("\nTreap after deleting data=30:")
treap.print_treap()
