#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:21:22 2021

@author: shreyamantripragada
"""

import izhikevich_cells as izh

class cCell(izh.izhCell):
    def __init__(self, stimVal):
        """ Call the super constructor from the izhCell class and redfine parameter values needed for the cCell """
        super().__init__(stimVal)
        self.celltype = "Chattering"
        self.C = 50
        self.k=1.5
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25     
        
def createCell():
    """ Create an cCell, call the simulate function, and plot the data """
    myCell = cCell(stimVal = 4000)
    myCell.simulate()
    izh.plotMyData(myCell)
        
if __name__ == '__main__':
    """ main method to call the createCell function """
    createCell()