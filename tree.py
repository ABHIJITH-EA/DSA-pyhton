#!/usr/bin/env python3
""" Tree implementation

    This module contains the TREE datastructure implementation
    Tree is a hierarchical data structure. Tree have nodes, which contain
    data and reference to other nodes. Topmost node of a tree is called
    root node, nodes below the root node is called child node.Child node
    can have one parent node and multiple child nodes itself. One of the
    best application of the tree is to implement the filesystem structure.
"""
from __future__ import annotations


class Node:
    def __init__(self, data: str, parent: Node | None = None):
        self.data = data
        self.parent = parent
        self.child = {}


class Tree:
    def __init__(self, data: str):
        self.root = Node(data)

    def insert_child(self, data: str, parent: Node | None = None):
        if not parent:
            self.root.child.append(Node(data, self.root))
        else:
            self.root.child

    def travers(self):
        pass


"""
    Implement a folder structure using the tree structure
    
    Example:
        - root
            - boot
                - grub
            - dev
            - etc
                - ssl
                - systemd
"""
if __name__ == '__main__':
    root_dir = Tree("root")
    root_dir.insert_child("boot")
    root_dir.insert_child("dev")
    root_dir.insert_child("etc")

    root_dir.travers()









