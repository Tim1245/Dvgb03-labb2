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
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False
        
        if self.value() == v:
            return True
 
        if self.value() < v:
            return   self.rc().is_member(v)
   
        return self.lc().is_member(v)
 
    
    

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        return 1 + self.lc().size() + self.rc().size()

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        else :
            # Calculate depth of left and right subtree
            lDepth = self.lc().height()
            rDepth = self.rc().height()
    
            # See which one is deeper and use that one
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
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        if self.is_empty():
            return []

        returnArr = []
        trueSize = (2**self.height())
        temp = []
        
        # Add root node to temp array
        temp.append(self)

        # Loop while array is not empty
        while(len(temp)>0):
            returnArr.append(temp[0].value())
            node = temp.pop(0)
            
            # Add child to array if not empty
            if node.lc() is not None:
                temp.append(node.lc())
            if node.rc() is not None:
                temp.append(node.rc())

        # Inserts None for each child at the correct index
        for i in range (0, trueSize-1):
            if returnArr[i] == None:
                returnArr.insert((i*2)+1, None)
                returnArr.insert((i*2)+2, None)

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
        if self.is_empty():
            return self
        if v is None:
            return self

        # If the value is less than current node, recur to the left
        if v < self.value():
            self.set_lc(self.lc().delete(v))
    
        # If the value is greater than current node, recur to the right
        elif(v > self.value()):
            self.set_rc(self.rc().delete(v))
    
        # Value == self.value()
        else:

            # Removes self and returns self.rc()
            if self.lc().is_empty():
                temp = self.rc()
                self = None
                return temp
            
            # Removes self and returns self.lc()
            elif self.rc().is_empty():
                temp = self.lc()
                self = None
                return temp

            rightH = self.rc().height()
            leftH = self.lc().height()

            # Returns deepest node in the given direction
            def minValueNode(node, dir):
                current = node
            
                if dir == "left":
                    while(not current.lc().is_empty()):
                        current = current.lc()
                elif dir == "right":
                    while(not current.rc().is_empty()):
                        current = current.rc()
            
                return current

            if(rightH > leftH):
                temp = minValueNode(self.rc(),"left")
                self.set_value(temp.value())
                self.set_rc(self.rc().delete(temp.value()))
            else:
                temp = minValueNode(self.lc(),"right")
                self.set_value(temp.value())
                self.set_lc(self.lc().delete(temp.value()))
            
            self.set_value(temp.value())
 
            # Remove and replace next node inorder
            self.set_rc(self.rc().delete(temp.value()))
    
        return self

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
