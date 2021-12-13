#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def delete(self, v):
        return bst.BST.delete(self, v).balance()

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        
        return bst.BST.add(self, v).balance()

    def balance(self):

        leftH = 0
        rightH = 0
        
        if self.lc() is not None:
            leftH = bst.BST.height(self.lc())
        if self.rc() is not None:
            rightH = bst.BST.height(self.rc())

        diff = abs(leftH - rightH)

        #SLR OR DLR
        if diff >= 2:
            
            if self.lc().height() < self.rc().height():

                #SLR
                if self.rc().lc().height() <= self.rc().rc().height():
                    return self.slr()

                #DLR
                else:
                    return self.dlr()

            #SRR OR DRR
            else:
                #SRR
                if self.lc().lc().height() >= self.lc().rc().height():
                    return self.srr()

                #DRR
                else:
                    return self.drr()
        else:
            return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        t = self.rc()
        self.set_rc(t.lc())
        t.set_lc(self)
        return t

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        t = self.lc()
        self.set_lc(t.rc())
        t.set_rc(self)
        return t

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.rc().srr())
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.lc().slr())
        return self.srr() 

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
