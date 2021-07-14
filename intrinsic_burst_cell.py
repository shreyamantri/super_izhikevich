#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:20:20 2021

@author: shreyamantripragada
"""

import izhikevich_cells as izh #import the izhikevich_cells as izh

class ibCell(izh.izhCell):
    def __init__(self, stimVal):
        """ Call the super constructor from the izhCell class and redfine parameter values needed for the ibCell """
        super().__init__(stimVal)
        self.celltype = "Intrinsically Bursting"
        self.C = 150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        
def createCell():
    """ Create an ibCell, call the simulate function, and plot the data """
    myCell = ibCell(stimVal = 4000)
    myCell.simulate()
    izh.plotMyData(myCell)
        
if __name__ == '__main__':
    """ main method to call the createCell function """
    createCell()
        
        