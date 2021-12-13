#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a self with the
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
        if self.is_empty():
            return []

        returnArr = []
        trueSize = (2**self.height())
        temp = []
        
        
        temp.append(self)

        while(len(temp)>0):
            returnArr.append(temp[0].value())
            node = temp.pop(0)

            if node.lc() is not None:
                temp.append(node.lc())
            if node.rc() is not None:
                temp.append(node.rc())

        for i in range (0, trueSize-1):
            if returnArr[i] == None or returnArr[i] == '*':
                returnArr.insert((i*2)+1, None)
                returnArr.insert((i*2)+2, None)

        for i, v in enumerate(returnArr):
            if v is '*':
                returnArr[i] = None
            if(len(returnArr) > trueSize-1):
                returnArr.pop()


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
    
    def minValueNode(node, dir):
        current = node
    
        # loop down to find the leftmost leaf
        if dir == "left":
            while(not current.lc().is_empty()):
                current = current.lc()
        elif dir == "right":
            while(not current.rc().is_empty()):
                current = current.rc()
    
        return current
    
    def delete(self, v):
        # base case: the key is not found in the tree
        if self.is_empty():
            return self
        if v is None:
            return self
    
        # if the given key is less than the self node, recur for the left subtree
        if v < self.value():
            self.set_lc(self.lc().delete(v))
    
        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif(v > self.value()):
            self.set_rc(self.rc().delete(v))
    
        # key found
        else:
    
            if self.lc().is_empty():
                temp = self.rc()
                self = None
                return temp
            
            elif self.rc().is_empty():
                temp = self.lc()
                self = None
                return temp

            rightH = self.rc().height()
            leftH = self.lc().height()

            if(rightH > leftH):
                temp = self.rc().minValueNode("left")
                self.set_value(temp.value())
                self.set_rc(self.rc().delete(temp.value()))
            else:
                temp = self.lc().minValueNode("right")
                self.set_value(temp.value())
                self.set_lc(self.lc().delete(temp.value()))
            
    
            self.set_value(temp.value())
 
            # Delete the inorder successor
            self.set_rc(self.rc().delete(temp.value()))
    
        return self

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
