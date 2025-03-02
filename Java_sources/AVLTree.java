/*******************************************************
 *  AvlTree.java
 *  Created by Stephen Hall on 11/13/17.
 *  Copyright (c) 2017 Stephen Hall. All rights reserved.
 *  AVL Tree implementation in Java
 ********************************************************/

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class AVLTree<T extends Comparable<T>> {
    /**
     * Node class for AVL Tree
     */
    public class Node {
        private T data;
        private Node left;
        private Node right;
        private int height;

        /**
         * Empty Node constructor
         * @param data: data for the node
         */
        public Node(T data){
            this(data, null, null);
        }

        /**
         * Node constructor with left and right leafs
         * @param data: data to hold
         * @param left: left child
         * @param right: right child
         */
        public Node(T data, Node left, Node right){
            this.data = data;
            this.left = left;
            this.right = right;
        }
    }

    private Node root;
    private int count;

    /**
     * AVLTree Constructor.
     */
    public AVLTree (){
        root = null;
        count = 0;
    }

    /**
     * Gets the height of a node
     * @param node: node to test
     * @return int: height of the node
     */
    public int height(Node node){
        return node == null ? -1 : node.height;
    }

    /**
     * Find the max value among the given numbers.
     * @param a First number
     * @param b Second number
     * @return Maximum value
     */
    public int max(int a, int b){
        return (a > b) ? a : b;
    }

    /**
     * Insert an element into the tree.
     * @param data: data to insert into the tree
     * @return boolean: success|fail
     */
    public boolean insert(T data){
        try {
            root = insert (data, root);
            count++;
            return true;
        } 
        catch(Exception e){
            return false;
        }
    }

    /**
     * Private Insert Helper
     * @param data: data to add
     * @param node Root of the tree
     * @return Node: New root of the tree
     * @throws Exception: failure or duplicate value
     */
    private Node insert(T data, Node node) throws Exception{
        if (node == null)
            node = new Node(data);
        else if (data.compareTo (node.data) < 0){
            node.left = insert (data, node.left);
            if (height(node.left) - height(node.right) == 2){
                if (data.compareTo (node.left.data) < 0){
                    node = rotateLeft(node);
                }
                else {
                    node = rotateRightLeft(node);
                }
            }
        }
        else if (data.compareTo (node.data) > 0){
            node.right = insert(data, node.right);

            if (height(node.right) - height(node.left) == 2)
                if (data.compareTo (node.right.data) > 0){
                    node = rotateRight(node);
                }
                else{
                    node = rotateLeftRight(node);
                }
        }
        else {
            throw new Exception("Attempting to insert duplicate value");
        }
        node.height = max(height(node.left), height(node.right)) + 1;
        return node;
    }

    /**
     * Rotates Node left
     * @param node: node to rotate
     * @return Node: new root node
     */
     private Node rotateLeft (Node node){
        Node tmp = node.left;
        node.left = tmp.right;
        tmp.right = node;
        node.height = max(height(node.left), height(node.right)) + 1;
        tmp.height = max(height(tmp.left), node.height) + 1;
        return tmp;
    }


    /**
     * Rotate left child Right then rotate left
     * @param node: node to rotate
     * @return Node: new root node
     */
    private Node rotateRightLeft(Node node){
        node.left = rotateRight(node.left);
        return rotateLeft (node);
    }

    /**
     * Rotate Right
     * @param node: node to rotate
     * @return Node: new root node
     */
    private Node rotateRight(Node node){
        Node tmp = node.right;
        node.right = tmp.left;
        tmp.left = node;
        node.height = max(height(node.left), height(node.right)) + 1;
        tmp.height = max(height(tmp.right), node.height) + 1;
        return (tmp);
    }

    /**
     * Rotate right child left then rotate right
     * @param node: node to rotate
     * @return Node: new root node
     */
    private Node rotateLeftRight (Node node){
        node.right = rotateLeft(node.right);
        return rotateRight(node);
    }

    /**
     * Deletes all nodes from the tree.
     */
    public void makeEmpty(){
        root = null;
    }

    /**
     * Determine if the tree is empty.
     * @return True if the tree is empty
     */
    public boolean isEmpty(){
        return (root == null);
    }

    /**
     * Find the smallest item in the tree.
     * @return T: smallest item or null if empty.
     */
    public T findMin(){
        return (isEmpty()) ? null : findMin(root).data;
    }

    /**
     * Find the largest item in the tree.
     * @return T: the largest item or null if empty.
     */
    public T findMax(){
        return (isEmpty()) ? null : findMax(root).data;
    }

    /**
     * Find min helper
     * @param node: root to test
     * @return Node: node containing the smallest item.
     */
    private Node findMin(Node node){
        if(node == null )
            return null;

        while(node.left != null )
            node = node.left;

        return node;
    }

    /**
     * Find max helper
     * @param node: root to test.
     * @return Node: node containing the largest item.
     */
    private Node findMax(Node node) {
        if(node == null)
            return null;

        while(node.right != null)
            node = node.right;

        return node;
    }

    /**
     * Remove item from the tree.
     * @param data: item to remove.
     */
    public void remove(T data) {
        root = remove(data, root);
    }

    /**
     * Remove helper function
     * @param data: data to remove
     * @param node: root to start at
     * @return Node: new root node
     */
    private Node remove(T data, Node node) {
        if (node == null){
            return null;
        }

        if (data.compareTo(node.data) < 0 ) {
            node.left = remove(data, node.left);
            int l = node.left != null ? node.left.height : 0;

            if((node.right != null) && (node.right.height - l >= 2)) {
                int rightHeight = node.right.right != null ? node.right.right.height : 0;
                int leftHeight = node.right.left != null ? node.right.left.height : 0;

                if(rightHeight >= leftHeight)
                    node = rotateLeft(node);
                else
                    node = rotateLeftRight(node);
            }
        }
        else if (data.compareTo(node.data) > 0) {
            node.right = remove(data, node.right);
            int r = node.right != null ? node.right.height : 0;
            if((node.left != null) && (node.left.height - r >= 2)) {
                int leftHeight = node.left.left != null ? node.left.left.height : 0;
                int rightHeight = node.left.right != null ? node.left.right.height : 0;
                if(leftHeight >= rightHeight)
                    node = rotateRight(node);
                else
                    node = rotateRightLeft(node);
            }
        }
        else if(node.left != null) {
            node.data = findMax(node.left).data;
            remove(node.data, node.left);

            if((node.right != null) && (node.right.height - node.left.height >= 2)) {
                int rightHeight = node.right.right != null ? node.right.right.height : 0;
                int leftHeight = node.right.left != null ? node.right.left.height : 0;

                if(rightHeight >= leftHeight)
                    node = rotateLeft(node);
                else
                    node = rotateLeftRight(node);
            }
        }
        else
            node = node.right;

        if(node != null) {
            int leftHeight = node.left != null ? node.left.height : 0;
            int rightHeight = node.right!= null ? node.right.height : 0;
            node.height = max(leftHeight, rightHeight) + 1;
        }
        return node;
    }

    /**
     * Determines is the data exists in the tree
     * @param data: data to find
     * @return boolean: success|fail
     */
    public boolean contains(T data){
        return contains(data, root);
    }

    /**
     * Contains helper method
     * @param data: data to find
     * @param node: node to test
     * @return boolean: success|fail
     */
    private boolean contains(T data, Node node) {
        if (node == null)
            return false; // The node was not found
        else if (data.compareTo(node.data) < 0)
            return contains(data, node.left);
        else if (data.compareTo(node.data) > 0)
            return contains(data, node.right);

        return true;
    }

    /**
     * Unit tests the {@code AVLTree} data type.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        AVLTree<Long> avlTree = new AVLTree<>();
        
        String[] sets = {"set1", "set2"};
        String[] dataFiles = {"data_1.txt", "data_2.txt", "data_3.txt"};
        String[] operations = {"insert", "search", "delete"};
        String resultsFile = "results/AVLTree_results.csv";
        
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter(resultsFile, true))) {
            pw.println("Operation,Set,DataFile,Duration(us),Error");
            for(String set : sets) {
                for(String fileName : dataFiles) {
                    for(String op : operations) {
                        String filePath = "data/" + op + "/" + set + "/" + fileName;
                        java.util.List<String> lines = java.nio.file.Files.readAllLines(java.nio.file.Paths.get(filePath));
                        java.util.List<Long> numbers = new java.util.ArrayList<>();
                        for(String line : lines){
                            for(String token : line.split(",")){
                                if(!token.trim().isEmpty())
                                    numbers.add(Long.parseLong(token.trim()));
                            }
                        }
                        long start = System.nanoTime();
                        String error = "";
                        try {
                            if(op.equals("insert")){
                                avlTree = new AVLTree<>();
                                for(Long num : numbers)
                                    avlTree.insert(num);
                            } else if(op.equals("search")){
                                for(Long num : numbers)
                                    avlTree.contains(num);
                            } else if(op.equals("delete")){
                                for(Long num : numbers)
                                    avlTree.remove(num);
                            }
                        } catch (StackOverflowError e) {
                            error = "StackOverflowError";
                        }
                        long duration = (System.nanoTime() - start) / 1000;
                        pw.println(op + "," + set + "," + fileName + "," + duration + "," + error);
                        pw.flush();
                    }
                }
            }
        } catch(Exception e){
            e.printStackTrace();
        }
    }
}





