# CS4523 - Advanced Algorithms - Assignment 1

This repository contains my solutions and supporting files for Assignment 1 of the CS4523 Advanced Algorithms course at the University of Moratuwa, Sri Lanka (Semester 8, Jan - May 2025). The assignment, worth 7.5% of the course grade, explores advanced algorithmic concepts including various tree structures and binary decision diagrams (BDDs).

## Assignment Overview

The assignment consists of six questions covering:
- **Red-Black Trees**: Maximizing the ratio of red to black nodes.
- **B-Trees**: Insertion and deletion operations.
- **Treaps**: Building and manipulating treaps with priorities.
- **BST Variants**: Visualizing operations on BST, AVL, Red-Black, and Splay trees.
- **BDDs**: Constructing and analyzing Reduced Ordered Binary Decision Diagrams.
- **Performance Analysis**: Timing operations (insert, search, delete) on BST, AVL, Red-Black, and Splay trees using Java.

## Contents

- **`answers.pdf`**: A PDF document with detailed answers to Questions 1-6, including explanations, proofs, screenshots (e.g., ChatGPT and DeepSeek responses for Q1), and justifications as required by the assignment.

- **`Java_sources/`**: Modified Java source files for Question 6:
  - `BST.java`: Basic Binary Search Tree.
  - `AVLTree.java`: AVL Tree.
  - `RedBlackBST.java`: Red-Black Tree.
  - `SplayBST.java`: Splay Tree.
  - These files include `main()` methods to read data files, perform operations, and output timing results.

- **`data/`**: Input data files for testing Java programs, organized into:
  - `insert/`: Data for insertion operations.
  - `search/`: Data for search operations.
  - `delete/`: Data for deletion operations.
  - Each folder contains `set1/` and `set2/`, with files `data_1.txt`, `data_2.txt`, and `data_3.txt`.

- **`results/`**: Output files from running the Java programs:
  - `BST_results.csv`, `AVLTree_results.csv`, `RedBlackBST_results.csv`, `SplayBST_results.csv`: Timing results for operations.
  - `bdd_f.dot`, `bdd_g.dot`: DOT files for BDD visualizations (Q5).
  - `treap_initial`, `treap_after_insert`, `treap_after_delete`: Treap visualizations (Q3).

- **`draw_bdd.py`**: Python script to visualize BDDs for Question 5 using `pyeda` and Graphviz.
- **`draw_treap.py`**: Python script to visualize treaps for Question 3 using Graphviz.
- **`treap.py`**: Helper Python module for treap operations.
- **`test_trees.sh`**: Bash script to compile and run all Java programs sequentially.

## Usage

### Viewing Answers
- Open `answers.pdf` with any PDF viewer to see responses to Questions 1-6, including theoretical solutions and justifications.

### Visualizing BDDs
For Question 5:
1. Install dependencies:
   ```bash
   pip install pyeda graphviz
   ```
2. Run the script:
   ```bash
   python draw_bdd.py
   ```
   - Outputs `bdd_f.png` and `bdd_g.png` in `results/`.

### Visualizing Treaps
For Question 3:
1. Ensure Graphviz is installed (required by `draw_treap.py`).
2. Run the script:
   ```bash
   python draw_treap.py
   ```
   - Generates `treap_initial.png`, `treap_after_insert.png`, and `treap_after_delete.png` in `results/`.

### Automating Tests
To compile and run all Java programs at once:
1. Make the script executable:
   ```bash
   chmod +x test_trees.sh
   ```
2. Execute:
   ```bash
   ./test_trees.sh
   ```

## Notes
- **Stack Overflow Warning**: For large datasets (e.g., `set2` in `BST_results.csv`), the basic BST may encounter stack overflow errors due to unbalanced recursion.
- **Results Interpretation**: The CSV files in `results/` show operation times in microseconds, with error fields indicating any issues (e.g., `StackOverflowError`).
- **Personalization**: The treap visualizations use `u=44` (from my registration number). Adjust `draw_treap.py` if your `u` differs.

**Disclaimer**: This repository contains solutions prepared by Prabhash Dissanayake (Registration Number: 200144X). It is intended for educational purposes and personal reference. Please do not misuse this material or violate the University of Moratuwa’s academic integrity policies.
