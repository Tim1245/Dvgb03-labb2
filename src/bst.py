#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
     

        if self.is_empty():
            return False
        
        if self.value() == v:
            return True
 
        if self.value() < v:
            return   self.rc().is_member(v)
   
        return self.lc().is_member(v)
 
    
    

    def size(self):
        if self.is_empty():
            return 0
        return 1 + self.lc().size() + self.rc().size()

    def height(self):
        if self.is_empty():
            return 0
        else :
            # Compute the depth of each subtree
            lDepth = self.lc().height()
            rDepth = self.rc().height()
    
            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return[]
        return self.lc().inorder() + [self.value()]  + self.rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return[]
        return self.lc().postorder() + self.rc().postorder() + [self.value()]

    
        

    def bfs_order_star(self):
        savedHeight = self.height()
        returnArr = []

        def returnCurrentLevel(self, i):
            if i == 1:
                if self is None:
                    returnArr.append(None)
                else:
                    returnArr.append(self.value())
            elif i > 1:
                returnCurrentLevel(self.lc(),i-1)
                returnCurrentLevel(self.rc(),i-1)

        for i in range(1,savedHeight+1):
            returnCurrentLevel(self, i)
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).
        '''
        return returnArr

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self
    
    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        log.info("TODO@src/bst.py: implement delete()")
        return self

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
