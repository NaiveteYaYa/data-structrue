# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 15:51
# @Author  : WuxieYaYa

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild==None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)

