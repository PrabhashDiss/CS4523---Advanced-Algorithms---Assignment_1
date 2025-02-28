#!/bin/bash
set -e

SRC_DIR="./Java_sources"
BIN_DIR="./bin"
RESULTS_DIR="./results"

# Create output and results directories if needed
mkdir -p "$BIN_DIR"
mkdir -p "$RESULTS_DIR"

# Compile all Java files
javac -d "$BIN_DIR" "$SRC_DIR"/*.java

# Run each class one by one
echo "Running SplayBST..."
java -cp "$BIN_DIR" SplayBST

echo "Running RedBlackBST..."
java -cp "$BIN_DIR" RedBlackBST

echo "Running BST..."
java -cp "$BIN_DIR" BST

echo "Running AVLTree..."
java -cp "$BIN_DIR" AVLTree